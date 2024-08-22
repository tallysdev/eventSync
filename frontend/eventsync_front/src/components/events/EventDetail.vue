<template>
  <v-container fluid class="pa-4 d-flex flex-column h-100 w-100">
    <v-row v-if="event" justify="center">
      <v-col cols="12" lg="10">
        <!-- Event Header Section -->
        <v-row class="mb-4 align-center">
          <v-col cols="12" md="6" class="text-start">
            <h1 class="text-h4 mb-4">{{ event.name }}</h1>
            <div class="d-flex align-center mb-4">
              <v-icon class="mr-1">mdi-calendar</v-icon>
              <span>{{ formatDate(event.start_date) }} - {{ formatDate(event.end_date) }}</span>
            </div>
            <div class="d-flex align-center" v-if="local">
              <v-icon class="mr-1">mdi-map-marker</v-icon>
              <span
                >{{ local.local_name }}, {{ local.street_name }} {{ local.street_number }},
                {{ local.city }} - {{ local.state }}</span
              >
            </div>
          </v-col>
          <v-col cols="12" md="6" class="d-flex justify-end align-end">
            <template v-if="isSubscribed">
              <v-btn color="success" class="text-no-wrap mr-2" disabled>
                <b>Inscrito</b>
              </v-btn>
              <v-btn @click="handleUnsubscription" color="error" class="text-no-wrap">
                <b>Cancelar Inscrição</b>
              </v-btn>
            </template>
            <v-btn v-else @click="handleSubscription" color="primary" class="text-no-wrap">
              <b>Inscrever-se</b>
            </v-btn>
          </v-col>
        </v-row>

        <!-- Event Description Section -->
        <v-card class="pa-4">
          <h4 class="text-h6 mb-4">Descrição do evento</h4>
          <v-card-text>{{ event.description }}</v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row v-else justify="center">
      <v-col cols="12" class="text-center">
        <v-alert type="info" color="info" variant="tonal">
          <b>Evento não encontrado</b>
        </v-alert>
      </v-col>
    </v-row>

    <!-- Snackbar -->
    <v-snackbar v-model="showSnackbar" :color="snackbarColor" timeout="4000" top>
      {{ snackbarMessage }}
    </v-snackbar>
  </v-container>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import {
  fetchEvent,
  fetchLocal,
  signupForEvent,
  cancelSubscription,
  checkUserSubscription
} from '@/services/eventService'
import { type Event } from '@/types/event'
import { type Local } from '@/types/local'
import type { AxiosError } from 'axios'
import { formatDate } from '@/utils/formatDate'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const event = ref<Event | null>(null)
const local = ref<Local | null>(null)
const isSubscribed = ref(false)

const showSnackbar = ref(false)
const snackbarMessage = ref('')
const snackbarColor = ref('')

const fetchEventDetailData = async () => {
  const eventId = Number(route.params.id)
  try {
    const response = await fetchEvent(eventId)
    event.value = response.data
    if (event.value && event.value.local) {
      await fetchLocalData(Number(event.value.local))
    }
  } catch (error) {
    console.error('Error fetching event detail:', error)
  }
}

const fetchLocalData = async (localId: number) => {
  try {
    const response = await fetchLocal(localId)
    local.value = response.data
  } catch (error) {
    console.error('Error fetching local detail:', error)
  }
}

const checkSubscriptionStatus = async () => {
  if (authStore.isAuthenticated && event.value) {
    try {
      if (event.value.id) {
        const response = await checkUserSubscription(event.value.id, authStore.getUser?.id ?? 0)
        isSubscribed.value = response.data
      }
    } catch (error) {
      console.error('Error checking subscription status:', error)
    }
  }
}

const handleSubscription = async () => {
  if (authStore.isAuthenticated && event.value) {
    try {
      if (event.value.id) {
        await signupForEvent(event.value.id, authStore.getUser?.id ?? 0)
        snackbarMessage.value = 'Inscrição realizada com sucesso!'
        snackbarColor.value = 'success'
        isSubscribed.value = true
      }
    } catch (error) {
      handleSubscriptionError(error)
    }
  } else {
    snackbarMessage.value = 'Você precisa estar logado para se inscrever.'
    snackbarColor.value = 'error'
    showSnackbar.value = true
    setTimeout(() => {
      router.push('/login')
    }, 2000)
    return
  }
  showSnackbar.value = true
}

const handleUnsubscription = async () => {
  if (authStore.isAuthenticated && event.value) {
    try {
      if (event.value.id) await cancelSubscription(event.value.id, authStore.getUser?.id ?? 0)
      snackbarMessage.value = 'Inscrição cancelada com sucesso!'
      snackbarColor.value = 'success'
      isSubscribed.value = false
    } catch (error) {
      snackbarMessage.value = 'Erro ao cancelar inscrição.'
      snackbarColor.value = 'error'
    }
  } else {
    snackbarMessage.value = 'Você precisa estar logado para cancelar a inscrição.'
    snackbarColor.value = 'error'
  }
  showSnackbar.value = true
}

const handleSubscriptionError = (error: unknown) => {
  console.error('Error signing up for event:', error)
  const axiosError = error as AxiosError

  interface ErrorResponse {
    non_field_errors?: string[]
  }

  if (axiosError.response?.data) {
    const responseData = axiosError.response.data as ErrorResponse

    if (responseData.non_field_errors) {
      if (
        responseData.non_field_errors.includes('Os campos user, event devem criar um set único.')
      ) {
        snackbarMessage.value = 'Usuário já está inscrito nesse evento.'
        isSubscribed.value = true
      }
    }
  } else {
    snackbarMessage.value = 'Erro ao realizar inscrição.'
  }
  snackbarColor.value = 'error'
  showSnackbar.value = true
}

onMounted(async () => {
  await fetchEventDetailData()
  await checkSubscriptionStatus()
})
</script>

<style scoped>
.text-h4 {
  font-weight: bold;
}

.text-h6 {
  font-weight: bold;
}
</style>
