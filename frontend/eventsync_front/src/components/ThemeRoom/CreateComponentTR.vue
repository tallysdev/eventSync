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
        </v-container>
    </v-main>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { addThemeRoom } from '@/services/themRoomService';
import {
    validateFields,
    validateNumberInput,
    snackbar,
    snackbarText,
    snackbarColor
} from '../../stores/validatorRoom';

const router = useRouter();

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
const eventTypeOptions = ['conference', 'workshop', 'seminar', 'meetup']
const valid = ref(false);
const submitting = ref(false);
const errorMessage = ref<string | null>(null);
const showError = ref(false);

const submitForm = async () => {
    if (submitting.value) return
    submitting.value = true

    if (
        !validateFields({
            name: roomForm.value.name,
            start_time: roomForm.value.start_time,
            start_date: roomForm.value.start_date,
            end_date: roomForm.value.end_date,
            local: roomForm.value.local,
            min_quantity: roomForm.value.min_quantity,
            max_quantity: roomForm.value.max_quantity,
            speaker: roomForm.value.speaker,
            description: roomForm.value.description,
            hours_quantity: roomForm.value.hours_quantity,
            audiences: roomForm.value.audiences,
            event_type: roomForm.value.event_type,
            status: 'upcoming'
        })
    ) {
        // console.log('Campos validados:', validateFields(roomForm.value.value));
        errorMessage.value = 'Por favor, preencha todos os campos obrigatórios.'
        submitting.value = false
        return
    }
    console.log('174');
    const form = new FormData();
    form.append('name', roomForm.value.name);
    form.append('start_time', roomForm.value.start_time);
    form.append('start_date', roomForm.value.start_date);
    form.append('end_date', roomForm.value.end_date);
    form.append('local', roomForm.value.local);
    form.append('min_quantity', roomForm.value.min_quantity.toString());
    form.append('max_quantity', roomForm.value.max_quantity.toString());
    form.append('speaker', roomForm.value.speaker);
    form.append('description', roomForm.value.description);
    form.append('hours_quantity', roomForm.value.hours_quantity.toString());
    form.append('audiences', roomForm.value.audiences);
    form.append('event_type', roomForm.value.event_type);
    form.append('status', 'upcoming');
    form.append('event', router.currentRoute.value.params.id.toString());
    try {
        console.log('teste');
        await addThemeRoom(form);
        console.log('Sala criada com sucesso');
        showSnackbar('Sala criada com sucesso', 'success');
        resetForm();
        // console.log('Sala criada com sucesso:', response.data);
        router.push('/success-page');
    } catch (error) {
        console.error('Erro ao criar sala:', error);
        errorMessage.value = 'Erro ao criar sala. Por favor, tente novamente.', 'error';
        showError.value = true;
    } finally {
        submitting.value = false;
    }
};

const showSnackbar = (message: string, type: string) => {
    snackbarText.value = message
    snackbarColor.value = type === 'success' ? 'green' : 'red'
    snackbar.value = true
}

const resetForm = () => {
    roomForm.value = new ThemeRoomForm()
}
const isFormValid = computed(() => {
    return (
        roomForm.value.name &&
        roomForm.value.start_time &&
        roomForm.value.start_date &&
        roomForm.value.end_date &&
        roomForm.value.local &&
        roomForm.value.min_quantity &&
        roomForm.value.max_quantity &&
        roomForm.value.description &&
        roomForm.value.hours_quantity &&
        roomForm.value.event_type
    )
})

const goBack = () => {
    router.back();  // Volta para a página anterior
};

</script>

<style scoped></style>
