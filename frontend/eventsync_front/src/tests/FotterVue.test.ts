import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import FooterVue from '@/components/Footer.vue'

describe('FooterVue.vue', () => {
  const wrapper = mount(FooterVue)
  it('renders correctly', () => {
    expect(wrapper.html()).toMatchSnapshot()
  })

  it('displays the correct number of findEventsItems', () => {
    expect(wrapper.findAll('v-list-item')).toHaveLength(10)
  })

  it('contains the correct footer sections', () => {
    expect(wrapper.text()).toContain('Encontre Eventos')
    expect(wrapper.text()).toContain('Mapa do site')
    expect(wrapper.text()).toContain('Contato')
  })
})
