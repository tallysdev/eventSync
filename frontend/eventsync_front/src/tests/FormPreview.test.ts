import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import FormPreview from '@/components/FormPreview.vue'

interface QuestionView {
  text: string
  type: 'Discursiva' | 'Múltipla escolha' | 'Objetiva'
  optionList: string[]
  selectedOptions: string[]
  selectedOption: string
}

describe('FormPreview.vue', () => {
  const questions: QuestionView[] = [
    {
      text: 'O que você mais gostou?',
      type: 'Discursiva',
      optionList: [],
      selectedOptions: [],
      selectedOption: ''
    },
    {
      text: 'Escolha seu tipo de evento:',
      type: 'Múltipla escolha',
      optionList: ['AAA', 'BBB', 'CCC'],
      selectedOptions: [],
      selectedOption: ''
    },
    {
      text: 'Qual é o seu gênero musical favorito?',
      type: 'Objetiva',
      optionList: ['Rock', 'Pop', 'Jazz'],
      selectedOptions: [],
      selectedOption: ''
    }
  ]

  const wrapper = mount(FormPreview, {
    props: {
      questions
    }
  })

  it('renders correctly', () => {
    expect(wrapper.html()).toMatchSnapshot()
  })

  it('renders the correct number of questions', () => {
    const questionCards = wrapper.findAll('v-card')
    expect(questionCards.length).toBe(questions.length)
  })
})
