<template>
  <v-row justify="center">
    <v-col cols="12" lg="10">
      <!-- New row for filters and header -->
      <v-row class="mb-6 align-center">
        <v-col cols="6" class="text-start">
          <h2 class="text-h4 font-weight-bold">Eventos</h2>
        </v-col>
        <v-col cols="6" class="d-flex justify-end">
          <v-text-field
            v-model="searchQuery"
            label="Buscar Evento"
            dense
            outlined
            hide-details
            class="mr-4"
            @keydown="handleKeydown"
          ></v-text-field>
          <v-select
            v-model="selectedStatus"
            :items="statuses"
            label="Status"
            dense
            outlined
            hide-details
            class="mr-4"
          ></v-select>
          <v-select
            v-model="selectedType"
            :items="eventTypes"
            label="Tipo de Evento"
            dense
            outlined
            hide-details
          ></v-select>
        </v-col>
      </v-row>

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
          <v-card
            class="event-card pa-4 d-flex flex-column align-start"
            @click="goToEvent(event.id)"
          >
            <v-card-title>{{ event.name }}</v-card-title>
            <v-card-subtitle>
              {{ formatDate(event.start_date) }} - {{ formatDate(event.end_date) }}
            </v-card-subtitle>
            <v-card-text>{{ event.description }}</v-card-text>
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
import { useRouter } from 'vue-router'

const router = useRouter()

const events = ref<Event[]>([])
const currentPage = ref(1)
const totalPages = ref(1)
const itemsPerPage = 6
const loading = ref(false)
const snackbar = ref(false)
const searchQuery = ref('')
const snackbarMessage = ref('')
const snackbarColor = ref('')

// Filter variables
const selectedStatus = ref<string | null>(null)
const selectedType = ref<string | null>(null)

const statuses = ['upcoming', 'ongoing', 'completed', 'cancelled']
const eventTypes = ['conference', 'workshop', 'seminar', 'meetup']

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
    const response = await fetchEvents(
      currentPage.value,
      itemsPerPage,
      selectedStatus.value,
      selectedType.value,
      searchQuery.value
    )
    events.value = response.data.results
    totalPages.value = Math.ceil(response.data.count / itemsPerPage)
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

const handleKeydown = (event: KeyboardEvent) => {
  if (event.key === 'Enter') {
    fetchEventsData()
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

const goToEvent = (id: number) => {
  router.push(`/events/${id}`)
}

onMounted(() => {
  fetchEventsData()
})

watch([currentPage, selectedStatus, selectedType], () => {
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
