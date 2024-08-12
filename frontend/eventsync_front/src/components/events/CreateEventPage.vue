<template>
  <v-app class="d-flex flex-column w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mb-10">
      <v-container fluid class="pa-6 d-flex flex-column align-center">
        <h1 class="form-title">Crie seu Evento</h1>
        <v-form
          ref="form"
          v-model="valid"
          lazy-validation
          @submit.prevent="submitForm"
          class="pa-3 d-flex flex-column align-center max-width-form"
        >
          <v-text-field
            v-model="eventForm.name"
            label="Nome do Evento"
            required
            class="field-size"
          ></v-text-field>
          <v-text-field
            v-model="eventForm.start_date"
            label="Data de Início do Evento"
            type="date"
            required
            class="field-size"
          ></v-text-field>
          <v-text-field
            v-model="eventForm.end_date"
            label="Data de Fim do Evento"
            type="date"
            required
            class="field-size"
          ></v-text-field>
          <v-select
            class="field-size pb-2"
            :label="'Localização do Evento'"
            v-model="eventForm.location"
            :items="locations"
            item-title="local_name"
            item-value="id"
            required
            :hint="locations.length === 0 ? 'Nenhum local disponível' : ''"
            :persistent-hint="true"
          ></v-select>
          <v-select
            v-model="eventForm.event_type"
            :items="eventTypeOptions"
            label="Tipo do Evento"
            required
            class="field-size"
          ></v-select>
          <v-text-field
            v-model="eventForm.min_quantity"
            label="Quantidade Mínima de Participantes"
            type="number"
            required
            class="field-size"
            min="1"
            @keypress="validateNumberInput"
          ></v-text-field>
          <v-text-field
            v-model="eventForm.max_quantity"
            label="Quantidade Máxima de Participantes"
            type="number"
            required
            class="field-size"
            min="1"
            @keypress="validateNumberInput"
          ></v-text-field>
          <v-text-field
            v-model="eventForm.hours_quantity"
            label="Quantidade de Horas"
            type="number"
            required
            class="field-size"
            min="1"
            @keypress="validateNumberInput"
          ></v-text-field>
          <v-textarea
            v-model="eventForm.description"
            label="Descrição do Evento"
            required
            class="field-size"
          ></v-textarea>
          <v-row class="mt-4">
            <v-col cols="6" class="d-flex justify-start">
              <v-btn @click="goBack" color="secondary" class="mt-4 px-10" elevation="2">
                <b> Voltar </b>
              </v-btn>
            </v-col>
            <v-col cols="6" class="d-flex justify-end">
              <v-btn
                type="submit"
                color="primary"
                class="mt-4 px-10"
                elevation="2"
                :disabled="!isFormValid || submitting"
              >
                <b> Criar </b>
              </v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-container>
    </v-main>
    <FooterVue />
    <v-snackbar v-model="snackbar" :color="snackbarColor" timeout="3000" top>
      {{ snackbarText }}
    </v-snackbar>
  </v-app>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import NavBar from '../NavBar.vue'
import FooterVue from '../Footer.vue'
import {
  validateFields,
  validateNumberInput,
  snackbar,
  snackbarText,
  snackbarColor
} from '../../stores/validatorEvent'
import { addEvent, fetchLocations } from '@/services/eventService'

class EventForm {
  name = ''
  start_date = ''
  end_date = ''
  location = ''
  event_type = ''
  min_quantity = ''
  max_quantity = ''
  hours_quantity = ''
  description = ''
}

const eventForm = ref(new EventForm())
const locations = ref<any[]>([])
const eventTypeOptions = ['conference', 'workshop', 'seminar', 'meetup']
const router = useRouter()
const valid = ref(false)
const submitting = ref(false)

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
  if (submitting.value) return // Se já está enviando, não fazer nada
  submitting.value = true

  if (
    !validateFields({
      name: eventForm.value.name,
      start_date: eventForm.value.start_date,
      end_date: eventForm.value.end_date,
      local: eventForm.value.location,
      min_quantity: eventForm.value.min_quantity,
      max_quantity: eventForm.value.max_quantity,
      hours_quantity: eventForm.value.hours_quantity,
      event_type: eventForm.value.event_type,
      description: eventForm.value.description,
      status: 'upcoming'
    })
  ) {
    submitting.value = false
    return
  }

  const formData = new FormData()
  formData.append('name', eventForm.value.name)
  formData.append('start_date', eventForm.value.start_date)
  formData.append('end_date', eventForm.value.end_date)
  formData.append('status', 'upcoming')
  formData.append('local', eventForm.value.location)
  formData.append('description', eventForm.value.description)
  formData.append('min_quantity', eventForm.value.min_quantity)
  formData.append('max_quantity', eventForm.value.max_quantity)
  formData.append('hours_quantity', eventForm.value.hours_quantity)
  formData.append('event_type', eventForm.value.event_type)

  try {
    await addEvent(formData)
    showSnackbar('Evento criado com sucesso!', 'success')
    resetForm()
  } catch (error) {
    console.error(error)
    errorMessage.value = 'Erro ao criar Evento!'
    showError.value = true
  } finally {
    submitting.value = false
  }
}

const showSnackbar = (message: string, type: string) => {
  snackbarText.value = message
  snackbarColor.value = type === 'success' ? 'green' : 'red'
  snackbar.value = true
}

const resetForm = () => {
  eventForm.value = new EventForm()
}

const goBack = () => {
  router.push({ name: 'home' })
}

const isFormValid = computed(() => {
  return (
    eventForm.value.name &&
    eventForm.value.start_date &&
    eventForm.value.end_date &&
    eventForm.value.location &&
    eventForm.value.min_quantity &&
    eventForm.value.max_quantity &&
    eventForm.value.hours_quantity &&
    eventForm.value.description &&
    eventForm.value.event_type
  )
})

onMounted(() => {
  fetchLocationsData()
})
</script>

<style scoped src="../styles/event.css"></style>
