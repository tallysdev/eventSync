<template>
    <v-app class="d-flex flex-column h-100 w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mb-10">
        <v-container fluid class="pa-6 d-flex flex-column align-center">
            <v-form class="d-flex flex-column align-center">
                <h1 class="form-title">Criar formulário</h1>
                
                <div v-for="(question, index) in questions" :key="index" class="field-size">
                    <v-card class="question-card" outlined elevation="4">
                        <v-card-title class="d-flex justify-space-between align-center">
                            <v-select
                                v-model="question.type"
                                :items="['Discursiva', 'Múltipla escolha']"
                                label="Tipo de Pergunta"
                                outlined
                                class="mt-2"
                            ></v-select>
                            
                            <v-btn @click="removeQuestion(index)" icon class="ml-2">
                                <v-icon>mdi-delete</v-icon>
                            </v-btn>

                        </v-card-title>

                        <v-card-subtitle>
                            <v-textarea
                                v-model="question.Discursiva"
                                label="Texto da Pergunta"
                                outlined
                                required
                                rows="4"
                            ></v-textarea>
                        </v-card-subtitle>

                        <v-card-subtitle> 
                            <div v-if="question.type === 'Múltipla escolha'">
                                <v-text-field
                                    v-model="question.optionInput"
                                    label="Adicionar Opção"
                                    outlined
                                    class="mt-2"
                                ></v-text-field>

                                <v-btn @click="addOption(index)" color="primary" class="mt-2">Adicionar Opção</v-btn>

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
                            
                    </v-card>
                                  
                </div>
                
                <v-btn @click="addQuestion" color="primary"  class="mt-4">Adicionar Pergunta</v-btn>
                <v-btn type="submit" color="primary" class="mt-4">Salvar Formulário</v-btn>
                
            </v-form>
        </v-container>
    </v-main>
    <FooterVue />
    </v-app>
</template>
  
<script setup>
    import NavBar from '../components/NavBar.vue'
    import FooterVue from '../components/Footer.vue'
    import { ref } from 'vue'

const questions = ref([{ text: '', type: 'Discursiva', options: [], optionList: [] }])

const addQuestion = () => {
  questions.value.push({ text: '', type: 'Discursiva', options: [], optionList: [] })
}

const removeQuestion = (index) => {
  questions.value.splice(index, 1)
}

const addOption = (index) => {
  if (questions.value[index].optionInput.trim()) {
    questions.value[index].optionList.push(questions.value[index].optionInput.trim())
    questions.value[index].optionInput = ''
  } else {
    alert('Digite uma opção válida')
  }
}

const removeOption = (questionIndex, optionIndex) => {
  questions.value[questionIndex].optionList.splice(optionIndex, 1)
}

</script>
  
<style scoped>
.form-title {
    text-align: center;
    margin-bottom: 30px;
    font-size: 2.8rem;
}

.field-size {
    max-width: 100%; 
    width: 100%;
    margin-bottom: auto;
    font-size: 1.2rem;
}

.question-card {
    width: 100%;
    margin-top: 16px;
}

.mt-4 {
    margin-top: 16px;
}

.mb-4 {
    margin-bottom: 16px;
}

.ml-2 {
    color: red;
}

</style>