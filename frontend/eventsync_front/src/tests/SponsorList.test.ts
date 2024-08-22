import { mount } from '@vue/test-utils'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import SponsorList from '@/components/sponsors/SponsorList.vue'

// Mock the service
vi.mock('@/services/sponsorService', () => ({
  fetchSponsors: vi.fn()
}))

describe('SponsorList.vue', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders correctly', () => {
    const wrapper = mount(SponsorList)
    expect(wrapper.html()).toMatchSnapshot()
  })

  it('opens the dialog when the Add Sponsor button is clicked', async () => {
    // Arrange
    const wrapper = mount(SponsorList)

    // Act
    await wrapper.find('v-btn').trigger('click')

    // Assert
    const dialog = (wrapper.vm as any).dialog
    expect(dialog.value).toBe(true)
  })
})
