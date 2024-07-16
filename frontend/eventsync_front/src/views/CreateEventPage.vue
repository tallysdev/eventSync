
<template>
  <v-app class="d-flex flex-column h-100 w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mt-10">
      <v-container fluid class="pa-4 d-flex flex-column h-100 w-100">
        <h1>Crie seu Evento</h1>
        <v-form @submit.prevent="submitForm" class="pa-4">
          <v-text-field v-model="eventName" label="Nome do Evento" required></v-text-field>
          <v-text-field v-model="eventDate" label="Data do Evento" type="date" required></v-text-field>
          <v-textarea v-model="eventDescription" label="Descrição do Evento" required></v-textarea>
          <v-btn type="submit" color="primary">Criar Evento</v-btn>
        </v-form>
        <v-btn @click="goBack" color="secondary">Voltar</v-btn>
      </v-container>
    </v-main>
    <FooterVue />
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import NavBar from '../components/NavBar.vue'
import FooterVue from '../components/Footer.vue'

const eventName = ref('')
const eventDate = ref('')
const eventDescription = ref('')
const router = useRouter()

const submitForm = () => {
  console.log('Evento criado:', {
    nome: eventName.value,
    data: eventDate.value,
    descrição: eventDescription.value
  })
  alert('Evento criado com sucesso!')
}

const goBack = () => {
  router.push({ name: 'home' })
}
</script>

<style scoped>
/* Estilos específicos da página de criação de evento */
.fill-height {
  min-height: 100vh;
  background-color: #2f3640;
  color: #ffffff;
}

/* Usando essa notação pra alterar a estilização de uma classe interna no vuetify*/
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
</style>
