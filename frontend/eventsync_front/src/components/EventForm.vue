<template>
    <v-app class="d-flex flex-column h-100 w-100">
        <NavBar />
        <v-main class="flex-grow-1 pa-16 mb-10">
            <v-container fluid class="pa-6 d-flex flex-column align-center">
                <v-form class="d-flex flex-column align-center">
                    <h1 class="form-title">Cadastrar formulário</h1>
                    
                    <v-card class="question-card" outlined elevation="4">
                        
                        <v-card-subtitle>
                            <v-text-field
                                label="Link do formulário"
                                v-model="link"
                                type="url"
                                outlined
                                dense
                            />
                        </v-card-subtitle>

                        <v-card-subtitle>
                            <v-text-field
                                label="Descrição"
                                v-model="description"
                                type="text"
                                outlined
                                required 
                            />
                        </v-card-subtitle>

                        <v-card-subtitle>
                            <v-text-field 
                                v-model="eventDate" 
                                label="Quando ficará disponível?" 
                                type="date" 
                                required 
                                class="field-size">
                            </v-text-field>

                        </v-card-subtitle>

                        <v-card-subtitle>
                            <v-text-field 
                                v-model="eventDate" 
                                label="Quando termina?" 
                                type="date" 
                                required 
                                class="field-size">
                            </v-text-field>

                        </v-card-subtitle>
                        
                    </v-card>

                    <v-btn @click="submitForm" color="primary" class="mt-4">Enviar</v-btn>

                </v-form>
            </v-container>
        </v-main>
        <FooterVue />
    </v-app>
</template>
  
<script setup>
import { ref } from 'vue'
import NavBar from '../components/NavBar.vue'
import FooterVue from '../components/Footer.vue'

const link = ref('')

const submitForm = () => {
    alert('Link enviado:', link.value)
}
</script>
  
<style scoped>
.form-title {
    text-align: center;
    margin-bottom: 30px;
    font-size: 2.8rem;
}

.question-card {
    width: 100%;
    max-width: 500px;
    margin: 16px;
    margin-top: 16px;
}

.mt-4 {
    margin-top: 16px;
    margin-bottom: 16px;
}

</style>
