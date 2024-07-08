<template>
  <section class="d-block">
    <!-- TODO: Make the event clickable and redirect to the event -->
    <v-row justify="center">
      <v-col cols="12" lg="10">
        <h2 class="text-h4 text-start mb-6 font-weight-bold">Eventos próximos</h2>
        <v-carousel height="500" show-arrows="hover" class="rounded-xl no-gap-carousel">
          <v-carousel-item v-for="event in upcomingEvents" :key="event.id">
            <v-row>
              <v-col cols="8" class="bg-primary hidden-sm-and-down">
                <div class="event-image-placeholder"></div>
              </v-col>
              <v-col cols="12" lg="4" class="m-0 pa-4 event-details bg-white">
                <div class="d-flex flex-column align-start justify-flex-start h-100 pl-4">
                  <div class="d-flex flex-column h-75 mt-4">
                    <p class="primary--text text-h6 font-weight-bold">
                      {{ event.date }} - {{ event.time }}
                    </p>
                    <h1 class="text-h4 font-weight-bold text-left event-title">{{ event.name }}</h1>
                    <p class="text-h6 font-weight-light" color="primary">{{ event.location }}</p>
                  </div>
                  <v-btn color="primary black--text mt-14" variant="outlined" dark>
                    <b>Ver detalhes</b>
                  </v-btn>
                </div>
              </v-col>
            </v-row>
          </v-carousel-item>
        </v-carousel>
      </v-col>
    </v-row>
  </section>
</template>

<script setup lang="ts">
defineProps({
  upcomingEvents: {
    type: Array,
    required: true
  }
})
</script>

<style scoped>
.no-gap-carousel {
  position: relative;
}

:deep(.v-carousel__controls) {
  bottom: 0 !important;
  align-items: center !important;
  /* margin-bottom: 38px !important; */
  width: 100% !important;
  /* border-radius: 0px 0px 24px 24px !important;
  background-color: transparent !important; */
  color: white !important;
}

.event-image-placeholder {
  width: 100%;
  height: 400px;
}

.event-details {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
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
