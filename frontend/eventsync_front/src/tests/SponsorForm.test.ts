import { mount } from '@vue/test-utils'
import { describe, it, expect, vi } from 'vitest'
import SponsorForm from '@/components/sponsors/SponsorForm.vue'
import { addSponsor } from '@/services/sponsorService'

vi.mock('@/services/sponsorService', () => ({
  addSponsor: vi.fn()
}))

describe('SponsorForm.vue', () => {

  it('render correctly', () => {
    const wrapper = mount(SponsorForm, {
      props: {
        dialog: true
      }
    })
    expect(wrapper.html()).toMatchSnapshot()
  })

  it('renders the form correctly', () => {
    const wrapper = mount(SponsorForm, {
      props: {
        dialog: true
      }
    })

    expect(wrapper.find('v-text-field[label="Nome"]').exists()).toBe(true)
    expect(wrapper.find('v-text-field[label="Email"]').exists()).toBe(true)
    expect(wrapper.find('v-text-field[label="Telefone"]').exists()).toBe(true)
    expect(wrapper.find('v-textarea[label="Descrição"]').exists()).toBe(true)
    expect(wrapper.find('v-file-input[label="Logo"]').exists()).toBe(true)
  })

  // it('shows an error message when there is an error', async () => {
  //   const errorMessage =
  //     'Ocorreu um erro ao tentar adicionar o patrocinador. Por favor, tente novamente.'
  //   vi.mocked(addSponsor).mockRejectedValue(new Error(errorMessage))

  //   const wrapper = mount(SponsorForm, {
  //     props: {
  //       dialog: true
  //     }
  //   })

  //   await wrapper.setData({
  //     newSponsor: { name: 'Test', email: 'test@example.com', phone: '', description: '', logo: '' }
  //   })
  //   await wrapper.find('v-btn[text="Salvar"]').trigger('click')

  //   expect(wrapper.find('v-alert').text()).toContain(errorMessage)
  // })

  // it('calls addSponsor when form is submitted successfully', async () => {
  //   vi.mocked(addSponsor).mockResolvedValue({
  //     data: undefined,
  //     status: 0,
  //     statusText: '',
  //     headers: undefined,
  //     config: undefined
  //   })

  //   const wrapper = mount(SponsorForm, {
  //     props: {
  //       dialog: true
  //     }
  //   })

  //   await wrapper.setData({
  //     newSponsor: { name: 'Test', email: 'test@example.com', phone: '', description: '', logo: '' }
  //   })
  //   await wrapper.find('v-btn[text="Salvar"]').trigger('click')

  //   expect(vi.mocked(addSponsor).toHaveBeenCalled())
  // })

  // it('emits update:dialog when the dialog is closed', async () => {
  //   const wrapper = mount(SponsorForm, {
  //     props: {
  //       dialog: true
  //     }
  //   })

  //   await wrapper.find('v-btn[text="Cancelar"]').trigger('click')

  //   expect(wrapper.emitted('update:dialog')).toBeTruthy()
  //   expect(wrapper.emitted('update:dialog')?.[0]).toEqual([false])
  // })
})
