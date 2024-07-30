<template>
  <v-app class="d-flex flex-column w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mb-10">
      <v-container fluid class="pa-6 d-flex flex-column align-center">
        <h1 class="form-title">Crie seu Evento</h1>
        <v-form @submit.prevent="submitForm" class="pa-3 d-flex flex-column align-center max-width-form">
          <v-text-field v-model="eventName" label="Nome do Evento" required class="field-size"></v-text-field>
          <v-text-field v-model="eventStartDate" label="Data de Início do Evento" type="date" required class="field-size"></v-text-field>
          <v-text-field v-model="eventEndDate" label="Data de Fim do Evento" type="date" required class="field-size"></v-text-field>
          <v-text-field v-model="eventPublic" label="Público Alvo" required class="field-size"></v-text-field>
          <v-text-field v-model="eventLocation" label="Local do Evento" required class="field-size"></v-text-field>
          <v-text-field 
            v-model="eventMinParticipants" 
            label="Quantidade Mínima de Participantes" 
            type="number" 
            required 
            class="field-size" 
            min="1"
            @keypress="validateNumberInput"
          ></v-text-field>
          <v-text-field 
            v-model="eventMaxParticipants" 
            label="Quantidade Máxima de Participantes" 
            type="number" 
            required 
            class="field-size" 
            min="1"
            @keypress="validateNumberInput"
          ></v-text-field>
          <v-text-field 
            v-model="eventHours" 
            label="Quantidade de Horas" 
            type="number" 
            required 
            class="field-size" 
            min="1"
            @keypress="validateNumberInput"
          ></v-text-field>
          <v-text-field v-model="eventType" label="Tipo do Evento" required class="field-size"></v-text-field>
          <v-textarea v-model="eventDescription" label="Descrição do Evento" required class="field-size"></v-textarea>
          <v-row class="mt-4">
            <v-col cols="6" class="d-flex justify-start">
              <v-btn @click="goBack" color="secondary" class="btn-size btn-style voltar-btn" elevation="2">Voltar</v-btn>
            </v-col>
            <v-col cols="6" class="d-flex justify-end">
              <v-btn type="submit" color="primary" class="btn-size btn-style" elevation="2">Criar Evento</v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-container>
    </v-main>
    <FooterVue />
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import NavBar from '../components/NavBar.vue'
import FooterVue from '../components/Footer.vue'

const eventName = ref('')
const eventStartDate = ref('')
const eventEndDate = ref('')
const eventDescription = ref('')
const eventPublic = ref('')
const eventLocation = ref('')
const eventMinParticipants = ref('')
const eventMaxParticipants = ref('')
const eventHours = ref('')
const eventType = ref('')
const router = useRouter()

const validateNumberInput = (event) => {
  const key = event.key
  if (!/[0-9]/.test(key)) {
    event.preventDefault()
  }
}

const validateFields = () => {
  const fields = [
    { value: eventName.value, message: 'Nome do Evento é obrigatório' },
    { value: eventStartDate.value, message: 'Data de Início do Evento é obrigatória' },
    { value: eventEndDate.value, message: 'Data de Fim do Evento é obrigatória' },
    { value: eventPublic.value, message: 'Público Alvo é obrigatório' },
    { value: eventLocation.value, message: 'Local do Evento é obrigatório' },
    { value: eventMinParticipants.value && eventMinParticipants.value > 0, message: 'Quantidade Mínima de Participantes é obrigatória e deve ser maior que 0' },
    { value: eventMaxParticipants.value && eventMaxParticipants.value > 0, message: 'Quantidade Máxima de Participantes é obrigatória e deve ser maior que 0' },
    { value: eventHours.value && eventHours.value > 0, message: 'Quantidade de Horas é obrigatória e deve ser maior que 0' },
    { value: eventType.value, message: 'Tipo do Evento é obrigatório' },
    { value: eventDescription.value, message: 'Descrição do Evento é obrigatória' },
  ]

  for (const field of fields) {
    if (!field.value) {
      alert(field.message)
      return false
    }
  }
  return true
}

const submitForm = async () => {
  if (!validateFields()) {
    return
  }

  try {
    const response = await axios.post('http://localhost:8000/api/eventos/', {
      nome: eventName.value,
      dataInicio: eventStartDate.value,
      dataFim: eventEndDate.value,
      public: eventPublic.value,
      location: eventLocation.value,
      descricao: eventDescription.value,
      minParticipants: eventMinParticipants.value,
      maxParticipants: eventMaxParticipants.value,
      horas: eventHours.value,
      tipo: eventType.value
    })
    console.log('Evento criado:', response.data)
    alert('Evento criado com sucesso!')
  } catch (error) {
    if (error.response) {
      console.error('Erro ao criar evento:', error.response.data)
      alert(`Erro ao criar evento: ${JSON.stringify(error.response.data)}`)
    } else {
      console.error('Erro ao criar evento:', error)
      alert('Erro ao criar evento')
    }
  }
}

const goBack = () => {
  router.push({ name: 'home' })
}
</script>

<style scoped>
.fill-height {
  min-height: 100vh;
  background-color: #2f3640;
  color: #ffffff;
}

:deep(.v-application__wrap) {
  min-width: 100% !important;
  margin: 0 auto !important;
}

.v-main {
  flex-grow: 1;
}

.v-footer {
  flex-shrink: 0;
}

.btn-size {
  width: 100%; 
  max-width: 300px; 
  margin-top: 10px;
}

.btn-style {
  font-weight: bold;
  border-radius: 2px;
  padding: 5px 24px;
  font-size: 1.2rem;
}

.voltar-btn {
  font-weight: bold;
  background-color: #ff6f61;
  color: #ffffff;
}

.form-title {
  text-align: center;
  margin-bottom: 30px;
  font-size: 2.8rem;
}

.mt-4 {
  margin-top: 2rem;
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
