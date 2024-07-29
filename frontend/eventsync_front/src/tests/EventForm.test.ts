import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import EventForm from '@/components/EventForm.vue'

describe('EventForm.vue', () => {
    const wrapper = mount(EventForm)

    it('renders correctly', () => {
        expect(wrapper.html()).toMatchSnapshot()
    })

    it('renders the component properly', () => {
        expect(wrapper.find('h1.form-title').text()).toBe('Criar formulário')
    })
    
  
})
