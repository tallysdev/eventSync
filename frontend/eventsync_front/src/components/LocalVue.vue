<template>
    <v-app class="d-flex flex-column h-100 w-100">
      <NavBar />
      <v-main class="flex-grow-1 pa-16 mt-10">
        <v-container fluid class="pa-4 d-flex flex-column h-100 w-100">
          <section class="d-block my-10">
            <LocalList />
          </section>
        </v-container>
      </v-main>
      <FooterVue />
    </v-app>
  </template>
  
  <script setup lang="ts">
  import NavBar from './NavBar.vue'
  import FooterVue from './Footer.vue'
  import LocalList from './locals/LocalList.vue';
  </script>
  
  <style scoped></style>
  