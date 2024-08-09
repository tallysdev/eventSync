<template>
    <v-app class="d-flex flex-column h-100 w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mb-10">
        <v-container fluid class="pa-6 d-flex flex-column align-center">
            <v-form class="d-flex flex-column align-center">
                <h1 class="form-title">Criar formulário</h1>
             
                <div v-for="(question, index) in questions" :key="index" class="field-size">
                    <v-card :class="['question-card', { 'invalid-card': !question.isValid }]" outlined elevation="4">
                        <v-card-title class="d-flex justify-space-between align-center">
                            <v-select
                                v-model="question.type"
                                :items="['Discursiva', 'Múltipla escolha', 'Objetiva']"
                                label="Tipo de Pergunta"
                                outlined
                                class="mt-2"
                                @change="(value: any) => handleTypeChange(index, value)"                               
                            ></v-select>
                            
                            <v-btn @click="removeQuestion(index)" icon class="ml-2">
                                <v-icon>mdi-delete</v-icon>
                            </v-btn>

                        </v-card-title>

                        <v-card-subtitle>
                            <v-textarea
                                v-model="question.text"
                                label="Texto da Pergunta"
                                outlined
                                required
                                rows="4"
                                @input="validateQuestion(index)"          
                            ></v-textarea>
                        </v-card-subtitle>
                        
                        <v-card-subtitle> 
                            <div v-if="question.type === 'Múltipla escolha' || question.type === 'Objetiva'">
                                <v-text-field
                                    v-model="question.optionInput"
                                    label="Adicionar Opção"
                                    outlined
                                    class="mt-2"
                                ></v-text-field>

                                <v-btn @click="addOption(index)" color="primary" class="mb-4">Adicionar Opção</v-btn>

                                <div v-for="(option, optIndex) in question.optionList" :key="optIndex" class="option-container d-flex align-center mt-2">
                                    <v-textarea
                                        :value="option"
                                        readonly
                                        outlined
                                        class="option-text mr-2"
                                    ></v-textarea>

                                    <v-btn @click="removeOption(index, optIndex)" icon class="ml-2">
                                        <v-icon>mdi-delete</v-icon>
                                    </v-btn>
                                </div>
                                  
                            </div>
                        </v-card-subtitle>

                        <v-card-subtitle>
                            <div class="d-flex align-center">
                                <v-btn @click="moveQuestion(index, -1)" icon :disabled="index === 0" class="move-btn">
                                  <v-icon>mdi-arrow-up</v-icon>
                                </v-btn>
                                <v-btn @click="moveQuestion(index, 1)" icon :disabled="index === questions.length - 1" class="move-btn">
                                  <v-icon>mdi-arrow-down</v-icon>
                                </v-btn>
                              </div>
                        </v-card-subtitle>
                            
                    </v-card>
                               
                </div>

                <v-btn @click="addQuestion" color="primary"  class="mt-4">Adicionar Pergunta</v-btn>
                <v-btn color="primary" class="mt-4">Salvar Formulário</v-btn>
                
            </v-form>

            <v-divider class="my-4"></v-divider>

            <h2 class="form-title">Visualizar Formulário</h2>
            <FormPreview :questions="questions" />

        </v-container>
    </v-main>
    <FooterVue />
    
    </v-app>
</template>
  
<script setup lang="ts">
import NavBar from '../components/NavBar.vue'
import FooterVue from '../components/Footer.vue'
import FormPreview from '../components/FormPreview.vue'
import type { QuestionCreate } from '@/types/types';
import { ref } from 'vue'

const questions = ref<QuestionCreate[]>([{ text: '', type: 'Discursiva', optionList: [], isValid: true}])

const addQuestion = () => {
    validateQuestions()
    questions.value.push({ text: '', type: 'Discursiva', optionList: [], isValid: true })
}

const removeQuestion = (index: number) => {
    questions.value.splice(index, 1)
}

const addOption = (index: number) => {
    const question = questions.value[index];
    if (question.optionInput?.trim()) {
        question.optionList.push(question.optionInput.trim())
        question.optionInput = ''
        validateQuestion(index);
    } else {
        alert('Digite uma opção válida')
    }
}

const moveQuestion = (index: number, direction: any) => {
    const newIndex = index + direction
    if (newIndex < 0 || newIndex >= questions.value.length) return
    const movedQuestion = questions.value.splice(index, 1)[0]
    questions.value.splice(newIndex, 0, movedQuestion)
}

const removeOption = (questionIndex: number, optionIndex: number) => {
    questions.value[questionIndex].optionList.splice(optionIndex, 1)
    validateQuestion(questionIndex)
}

const handleTypeChange = (index: number, type: 'Discursiva' | 'Múltipla escolha' | 'Objetiva') => {
    const question = questions.value[index]
    question.type = type

    if (type === 'Discursiva') {
        question.optionList = []
    } 
    validateQuestion(index)
}

const validateQuestion = (index: number) => {
    const question = questions.value[index]
    
    if(question.type === 'Discursiva') {
        question.isValid = question.text.trim() !== ''
    }
    else {
        question.isValid = question.text.trim() !== '' && question.optionList.length > 0
    }
}

const validateQuestions = () => {
    questions.value.forEach((_: any, index: number) => validateQuestion(index))
}

</script>

<style scoped>
.form-title {
    text-align: center;
    margin-bottom: 30px;
    font-size: 2.8rem;
}

.field-size {
    max-width: 450px; 
    min-width: 300px;
    width: 100%;
    margin-bottom: auto;
    font-size: 1.2rem;
    margin-left: auto;
    margin-right: auto; 
}

.question-card {
    width: 100%;
    margin-top: 16px;
}

.invalid-card {
    background-color: #fa8a93;
    border-color: #55010a;
    color: #721c24;
}

.mt-4 {
    margin-top: 16px;
}

.ml-2 {
    color: red;
}

.move-btn {
    margin-bottom: 16px;
    margin-left: 8px;
}

</style>