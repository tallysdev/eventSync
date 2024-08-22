<template>
<v-container fluid class="d-flex flex-column align-center">
    <v-btn v-if="admin" :to="`/events/${EventId}/create/theme-room`" color="success">Cadastrar Sala Tematica
    </v-btn>
    <h2 v-if="rooms.length === 0">Nenhuma Sala Cadastrada ainda...</h2>
    <v-container fluid class="d-flex flex-wrap ga-5 justify-center">
        <v-card class="mx-2 my-2 justify-center w-100" variant="outlined" elevation="20" max-width="400"
            min-width="50" v-for="(room, id) in rooms" :key="id">
            <v-card-actions v-if="admin" class="d-flex flex-wrap w-100 justify-space-between">
                <v-btn color="yellow" variant="text"
                    :to="`/events/${EventId}/edit/theme-room/${room.id}`">Editar</v-btn>
                <v-btn color="red" variant="text" @click="fetchDeleteRoom(room.id)">Exluir</v-btn>
            </v-card-actions>
            <v-card-title class="font-weight-bold text-h5 text-center">{{ room.name }}</v-card-title>
            <v-card-subtitle class="text-caption grey--text">
                <v-icon class="mr-1" small>mdi-calendar</v-icon>
                De {{ room.start_date }} - Até {{ room.end_date }}
            </v-card-subtitle>
            <v-card-subtitle class="text-caption grey--text">
                <v-icon class="mr-1" small>mdi-clock-outline</v-icon>
                Horário de início {{ room.start_time }}
            </v-card-subtitle>
            <v-card-subtitle class="text-caption grey--text">
                <v-icon class="mr-1" small>mdi-map-marker-outline</v-icon>
                <span class="font-weight-bold">{{ room.local }}</span>
            </v-card-subtitle>
            <v-card-text>
                <v-row class="d-flex flex-column">
                    <v-col>
                        <p class="font-weight-bold">Palestrante: {{ room.speaker }}</p>
                    </v-col>
                    <v-col>
                        <v-icon class="mr-1" small>mdi-information-outline</v-icon>
                        <span class="font-weight-bold">Tipo: </span>
                        {{ room.event_type }}
                    </v-col>
                    <v-col class="d-flex flex-wrap">
                        <v-icon class="mr-1" small>mdi-account-group</v-icon>
                        <p class="font-weight-bold">Participantes:</p>
                        <p>Máximo {{ room.max_quantity }} - Mínimo {{ room.min_quantity }}
                        </p>
                    </v-col>
                </v-row>
            </v-card-text>
            <v-card-actions class="d-flex flex-wrap w-100 justify-space-between">
                <v-btn color="blue" text @click="room.showDetails = !room.showDetails">Ver detalhes</v-btn>
                <template v-if="isSubscribed">
                    <v-btn @click="handleUnsubscription" color="error" class="text-no-wrap">
                        <b>Cancelar Inscrição</b>
                    </v-btn>
                </template>
                <v-btn v-else @click="handleSubscription" color="success" class="text-no-wrap">
                    Participar
                </v-btn>
            </v-card-actions>
            <v-expand-transition>
                <div v-show="room.showDetails">
                    <v-divider></v-divider>
                    <v-row class="pa-2">
                        <v-card-text>
                            Público Alvo: {{ room.audiences }}
                        </v-card-text>
                        <v-card-text>
                            Descrição: {{ room.description }}
                        </v-card-text>
                    </v-row>
                </div>
            </v-expand-transition>
        </v-card>
        <v-snackbar v-model="showSnackbar" :color="snackbarColor" timeout="4000" top>
            {{ snackbarMessage }}
        </v-snackbar>
    </v-container>
</v-container>
</template>

<script setup lang="ts">

import { ref, onMounted } from 'vue'
import { fetchThemeRooms, deleteThemeRoom } from '@/services/themRoomService';
import { useAuthStore } from '@/stores/auth';
import {
    signupForEvent,
    cancelSubscription,
    checkUserSubscription
} from '@/services/eventService';
import { type ThemeRoom } from '@/types/themeRoom';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
const router = useRouter()
const EventId = Number(route.params.id)
const rooms = ref<ThemeRoom[]>([])
const loading = ref(false)
const errorMessage = ref<string | null>(null)
const admin = true
const authStore = useAuthStore()
const isSubscribed = ref(false)
const showSnackbar = ref(false)
const snackbarMessage = ref('')
const snackbarColor = ref('')

const checkSubscriptionStatus = async () => {
    if (authStore.isAuthenticated) {
        try {
            console.log(authStore.token)
            const response = await checkUserSubscription(rooms.value.id, authStore.getUser.id)
            console.log('Subscription status:', response.data)
            isSubscribed.value = await checkUserSubscription(rooms.value.id, authStore.getUser.id)
        } catch (error) {
            console.error('Error checking subscription status:', error)
        }
    }
}

const handleSubscription = async () => {
    if (authStore.isAuthenticated) {
        try {
            await signupForEvent(rooms.value.id, authStore.getUser.id)
            snackbarMessage.value = 'Inscrição realizada com sucesso!'
            snackbarColor.value = 'success'
            isSubscribed.value = true
        } catch (error) {
            console.error('Error subscribing:', error)
        }
    } else {
        snackbarMessage.value = 'Você precisa estar logado para se inscrever.'
        snackbarColor.value = 'error'
        setTimeout(() => {
            router.push('/login')
        }, 2000)
    }
}

// Função para alternar o estado 'showDetails' para cada sala individualmente
const toggleDetails = (id: number) => {

    const room = rooms.value.find((room: { id: number; }) => room.id === id)
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
        const response = await fetchThemeRooms(EventId)
        // rooms.value = response.data
        rooms.value = response.data.map((room: ThemeRoom) => ({
            ...room,
            showDetails: false, // Adiciona a propriedade showDetails a cada sala
        }))
        clearTimeout(loadingTimeout)
    } catch (error) {
        console.error('Error fetching rooms:', error)
    } finally {
        loading.value = false
    }
}

const fetchDeleteRoom = async (id: number) => {
    loading.value = true
    errorMessage.value = null

    const loadingTimeout = setTimeout(() => {
        loading.value = false
        errorMessage.value = 'O tempo de carregamento expirou. Tente novamente.'
    }, 10000) // 10 seconds timeout

    try {
        const response = await deleteThemeRoom(id)
        clearTimeout(loadingTimeout)
    } catch (error) {
        console.error('Error deleting room:', error)
    } finally {
        loading.value = false
        fetchRoomsData()
    }
}

onMounted(() => {
    fetchRoomsData()
})

</script>

<style scoped lang="css"></style>