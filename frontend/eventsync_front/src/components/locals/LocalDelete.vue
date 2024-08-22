<template>
  <v-dialog v-model="dialog" max-width="400px">
    <v-card>
      <v-card-title class="text-h6">Confirmar Exclusão</v-card-title>
      <v-card-text>
        <p>Tem certeza de que deseja excluir o local "{{ local?.local_name }}"?</p>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="confirmDelete" color="red" text>Excluir</v-btn>
        <v-btn @click="dialog = false" color="grey" text>Cancelar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, defineProps, defineEmits, watch } from 'vue'
import { deleteLocal } from '@/services/localService'
import type { Local } from '@/types/local'

const props = defineProps<{
  dialog: boolean
  local: Local | null
}>()

const emit = defineEmits<{
  (e: 'update:dialog', value: boolean): void
  (e: 'local-deleted', message: string, color: string): void
}>()

const dialog = ref(props.dialog)
const local = ref(props.local)

const confirmDelete = async () => {
  if (local.value) {
    try {
      if (local.value.id) {
        await deleteLocal(local.value.id)
        emit('local-deleted', 'Local excluído com sucesso', 'green')
      }
    } catch (error) {
      console.error('Error deleting local:', error)
      emit('local-deleted', 'Erro ao excluir local', 'red')
    } finally {
      dialog.value = false
      emit('update:dialog', dialog.value)
    }
  }
}

watch(
  () => props.dialog,
  (newVal) => (dialog.value = newVal)
)
watch(
  () => props.local,
  (newVal) => (local.value = newVal)
)

watch(dialog, (newVal) => emit('update:dialog', newVal))
</script>
