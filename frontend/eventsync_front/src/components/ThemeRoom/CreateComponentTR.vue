<template>
    <v-main class="h-100 pa-0">
        <v-container>
            <h1>Evento: Nome do Evento</h1>
            <h1 class="text-center">Criar sala temática.</h1>
            <v-form 
            v-model="valid"
            ref="form"
            lazy-validation
            @submit.prevent="submitForm" 
            class="mb-10">

                <v-text-field 
                v-model="roomForm.name" 
                variant="outlined" 
                label="Nome da sala" 
                required></v-text-field>

                <v-text-field 
                v-model="roomForm.start_date" 
                variant="outlined" 
                label="Data Inicial" 
                type="date"
                required></v-text-field>

                <v-text-field 
                v-model="roomForm.end_date" 
                variant="outlined" 
                label="Data Final" 
                type="date"
                required></v-text-field>

                <v-text-field 
                v-model="roomForm.start_time" 
                variant="outlined" 
                label="Horário inicial da sala" 
                type="time"
                required></v-text-field>

                <v-text-field 
                v-model="roomForm.local" 
                variant="outlined" 
                label="Local da sala" 
                required></v-text-field>

                <v-text-field 
                v-model="roomForm.min_quantity" 
                variant="outlined" 
                label="Número Min. de Participantes"
                type="number"
                min="1"
                @keypress="validateNumberInput"
                required></v-text-field>

                <v-text-field 
                v-model="roomForm.max_quantity" 
                variant="outlined" 
                label="Número Máx. de Participantes"
                type="number"
                min="1"
                @keypress="validateNumberInput"
                required></v-text-field>

                <v-text-field 
                v-model="roomForm.speaker" 
                variant="outlined" 
                label="Palestrante" 
                required></v-text-field>

                <v-textarea 
                v-model="roomForm.description" 
                variant="outlined" 
                label="Descrição" 
                required></v-textarea>

                <v-text-field 
                v-model="roomForm.hours_quantity" 
                variant="outlined"
                min="1"
                @keypress="validateNumberInput"
                label="Quantidade horas no certificado" 
                type="number"></v-text-field>

                <v-text-field 
                v-model="roomForm.audiences"
                variant="outlined"
                label="Público Alvo" 
                required></v-text-field>

                <v-select
                v-model="roomForm.event_type"
                :items="eventTypeOptions" 
                variant="outlined" 
                label="Tipo de evento"
                required></v-select>

                <v-container grid-list-xs class="d-flex justify-center ga-10">
                    <v-btn 
                    type="submit" 
                    color="primary"
                    :disabled="!isFormValid || submitting"
                    >Criar</v-btn>
                    <v-btn color="secondary" @click="goBack">Voltar</v-btn>
                </v-container>
            </v-form>

            <!-- Snackbar para mensagens de sucesso ou erro -->
            <v-snackbar v-model="snackbar" :color="snackbarColor" timeout="3000" top right>
                {{ snackbarText }}
                <template v-slot:action="{ attrs }">
                    <v-btn color="white" text v-bind="attrs" @click="snackbar = false">Fechar</v-btn>
                </template>
            </v-snackbar>
        </v-container>
    </v-main>
</template>


<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { addThemeRoom, updateThemeRoom } from '@/services/themRoomService';
import { validateFields, validateNumberInput, snackbar, snackbarText, snackbarColor } from '../../stores/validatorRoom';

// Classe do formulário
class ThemeRoomForm {
    name = "";
    start_time = "";
    start_date = "";
    end_date = "";
    local = "";
    min_quantity = '';
    max_quantity = '';
    speaker = "";
    description = "";
    hours_quantity = '';
    audiences = "";
    event_type = "";
    status = "upcoming";
}

const roomForm = ref(new ThemeRoomForm());
const valid = ref(false);
const submitting = ref(false);
const errorMessage = ref<string | null>(null);
const showError = ref(false);
const eventTypeOptions = ['conference', 'workshop', 'seminar', 'meetup'];

const router = useRouter();

const isFormValid = computed(() => {
    return Object.values(roomForm.value).every(field => field);
});

const showSnackbar = (message: string, type: string) => {
    snackbarText.value = message;
    snackbarColor.value = type === 'success' ? 'green' : 'red';
    snackbar.value = true;
};

const resetForm = () => {
    roomForm.value = new ThemeRoomForm();
};

const buildFormData = () => {
    const form = new FormData();
    Object.entries(roomForm.value).forEach(([key, value]) => {
        form.append(key, value.toString());
        console.log(key, value);
    });
    form.append('event_id', router.currentRoute.value.params.id.toString());
    return form;
};

const addRoom = async (form: FormData) => {
    await addThemeRoom(form);
    showSnackbar('Sala criada com sucesso', 'success');
};

const updateRoom = async (roomId: number, form: FormData) => {
    await updateThemeRoom(roomId, form);
    showSnackbar('Sala atualizada com sucesso', 'success');
};

const submitForm = async () => {
    if (submitting.value || !isFormValid.value) return;

    submitting.value = true;

    if (!validateFields(roomForm.value)) {
        errorMessage.value = 'Por favor, preencha todos os campos obrigatórios.';
        submitting.value = false;
        return;
    }

    const form = buildFormData();

    try {
        const roomId = router.currentRoute.value.params.room_id;
        if (roomId) {
            await updateRoom(Number(roomId), form);
        } else {
            await addRoom(form);
        }
        
        resetForm();
        router.back();

    } catch (error) {
        console.error('Erro ao processar sala:', error);
        showSnackbar(error.response.data.detail.toString() ?? 'Erro ao processar sala', 'error');
        errorMessage.value = 'Erro ao processar sala. Por favor, tente novamente.';
        showError.value = true;
    } finally {
        submitting.value = false;
    }
};

const goBack = () => {
    router.back();
};
</script>


<style scoped></style>
