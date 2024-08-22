<template>
  <v-dialog :model-value="dialog" @update:model-value="updateDialog" max-width="600">
    <v-card>
      <v-card-title>
        <span class="headline">Novo Local</span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
            v-model="newLocal.local_name"
            label="Nome"
            :rules="[rules.required]"
            required
          ></v-text-field>
          <v-select
            v-model="newLocal.state"
            :items="UFs"
            item-value="value"
            item-title="label"
            label="Estado"
            :rules="[rules.required]"
            required
          ></v-select>
          <v-text-field
            v-model="newLocal.cep"
            label="CEP"
            :rules="[rules.required, rules.cep]"
            :disabled="!newLocal.state"
            required
            @input="formatCEP"
          ></v-text-field>
          <v-text-field
            v-model="newLocal.street_name"
            label="Nome da Rua"
            :rules="[rules.required]"
            required
          ></v-text-field>
          <v-text-field
            v-model="newLocal.street_number"
            label="Número da Rua"
            :rules="[rules.required, validateNumberInput]"
            :error-messages="errorMessages.street_number"
            @input="validateNumberField"
            required
            type="number"
          ></v-text-field>
          <v-autocomplete
            v-model="newLocal.city"
            :items="citiesOptions"
            item-value="value"
            item-title="label"
            label="Cidade"
            :rules="[rules.required]"
          ></v-autocomplete>
          <v-text-field v-model="newLocal.reference" label="Referência"></v-text-field>
          <v-alert v-if="errorMessage" type="error" dismissible v-model="showError">
            {{ errorMessage }}
          </v-alert>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="closeDialog">Cancelar</v-btn>
        <v-btn color="green" text @click="addLocalData" :disabled="!valid || hasErrors"
          >Salvar</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from 'vue'
import { type Local } from '@/types/local'
import { addLocal } from '@/services/localService'
import {
  requiredValidation,
  isNotEmpty,
  isValidCEP,
  UFs,
  validateNumberInput
} from '@/utils/validation'
import axios from 'axios'

const props = defineProps({
  dialog: {
    type: Boolean,
    required: true
  }
})

const emit = defineEmits(['update:dialog', 'local-added'])

const citiesOptions = ref<any[]>([])
const errorMessages = ref<{ [key: string]: string[] }>({
  street_number: []
})
const hasErrors = ref(false)
const userInteracted = ref(false)

const fetchCities = async (state: string) => {
  try {
    const response = await axios.get(
      `https://servicodados.ibge.gov.br/api/v1/localidades/estados/${state}/distritos`
    )
    citiesOptions.value = response.data.map((city: any) => ({ value: city.nome, label: city.nome }))
  } catch (error) {
    console.error('Erro ao buscar cidades:', error)
  }
}

const rules = {
  required: requiredValidation,
  cep: isValidCEP,
  validateNumberInput
}

const valid = ref(false)
const newLocal = ref<Local>({
  local_name: '',
  street_name: '',
  street_number: '',
  city: '',
  state: '',
  cep: '',
  reference: ''
})

const errorMessage = ref<string | null>(null)
const showError = ref(false)

const closeDialog = () => {
  emit('update:dialog', false)
}

const updateDialog = (value: boolean) => {
  emit('update:dialog', value)
}

const addLocalData = async () => {
  if (hasErrors.value) {
    errorMessage.value = 'Por favor, corrija os erros no formulário.'
    showError.value = true
    return
  }

  const formData = new FormData()
  formData.append('local_name', newLocal.value.local_name)
  formData.append('street_name', newLocal.value.street_name)
  formData.append('street_number', newLocal.value.street_number)
  formData.append('city', newLocal.value.city)
  formData.append('state', newLocal.value.state)
  formData.append('cep', newLocal.value.cep)
  formData.append('reference', newLocal.value.reference || '')

  try {
    await addLocal(formData)
    closeDialog()
    newLocal.value = {
      local_name: '',
      street_name: '',
      street_number: '',
      city: '',
      state: '',
      cep: '',
      reference: ''
    }
    emit('local-added', 'Local adicionado com sucesso!', 'green')
  } catch (error) {
    console.error(error)
    errorMessage.value = 'Ocorreu um erro ao tentar adicionar o local. Por favor, tente novamente.'
    showError.value = true
  }
}

const formatCEP = () => {
  let value = newLocal.value.cep.replace(/\D/g, '')
  if (value.length > 5) {
    value = `${value.slice(0, 5)}-${value.slice(5, 8)}`
  }
  newLocal.value.cep = value
  rules.cep(newLocal.value.cep)
}

const validateNumberField = () => {
  userInteracted.value = true
  rules.validateNumberInput(newLocal.value.street_number)
}

watch(
  () => props.dialog,
  (newValue) => {
    if (!newValue) {
      newLocal.value = {
        local_name: '',
        street_name: '',
        street_number: '',
        city: '',
        state: '',
        cep: '',
        reference: ''
      }
      showError.value = false
      errorMessage.value = null
    }
  }
)

watch(
  () => newLocal.value.state,
  (newState) => {
    if (newState) {
      fetchCities(newState)
    } else {
      citiesOptions.value = []
    }
  }
)

watch(
  () => newLocal.value.street_number,
  (newValue) => {
    if (userInteracted.value) {
      rules.validateNumberInput(newValue)
    }
  }
)

onMounted(async () => {
  await fetchCities('')
})
</script>

<style scoped></style>
