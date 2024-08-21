<template>
    <v-row justify="center">
      <v-col cols="12" lg="10">
        <!-- Cabeçalho e filtros -->
        <v-row class="mb-6 align-center">
          <v-col cols="12" sm="6" class="text-start">
            <h2 class="text-h4 font-weight-bold">Meus Eventos Organizados</h2>
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
            <v-card class="event-card pa-4 d-flex flex-column align-start">
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
              <v-card-actions>
                <v-btn color="primary" @click="editEvent(event.id)">Editar</v-btn>
                <v-btn color="error" @click="confirmDelete(event.id)">Deletar</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row justify="center" class="mt-4">
          <v-col cols="auto">
            <v-pagination
              :key="totalPages"
              v-model="currentPage"
              :length="totalPages"
              @input="fetchEventsData"
            ></v-pagination>
          </v-col>
        </v-row>
      </v-col>
      <v-snackbar v-model="snackbar" :timeout="4000" top :color="snackbarColor">
        {{ snackbarMessage }}
      </v-snackbar>
      <v-dialog v-model="confirmDeleteDialog" max-width="500px">
        <v-card>
          <v-card-title class="headline">Confirmar Deleção</v-card-title>
          <v-card-text>Você tem certeza que deseja deletar este evento?</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" text @click="cancelDelete">Cancelar</v-btn>
            <v-btn color="red darken-1" text @click="deleteThisEvent">Deletar</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </template>
  
  <script setup lang="ts">
  import { fetchMyEvents, deleteEvent } from '@/services/eventService'
  import { ref, onMounted, watch, nextTick } from 'vue'
  import { type Event } from '@/types/event'
  import { useRouter, useRoute } from 'vue-router'
  
  const router = useRouter()
  const route = useRoute()
  
  const events = ref<Event[]>([])
  const currentPage = ref(1)
  const totalPages = ref(1)
  const itemsPerPage = 6
  const loading = ref(false)
  const snackbar = ref(false)
  const searchQuery = ref('')
  const snackbarMessage = ref('')
  const snackbarColor = ref('')
  
  // Variáveis para filtros
  const selectedStatus = ref<string | null>(null)
  const selectedType = ref<string | null>(null)
  const confirmDeleteDialog = ref(false)
  const eventIdToDelete = ref<number | null>(null)
  
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
  
  // Buscar eventos organizados por mim
  const fetchEventsData = async () => {
    loading.value = true
    const loadingTimeout = setTimeout(() => {
      loading.value = false
      snackbarMessage.value = 'O tempo de carregamento expirou. Tente novamente.'
      snackbarColor.value = 'error'
      snackbar.value = true
    }, 10000) // 10 segundos de timeout
  
    try {
      const response = await fetchMyEvents(
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
      fetchEventsData()
    }
  }
  
  // Formatar a data
  const formatDate = (date: string): string => {
    return new Date(date).toLocaleDateString()
  }
  
  // Obter a cor do chip com base no status do evento
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
  
  // Redirecionar para a página de edição
  const editEvent = (id: number): void => {
    router.push(`/events-organized/update/${id}`)
  }
  
  // Confirmar deleção
  const confirmDelete = (id: number): void => {
    eventIdToDelete.value = id
    confirmDeleteDialog.value = true
  }
  
  // Cancelar deleção
  const cancelDelete = (): void => {
    eventIdToDelete.value = null
    confirmDeleteDialog.value = false
  }
  
  // Deletar evento
  const deleteThisEvent = async () => {
    if (!eventIdToDelete.value) return
  
    try {
      await deleteEvent(eventIdToDelete.value)
      snackbarMessage.value = 'Evento deletado com sucesso!'
      snackbarColor.value = 'success'
      fetchEventsData()
    } catch (error) {
      console.error('Error deleting event:', error)
      snackbarMessage.value = 'Erro ao deletar evento. Tente novamente.'
      snackbarColor.value = 'error'
    } finally {
      snackbar.value = true
      confirmDeleteDialog.value = false
    }
  }
  
  // Verificar se o parâmetro de tipo de consulta existe e é válido
  onMounted(() => {
    const queryType = route.query.type as string | null
  
    if (queryType && eventTypes.some((type) => type.value === queryType)) {
      selectedType.value = queryType
    }
  
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
  