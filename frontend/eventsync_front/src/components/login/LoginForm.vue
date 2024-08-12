<template>
    <v-app class="d-flex flex-column h-100 w-100">
      <NavBar />
      <v-main class="flex-grow-1 pa-16 mb-10">
        <v-container fluid class="d-flex justify-center align-center" style="height: 100vh">
          <v-card class="mx-auto pa-16 py-8 responsive-card" elevation="8" max-width="400" rounded="lg">
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
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore, type User } from '@/stores/auth'
import { emailValidation, passwordValidation } from '@/utils/validation'
import NavBar from '../../components/NavBar.vue'
import FooterVue from '../../components/Footer.vue'

const props = defineProps({
  dialog: {
    type: Boolean,
    required: true
  }
})

const emit = defineEmits(['update:dialog', 'login-success'])

const router = useRouter()
const authStore = useAuthStore()
const visible = ref(false)
const email = ref('')
const password = ref('')
const valid = ref(false)

const rules = {
  email: emailValidation,
  password: passwordValidation
}

const errorMessage = ref<string | null>(null)
const showError = ref(false)

const closeDialog = () => {
  emit('update:dialog', false)
}

const updateDialog = (value: boolean) => {
  emit('update:dialog', value)
}

const handleSubmit = async () => {
  if (email.value && password.value) {
    try {
      const user: User = {
        email: email.value,
        password: password.value
      }
      await authStore.login(user)
      if (authStore.isAuthenticated) {
        emit('login-success', 'Login realizado com sucesso!')
        closeDialog()
        setTimeout(() => {
          router.push('/')
        }, 2000)
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

watch(
  () => props.dialog,
  (newValue) => {
    if (!newValue) {
      email.value = ''
      password.value = ''
      showError.value = false
      errorMessage.value = null
    }
  }
)
</script>
  
  <style scoped></style>
  