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
          <v-card class="mb-4 hover-elevation">
            <v-card-title class="text-h6">
              <strong>{{ local.local_name }}</strong>
            </v-card-title>
            <v-card-text>
              <div><strong>Rua:</strong> {{ local.street_name }}</div>
              <div><strong>Cidade:</strong> {{ local.city }}</div>
              <div><strong>Estado:</strong> {{ local.state }}</div>
              <div><strong>Referência:</strong> {{ local.reference }}</div>
            </v-card-text>
            <v-card-actions>
              <v-row class="d-flex flex-column flex-md-row">
                <v-btn @click.stop="openDetailDialog(local)" color="light-blue lighten-3" text-color="white" class="custom-btn mb-2 mb-md-0 mr-md-2">Ver</v-btn>
                <v-btn @click.stop="openEditDialog(local)" color="amber lighten-3" text-color="black" class="custom-btn mb-2 mb-md-0 mr-md-2">Editar</v-btn>
                <v-btn @click.stop="openDeleteDialog(local)" color="red lighten-4" text-color="black" class="custom-btn">Excluir</v-btn>
              </v-row>
            </v-card-actions>
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
      <LocalDetailDialog :dialog="detailDialog" :local="selectedLocal" @update:dialog="detailDialog = $event" />
      <LocalEditDialog
        :dialog="editDialog"
        :local="selectedLocal"
        @update:dialog="editDialog = $event"
        @local-updated="onLocalUpdated"
      />
      <LocalDeleteDialog :dialog="deleteDialog" :local="selectedLocal" @update:dialog="deleteDialog = $event" @local-deleted="onLocalDeleted" />
    </v-col>
    <v-snackbar v-model="snackbar" :timeout="4000" top :color="snackbarColor">
      {{ snackbarMessage }}
    </v-snackbar>
  </v-row>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import { fetchLocations } from '@/services/localService';
import type { Local } from '@/types/local';
import LocalForm from './LocalForm.vue';
import LocalDetailDialog from './LocalDetail.vue';
import LocalEditDialog from './LocalEdit.vue';
import LocalDeleteDialog from './LocalDelete.vue';

const locals = ref<Local[]>([]);
const currentPage = ref(1);
const totalPages = ref(1);
const itemsPerPage = 6;
const dialog = ref(false);
const detailDialog = ref(false);
const editDialog = ref(false);
const deleteDialog = ref(false);
const selectedLocal = ref<Local | null>(null);
const loading = ref(false);
const errorMessage = ref<string | null>(null);
const snackbar = ref(false);
const snackbarMessage = ref('');
const snackbarColor = ref('');

const openDialog = () => {
  dialog.value = true;
};

const openDetailDialog = (local: Local) => {
  selectedLocal.value = local;
  detailDialog.value = true;
};

const openEditDialog = (local: Local) => {
  selectedLocal.value = local;
  editDialog.value = true;
};

const openDeleteDialog = (local: Local) => {
  selectedLocal.value = local;
  deleteDialog.value = true;
};

const fetchLocalsData = async () => {
  loading.value = true;
  errorMessage.value = null;

  const loadingTimeout = setTimeout(() => {
    loading.value = false;
    errorMessage.value = 'O tempo de carregamento expirou. Tente novamente.';
  }, 10000); // 10 seconds timeout

  try {
    const response = await fetchLocations(currentPage.value, itemsPerPage);
    locals.value = response.data.results;
    totalPages.value = Math.ceil(response.data.count / itemsPerPage);
    clearTimeout(loadingTimeout);
  } catch (error) {
    console.error('Error fetching locations:', error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchLocalsData();
});

watch(currentPage, () => {
  fetchLocalsData();
});

const onLocalAdded = (message: string, color: string) => {
  snackbarMessage.value = message;
  snackbarColor.value = color;
  snackbar.value = true;
  fetchLocalsData();
};

const onLocalUpdated = (message: string, color: string) => {
  snackbarMessage.value = message;
  snackbarColor.value = color;
  snackbar.value = true;
  fetchLocalsData();
};

const onLocalDeleted = (message: string, color: string) => {
  snackbarMessage.value = message;
  snackbarColor.value = color;
  snackbar.value = true;
  fetchLocalsData();
};
</script>

<style scoped>
.custom-btn {
  transition: background-color 0.3s ease, color 0.3s ease;
}

.custom-btn:hover {
  background-color: lighten(#ffffff, 10%);
  color: darken(#000000, 10%);
}
</style>
