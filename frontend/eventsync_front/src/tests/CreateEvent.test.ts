import { mount } from '@vue/test-utils'
import { describe, it, expect, beforeEach, vi } from 'vitest'
import EventForm from '@/components/CreateEventPage.vue'
import axios from 'axios'
import { snackbar, snackbarColor, snackbarText } from '@/stores/validatorEvent'

vi.mock('axios')

describe('CreateEventPage.vue', () => {
  let wrapper: any

  beforeEach(() => {
    wrapper = mount(EventForm)
  })

  it('renders correctly', () => {
    expect(wrapper.html()).toMatchSnapshot()
  })

  it('contains NavBar component', () => {
    expect(wrapper.findComponent({ name: 'NavBar' }).exists()).toBe(true)
  })

  it('contains Footer component', () => {
    expect(wrapper.findComponent({ name: 'Footer' }).exists()).toBe(true)
  })

  it('contains form fields', () => {
    expect(wrapper.find('v-text-field[label="Nome do Evento"]').exists()).toBe(true)
    expect(wrapper.find('v-text-field[label="Data de Início do Evento"]').exists()).toBe(true)
    expect(wrapper.find('v-text-field[label="Data de Fim do Evento"]').exists()).toBe(true)
    expect(wrapper.find('v-text-field[label="Quantidade Mínima de Participantes"]').exists()).toBe(true)
    expect(wrapper.find('v-text-field[label="Quantidade Máxima de Participantes"]').exists()).toBe(true)
    expect(wrapper.find('v-text-field[label="Quantidade de Horas"]').exists()).toBe(true)
    expect(wrapper.find('v-textarea[label="Descrição do Evento"]').exists()).toBe(true)
    expect(wrapper.find('v-select[label="Localização do Evento"]').exists()).toBe(true)
    expect(wrapper.find('v-select[label="Tipo do Evento"]').exists()).toBe(true)
    expect(wrapper.find('v-btn[type="submit"]').text()).toContain('Criar Evento')
    expect(wrapper.find('v-snackbar').exists()).toBe(true)
  })

  it('fetches locations on mount', async () => {
    const mockData = {
      data: {
        results: [
          { id: 1, local_name: 'Local A' },
          { id: 2, local_name: 'Local B' },
        ],
      },
    }
    axios.get.mockResolvedValueOnce(mockData)

    await wrapper.vm.$nextTick()
    await wrapper.vm.fetchLocations()

    expect(wrapper.vm.locations).toEqual(mockData.data.results)
    expect(axios.get).toHaveBeenCalledWith('http://127.0.0.1:8000/eventsync/api/v1/locals')
  })

  it('submits form and creates event successfully', async () => {
    const mockData = {
      data: {
        results: [
          { id: 1, local_name: 'Local A' },
          { id: 2, local_name: 'Local B' },
        ],
      },
    }
    axios.get.mockResolvedValueOnce(mockData)

    await wrapper.vm.$nextTick()
    await wrapper.vm.fetchLocations()

    const mockResponse = {
      data: {
        id: 1,
        name: 'Evento Teste',
        start_date: '2024-08-10',
        end_date: '2024-08-11',
        status: 'upcoming',
        local: 1,
        description: 'Descrição do evento teste',
        min_quantity: 10,
        max_quantity: 100,
        hours_quantity: 2,
        event_type: 'conference',
      },
    }
    axios.post.mockResolvedValueOnce(mockResponse)


    wrapper.setData({
      name: 'Evento Teste',
      start_date: '2024-08-10',
      end_date: '2024-08-11',
      local: 1,
      min_quantity: 10,
      max_quantity: 100,
      hours_quantity: 2,
      event_type: 'conference',
      description: 'Descrição do evento teste',
    })

    await wrapper.find('v-btn[type="submit"]').trigger('click')

    expect(axios.post).toHaveBeenCalledWith('http://127.0.0.1:8000/eventsync/api/v1/events/', {
      name: 'Evento Teste',
      start_date: '2024-08-10',
      end_date: '2024-08-11',
      status: 'upcoming',
      local: 1,
      description: 'Descrição do evento teste',
      min_quantity: 10,
      max_quantity: 100,
      hours_quantity: 2,
      event_type: 'conference',
    })

    expect(snackbar.value).toBe(true)
    expect(snackbarText.value).toBe('Evento criado com sucesso!')
    expect(snackbarColor.value).toBe('green')

  })

  it('handles event creation error', async () => {
    const errorResponse = {
      response: {
        data: {
          message: 'Erro ao criar evento',
        },
      },
    }
    axios.post.mockRejectedValueOnce(errorResponse)

    wrapper.setData({
      name: 'Evento Teste',
      start_date: '2024-08-10',
      end_date: '2024-08-11',
      local: 'Local A',
      min_quantity: 10,
      max_quantity: 100,
      hours_quantity: 2,
      event_type: 'conference',
      description: 'Descrição do evento teste',
    })

    await wrapper.find('v-btn[type="submit"]').trigger('click')
    await wrapper.vm.$nextTick()  // Aguarda a atualização do estado

    expect(snackbar.value).toBe(true)
    expect(snackbarText.value).toBe('Erro ao criar evento')
    expect(snackbarColor.value).toBe('red')
  })
})

