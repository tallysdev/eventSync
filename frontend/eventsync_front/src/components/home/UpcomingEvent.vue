<template>
  <section class="d-block">
    <v-row justify="center">
      <v-col cols="12" lg="10">
        <h2 class="text-h4 text-start mb-6 font-weight-bold">Eventos próximos</h2>
        <v-carousel
          v-if="upcomingEvents.length > 0"
          height="500"
          show-arrows="hover"
          class="rounded-xl position-relative"
        >
          <v-carousel-item v-for="event in upcomingEvents" :key="event.id">
            <v-row class="no-gutters height93">
              <v-col cols="12" md="8" class="bg-primary d-none d-md-flex">
                <div class="h-100 w-100"></div>
              </v-col>
              <v-col cols="12" md="4" class="m-0 pa-4 event-details bg-white">
                <div class="d-flex flex-column align-start justify-flex-start h-100">
                  <div class="d-flex flex-column h-75 mt-4">
                    <div class="d-flex align-center mb-2">
                      <v-icon class="mr-2" color="background">mdi-calendar</v-icon>
                      <p class="primary--text text-h6 font-weight-bold">
                        {{ formatDate(event.start_date) }} - {{ formatDate(event.end_date) }}
                      </p>
                    </div>
                    <h1 class="text-h4 font-weight-bold text-left event-title">
                      {{ event.name }}
                    </h1>
                    <div class="d-flex align-center mb-2" v-if="locations[event.local]">
                      <v-icon class="mr-2" color="background">mdi-map-marker</v-icon>
                      <p class="text-h6 font-weight-light primary--text">
                        {{ locations[event.local].local_name }},
                        {{ locations[event.local].street_name }}
                        {{ locations[event.local].street_number }},
                        {{ locations[event.local].city }} -
                        {{ locations[event.local].state }}
                      </p>
                    </div>
                    <p class="text-h5">
                      {{ event.description }}
                    </p>
                  </div>
                  <v-btn
                    color="primary black--text mt-14"
                    variant="outlined"
                    dark
                    @click="goToEvent(event.id)"
                  >
                    <b>Ver detalhes</b>
                  </v-btn>
                </div>
              </v-col>
            </v-row>
          </v-carousel-item>
        </v-carousel>
        <div v-else class="text-center mt-10">
          <p class="text-h5 primary--text">Nenhum evento próximo disponível.</p>
        </div>
      </v-col>
    </v-row>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { fetchEvents, fetchLocal } from '@/services/eventService'
import { useRouter } from 'vue-router'
import { formatDate } from '@/utils/formatDate'
import type { Event } from '@/types/event'
import type { Local } from '@/types/local'

const router = useRouter()
const upcomingEvents = ref<Event[]>([])
const locations = ref<Record<number, Local>>({})

const fetchLocationDetails = async (localId: number): Promise<void> => {
  try {
    if (!locations.value[localId]) {
      const response = await fetchLocal(localId)
      locations.value[localId] = response.data
    }
  } catch (error) {
    console.error('Error fetching local detail:', error)
  }
}

const fetchUpcomingEvents = async () => {
  const response = await fetchEvents(1, 4, 'upcoming')
  const events = response.data.results as Event[]

  for (const event of events) {
    if (event.local) {
      await fetchLocationDetails(event.local)
    }
  }

  upcomingEvents.value = events
}

const goToEvent = (id: number | undefined): void => {
  if (!id) return
  router.push(`/events/${id}`)
}

onMounted(() => {
  fetchUpcomingEvents()
})
</script>

<style scoped>
.no-gap-carousel {
  position: relative;
}
.height93 {
  height: 93%;
}
/* Additional styles */
</style>
