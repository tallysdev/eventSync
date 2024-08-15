<template>
  <main class="d-flex align-center justify-center flex-column h-100 w-100">
    <EventDetail />
  </main>
</template>

<script setup lang="ts">
import EventDetail from '../components/EventDetail.vue'
</script>

<style scoped>
main {
  flex-grow: 1;
}
</style>
