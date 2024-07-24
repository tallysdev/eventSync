<template>
    <v-app class="d-flex flex-column h-100 w-100">
    <NavBar />
    <v-main class="flex-grow-1 pa-16 mb-10">
        <v-container fluid class="pa-4 d-flex flex-column h-100 w-100">
            <v-form class="d-flex flex-column align-center">
                <h1 class="form-title">Criar Formulário</h1>
                
            </v-form>
        </v-container>
    </v-main>
    <FooterVue />
    </v-app>
</template>
  
<script setup>
    import NavBar from '../components/NavBar.vue'
    import FooterVue from '../components/Footer.vue'
  
</script>
  
<style scoped>
  .form-title {
    text-align: center;
    margin-bottom: 30px;
    font-size: 2rem;
}
  
</style>
  