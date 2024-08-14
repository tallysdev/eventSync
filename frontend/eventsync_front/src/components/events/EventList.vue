<template>
  <v-row justify="center">
    <v-col cols="12" lg="10">
      <h2 class="text-h4 text-start mb-6 font-weight-bold">Eventos</h2>
      <template v-if="loading">
        <v-progress-circular indeterminate color="primary"></v-progress-circular>
      </template>
      <template v-else-if="events.length === 0">
        <v-alert type="info" color="info" variant="tonal">
          <b>Nenhum evento encontrado</b>
        </v-alert>
      </template>
      <v-row v-else>
        <v-col cols="12" md="6" v-for="event in events" :key="event.id">
          <v-card class="event-card pa-4 d-flex flex-column align-start">
            <v-card-title>{{ event.name }}</v-card-title>
            <v-card-subtitle>
              {{ formatDate(event.start_date) }} - {{ formatDate(event.end_date) }}
            </v-card-subtitle>
            <v-card-text>{{ event.description }}</v-card-text>
            <!-- Applied Vuetify gap class for chips -->
            <div class="d-flex pl-3">
              <v-chip :color="getStatusColor(event.status)" class="mr-2" variant="elevated">
                {{ event.status }}
              </v-chip>
              <v-chip>{{ event.event_type }}</v-chip>
            </div>
          </v-card>
        </v-col>
      </v-row>
      <v-row justify="center" class="mt-4">
        <v-col cols="auto">
          <v-pagination
            :key="totalPages"
            v-model="currentPage"
            :length="totalPages"
            @input="fetchEvents"
          ></v-pagination>
        </v-col>
      </v-row>
    </v-col>
    <v-snackbar v-model="snackbar" :timeout="4000" top :color="snackbarColor">
      {{ snackbarMessage }}
    </v-snackbar>
  </v-row>
</template>

<script setup lang="ts">
import { fetchEvents } from '@/services/eventService'
import { ref, onMounted, watch, nextTick } from 'vue'
import { type Event } from '@/types/event'

const events = ref<Event[]>([])
const currentPage = ref(1)
const totalPages = ref(1)
const itemsPerPage = 6
const loading = ref(false)
const snackbar = ref(false)
const snackbarMessage = ref('')
const snackbarColor = ref('')

// Fetch events data
const fetchEventsData = async () => {
  loading.value = true
  const loadingTimeout = setTimeout(() => {
    loading.value = false
    snackbarMessage.value = 'O tempo de carregamento expirou. Tente novamente.'
    snackbarColor.value = 'error'
    snackbar.value = true
  }, 10000) // 10 seconds timeout

  try {
    const response = await fetchEvents(currentPage.value, itemsPerPage)
    events.value = response.data.results
    totalPages.value = Math.ceil(response.data.count / itemsPerPage)
    console.log(totalPages.value)
    await nextTick()
    clearTimeout(loadingTimeout)
  } catch (error) {
    console.error('Error fetching events:', error)
    snackbarMessage.value = 'Erro ao buscar eventos. Tente novamente.'
    snackbarColor.value = 'error'
    snackbar.value = true
  } finally {
    loading.value = false
  }
}

// Format the date to a more readable format
const formatDate = (date: string) => {
  return new Date(date).toLocaleDateString()
}

// Get the chip color based on event status
const getStatusColor = (status: string) => {
  switch (status) {
    case 'upcoming':
      return 'yellow'
    case 'ongoing':
      return 'blue'
    case 'completed':
      return 'green'
    case 'cancelled':
      return 'red'
    default:
      return 'gray'
  }
}

onMounted(() => {
  fetchEventsData()
})

watch(currentPage, () => {
  fetchEventsData()
})
</script>

<style scoped>
.event-card {
  transition:
    transform 0.2s,
    box-shadow 0.2s;
}

.event-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.v-chip {
  margin-right: 8px;
}
</style>
