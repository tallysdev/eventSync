<template>
  <section class="d-block my-10">
    <!-- TODO: Make the type clickable and redirect to events of this type -->
    <v-row justify="center">
      <v-col cols="12" lg="10">
        <h2 class="text-h4 text-start mb-6 font-weight-bold">Escolha o seu tipo de evento</h2>
        <v-row class="d-flex justify-center">
          <v-col cols="auto" lg="2" v-for="type in eventTypes" :key="type.id" class="text-center">
            <v-avatar size="100" color="primary">
              <v-icon size="50">{{ type.icon }}</v-icon>
            </v-avatar>
            <span class="d-block mt-6 text-h6">{{ type.name }}</span>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </section>
</template>

<script setup lang="ts">
// defineProps agora é um macro de compilador e não precisa mais ser importado
defineProps({
  eventTypes: {
    type: Array,
    required: true
  }
})
</script>

<style scoped></style>
