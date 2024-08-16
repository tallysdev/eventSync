<template>
    <v-dialog v-model="dialog" max-width="600px">
      <v-card>
        <v-card-title class="text-h6">Detalhes do Local</v-card-title>
        <v-card-text>
          <div><strong>Nome:</strong> {{ local?.local_name }}</div>
          <div><strong>Rua:</strong> {{ local?.street_name }}</div>
          <div><strong>Nº:</strong> {{ local?.street_number }}</div>
          <div><strong>Cidade:</strong> {{ local?.city }}</div>
          <div><strong>Estado:</strong> {{ local?.state }}</div>
          <div><strong>CEP:</strong> {{ local?.cep }}</div>
          <div><strong>Referência:</strong> {{ local?.reference }}</div>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="dialog = false" color="primary">Fechar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script setup lang="ts">
  import { ref, defineProps, watch } from 'vue';
  import type { Local } from '@/types/local';
  
  const props = defineProps<{
    dialog: boolean;
    local: Local | null;
  }>();
  
  const emit = defineEmits<{
    (e: 'update:dialog', value: boolean): void;
  }>();
  
  const dialog = ref(props.dialog);
  const local = ref(props.local);
  
  watch(() => props.dialog, (newVal) => dialog.value = newVal);
  watch(() => props.local, (newVal) => local.value = newVal);
  
  
  watch(dialog, (newVal) => emit('update:dialog', newVal));
  </script>
  