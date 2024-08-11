import { mount } from '@vue/test-utils'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import SponsorList from '@/components/sponsors/SponsorList.vue'
import { fetchSponsors } from '@/services/sponsorService'

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

  // it('renders a loading spinner when data is being fetched', async () => {
  //   const wrapper = mount(SponsorList)

  //   wrapper.get('v-progess-circular')

  //   wrapper.vm.$options.setup = () => ({
  //     sponsors: [],
  //     loading: true,
  //     dialog: false
  //   })

  //   expect(wrapper.findComponent({ name: 'v-progress-circular' }).exists())
  // })

  // it('renders a message when no sponsors are found', async () => {
  //   // Arrange
  //   const fetchSponsorsMock = vi.mocked(fetchSponsors)
  //   fetchSponsorsMock.mockResolvedValue({
  //     data: { results: [], count: 0 },
  //     status: 0,
  //     statusText: '',
  //     headers: undefined,
  //     config: undefined
  //   })

  //   const wrapper = mount(SponsorList)

  //   // wrapper.vm.$options.setup = () => ({
  //   //   sponsors: [],
  //   //   loading: false,
  //   //   dialog: false
  //   // })

  //   // Act
  //   await wrapper.vm.$nextTick()

  //   // Assert
  //   const alert = wrapper.findComponent({ name: 'v-alert' })
  //   expect(alert.exists()).to
  //   expect(alert.text()).toContain('Nenhum patrocinador encontrado')
  // })

  // it('renders a list of sponsors when data is fetched', async () => {
  //   // Arrange
  //   const fetchSponsorsMock = vi.mocked(fetchSponsors)
  //   fetchSponsorsMock.mockResolvedValue({
  //     data: {
  //       results: [
  //         {
  //           id: 1,
  //           name: 'Sponsor 1',
  //           email: 'email1@example.com',
  //           description: 'Description 1',
  //           logo: ''
  //         },
  //         {
  //           id: 2,
  //           name: 'Sponsor 2',
  //           email: 'email2@example.com',
  //           description: 'Description 2',
  //           logo: ''
  //         }
  //       ],
  //       count: 2
  //     },
  //     status: 0,
  //     statusText: '',
  //     headers: undefined,
  //     config: undefined
  //   })

  //   const wrapper = mount(SponsorList)

  //   // Act
  //   await wrapper.vm.$nextTick()

  //   // Assert
  //   const sponsorCards = wrapper.findAllComponents({ name: 'v-card' })
  //   expect(sponsorCards).toHaveLength(2)
  // })

  it('opens the dialog when the Add Sponsor button is clicked', async () => {
    // Arrange
    const wrapper = mount(SponsorList)

    // Act
    await wrapper.find('v-btn').trigger('click')

    // Assert
    expect(wrapper.vm.dialog).toBe(true)
  })
})
