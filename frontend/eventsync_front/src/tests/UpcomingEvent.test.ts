import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import UpcomingEvents from '@/components/home/UpcomingEvent.vue'

describe('UpcomingEvents.vue', () => {
  const upcomingEvents = [
    {
      id: 1,
      name: 'Titulo para encher linguiça e preencher o espaço para mostrar o texto',
      date: 'Sex, 30 ago',
      time: '19:00 - 21:00',
      location: 'UFRN/Ceres - Caicó, RN',
      buttonText: 'Saiba mais'
    },
    {
      id: 2,
      name: 'Partida de Futebol',
      date: '15 de Julho',
      time: '16:00 - 18:00',
      location: 'Estádio ABC',
      buttonText: 'Saiba mais'
    },
    {
      id: 3,
      name: 'Peça de Teatro',
      date: '20 de Julho',
      time: '20:00 - 22:00',
      location: 'Teatro 123',
      buttonText: 'Saiba mais'
    }
  ]
  const wrapper = mount(UpcomingEvents, {
    props: { upcomingEvents },
  })

  it('renders correctly', () => {
    expect(wrapper.html()).toMatchSnapshot()
  })

  it('renders the correct number of upcoming events', () => {
    expect(wrapper.findAll('v-carousel-item')).toHaveLength(upcomingEvents.length)
  })
})
