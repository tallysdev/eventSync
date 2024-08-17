<template>
    <NavBar />
    <v-main>
        <h1 class="text-center">Evento 1</h1>
        <h1>Programação:</h1>
        <ListCard />
    </v-main>
    <FooterVue />
</template>
<script setup lang="ts">
import NavBar from '../NavBar.vue';
import FooterVue from '../Footer.vue';
import ListCard from './ListCardTRComponent.vue';
</script>   
<style lang="">

</style>