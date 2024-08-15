<template>
    <v-row justify="center">
      <v-col cols="12" lg="10">
        <h2 class="text-h4 text-start mb-6 font-weight-bold">Locais</h2>
        <template v-if="loading">
          <v-progress-circular indeterminate color="primary"></v-progress-circular>
        </template>
        <template v-else-if="locals.length === 0">
          <v-alert type="info" color="info" variant="tonal">
            <b>Nenhum Local Encontrado</b>
          </v-alert>
        </template>
        <v-row v-else>
          <v-col cols="12" md="6" lg="4" v-for="local in locals" :key="local.id">
            <v-card
              class="mb-4 hover-elevation"
              @click="openDetailDialog(local)"
            >
              <v-card-title class="text-h6">{{ local.local_name }}</v-card-title>
              <v-card-text>
                <div><strong>Rua:</strong> {{ local.street_name }}</div>
                <div><strong>Cidade:</strong> {{ local.city }}</div>
                <div><strong>Estado:</strong> {{ local.state }}</div>
                <div><strong>Referência:</strong> {{ local.reference }}</div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-row justify="center" class="mt-4">
          <v-col cols="auto">
            <v-pagination
              v-model="currentPage"
              :length="totalPages"
              @input="fetchLocalsData"
            ></v-pagination>
          </v-col>
        </v-row>
        <v-btn @click="openDialog" color="primary" class="mt-4">
          <b>Adicionar Locais</b>
        </v-btn>
        <LocalForm :dialog="dialog" @update:dialog="dialog = $event" @local-added="onLocalAdded" />
      </v-col>
      <v-snackbar v-model="snackbar" :timeout="4000" top :color="snackbarColor">
        {{ snackbarMessage }}
      </v-snackbar>
  
      <!-- Dialog para detalhes do local -->
      <v-dialog v-model="detailDialog" max-width="600px">
        <v-card>
          <v-card-title class="text-h6">{{ selectedLocal.local_name }}</v-card-title>
          <v-card-text>
            <div><strong>Rua:</strong> {{ selectedLocal.street_name }}</div>
            <div><strong>Nº:</strong> {{ selectedLocal.street_number }}</div>
            <div><strong>Cidade:</strong> {{ selectedLocal.city }}</div>
            <div><strong>Estado:</strong> {{ selectedLocal.state }}</div>
            <div><strong>CEP:</strong> {{ selectedLocal.cep }}</div>
            <div><strong>Referência:</strong> {{ selectedLocal.reference }}</div>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="detailDialog = false" color="primary">Fechar</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </template>
  
    
  
  <script setup lang="ts">
  import { fetchLocations } from '@/services/localService'
  import { ref, onMounted, watch } from 'vue'
  import { type Local } from '@/types/local'
  import LocalForm from './LocalForm.vue'
  
  const locals = ref<Local[]>([])
  const currentPage = ref(1)
  const totalPages = ref(1)
  const itemsPerPage = 6
  const dialog = ref(false)
  const detailDialog = ref(false)
  const selectedLocal = ref<Local | null>(null)
  const loading = ref(false)
  const errorMessage = ref<string | null>(null)
  const snackbar = ref(false)
  const snackbarMessage = ref('')
  const snackbarColor = ref('')
  
  const openDialog = () => {
    dialog.value = true
  }
  
  const openDetailDialog = (local: Local) => {
    selectedLocal.value = local
    detailDialog.value = true
  }
  
  const fetchLocalsData = async () => {
    loading.value = true
    errorMessage.value = null
  
    const loadingTimeout = setTimeout(() => {
      loading.value = false
      errorMessage.value = 'O tempo de carregamento expirou. Tente novamente.'
    }, 10000) // 10 seconds timeout
  
    try {
      const response = await fetchLocations(currentPage.value, itemsPerPage)
      locals.value = response.data.results
      totalPages.value = Math.ceil(response.data.count / itemsPerPage)
      clearTimeout(loadingTimeout)
    } catch (error) {
      console.error('Error fetching sponsors:', error)
    } finally {
      loading.value = false
    }
  }
  
  onMounted(() => {
    fetchLocalsData()
  })
  
  watch(currentPage, () => {
    fetchLocalsData()
  })
  
  const onLocalAdded = (message: string) => {
    snackbarMessage.value = message
    snackbarColor.value = 'success'
    snackbar.value = true
    fetchLocalsData()
  }
  </script>
  
  <style scoped>
  .hover-elevation {
    transition: box-shadow 0.3s ease-in-out;
  }
  
  .hover-elevation:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  }
  </style>
  
  