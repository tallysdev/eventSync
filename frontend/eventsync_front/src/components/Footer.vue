<template>
  <v-footer color="secondary" class="py-6" width="auto" height="auto">
    <v-container>
      <v-row>
        <v-col cols="2" class="d-flex align-center">
          <v-img src="../../favicon.ico" alt="Platform Logo" height="40"></v-img>
        </v-col>
        <v-col cols="3">
          <h3 class="text-h6 font-weight-bold">Encontre Eventos</h3>
          <v-list dense>
            <v-list-item v-for="item in findEventsItems" :key="item">
              <v-list-item-title>{{ item }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-col>
        <v-col cols="3">
          <h3 class="text-h6 font-weight-bold">Mapa do site</h3>
          <v-list dense>
            <v-list-item v-for="item in siteMapItems" :key="item">
              <v-list-item-title>{{ item }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-col>
        <v-col cols="4">
          <h3 class="text-h6 font-weight-bold">Contato</h3>
          <v-list dense>
            <v-list-item v-for="item in contactItems" :key="item">
              <v-list-item-title>{{ item }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script setup lang="ts">
const findEventsItems = ['Hoje', 'Amanhã', 'Esta Semana', 'Próxima Semana']
const siteMapItems = ['Home', 'Eventos', 'Login', 'Contato']
const contactItems = ['Email: fakeemail@gmail.com', 'Celular: 213214124124']
</script>

<style scoped>
/* Add any additional styles if needed */
</style>
