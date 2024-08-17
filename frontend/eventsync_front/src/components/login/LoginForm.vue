<template>
  <v-app class="d-flex flex-column h-100 w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mb-10">
      <v-container fluid class="d-flex justify-center align-center" style="height: 100vh">
        <v-card class="mx-auto pa-16 py-8 responsive-card" elevation="8" max-width="600" min-width="400" rounded="lg">
          <h3 class="text-subtitle-1 font-weight-bold">Login</h3>
          <v-responsive class="mx-auto pb-2" max-width="344">
            <v-text-field
              v-model="email"
              density="compact"
              placeholder="Email"
              prepend-inner-icon="mdi-account"
              variant="outlined"
              :rules="[rules.email]"
            ></v-text-field>
          </v-responsive>
          <h3 class="text-subtitle-1 font-weight-bold">Password</h3>
          <v-responsive class="mx-auto pb-4" max-width="344">
            <v-text-field
              v-model="password"
              :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
              :type="visible ? 'text' : 'password'"
              density="compact"
              placeholder="Senha"
              prepend-inner-icon="mdi-lock-outline"
              variant="outlined"
              @click:append-inner="visible = !visible"
              :rules="[rules.password]"
            ></v-text-field>
          </v-responsive>
          <v-btn
            block
            class="mb-4"
            color="blue-darken-2"
            size="large"
            variant="tonal"
            :disabled="!isFormValid || showError"
            @click="handleSubmit"
          >
            Login
          </v-btn>
          <v-card-text class="text-center">
            <router-link to="/register" class="text-blue-darken-2 text-decoration-none text-subtitle-1">
              Cadastre-se <v-icon icon="mdi-chevron-right"></v-icon>
            </router-link>
          </v-card-text>
        </v-card>
      </v-container>
    </v-main>
    <FooterVue />
  </v-app>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { emailValidation, passwordValidation } from '@/utils/validation'
import NavBar from '../../components/NavBar.vue'
import FooterVue from '../../components/Footer.vue'
import { type User } from '@/types/users'

const router = useRouter()
const authStore = useAuthStore()
const visible = ref(false)
const email = ref('')
const password = ref('')

const rules = {
  email: emailValidation,
  password: passwordValidation
}

const errorMessage = ref<string | null>(null)
const showError = ref(false)

// Computed property to determine if the form is valid
const isFormValid = computed(() => {
  return (
    rules.email(email.value) === true &&
    rules.password(password.value) === true
  )
})

const handleSubmit = async () => {
  if (email.value && password.value) {
    try {
      const user: User = {
        email: email.value,
        password: password.value
      }
      await authStore.login(user)
      if (authStore.isAuthenticated) {
          router.push('/')
      } else {
        console.error('Login falhou')
        errorMessage.value = 'Login falhou. Usuário ou senha incorretos.'
        showError.value = true
      }
    } catch (error) {
      console.error('Erro no login:', error)
      errorMessage.value = 'Erro no login. Por favor, tente novamente.'
      showError.value = true
    }
  }
}

</script>

<style scoped></style>
