<template>
    <v-app>
        <NavBar />
        <v-main>
            <ThemeRoom />
        </v-main>
        <FooterVue />
    </v-app>
</template>

<style scoped>

</style>

<script setup lang="ts">
import ThemeRoom from '@/components/ThemeRoom.vue';
import NavBar from '@/components/NavBar.vue';
import FooterVue from '@/components/Footer.vue';

</script>