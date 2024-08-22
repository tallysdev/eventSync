import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import EventType from '@/components/home/EventType.vue'

describe('EventType.vue', () => {
  const eventTypes = [
    { id: 1, name: 'Show', icon: 'mdi-music' },
    { id: 2, name: 'Esporte', icon: 'mdi-basketball' },
    { id: 3, name: 'Teatro', icon: 'mdi-drama-masks' },
    { id: 4, name: 'Cinema', icon: 'mdi-movie' }
  ]

  const wrapper = mount(EventType, {
    props: { eventTypes }
  })

  it('renders correctly', () => {
    expect(wrapper.html()).toMatchSnapshot()
  })

  it('renders the correct number of event types', () => {
    expect(wrapper.findAll('v-avatar')).toHaveLength(eventTypes.length)
  })
})
