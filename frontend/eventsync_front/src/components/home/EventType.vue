<template>
  <section class="d-block my-10">
    <v-row justify="center">
      <v-col cols="12" lg="10">
        <h2 class="text-h4 text-start mb-6 font-weight-bold">Escolha o seu tipo de evento</h2>
        <v-row class="d-flex justify-center">
          <v-col
            cols="auto"
            lg="2"
            v-for="type in eventTypes"
            :key="type.value"
            class="text-center"
            @click="redirectToEventList(type.value)"
            style="cursor: pointer"
          >
            <v-avatar size="100" color="primary">
              <v-icon size="50">{{ type.icon }}</v-icon>
            </v-avatar>
            <span class="d-block mt-6 text-h6">{{ type.title }}</span>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </section>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const eventTypes = [
  { title: 'Todos', value: null, icon: 'mdi-calendar' },
  { title: 'Conferência', value: 'conference', icon: 'mdi-account-group' },
  { title: 'Oficina', value: 'workshop', icon: 'mdi-lightbulb-outline' },
  { title: 'Seminário', value: 'seminar', icon: 'mdi-school' },
  { title: 'Encontro', value: 'meetup', icon: 'mdi-handshake' }
]

const redirectToEventList = (type: string | null) => {
  router.push({ name: 'events', query: { type } })
}
</script>

<style scoped></style>
