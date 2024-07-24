<template>
    <v-app class="d-flex flex-column h-100 w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mb-10">
        <v-container fluid class="pa-6 d-flex flex-column align-center">
            <v-form class="d-flex flex-column align-center">
                <h1 class="form-title">Criar formulário</h1>
                
                <div v-for="(question, index) in questions" :key="index" class="field-size">
                    <v-textarea
                        v-model="question.text"
                        :label="'Pergunta ' + (index + 1)"
                        outlined
                        required
                    ></v-textarea>
               
                </div>
        
                <v-btn @click="addQuestion" color="primary">Adicionar Pergunta</v-btn>
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

const questions = ref([{ text: '', type: 'text', options: [], optionList: [] }])

const addQuestion = () => {
  questions.value.push({ text: '', type: 'text', options: [], optionList: [] })
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
  
</style>
  