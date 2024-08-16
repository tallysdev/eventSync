<template>
  <v-app class="d-flex flex-column w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mb-10">
      <v-container fluid class="pa-6 d-flex flex-column align-center">
        <h1 class="form-title">Registro</h1>
        <v-form
          ref="form"
          v-model="valid"
          lazy-validation
          @submit.prevent="handleSubmit"
          class="pa-3 d-flex flex-column align-center max-width-form"
        >
          <v-text-field
            v-model="email"
            density="compact"
            placeholder="Email"
            prepend-inner-icon="mdi-account"
            variant="outlined"
            class="field-size"
            :rules="[rules.email]"
          ></v-text-field>

          <v-text-field
            v-model="cpf"
            density="compact"
            placeholder="CPF - apenas números"
            prepend-inner-icon="mdi-account"
            variant="outlined"
            class="field-size"
            :rules="[rules.cpf]"
          ></v-text-field>

          <v-text-field
            v-model="name"
            density="compact"
            placeholder="Nome"
            prepend-inner-icon="mdi-account-outline"
            variant="outlined"
            class="field-size"
            :rules="[rules.name]"
          ></v-text-field>

          <v-text-field
            v-model="birthDate"
            label="Data de Nascimento"
            type="date"
            required
            class="field-size"
            :rules="[rules.birthDate]"
          ></v-text-field>

          <v-text-field
            v-model="phone"
            density="compact"
            placeholder="Telefone - apenas números"
            prepend-inner-icon="mdi-phone"
            variant="outlined"
            class="field-size"
            :rules="[rules.phone]"
          ></v-text-field>

          <v-text-field
            v-model="password"
            :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
            :type="visible ? 'text' : 'password'"
            density="compact"
            placeholder="Senha"
            prepend-inner-icon="mdi-lock-outline"
            variant="outlined"
            class="field-size"
            @click:append-inner="visible = !visible"
            :rules="[rules.password]"
          ></v-text-field>

          <v-text-field
            v-model="password2"
            :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
            :type="visible ? 'text' : 'password'"
            density="compact"
            placeholder="Confirme a Senha"
            prepend-inner-icon="mdi-lock-outline"
            variant="outlined"
            class="field-size"
            @click:append-inner="visible = !visible"
            :rules="[confirmPasswordRule]"
          ></v-text-field>

          <v-btn
            block
            class="mb-4"
            color="blue-darken-2"
            size="large"
            variant="tonal"
            :disabled="!isFormValid || showError"
            @click="handleSubmit"
          >
            Registrar
          </v-btn>

          <v-card-text class="text-center">
            <router-link to="/login" class="text-blue-darken-2 text-decoration-none text-subtitle-1">
              Já tem uma conta? <v-icon icon="mdi-chevron-right"></v-icon>
            </router-link>
          </v-card-text>
        </v-form>
      </v-container>
    </v-main>
    <FooterVue />
  </v-app>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { emailValidation, passwordValidation, confirmPasswordValidation, isValidCPF, isValidPhoneNumber } from '@/utils/validation'
import NavBar from '../../components/NavBar.vue'
import FooterVue from '../../components/Footer.vue'
import { type RegisterUser } from '@/types/users'
import { registerUserInDB } from '@/services/registerService'

const router = useRouter()
const visible = ref(false)
const email = ref('')
const cpf = ref('')
const name = ref('')
const birthDate = ref('')
const phone = ref('')
const password = ref('')
const password2 = ref('')

const rules = {
  email: emailValidation,
  cpf: isValidCPF,
  name: (value: string) => !!value || 'Nome é necessário',
  birthDate: (value: string) => !!value || 'Data de nascimento é necessária',
  phone: isValidPhoneNumber,
  password: passwordValidation,
  confirmPassword: confirmPasswordValidation,
}

const errorMessage = ref<string | null>(null)
const showError = ref(false)

const isFormValid = computed(() => {
  return (
    rules.email(email.value) === true &&
    rules.cpf(cpf.value) === true &&
    rules.name(name.value) === true &&
    rules.birthDate(birthDate.value) === true &&
    rules.phone(phone.value) === true &&
    rules.password(password.value) === true &&
    rules.confirmPassword(password.value, password2.value) === true
  )
})

const handleSubmit = async () => {
  if (isFormValid.value) {
    try {
      const newUser: RegisterUser = {
        email: email.value,
        cpf: cpf.value,
        name: name.value,
        birth_date: birthDate.value,
        phone: phone.value,
        password: password.value,
        password2: password2.value
      }
      await registerUserInDB(newUser)
      router.push('/login')
    } catch (error) {
      console.error('Erro no registro:', error)
      errorMessage.value = 'Erro no registro. Por favor, tente novamente.'
      showError.value = true
    }
  }
}

const confirmPasswordRule = computed(() => {
  return () => rules.confirmPassword(password.value, password2.value)
})
</script>

<style scoped>
.fill-height {
  min-height: 100vh;
  background-color: #2f3640;
  color: #ffffff;
}

.field-size {
  max-width: 100%;
  width: 100%;
  margin-bottom: auto;
  font-size: 1.2rem;
}

.max-width-form {
  max-width: 1000px;
  width: 100%;
}
</style>
