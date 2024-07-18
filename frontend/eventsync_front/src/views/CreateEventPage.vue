<template>
  <v-app class="d-flex flex-column w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mb-10">
      <v-container fluid class="pa-6 d-flex flex-column align-center">
        <h1 class="form-title">Crie seu Evento</h1>
        <v-form @submit.prevent="submitForm" class="pa-3 d-flex flex-column align-center max-width-form">
          <v-text-field v-model="eventName" label="Nome do Evento" required class="field-size"></v-text-field>
          <v-text-field v-model="eventDate" label="Data do Evento" type="date" required class="field-size"></v-text-field>
          <v-text-field v-model="eventPublic" label="Público Alvo" required class="field-size"></v-text-field>
          <v-text-field v-model="eventLocation" label="Local do Evento" required class="field-size"></v-text-field>
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
const eventDate = ref('')
const eventDescription = ref('')
const eventPublic = ref('')
const eventLocation = ref('')
const router = useRouter()

const submitForm = async () => {
  try {
    const response = await axios.post('http://localhost:8000/api/eventos/', {
      nome: eventName.value,
      data: eventDate.value,
      public: eventPublic.value,
      location: eventLocation.value,
      descrição: eventDescription.value
    })
    console.log('Evento criado:', response.data)
    alert('Evento criado com sucesso!')
  } catch (error) {
    console.error('Erro ao criar evento:', error)
    alert('Erro ao criar evento')
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
