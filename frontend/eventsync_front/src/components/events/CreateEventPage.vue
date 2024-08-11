<template>
  <v-app class="d-flex flex-column w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mb-10">
      <v-container fluid class="pa-6 d-flex flex-column align-center">
        <h1 class="form-title">Crie seu Evento</h1>
        <v-form ref="form" v-model="valid" lazy-validation 
          @submit.prevent="submitForm"
          class="pa-3 d-flex flex-column align-center max-width-form"
        >
          <v-text-field
            v-model="name"
            label="Nome do Evento"
            required
            class="field-size"
          ></v-text-field>
          <v-text-field
            v-model="start_date"
            label="Data de Início do Evento"
            type="date"
            required
            class="field-size"
          ></v-text-field>
          <v-text-field
            v-model="end_date"
            label="Data de Fim do Evento"
            type="date"
            required
            class="field-size"
          ></v-text-field>
          <v-select
            class="field-size"
            :label="'Localização do Evento'"
            v-model="location"
            :items="locations"
            item-title="local_name"
            item-value="id"
            required
            :hint="locations.length === 0 ? 'Nenhum local disponível' : ''"
            :persistent-hint="true"
          ></v-select>
          <v-select
            v-model="event_type"
            :items="eventTypeOptions"
            label="Tipo do Evento"
            required
            class="field-size"
          ></v-select>
          <v-text-field
            v-model="min_quantity"
            label="Quantidade Mínima de Participantes"
            type="number"
            required
            class="field-size"
            min="1"
            @keypress="validateNumberInput"
          ></v-text-field>
          <v-text-field
            v-model="max_quantity"
            label="Quantidade Máxima de Participantes"
            type="number"
            required
            class="field-size"
            min="1"
            @keypress="validateNumberInput"
          ></v-text-field>
          <v-text-field
            v-model="hours_quantity"
            label="Quantidade de Horas"
            type="number"
            required
            class="field-size"
            min="1"
            @keypress="validateNumberInput"
          ></v-text-field>
          <v-textarea
            v-model="description"
            label="Descrição do Evento"
            required
            class="field-size"
          ></v-textarea>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn class="btn-cancel" @click="goBack">Cancelar</v-btn>
            <v-btn class="btn-create" @click="submitForm" :disabled="!isFormValid">Criar Evento</v-btn>
          </v-card-actions>
        </v-form>
      </v-container>
    </v-main>
    <FooterVue />
    <v-snackbar
      v-model="snackbar"
      :color="snackbarColor"
      timeout="3000"
      top
    >
      {{ snackbarText }}
    </v-snackbar>
  </v-app>
</template>

// src/views/CreateEventPage.vue
<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import NavBar from '../NavBar.vue'
import FooterVue from '../Footer.vue'
import { validateFields, validateNumberInput, snackbar, snackbarText, snackbarColor } from '../../stores/validatorEvent'
import { addEvent, fetchLocations } from '@/services/eventService'


const name = ref('')
const start_date = ref('')
const end_date = ref('')
const max_quantity = ref('')
const min_quantity = ref('')
const hours_quantity = ref('')
const description = ref('')
const event_type = ref('')
const location = ref('')
const locations = ref<any[]>([]) 
const eventTypeOptions = ['conference', 'workshop', 'seminar', 'meetup']
const router = useRouter()
const valid = ref(false)

const errorMessage = ref<string | null>(null)
const showError = ref(false)

const fetchLocationsData = async () => {
  try {
    const response = await fetchLocations()
    locations.value = response.data.results
    if (locations.value.length === 0) {
      showSnackbar('Nenhum local encontrado', 'info')
    }
  } catch (error) {
    showSnackbar('Erro ao buscar locais', 'error')
  }
}

const submitForm = async () => {
  if (
    !validateFields({
      name: name.value,
      start_date: start_date.value,
      end_date: end_date.value,
      local: location.value,
      min_quantity: min_quantity.value,
      max_quantity: max_quantity.value,
      hours_quantity: hours_quantity.value,
      event_type: event_type.value,
      description: description.value,
      status: 'upcoming'
    })
  ) {
    return
  }

  const formData = new FormData()
  formData.append('name', name.value)
  formData.append('start_date', start_date.value)
  formData.append('end_date', end_date.value)
  formData.append('status', 'upcoming')
  formData.append('local', location.value)
  formData.append('description', description.value)
  formData.append('min_quantity', min_quantity.value)
  formData.append('max_quantity', max_quantity.value)
  formData.append('hours_quantity', hours_quantity.value)
  formData.append('event_type', event_type.value)

  try {
    await addEvent(formData)
    showSnackbar('Evento criado com sucesso!', 'success')
    resetForm()
  } catch (error) {
    console.error(error)
    errorMessage.value =
      'Erro ao criar Evento!'
    showError.value = true
  }
}

const showSnackbar = (message: string, type: string) => {
  snackbarText.value = message
  snackbarColor.value = type === 'success' ? 'green' : 'red'
  snackbar.value = true
}

const resetForm = () => {
  name.value = ''
  start_date.value = ''
  end_date.value = ''
  max_quantity.value = ''
  min_quantity.value = ''
  hours_quantity.value = ''
  description.value = ''
  event_type.value = ''
  location.value = ''
}

const goBack = () => {
  router.push({ name: 'home' })
}

const isFormValid = computed(() => {
  return name.value && start_date.value && end_date.value && location.value &&
    min_quantity.value && max_quantity.value && hours_quantity.value &&
    description.value && event_type.value
})

onMounted(() => {
  fetchLocationsData()
})
</script>

<style scoped src="../styles/event.css"></style>