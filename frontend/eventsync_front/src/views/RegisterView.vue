<script setup lang="ts">
import RegisterForm from '@/components/register/RegisterForm.vue'
</script>

<template>
  <main class="d-flex align-center justify-center flex-column h-100 w-100">
    <RegisterForm />
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
