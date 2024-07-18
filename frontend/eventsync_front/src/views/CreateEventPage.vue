<template>
  <v-app class="d-flex flex-column h-100 w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mt-10">
      <v-container fluid class="pa-4 d-flex flex-column h-100 w-100">
        <h1>Crie seu Evento</h1>
        <v-form @submit.prevent="submitForm" class="pa-4 d-flex flex-column">
          <v-text-field v-model="eventName" label="Nome do Evento" required></v-text-field>
          <v-text-field v-model="eventDate" label="Data do Evento" type="date" required></v-text-field>
          <v-textarea v-model="eventDescription" label="Descrição do Evento" required></v-textarea>
          <v-btn type="submit" color="primary" class="btn-size">Criar Evento</v-btn>
          <v-btn @click="goBack" color="secondary" class="btn-size voltar-btn">Voltar</v-btn>
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
const router = useRouter()

const submitForm = async () => {
  try {
    const response = await axios.post('http://localhost:8000/api/eventos/', {
      nome: eventName.value,
      data: eventDate.value,
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
  width: 200px;
  margin-top: 10px;
}

.voltar-btn {
  background-color: #ff6f61;
  color: #ffffff;
  font-weight: bold;
  border-radius: 8px;
  padding: 10px 20px;
}
</style>
