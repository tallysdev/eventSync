  <template>
    <v-app class="d-flex flex-column w-100">
      <NavBar />
      <v-main class="flex-grow-1 pa-16 mb-10">
        <v-container fluid class="pa-6 d-flex flex-column align-center">
          <h1 class="form-title">Crie seu Evento</h1>
          <v-form @submit.prevent="submitForm" class="pa-3 d-flex flex-column align-center max-width-form">
            <v-text-field v-model="name" label="Nome do Evento" required class="field-size"></v-text-field>
            <v-text-field v-model="start_date" label="Data de Início do Evento" type="date" required
              class="field-size"></v-text-field>
            <v-text-field v-model="end_date" label="Data de Fim do Evento" type="date" required
              class="field-size"></v-text-field>
            <v-select class="field-size">
              <option v-for="loc in locations" 
              :key="loc.id" 
              :value="loc.id" 
              :selected="local.value === loc.id"> {{
                loc.local_name }}</option>
            </v-select>
            <v-select v-model="event_type" :items="eventTypeOptions" label="Tipo do Evento" required
              class="field-size"></v-select>
            <v-text-field v-model="min_quantity" label="Quantidade Mínima de Participantes" type="number" required
              class="field-size" min="1" @keypress="validateNumberInput"></v-text-field>
            <v-text-field v-model="max_quantity" label="Quantidade Máxima de Participantes" type="number" required
              class="field-size" min="1" @keypress="validateNumberInput"></v-text-field>
            <v-text-field v-model="hours_quantity" label="Quantidade de Horas" type="number" required class="field-size"
              min="1" @keypress="validateNumberInput"></v-text-field>
            <v-textarea v-model="description" label="Descrição do Evento" required class="field-size"></v-textarea>
            <v-row class="mt-4">
              <v-col cols="6" class="d-flex justify-start">
                <v-btn @click="goBack" color="secondary" class="btn-size btn-style voltar-btn"
                  elevation="2">Voltar</v-btn>
              </v-col>
              <v-col cols="6" class="d-flex justify-end">
                <v-btn type="submit" color="primary" class="btn-size btn-style" elevation="2">Criar Evento</v-btn>
              </v-col>
            </v-row>
          </v-form>
        </v-container>
      </v-main>
      <FooterVue />
    </v-app>
  </template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import NavBar from '../components/NavBar.vue'
import FooterVue from '../components/Footer.vue'
import { validateFields, validateNumberInput } from '../stores/validatorEvent.ts'

const name = ref('')
const start_date = ref('')
const end_date = ref('')
const max_quantity = ref('')
const min_quantity = ref('')
const hours_quantity = ref('')
const description = ref('')
const event_type = ref('')
const local = ref('')
const locations = ref([])
const eventTypeOptions = ['conference', 'workshop', 'seminar', 'meetup']
const router = useRouter()


const fetchLocations = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/eventsync/api/v1/locals')
    console.log('Dados da API:', response.data.results)
    locations.value = response.data.results
    console.log(locations.value)
  } catch (error) {
    console.error('Erro ao buscar locais:', error)
  }
}

const submitForm = async () => {
  if (!validateFields({ name: name.value, start_date: start_date.value, end_date: end_date.value, local: local.value, min_quantity: min_quantity.value, max_quantity: max_quantity.value, hours_quantity: hours_quantity.value, event_type: event_type.value, description: description.value })) {
    return
  }

  try {
    const response = await axios.post('http://127.0.0.1:8000/eventsync/api/v1/events/', {
      name: name.value,
      start_date: start_date.value,
      end_date: end_date.value,
      status: 'upcoming',
      local: local.id,
      description: description.value,
      min_quantity: min_quantity.value,
      max_quantity: max_quantity.value,
      hours_quantity: hours_quantity.value,
      event_type: event_type.value
    })
    console.log('Evento criado:', response.data)
    alert('Evento criado com sucesso!')
  } catch (error) {
    if (error.response) {
      console.error('Erro ao criar evento:', error.response.data)
      alert(`Erro ao criar evento: ${JSON.stringify(error.response.data)}`)
    } else {
      console.error('Erro ao criar evento:', error)
      alert('Erro ao criar evento')
    }
  }
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
