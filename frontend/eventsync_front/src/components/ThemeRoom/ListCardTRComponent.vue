<template>
    <v-container fluid class="ma-4 d-flex ga-5 w-100 flex-wrap border-red">
        <v-card class="mx-auto flex-wrap" variant="outlined" max-width="400" v-for="(room, id) in rooms" :key="id">
            <v-card-title class="font-weight-bold text-h5">{{ room.name }}</v-card-title>

            <v-card-subtitle class="text-caption grey--text">
                <v-icon class="mr-1" small>mdi-calendar</v-icon>
                De {{ room.start_date }} - Até {{ room.end_date }}
            </v-card-subtitle>

            <v-card-subtitle class="text-caption grey--text">
                <v-icon class="mr-1" small>mdi-clock-outline</v-icon>
                Horário de início {{ room.start_time }}
            </v-card-subtitle>

            <v-card-text>
                <v-row>
                    <v-col cols="12">
                        <v-icon class="mr-1" small>mdi-map-marker-outline</v-icon>
                        <span class="font-weight-bold">{{ room.local }}</span>
                    </v-col>

                    <v-col cols="12">
                        <v-icon class="mr-1" small>mdi-account-group</v-icon>
                        <span class="font-weight-bold">Participantes: </span>
                        Máximo {{ room.max_quantity }} - Mínimo {{ room.min_quantity }}
                    </v-col>

                    <v-col cols="12">
                        <v-icon class="mr-1" small>mdi-information-outline</v-icon>
                        <span class="font-weight-bold">Tipo: </span>
                        {{ room.event_type }}
                    </v-col>

                    <v-col cols="12">
                        <p class="mt-2">{{ room.description }}</p>
                    </v-col>

                    <v-col cols="12">
                        <p>Público alvo: {{ room.audiences }}</p>
                    </v-col>

                    <v-col cols="12">
                        <p>Palestrante: {{ room.speaker }}</p>
                    </v-col>
                </v-row>
            </v-card-text>

            <v-card-actions>
                <v-btn color="blue" text @click="toggleDetails(id)">Ver Detalhes</v-btn>
                <v-btn color="green" text>Participar</v-btn>
            </v-card-actions>

            <v-expand-transition>
                <div v-show="room.showDetails">
                    <v-divider></v-divider>

                    <v-card-text>
                        Detalhes adicionais da Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat neque pariatur veniam, distinctio illo dolores, quisquam molestiae iure voluptates ab consequuntur, quis suscipit autem qui fuga facilis facere aliquid. Molestias. sala. Você pode adicionar mais informações aqui.
                    </v-card-text>
                </div>
            </v-expand-transition>
        </v-card>
    </v-container>
</template>


<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { fetchThemeRooms } from '@/services/themRoomService';
import { type ThemeRoom } from '@/types/themeRoom';

const rooms = ref<ThemeRoom[]>([])
const currentPage = ref(1)
const totalPages = ref(1)
const itemsPerPage = 12
const loading = ref(false)
const errorMessage = ref<string | null>(null)

// Função para alternar o estado 'showDetails' para cada sala individualmente
const toggleDetails = (id: string) => {
  const room = rooms.value.find((room: { id: string; }) => room.id === id)
  if (room) {
    room.showDetails = !room.showDetails
  }
}

const fetchRoomsData = async () => {
  loading.value = true
  errorMessage.value = null

  const loadingTimeout = setTimeout(() => {
    loading.value = false
    errorMessage.value = 'O tempo de carregamento expirou. Tente novamente.'
  }, 10000) // 10 seconds timeout

  try {
    const response = await fetchThemeRooms(currentPage.value, itemsPerPage)
    rooms.value = response.data.results.map((room: ThemeRoom) => ({
      ...room,
      showDetails: false, // Adiciona a propriedade showDetails a cada sala
    }))
    console.log(rooms.value)
    totalPages.value = Math.ceil(response.data.count / itemsPerPage)
    clearTimeout(loadingTimeout)
  } catch (error) {
    console.error('Error fetching rooms:', error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchRoomsData()
})

watch(currentPage, () => {
  fetchRoomsData()
})
</script>

<style scoped lang="css"></style>
<style scoped lang="css"></style>