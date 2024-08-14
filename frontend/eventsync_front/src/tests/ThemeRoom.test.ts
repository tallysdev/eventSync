import { mount } from "@vue/test-utils";
import { describe, it, expect } from "vitest";
import ThemeRoom from "@/components/ThemeRoom/CreateComponentTR.vue";

describe("ThemeRoom.vue", () => {
    const wrapper = mount(ThemeRoom);

    it("renders correctly", () => {
        expect(wrapper.html()).toMatchSnapshot();
    });
    it('contains the event title', () => {
        const title = wrapper.find('h1');
        expect(title.exists()).toBe(true);
        expect(title.text()).toBe('Evento: Nome do Evento');
    });

    it('contains the form title', () => {
        const formTitle = wrapper.find('h1.text-center');
        expect(formTitle.exists()).toBe(true);
        expect(formTitle.text()).toBe('Criar sala temática.');
    });

    it('contains all form fields', () => {
        const labels = [
            'Local da sala',
            'Nome da sala',
            'Descrição',
            'Público Alvo',
            'Data',
            'Horário',
            'Número Min. de Participantes',
            'Número Máx. de Participantes'
        ];

        labels.forEach(label => {
            expect(wrapper.find(`input[label="${label}"]`).exists())
        });
    });

    it('contains create and back buttons', () => {
        const createButton = wrapper.find('v-btn[color="primary"]');
        const backButton = wrapper.find('v-btn[color="secondary"]');

        expect(createButton.exists()).toBe(true);
        expect(createButton.text()).toBe('Criar');

        expect(backButton.exists()).toBe(true);
        expect(backButton.text()).toBe('Voltar');
    });
})