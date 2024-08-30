<template>
  <v-app class="d-flex flex-column h-100 w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mt-10">
      <v-container fluid class="pa-4 d-flex flex-column h-100 w-100">
        <section class="d-block my-10">
          <EventDetail />
        </section>
        <ListRooms class="pa-0" />
      </v-container>
    </v-main>
    <FooterVue />
  </v-app>
</template>
<script setup lang="ts">
import EventDetail from '@/components/events/EventDetail.vue'
import FooterVue from '../components/Footer.vue'
import NavBar from '../components/NavBar.vue'
import ListRooms from '@/components/ThemeRoom/ListRooms.vue';
</script>

<style scoped>
main {
  flex-grow: 1;
}
</style>
