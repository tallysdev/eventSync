<script setup lang="ts">
import EventForm from '@/components/EventForm.vue';
</script>

<template>
  <main class="d-flex align-center justify-center flex-column h-100 w-100">
    <EventForm />
  </main>
</template>
  
<style>
@media (min-width: 1024px) {
  .forms {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
