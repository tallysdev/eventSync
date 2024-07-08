<template>
  <v-app class="d-flex flex-column justify-center align-center h-100 w-100">
    <NavBar />
    <v-main class="d-flex flex-column align-center justify-space-around h-100 w-100 pa-16 mt-10 mb-16 main-content">
      <v-container fluid class="pa-4 d-flex flex-column h-100 w-100">
        <EventType :event-types="eventTypes" />
        <UpcomingEvents :upcoming-events="upcomingEvents" />
      </v-container>
    </v-main>
    <Footer  class="pt-16 mt-16"/>
  </v-app>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import NavBar from './NavBar.vue'
import EventType from './home/EventType.vue'
import UpcomingEvents from './home/UpcomingEvent.vue'
import Footer from './Footer.vue'

// Event types for the event type slider
const eventTypes = ref([
  { id: 1, name: 'Show', icon: 'mdi-music' },
  { id: 2, name: 'Esporte', icon: 'mdi-basketball' },
  { id: 3, name: 'Teatro', icon: 'mdi-drama-masks' },
  { id: 4, name: 'Cinema', icon: 'mdi-movie' }
])

// Upcoming events for the upcoming events slider
const upcomingEvents = ref([
  {
    id: 1,
    name: 'Titulo para encher linguiça e preencher o espaço para mostrar o texto',
    date: 'Sex, 30 ago',
    time: '19:00 - 21:00',
    location: 'UFRN/Ceres - Caicó, RN',
    buttonText: 'Saiba mais'
  },
  {
    id: 2,
    name: 'Partida de Futebol',
    date: '15 de Julho',
    time: '16:00 - 18:00',
    location: 'Estádio ABC',
    buttonText: 'Saiba mais'
  },
  {
    id: 3,
    name: 'Peça de Teatro',
    date: '20 de Julho',
    time: '20:00 - 22:00',
    location: 'Teatro 123',
    buttonText: 'Saiba mais'
  }
])
</script>

<style scoped>
.fill-height {
  min-height: 100vh;
  background-color: #2f3640;
  color: #ffffff;
}

.v-main {
  flex-grow: 1;
}

.v-footer {
  flex-shrink: 0;
}

:deep(.v-application__wrap) {
  min-width: 100% !important;
  margin: 0 auto !important;
}

@media (max-width: 600px) {
  .v-main {
    padding-bottom: 120px; /* Increase padding for smaller screens */
  }
}
</style>
