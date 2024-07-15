import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import NavBar from '@/components/NavBar.vue'

describe('NavBar.vue', () => {
  const wrapper = mount(NavBar)
  it('renders correctly', () => {
    expect(wrapper.html()).toMatchSnapshot()
  })

  it('toggles search field visibility', async () => {
    const toggleSearchField = wrapper.vm.toggleSearchField
    await toggleSearchField()
    expect(wrapper.find('v-text-field').exists()).toBe(true)
  })
})
