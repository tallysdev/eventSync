export interface QuestionView {
  text: string
  type: 'Discursiva' | 'Múltipla escolha' | 'Objetiva'
  optionList?: string[]
  selectedOptions?: string[]
  selectedOption?: string
}

export interface QuestionCreate {
  text: string
  type: 'Discursiva' | 'Múltipla escolha' | 'Objetiva'
  optionList: string[]
  optionInput?: string
  isValid: boolean
}
