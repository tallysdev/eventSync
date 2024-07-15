import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import Home from '@/components/Home.vue'

describe('Home.vue', () => {
  const wrapper = mount(Home)

  it('renders correctly', () => {
    expect(wrapper.html()).toMatchSnapshot()
  })

  it('contains NavBar component', () => {
    expect(wrapper.findComponent({ name: 'NavBar' }).exists()).toBe(true)
  })

  it('contains EventType component', () => {
    expect(wrapper.findComponent({ name: 'EventType' }).exists()).toBe(true)
  })

  it('contains UpcomingEvents component', () => {
    expect(wrapper.findComponent({ name: 'UpcomingEvent' }).exists()).toBe(true)
  })

  it('contains Footer component', () => {
    expect(wrapper.findComponent({ name: 'Footer' }).exists()).toBe(true)
  })
})
