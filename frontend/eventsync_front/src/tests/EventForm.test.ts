import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import EventForm from '@/components/EventForm.vue'

describe('EventForm.vue', () => {
  const wrapper = mount(EventForm)

  it('renders correctly', () => {
    expect(wrapper.html()).toMatchSnapshot()
  })

  it('renders the components properly', () => {
    expect(wrapper.find('h1.form-title').text()).toBe('Criar formulário')
    expect(wrapper.find('h2.form-title').text()).toBe('Visualizar Formulário')
  })

  it('contains v-select component for question type', () => {
    expect(wrapper.find('v-select').exists()).toBe(true)
  })

  it('contains v-text-field component for question title', () => {
    expect(wrapper.find('v-text-field').exists()).toBe(true)
  })
})
