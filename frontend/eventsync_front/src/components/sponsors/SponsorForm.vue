<template>
  <v-dialog :model-value="dialog" @update:model-value="updateDialog" max-width="600">
    <v-card>
      <v-card-title>
        <span class="headline">Novo Patrocinador</span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
            v-model="newSponsor.name"
            label="Nome"
            :rules="[rules.required]"
            required
          ></v-text-field>
          <v-text-field
            v-model="newSponsor.email"
            label="Email"
            :rules="[rules.required, rules.email]"
            required
          ></v-text-field>
          <v-text-field
            v-model="newSponsor.phone"
            label="Telefone"
            :rules="[rules.required]"
            required
          ></v-text-field>
          <v-textarea
            v-model="newSponsor.description"
            label="Descrição"
            :rules="[rules.required]"
            required
          ></v-textarea>
          <v-file-input
            v-model="newSponsor.logo"
            label="Logo"
            :rules="[rules.required]"
            required
          ></v-file-input>
        </v-form>
        <v-alert v-if="errorMessage" type="error" dismissible v-model="showError">
          {{ errorMessage }}
        </v-alert>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="closeDialog">Cancelar</v-btn>
        <v-btn color="blue darken-1" text @click="addSponsorData" :disabled="!valid">Salvar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { addSponsor } from '@/services/sponsorService'
import { emailValidation, requiredValidation } from '@/utils/validation'
import { ref, watch } from 'vue'
import { type Sponsor } from '@/types/sponsor'

const props = defineProps({
  dialog: {
    type: Boolean,
    required: true
  }
})

const emit = defineEmits(['update:dialog', 'sponsor-added'])

const rules = {
  required: requiredValidation,
  email: emailValidation
}

const valid = ref(false)
const newSponsor = ref<Sponsor>({
  name: '',
  email: '',
  phone: '',
  description: '',
  logo: ''
})

const errorMessage = ref<string | null>(null)
const showError = ref(false)

const closeDialog = () => {
  emit('update:dialog', false)
}

const updateDialog = (value: boolean) => {
  emit('update:dialog', value)
}

const addSponsorData = async () => {
  const formData = new FormData()
  formData.append('name', newSponsor.value.name)
  formData.append('email', newSponsor.value.email)
  formData.append('phone', newSponsor.value.phone)
  formData.append('description', newSponsor.value.description)
  formData.append('logo', newSponsor.value.logo || '')

  try {
    await addSponsor(formData)
    closeDialog()
    newSponsor.value = {
      name: '',
      email: '',
      phone: '',
      description: '',
      logo: ''
    }
    emit('sponsor-added', 'Patrocinador adicionado com sucesso!')
  } catch (error) {
    console.error(error)
    errorMessage.value =
      'Ocorreu um erro ao tentar adicionar o patrocinador. Por favor, tente novamente.'
    showError.value = true
  }
}

watch(
  () => props.dialog,
  (newValue) => {
    if (!newValue) {
      newSponsor.value = {
        name: '',
        email: '',
        phone: '',
        description: '',
        logo: ''
      }
      showError.value = false
      errorMessage.value = null
    }
  }
)
</script>

<style scoped></style>
