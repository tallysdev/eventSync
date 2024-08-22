<template>
  <div>
    <!-- Desktop Navbar -->
    <v-app-bar app color="secondary" dense flat class="py-2 mb-2 hidden-sm-and-down fill-width">
      <v-container>
        <v-row class="d-flex align-center justify-space-between">
          <v-col cols="1">
            <v-img
              @click="navigateTo('/')"
              class="cursor-pointer"
              src="../../favicon.ico"
              alt="Platform Logo"
              height="40"
            ></v-img>
          </v-col>
          <v-col cols="3">
            <v-text-field
              v-model="searchQuery"
              color="primary"
              bg-color="complementary"
              placeholder="Pesquisar eventos..."
              prepend-inner-icon="mdi-magnify"
              variant="outlined"
              flat
              hide-details
              rounded
            ></v-text-field>
          </v-col>
          <v-col cols="7" class="d-flex align-center justify-space-between">
            <v-btn :to="{ name: 'create-event' }">Crie seu evento</v-btn>
            <template v-if="isAuthenticated">
              <v-btn :to="{ name: 'certificates' }">Certificados</v-btn>
              <v-btn :to="{ name: 'events-organized' }">Eventos Organizados</v-btn>
              <v-btn
                class="text-none"
                color="primary-darken-1"
                variant="flat"
                style="border: 1px solid white"
                rounded="xs"
                @click="handleLogout"
              >
                <b>Logout</b>
              </v-btn>
            </template>
            <template v-else>
              <v-btn to="/login">Acesse sua conta</v-btn>
              <v-btn
                class="text-none"
                color="primary"
                variant="flat"
                style="border: 1px solid white"
                rounded="xs"
              >
                <v-btn to="/register">Cadastre-se</v-btn>
              </v-btn>
            </template>
          </v-col>
        </v-row>
      </v-container>
    </v-app-bar>

    <!-- Mobile Navbar -->
    <v-app-bar
      app
      color="secondary"
      dense
      flat
      class="py-2 mb-0 hidden-md-and-up"
      style="position: fixed; top: 0; left: 0; right: 0"
    >
      <v-container>
        <v-row class="d-flex align-center justify-space-between">
          <v-col cols="2">
            <v-img
              @click="navigateTo('/')"
              src="../../favicon.ico"
              alt="Platform Logo"
              height="40"
            ></v-img>
          </v-col>
          <v-col cols="8" class="d-flex align-center justify-end">
            <v-btn icon @click="dialog = true">
              <v-icon>mdi-menu</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-app-bar>

    <!-- Mobile Navigation Dialog -->
    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
      <v-card>
        <v-toolbar flat color="secondary">
          <v-toolbar-title>
            <template v-if="isAuthenticated"> Olá, {{ userName }} </template>
            <template v-else> Mobile Menu </template>
          </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon @click="dialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>
        <v-list>
          <v-list-item @click="toggleSearchField">
            <template v-slot:prepend>
              <v-icon>mdi-magnify</v-icon>
            </template>
            <v-list-item-title>Pesquisar eventos</v-list-item-title>
          </v-list-item>
          <v-list-item @click="() => router.push({ name: 'create-event' })">
            <template v-slot:prepend>
              <v-icon>mdi-plus</v-icon>
            </template>
            <v-list-item-title>Crie seu evento</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="!isAuthenticated" to="/login">
            <template v-slot:prepend>
              <v-icon>mdi-login</v-icon>
            </template>
            <v-list-item-title>Acesse sua conta</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="!isAuthenticated" to="/register">
            <template v-slot:prepend>
              <v-icon>mdi-account-plus</v-icon>
            </template>
            <v-list-item-title>Cadastre-se</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="isAuthenticated" @click="navigateTo('/certificates')">
            <template v-slot:prepend>
              <v-icon>mdi-certificate</v-icon>
            </template>
            <v-list-item-title>Certificados</v-list-item-title>
          </v-list-item>

          <v-list-item v-if="isAuthenticated" @click="navigateTo('/events-organized')">
            <template v-slot:prepend>
              <v-icon>mdi-calendar-check</v-icon>
            </template>
            <v-list-item-title>Eventos Organizados</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="isAuthenticated" @click="handleLogout">
            <template v-slot:prepend>
              <v-icon>mdi-logout</v-icon>
            </template>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list>
        <v-card v-if="showSearchField" class="mx-4 my-2 pa-6">
          <v-text-field
            v-model="searchQuery"
            color="primary"
            bg-color="complementary"
            placeholder="Pesquisar eventos..."
            prepend-inner-icon="mdi-magnify"
            variant="outlined"
            flat
            hide-details
            rounded
          ></v-text-field>
          <v-btn @click="searchEvents" class="mx-1 my-2">Search</v-btn>
        </v-card>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

// Sidebar state for mobile menu
const dialog = ref(false)
const showSearchField = ref(false)
const searchQuery = ref('')

// Locations for the select dropdown
const locations = ref(['Localização 1', 'Localização 2', 'Localização 3'])

const toggleSearchField = () => {
  showSearchField.value = !showSearchField.value
}

const searchEvents = () => {
  console.log('Searching for events with query:', searchQuery.value)
}

const navigateTo = (route: string) => {
  router.push(route)
}

// Authentication state
const authStore = useAuthStore()
const isAuthenticated = ref(authStore.isAuthenticated)
const router = useRouter()

// Função para extrair o primeiro nome
const getFirstName = (fullName: string) => {
  return fullName.split(' ')[0] // Divide o nome completo e retorna o primeiro nome
}

const userName = ref(getFirstName(authStore.getUser?.name || ''))

// Watch for changes in authentication state
authStore.$subscribe(() => {
  isAuthenticated.value = authStore.isAuthenticated
  userName.value = getFirstName(authStore.getUser?.name || '')
})

const handleLogout = () => {
  authStore.logout() // Chama o método de logout
  router.push('/')
  setTimeout(() => {
    router.go(0)
  }, 100)
}
</script>

<style scoped></style>
