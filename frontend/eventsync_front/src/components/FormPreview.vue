<template>
    <v-form class="d-flex flex-column align-center">
        <div v-for="(question, index) in questions" :key="index" class="field-size">
            <v-card outlined elevation="4">
            <v-card-title class="d-flex justify-space-between align-center">
                <p class="question-text">{{ question.text }}</p>
            </v-card-title>
    
            <v-card-subtitle v-if="question.type === 'Discursiva'">
                <v-textarea readonly :placeholder="`Resposta para: ${question.text}`" outlined></v-textarea>
            </v-card-subtitle>
    
            <v-card-subtitle v-if="question.type === 'Múltipla escolha'">
                <v-checkbox v-for="(option, optIndex) in question.optionList" :key="optIndex" :label="option" :value="option"></v-checkbox>
            </v-card-subtitle>
    
            <v-card-subtitle v-if="question.type === 'Objetiva'">
                <v-radio-group v-model="question.selectedOption" column>
                    <v-radio v-for="(option, optIndex) in question.optionList" :key="optIndex" :label="option" :value="option"></v-radio>
                </v-radio-group>
                </v-card-subtitle>
            </v-card>
        </div>
    </v-form>
</template>
  
<script setup lang="ts"> 
import type { QuestionView } from '@/types/questions';

const props = defineProps<{
    questions: QuestionView[]
}>()
</script>
  
<style scoped>
.field-size {
    max-width: 350px;
    min-width: 300px;
    width: 100%;
    margin-bottom: auto;
    font-size: 1.2rem;

}

.question-text {
    word-wrap: break-word; /* Garante que o texto longo seja quebrado */
    overflow-wrap: break-word; /* Garante que o texto longo seja quebrado */
    white-space: pre-wrap; /* Mantém espaços e quebras de linha */
}
</style>
  