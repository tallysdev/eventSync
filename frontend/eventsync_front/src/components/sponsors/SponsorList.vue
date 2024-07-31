<template>
  <v-row justify="center">
    <v-col cols="12" lg="10">
      <h2 class="text-h4 text-start mb-6 font-weight-bold">Patrocinadores</h2>
      <template v-if="sponsors.length === 0">
        <v-alert type="info" color="info" variant="tonal">
          <b> Nenhum patrocinador encontrado </b>
        </v-alert>
      </template>
      <v-row v-else>
        <v-col cols="12" md="6" v-for="sponsor in sponsors" :key="sponsor.id">
          <v-card>
            <v-card-title>{{ sponsor.name }}</v-card-title>
            <v-card-subtitle>{{ sponsor.email }}</v-card-subtitle>
            <v-card-text>{{ sponsor.description }}</v-card-text>
            <v-avatar size="100">
              <v-img :src="sponsor.logo"></v-img>
            </v-avatar>
          </v-card>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '@/services/api'
import { type Sponsor } from '@/types/sponsor'

const sponsors = ref<Sponsor[]>([])

const fetchSponsors = async () => {
  try {
    const response = await api.get('sponsors/')
    sponsors.value = response.data.results
    console.log(sponsors.value)
  } catch (error) {
    console.error(error)
  }
}

onMounted(() => {
  fetchSponsors()
})
</script>

<style scoped></style>
