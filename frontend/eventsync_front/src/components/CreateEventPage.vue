<template>
  <v-app class="d-flex flex-column w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mb-10">
      <v-container fluid class="pa-6 d-flex flex-column align-center">
        <h1 class="form-title">Crie seu Evento</h1>
        <v-form
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
          <v-row class="mt-4">
            <v-col cols="6" class="d-flex justify-start">
              <v-btn
                @click="goBack"
                color="secondary"
                class="btn-size btn-style voltar-btn"
                elevation="2"
                >Voltar</v-btn
              >
            </v-col>
            <v-col cols="6" class="d-flex justify-end">
              <v-btn type="submit" color="primary" class="btn-size btn-style" elevation="2"
                >Criar Evento</v-btn
              >
            </v-col>
          </v-row>
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

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import NavBar from '../components/NavBar.vue'
import FooterVue from '../components/Footer.vue'
import { validateFields, validateNumberInput, snackbar, snackbarText, snackbarColor } from '../stores/validatorEvent'
import { addEvent } from '@/services/eventService'



const name = ref('')
const start_date = ref('')
const end_date = ref('')
const max_quantity = ref('')
const min_quantity = ref('')
const hours_quantity = ref('')
const description = ref('')
const event_type = ref('')
const location = ref('')
const locations = ref([])
const eventTypeOptions = ['conference', 'workshop', 'seminar', 'meetup']
const router = useRouter()

const fetchLocations = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/eventsync/api/v1/locals')
    locations.value = response.data.results
    console.log(locations.value)
  } catch (error) {
    console.error('Erro ao buscar locais:', error)
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
    const response = await addEvent(formData)
    console.log('Evento criado:', response.data)
    showSnackbar('Evento criado com sucesso!', 'success')
    resetForm()
  } catch (error) {
    if (error.response) {
      console.error('Erro ao criar evento:', error.response.data)
      showSnackbar(`Erro ao criar evento: ${JSON.stringify(error.response.data)}`, 'error')
    } else {
      console.error('Erro ao criar evento:', error)
      showSnackbar('Erro ao criar evento', 'error')
    }
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

onMounted(() => {
  fetchLocations()
})
</script>



<style scoped>
.fill-height {
  min-height: 100vh;
  background-color: #2f3640;
  color: #ffffff;
}

:deep(.v-application__wrap) {
  min-width: 100% !important;
  margin: 0 auto !important;
}

.v-main {
  flex-grow: 1;
}

.v-footer {
  flex-shrink: 0;
}

.btn-size {
  width: 100%;
  max-width: 300px;
  margin-top: 10px;
}

.btn-style {
  font-weight: bold;
  border-radius: 2px;
  padding: 5px 24px;
  font-size: 1.2rem;
}

.voltar-btn {
  font-weight: bold;
  background-color: #ff6f61;
  color: #ffffff;
}

.form-title {
  text-align: center;
  margin-bottom: 30px;
  font-size: 2.8rem;
}

.mt-4 {
  margin-top: 2rem;
}

.field-size {
  max-width: 100%;
  width: 100%;
  margin-bottom: auto;
  font-size: 1.2rem;
}

.max-width-form {
  max-width: 1000px;
  width: 100%;
}
</style>
