<template>
  <v-row justify="center">
    <v-col cols="12" lg="10">
      <v-row class="mb-6 align-center">
        <v-col cols="12" sm="6" class="text-start">
          <h2 class="text-h4 font-weight-bold">Participantes do Evento</h2>
        </v-col>
      </v-row>

      <template v-if="loading">
        <v-progress-circular indeterminate color="primary"></v-progress-circular>
      </template>
      <template v-else-if="participants.length === 0">
        <v-alert type="info" color="info" variant="tonal">
          <b>Nenhum participante encontrado</b>
        </v-alert>
      </template>
      <v-row v-else>
        <v-col cols="12" md="6" v-for="participant in participants" :key="participant.id">
          <v-card class="participant-card pa-4 d-flex flex-column align-start">
            <v-card-title>{{ participant.name }}</v-card-title>
            <v-card-subtitle>{{ participant.email }}</v-card-subtitle>
            <v-card-text>{{ participant.registration_date }}</v-card-text>
            <v-card-actions v-if="isOrganizer">
              <template v-if="!participant.isPresent">
                <v-btn color="primary" @click="markAsApproved(participant.id)">
                  Marcar presença
                </v-btn>
              </template>
              <template v-else>
                <v-alert type="success" color="success" variant="filled">Já presente</v-alert>
              </template>
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
            @input="fetchParticipantsData"
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
import {
  markParticipantAsApproved,
  fetchOrganizerId,
  checkPresenceStatus
} from '@/services/eventService'
import { fetchParticipants } from '@/services/participantsService'
import { ref, onMounted, watch, nextTick } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()
const route = useRoute()

const participants = ref([])
const currentPage = ref(1)
const totalPages = ref(1)
const itemsPerPage = 10
const loading = ref(false)
const snackbar = ref(false)
const snackbarMessage = ref('')
const snackbarColor = ref('')
const isOrganizer = ref(false)

const fetchParticipantsData = async () => {
  loading.value = true
  const loadingTimeout = setTimeout(() => {
    loading.value = false
    snackbarMessage.value = 'O tempo de carregamento expirou. Tente novamente.'
    snackbarColor.value = 'error'
    snackbar.value = true
  }, 10000) // 10 segundos de timeout

  try {
    const eventId = route.params.id
    const response = await fetchParticipants(Number(eventId))
    participants.value = response.data.results

    // Check presence status for each participant
    for (const participant of participants.value) {
      participant.isPresent = await checkPresence(Number(eventId), participant.id)
    }

    totalPages.value = Math.ceil(response.data.count / itemsPerPage)
    await nextTick()
    clearTimeout(loadingTimeout)
  } catch (error) {
    console.error('Error fetching participants:', error)
    snackbarMessage.value = 'Erro ao buscar participantes. Tente novamente.'
    snackbarColor.value = 'error'
    snackbar.value = true
  } finally {
    loading.value = false
  }
}

const checkIfOrganizer = async () => {
  const eventId = Number(route.params.id)
  const userId = auth.profile.id
  try {
    const organizerId = await fetchOrganizerId(eventId)
    isOrganizer.value = organizerId.data.id === userId
  } catch (error) {
    if (error.response && error.response.data && error.response.data.detail === 'Não encontrado.') {
      snackbarMessage.value = 'Você não é organizador deste evento.'
    } else {
      snackbarMessage.value = 'Erro ao verificar organizador.'
    }
    snackbarColor.value = 'error'
    snackbar.value = true
  }
}

const markAsApproved = async (participantId: number) => {
  try {
    // Check current presence status before marking as approved
    const eventId = Number(route.params.id)
    const isPresent = await checkPresence(eventId, participantId)

    if (!isPresent) {
      await markParticipantAsApproved(eventId, participantId)
      // Update local state
      const participant = participants.value.find((p) => p.id === participantId)
      if (participant) {
        participant.isPresent = true
      }
      snackbarMessage.value = 'Participante aprovado com sucesso!'
      snackbarColor.value = 'success'
      snackbar.value = true
    } else {
      snackbarMessage.value = 'Participante já está presente.'
      snackbarColor.value = 'info'
      snackbar.value = true
    }
  } catch (error) {
    console.error('Error approving participant:', error)
    snackbarMessage.value = 'Erro ao aprovar participante. Tente novamente.'
    snackbarColor.value = 'error'
    snackbar.value = true
  }
}

const checkPresence = async (eventId: number, participantId: number) => {
  try {
    const response = await checkPresenceStatus(eventId, participantId)
    return response.data.presence
  } catch (error) {
    console.error('Error checking presence:', error)
    return false
  }
}

// Fetch participants when the component is mounted
onMounted(() => {
  fetchParticipantsData()
  checkIfOrganizer()
})

// Refetch participants when the current page changes
watch(currentPage, () => {
  fetchParticipantsData()
})
</script>

<style scoped>
.participant-card {
  transition:
    transform 0.2s,
    box-shadow 0.2s;
}

.participant-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}
</style>
