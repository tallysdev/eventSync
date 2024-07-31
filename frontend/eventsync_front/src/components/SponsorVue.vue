<template>
  <v-app class="d-flex flex-column h-100 w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mt-10">
      <v-container fluid class="pa-4 d-flex flex-column h-100 w-100">
        <section class="d-block my-10">
          <SponsorList />
          <v-btn @click="openDialog" color="primary" class="mt-4">
            <b> Adicionar Patrocinador </b>
          </v-btn>
          <SponsorForm :dialog="dialog" @update:dialog="dialog = $event" />
        </section>
      </v-container>
    </v-main>
    <FooterVue />
  </v-app>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import NavBar from './NavBar.vue'
import FooterVue from './Footer.vue'
import SponsorList from './sponsors/SponsorList.vue'
import SponsorForm from './sponsors/SponsorForm.vue'

const dialog = ref(false)

const openDialog = () => {
  dialog.value = true
}
</script>

<style scoped></style>
