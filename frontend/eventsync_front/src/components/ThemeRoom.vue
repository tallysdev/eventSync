<template>
    <v-main class="h-100 pa-0">
        <v-container class="">
            <h1>Evento: Nome do Evento</h1>
            <h1 class="text-center">Criar sala temática.</h1>
            <v-form class="mb-10">
                <v-text-field variant="outlined" label="Data Inicial" type="date"></v-text-field>
                <v-text-field variant="outlined" label="Data Final" type="date"></v-text-field>
                <v-text-field variant="outlined"
                name="name"
                label="Horario inicial da sala."
                id="id"
                type="time"
                ></v-text-field>
                <v-text-field variant="outlined" label="Local da sala"></v-text-field>
                <v-text-field variant="outlined" label="Número Min. de Participantes"></v-text-field>
                <v-text-field variant="outlined" label="Número Máx. de Participantes"></v-text-field>
                <v-text-field variant="outlined" label="Palestrante"></v-text-field>
                <v-text-field variant="outlined" label="Nome da sala"></v-text-field>
                <v-text-field variant="outlined" label="Descrição"></v-text-field>
                <v-text-field variant="outlined" label="Quantidade horas no certificado"></v-text-field>
                <v-text-field variant="outlined" label="Público Alvo"></v-text-field>
                <v-text-field variant="outlined" label="Tipo de evento."></v-text-field>

                <v-container grid-list-xs class="d-flex justify-center ga-10">
                    <v-btn color="primary">Criar</v-btn>
                    <v-btn color="secondary">Voltar</v-btn>
                </v-container>
            </v-form>
        </v-container>
    </v-main>
</template>

<script>
export default {

}
</script>
<style lang="">

</style>