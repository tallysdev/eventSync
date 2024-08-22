<script setup lang="ts">
import LoginForm from '@/components/login/LoginForm.vue'
</script>

<template>
  <main class="d-flex align-center justify-center flex-column h-100 w-100">
    <LoginForm />
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
