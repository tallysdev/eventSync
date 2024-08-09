<template>
  <v-row justify="center">
    <v-col cols="12" lg="10">
      <h2 class="text-h4 text-start mb-6 font-weight-bold">Patrocinadores</h2>
      <template v-if="loading">
        <v-progress-circular indeterminate color="primary"></v-progress-circular>
      </template>
      <template v-else-if="sponsors.length === 0">
        <v-alert type="info" color="info" variant="tonal">
          <b>Nenhum patrocinador encontrado</b>
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
      <v-row justify="center" class="mt-4">
        <v-col cols="auto">
          <v-pagination
            v-model="currentPage"
            :length="totalPages"
            @input="fetchSponsors"
          ></v-pagination>
        </v-col>
      </v-row>
      <v-btn @click="openDialog" color="primary" class="mt-4">
        <b> Adicionar Patrocinador </b>
      </v-btn>
      <SponsorForm :dialog="dialog" @update:dialog="dialog = $event" @sponsor-added="onSponsorAdded" />
    </v-col>
    <v-snackbar v-model="snackbar" :timeout="4000" top :color="snackbarColor" p>
      {{ snackbarMessage }}
    </v-snackbar>
  </v-row>
</template>

<script setup lang="ts">
import { fetchSponsors } from '@/services/sponsorService'
import { ref, onMounted, watch } from 'vue'
import { type Sponsor } from '@/types/sponsor'
import SponsorForm from './SponsorForm.vue'

const sponsors = ref<Sponsor[]>([])
const currentPage = ref(1)
const totalPages = ref(1)
const itemsPerPage = 6
const dialog = ref(false)
const loading = ref(false)
const errorMessage = ref<string | null>(null)
const snackbar = ref(false)
const snackbarMessage = ref('')
const snackbarColor = ref('')

const openDialog = () => {
  dialog.value = true
}

const fetchSponsorsData = async () => {
  loading.value = true
  errorMessage.value = null

  const loadingTimeout = setTimeout(() => {
    loading.value = false
    errorMessage.value = 'O tempo de carregamento expirou. Tente novamente.'
  }, 10000) // 10 seconds timeout

  try {
    const response = await fetchSponsors(currentPage.value, itemsPerPage)
    sponsors.value = response.data.results
    totalPages.value = Math.ceil(response.data.count / itemsPerPage)
    clearTimeout(loadingTimeout)
  } catch (error) {
    console.error('Error fetching sponsors:', error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchSponsorsData()
})

watch(currentPage, () => {
  fetchSponsorsData()
})

const onSponsorAdded = (message: string) => {
  snackbarMessage.value = message
  snackbarColor.value = 'success'
  snackbar.value = true
  fetchSponsorsData()
}
</script>

<style scoped></style>
