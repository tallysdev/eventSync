<template>
  <v-footer color="secondary" class="py-6" width="auto" height="auto">
    <v-container>
      <v-row class="footer-row" align="center" justify="space-between">
        <v-col cols="12" md="2" class="d-flex align-center justify-center mb-4 mb-md-0">
          <v-img src="../../favicon.ico" alt="Platform Logo" height="40"></v-img>
        </v-col>
        <v-col cols="12" md="3" class="text-center text-md-left">
          <h3 class="text-h6 font-weight-bold">Encontre Eventos</h3>
          <v-list dense>
            <v-list-item v-for="item in findEventsItems" :key="item">
              <v-list-item-title>{{ item }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-col>
        <v-col cols="12" md="3" class="text-center text-md-left">
          <h3 class="text-h6 font-weight-bold">Mapa do site</h3>
          <v-list dense>
            <v-list-item @click="navigateTo('/')">
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item>
            <v-list-item @click="navigateTo('/events')">
              <v-list-item-title>Eventos</v-list-item-title>
            </v-list-item>
            <v-list-item @click="navigateTo('/login')">
              <v-list-item-title>Login</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-col>
        <v-col cols="12" md="4" class="text-center text-md-left">
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
import { useRouter } from 'vue-router'

const router = useRouter()

const findEventsItems = ['Hoje', 'Amanhã', 'Esta Semana', 'Próxima Semana']
const contactItems = ['Email: fakeemail@gmail.com', 'Celular: 213214124124']

const navigateTo = (route: string) => {
  router.push(route)
}
</script>

<style scoped>
.footer-row {
  display: flex;
  flex-direction: column;
}

.footer-row > .v-col {
  margin-bottom: 16px;
  cursor: pointer;
}

@media (min-width: 960px) {
  .footer-row {
    flex-direction: row;
  }
  .footer-row > .v-col {
    margin-bottom: 0;
  }
}
</style>
