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
                    <div class="d-flex align-center mb-2">
                      <v-icon class="mr-2" color="background">mdi-map-marker</v-icon>
                      <p class="text-h6 font-weight-light primary--text">
                        {{ event.locationDetails.local_name }},
                        {{ event.locationDetails.street_name }}
                        {{ event.locationDetails.street_number }},
                        {{ event.locationDetails.city }} -
                        {{ event.locationDetails.state }}
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

const router = useRouter()
const upcomingEvents = ref([])

const fetchLocationDetails = async (localId: number) => {
  try {
    const response = await fetchLocal(localId)
    return response.data
  } catch (error) {
    console.error('Error fetching local detail:', error)
    return null
  }
}

const fetchUpcomingEvents = async () => {
  const response = await fetchEvents(1, 4, 'upcoming')
  const events = response.data.results

  // Fetch location details for each event
  for (const event of events) {
    if (event.local) {
      event.locationDetails = await fetchLocationDetails(event.local)
    } else {
      event.locationDetails = {}
    }
  }

  upcomingEvents.value = events
}

const goToEvent = (id: number): void => {
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
:deep(.v-carousel__controls) {
  bottom: 0 !important;
  align-items: center !important;
  width: 100% !important;
  color: white !important;
}

.event-details {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  height: 100%;
}

.event-details h3 {
  margin: 0;
  color: black;
}

.event-details p.primary--text {
  color: #3b5998;
}

.event-details p {
  margin: 10px 0;
}

@media (max-width: 601px) {
  .event-title {
    font-size: 1.5rem !important;
  }
}
</style>
