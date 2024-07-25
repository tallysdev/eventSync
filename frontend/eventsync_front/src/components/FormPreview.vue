<template>
    <v-form class="d-flex flex-column align-center">
        <div v-for="(question, index) in questions" :key="index" class="field-size">
            <v-card outlined elevation="4">
            <v-card-title class="d-flex justify-space-between align-center">
                <h3>{{ question.text }}</h3>
            </v-card-title>
    
            <v-card-subtitle v-if="question.type === 'Discursiva'">
                <v-textarea readonly :placeholder="`Resposta para: ${question.text}`" outlined></v-textarea>
            </v-card-subtitle>
    
            <v-card-subtitle v-if="question.type === 'Múltipla escolha'">
                <v-checkbox-group v-model="question.selectedOptions" column>
                <v-checkbox v-for="(option, optIndex) in question.optionList" :key="optIndex" :label="option" :value="option"></v-checkbox>
                </v-checkbox-group>
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
  
<script setup> 
const props = defineProps({
    questions: Array
})
</script>
  
<style scoped>
.field-size {
    max-width: 450px;
    min-width: 450px;
    width: 100%;
    margin-bottom: auto;
    font-size: 1.2rem;
    margin-left: auto;
    margin-right: auto; 
}
</style>
  