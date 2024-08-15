<template>
  <v-container fluid class="pa-4 d-flex flex-column h-100 w-100">
    <v-row v-if="event" justify="center">
      <v-col cols="12" lg="10">
        <!-- Event Header Section -->
        <v-row class="mb-4 align-center">
          <v-col cols="6" class="text-start">
            <h1 class="text-h4 mb-2">{{ event.name }}</h1>
            <div class="d-flex align-center mb-2">
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
          <v-col cols="6" class="d-flex justify-end align-end">
            <v-btn color="primary" class="text-no-wrap">Inscrever-se</v-btn>
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
  </v-container>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { fetchEvent } from '@/services/eventService'
import { fetchLocal } from '@/services/eventService'
import { type Event } from '@/types/event'
import { type Local } from '@/types/event'

const route = useRoute()
const event = ref<Event | null>(null)
const local = ref<Local | null>(null)

// Fetch event detail based on route parameter
const fetchEventDetailData = async () => {
  const eventId = Number(route.params.id)
  try {
    const response = await fetchEvent(eventId)
    event.value = response.data
    await fetchLocalData(event.value.local)
  } catch (error) {
    console.error('Error fetching event detail:', error)
  }
}

// Fetch local detail based on event's local_id
const fetchLocalData = async (localId: string) => {
  try {
    const localIdNumber = Number(localId)
    const response = await fetchLocal(localIdNumber)
    console.log(response, localIdNumber)
    local.value = response.data
  } catch (error) {
    console.error('Error fetching local detail:', error)
  }
}

const formatDate = (date: string) => {
  return new Date(date).toLocaleDateString(undefined, {
    weekday: 'long',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(() => {
  fetchEventDetailData()
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
