<script setup lang="ts">
import ParticipantList from '@/components/ParticipantList.vue'
import NavBar from '@/components/NavBar.vue'
import FooterVue from '@/components/Footer.vue'
</script>

<template>
  <v-app class="d-flex flex-column h-100 w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mt-10">
      <v-container fluid class="pa-4 d-flex flex-column h-100 w-100">
        <section class="d-block my-10">
          <ParticipantList />
        </section>
      </v-container>
    </v-main>
    <FooterVue />
  </v-app>
</template>

<style scoped>
main {
  flex-grow: 1;
}
</style>
