<template>
    <v-app class="d-flex flex-column h-100 w-100">
      <NavBar />
      <v-main class="flex-grow-1 pa-16 mb-10">
        <v-container fluid class="d-flex justify-center align-center" style="height: 100vh">
          <v-card class="mx-auto pa-16 py-8 responsive-card" elevation="8" max-width="600" min-width="400" rounded="lg">
            <h3 class="text-subtitle-1 font-weight-bold">Registro</h3>
  
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
  
            <v-responsive class="mx-auto pb-2" max-width="344">
              <v-text-field
                v-model="cpf"
                density="compact"
                placeholder="CPF"
                prepend-inner-icon="mdi-account-card-details-outline"
                variant="outlined"
                :rules="[rules.cpf]"
              ></v-text-field>
            </v-responsive>
  
            <v-responsive class="mx-auto pb-2" max-width="344">
              <v-text-field
                v-model="name"
                density="compact"
                placeholder="Nome"
                prepend-inner-icon="mdi-account-outline"
                variant="outlined"
                :rules="[rules.name]"
              ></v-text-field>
            </v-responsive>
  
            <v-responsive class="mx-auto pb-2" max-width="344">
              <v-text-field
              v-model="birthDate"
              label="Data de Nascimento"
              type="date"
              required
              class="field-size"
              :rules="[rules.birthDate]"
              ></v-text-field>
            </v-responsive>
  
            <v-responsive class="mx-auto pb-2" max-width="344">
              <v-text-field
                v-model="phone"
                density="compact"
                placeholder="Telefone"
                prepend-inner-icon="mdi-phone"
                variant="outlined"
                :rules="[rules.phone]"
              ></v-text-field>
            </v-responsive>
  
            <v-responsive class="mx-auto pb-2" max-width="344">
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
  
            <v-responsive class="mx-auto pb-4" max-width="344">
              <v-text-field
                v-model="password2"
                :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                :type="visible ? 'text' : 'password'"
                density="compact"
                placeholder="Confirme a Senha"
                prepend-inner-icon="mdi-lock-outline"
                variant="outlined"
                @click:append-inner="visible = !visible"
                :rules="[rules.confirmPassword]"
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
              Registrar
            </v-btn>
  
            <v-card-text class="text-center">
              <router-link to="/login" class="text-blue-darken-2 text-decoration-none text-subtitle-1">
                Já tem uma conta? <v-icon icon="mdi-chevron-right"></v-icon>
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
    confirmPassword: confirmPasswordValidation(password.value)
  }
  
  const errorMessage = ref<string | null>(null)
  const showError = ref(false)
  
  // Computed property to determine if the form is valid
  const isFormValid = computed(() => {
    return (
      rules.email(email.value) === true &&
      rules.cpf(cpf.value) === true &&
      rules.name(name.value) === true &&
      rules.birthDate(birthDate.value) === true &&
      rules.phone(phone.value) === true &&
      rules.password(password.value) === true &&
      rules.confirmPassword(password2.value) === true
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
  
  </script>
  
  <style scoped></style>
  