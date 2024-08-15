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
              :rules="[rules.requiredCamp && rules.required]"
              required
            ></v-text-field>
            <v-select
              v-model="newLocal.state"
              :items="ufOptions"
              label="Estado"
              :rules="[rules.requiredCamp]"
              @change="onStateChange"
              required
            ></v-select>
            <v-text-field
              v-model="newLocal.cep"
              label="CEP"
              :rules="[rules.requiredCamp, rules.cep]"
              :disabled="!newLocal.state"
              required
            ></v-text-field>
            <v-text-field
              v-model="newLocal.street_name"
              label="Nome da Rua"
              :rules="[rules.requiredCamp && rules.required]"
              required
            ></v-text-field>
            <v-text-field
              v-model="newLocal.street_number"
              label="Número da Rua"
              :rules="[rules.requiredCamp && rules.isValidStreetNumber]"
              required
            ></v-text-field>
            <v-text-field
              v-model="newLocal.city"
              label="Cidade"
              :rules="[rules.requiredCamp && rules.required]"
              required
            ></v-text-field>
            <v-text-field
              v-model="newLocal.reference"
              label="Referência"
            ></v-text-field>
  
            <v-alert v-if="errorMessage" type="error" dismissible v-model="showError">
              {{ errorMessage }}
            </v-alert>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDialog">Cancelar</v-btn>
          <v-btn color="blue darken-1" text @click="addLocalData" :disabled="!valid">Salvar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  
  
  <script setup lang="ts">
import { ref, watch } from 'vue';
import { type Local } from '@/types/local';
import { addLocal } from '@/services/localService';
import { requiredValidation, defaultCEPs, isNotEmpty, isValidCEP, isValidStreetNumber } from '@/utils/validation';

const props = defineProps({
  dialog: {
    type: Boolean,
    required: true
  }   
});

const emit = defineEmits(['update:dialog', 'local-added']);

// Define a lista de opções de estados
const ufOptions = [
  { label: 'Acre', value: 'AC' },
  { label: 'Alagoas', value: 'AL' },
  { label: 'Amapá', value: 'AP' },
  { label: 'Amazonas', value: 'AM' },
  { label: 'Bahia', value: 'BA' },
  { label: 'Ceará', value: 'CE' },
  { label: 'Distrito Federal', value: 'DF' },
  { label: 'Espírito Santo', value: 'ES' },
  { label: 'Goiás', value: 'GO' },
  { label: 'Maranhão', value: 'MA' },
  { label: 'Mato Grosso', value: 'MT' },
  { label: 'Mato Grosso do Sul', value: 'MS' },
  { label: 'Minas Gerais', value: 'MG' },
  { label: 'Pará', value: 'PA' },
  { label: 'Paraíba', value: 'PB' },
  { label: 'Paraná', value: 'PR' },
  { label: 'Pernambuco', value: 'PE' },
  { label: 'Piauí', value: 'PI' },
  { label: 'Rio de Janeiro', value: 'RJ' },
  { label: 'Rio Grande do Norte', value: 'RN' },
  { label: 'Rio Grande do Sul', value: 'RS' },
  { label: 'Rondônia', value: 'RO' },
  { label: 'Roraima', value: 'RR' },
  { label: 'Santa Catarina', value: 'SC' },
  { label: 'São Paulo', value: 'SP' },
  { label: 'Sergipe', value: 'SE' },
  { label: 'Tocantins', value: 'TO' }
];

// Função para lidar com a mudança no estado
const onStateChange = (state: string) => {
  newLocal.value.cep = defaultCEPs || '';
};

// Define as regras de validação
const rules = {
  required: isNotEmpty,
  requiredCamp: requiredValidation,
  cep: isValidCEP,
  street_number: isValidStreetNumber,
  state: ufOptions,

};

const valid = ref(false);
const newLocal = ref<Local>({
  local_name: '',
  street_name: '',
  street_number: '',
  city: '',
  state: '',
  cep: '',
  reference: ''
});

const errorMessage = ref<string | null>(null);
const showError = ref(false);

const closeDialog = () => {
  emit('update:dialog', false);
};

const updateDialog = (value: boolean) => {
  emit('update:dialog', value);
};

const addLocalData = async () => {
  const formData = new FormData();
  formData.append('local_name', newLocal.value.local_name);
  formData.append('street_name', newLocal.value.street_name);
  formData.append('street_number', newLocal.value.street_number);
  formData.append('city', newLocal.value.city);
  formData.append('state', newLocal.value.state);
  formData.append('cep', newLocal.value.cep);
  formData.append('reference', newLocal.value.reference || '');

  try {
    await addLocal(formData);
    closeDialog();
    newLocal.value = {
      local_name: '',
      street_name: '',
      street_number: '',
      city: '',
      state: '',
      cep: '',
      reference: ''
    };
    emit('local-added', 'Local adicionado com sucesso!');
  } catch (error) {
    console.error(error);
    errorMessage.value = 'Ocorreu um erro ao tentar adicionar o local. Por favor, tente novamente.';
    showError.value = true;
  }
};

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
      };
      showError.value = false;
      errorMessage.value = null;
    }
  }
);
</script>

  
  
  <style scoped></style>
  