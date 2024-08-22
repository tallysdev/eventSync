<template>
  <v-dialog v-model="localDialog" max-width="600px">
    <v-card>
      <v-card-title class="text-h6">Editar Local</v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="formValid">
          <v-text-field v-model="local!.local_name" label="Nome" :rules="rules.required" required />
          <v-text-field v-model="local!.street_name" label="Rua" :rules="rules.required" required />
          <v-text-field
            v-model="local!.street_number"
            label="Número"
            :rules="rules.validateNumberInput"
          />
          <v-autocomplete
            v-model="local!.city"
            :items="citiesOptions"
            item-value="value"
            item-title="label"
            label="Cidade"
            :rules="[rules.required]"
          />
          <v-select
            v-model="local!.state"
            :items="UFs"
            item-value="value"
            item-title="label"
            label="Estado"
            :rules="[rules.required]"
            required
          />
          <v-text-field v-model="local!.cep" label="CEP" :rules="rules.cep" />
          <v-text-field v-model="local!.reference" label="Referência" />
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click="saveChanges"
          :disabled="!formValid"
          color="light-blue lighten-2"
          text-color="white"
        >
          Salvar
        </v-btn>
        <v-btn @click="closeDialog" color="grey lighten-2" text-color="black"> Cancelar </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from 'vue'
import type { Local } from '@/types/local'
import {
  requiredValidation,
  isNotEmpty,
  isValidCEP,
  UFs,
  validateNumberInput
} from '@/utils/validation'
import { updateLocal } from '@/services/localService'
import axios from 'axios'

const citiesOptions = ref<any[]>([])
const props = defineProps<{
  dialog: boolean
  local: Local | null
}>()

const emit = defineEmits<{
  (e: 'update:dialog', value: boolean): void
  (e: 'local-updated', message: string, color: string): void
}>()

const localDialog = ref(props.dialog)
const local = ref<Local | null>(props.local)
const formValid = ref(false)

watch(
  () => props.dialog,
  (newValue) => {
    localDialog.value = newValue
  }
)

watch(
  () => props.local,
  (newValue) => {
    local.value = { ...newValue } as Local
  },
  { immediate: true }
)

const rules = {
  required: [(v: string) => !!v || 'Este campo é obrigatório'],
  validateNumberInput: [(v: string) => /^\d+$/.test(v) || 'Digite apenas números'],
  cep: [(v: string) => /^\d{5}-\d{3}$/.test(v) || 'CEP inválido']
}

const fetchCities = async (state: string) => {
  try {
    const response = await axios.get(
      `https://servicodados.ibge.gov.br/api/v1/localidades/estados/${state}/distritos`
    )
    citiesOptions.value = response.data.map((city: any) => city.nome)
  } catch (error) {
    console.error('Erro ao buscar cidades:', error)
  }
}

const saveChanges = async () => {
  if (local.value) {
    try {
      await updateLocal(local.value)
      emit('local-updated', 'Local atualizado com sucesso', 'green')
      emit('update:dialog', false)
    } catch (error) {
      console.error('Error saving changes:', error)
      emit('local-updated', 'Erro ao atualizar o local', 'red')
    }
  }
}

const closeDialog = () => {
  emit('update:dialog', false)
}

watch(localDialog, (newValue) => {
  if (!newValue) {
    closeDialog()
  }
})

watch(
  () => local.value?.state,
  (newState) => {
    if (newState) {
      fetchCities(newState)
    } else {
      citiesOptions.value = []
    }
  }
)

onMounted(() => {
  if (local.value?.state) {
    fetchCities(local.value.state)
  }
})
</script>
