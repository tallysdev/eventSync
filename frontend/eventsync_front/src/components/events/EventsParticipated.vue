<template>
  <v-row justify="center">
    <v-col cols="12" lg="10">
      <!-- New row for filters and header -->
      <v-row class="mb-6 align-center">
        <v-col cols="12" sm="6" class="text-start">
          <h2 class="text-h4 font-weight-bold">Meus Eventos Participados</h2>
        </v-col>
        <v-col cols="12" sm="6" class="d-flex justify-end flex-column flex-sm-row">
          <v-text-field
            v-model="searchQuery"
            label="Buscar Evento"
            dense
            outlined
            hide-details
            class="mr-sm-4 mb-4 mb-sm-0"
            @keydown="handleKeydown"
          ></v-text-field>
          <v-select
            v-model="selectedStatus"
            :items="statuses"
            label="Status"
            dense
            outlined
            hide-details
            class="mr-sm-4 mb-4 mb-sm-0"
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
            <!-- Botão de Gerar Certificado -->
            <v-btn
              color="success"
              class="mt-4"
              @click="handleGenerateCertificate(event)"
            >
              Gerar Certificado
            </v-btn>
          </v-card>
        </v-col>
      </v-row>
      <v-row justify="center" class="mt-4">
        <v-col cols="auto">
          <v-pagination
            :key="totalPages"
            v-model="currentPage"
            :length="totalPages"
            @input="fetchEventsPresenceData"
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
import { fetchEventsPresence } from '@/services/eventService'
import { gerarCertificado } from '@/utils/certificate'
import { ref, onMounted, watch, nextTick } from 'vue'
import { type Event } from '@/types/event'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

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

const statuses = [
  { title: 'Todos', value: null },
  { title: 'Próximos', value: 'upcoming' },
  { title: 'Em andamento', value: 'ongoing' },
  { title: 'Concluídos', value: 'completed' },
  { title: 'Cancelados', value: 'cancelled' }
]

const eventTypes = [
  { title: 'Todos', value: null },
  { title: 'Conferência', value: 'conference' },
  { title: 'Oficina', value: 'workshop' },
  { title: 'Seminário', value: 'seminar' },
  { title: 'Encontro', value: 'meetup' }
]

// Fetch events data
const fetchEventsPresenceData = async () => {
  loading.value = true
  const loadingTimeout = setTimeout(() => {
    loading.value = false
    snackbarMessage.value = 'O tempo de carregamento expirou. Tente novamente.'
    snackbarColor.value = 'error'
    snackbar.value = true
  }, 10000) // 10 seconds timeout

  try {
    const response = await fetchEventsPresence(
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

const handleKeydown = (event: KeyboardEvent): void => {
  if (event.key === 'Enter') {
    fetchEventsPresenceData()
  }
}

// Format the date to a more readable format
const formatDate = (date: string): string => {
  return new Date(date).toLocaleDateString()
}

// Get the chip color based on event status
const getStatusColor = (status: string): string => {
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

const handleGenerateCertificate = async (event: Event) => {
  try {
    await gerarCertificado(
      authStore.getUser.name,
      authStore.getUser.cpf, // Substitua pelo nome do usuário
      event.name,
      event.hours_quantity, // Substitua pela duração do evento
      event.start_date,
      event.end_date,
      event.id
    )
    snackbarMessage.value = 'Certificado gerado com sucesso!'
    snackbarColor.value = 'success'
  } catch (error) {
    console.error('Erro ao gerar certificado:', error)
    snackbarMessage.value = 'Erro ao gerar certificado. Tente novamente.'
    snackbarColor.value = 'error'
  } finally {
    snackbar.value = true
  }
}

// Check if the query parameter for type exists and is valid
onMounted(() => {
  const queryType = route.query.type as string | null

  if (queryType && eventTypes.some((type) => type.value === queryType)) {
    selectedType.value = queryType
  }

  fetchEventsPresenceData()
})

watch([currentPage, selectedStatus, selectedType], () => {
  fetchEventsPresenceData()
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
