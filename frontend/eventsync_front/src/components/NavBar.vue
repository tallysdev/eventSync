<template>
  <div>
    <!-- Desktop Navbar -->
    <v-app-bar app color="secondary" dense flat class="py-2 mb-2 hidden-sm-and-down fill-width">
      <v-container>
        <v-row class="d-flex align-center justify-space-around">
          <v-col cols="1">
            <v-img src="../../favicon.ico" alt="Platform Logo" height="40"></v-img>
          </v-col>
          <v-col cols="3">
            <v-text-field
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
          <v-col cols="2">
            <v-select
              :items="locations"
              item-text="name"
              item-value="id"
              label="Localizações"
              prepend-inner-icon="mdi-map-marker"
              variant="solo"
              density="comfortable"
              bg-color="transparent"
              flat
              rounded
              hide-details
            ></v-select>
          </v-col>
          <v-col cols="3" class="d-flex align-center justify-space-around">
            <v-btn>Crie seu evento</v-btn>
            <v-btn>Acesse sua conta</v-btn>
            <v-btn
              class="text-none"
              color="primary"
              variant="flat"
              style="border: 1px solid white"
              rounded="xs"
            >
              <b>Cadastre-se</b>
            </v-btn>
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
            <v-img src="../../favicon.ico" alt="Platform Logo" height="40"></v-img>
          </v-col>
          <v-col cols="2" class="d-flex align-center justify-end">
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
          <v-toolbar-title>Mobile Menu</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon @click="dialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>
        <v-list>
          <v-list-item v-for="(item, index) in menuItems" :key="index" @click="dialog = false">
            <template v-slot:prepend>
              <v-icon :icon="item.icon"></v-icon>
            </template>
            <v-list-item-title>{{ item.text }}</v-list-item-title>
          </v-list-item>
          <v-list-group>
            <template v-slot:activator="{ props }">
              <v-list-item v-bind="props" prepend-icon="mdi-map-marker" title="Localizações"></v-list-item>
            </template>
            <v-list-item v-for="(location, index) in locations" :key="index">
              <v-list-item-title>{{ location }}</v-list-item-title>
            </v-list-item>
          </v-list-group>
        </v-list>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// Sidebar state for mobile menu
const dialog = ref(false)

// Locations for the select dropdown
const locations = ref(['Localização 1', 'Localização 2', 'Localização 3'])

// Menu items for the navigation drawer
const menuItems = ref([
  { text: 'Pesquisar eventos', icon: 'mdi-magnify' },
  { text: 'Crie seu evento', icon: 'mdi-plus' },
  { text: 'Acesse sua conta', icon: 'mdi-login' },
  { text: 'Cadastre-se', icon: 'mdi-account-plus' }
])
</script>
