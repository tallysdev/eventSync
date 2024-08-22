// Lista de siglas de estados válidos
// Adiciona um mapeamento de estados para CEPs padrões
export const UFs = [
  { value: 'AC', label: 'Acre' },
  { value: 'AL', label: 'Alagoas' },
  { value: 'AP', label: 'Amapá' },
  { value: 'AM', label: 'Amazonas' },
  { value: 'BA', label: 'Bahia' },
  { value: 'CE', label: 'Ceará' },
  { value: 'DF', label: 'Distrito Federal' },
  { value: 'ES', label: 'Espírito Santo' },
  { value: 'GO', label: 'Goiás' },
  { value: 'MA', label: 'Maranhão' },
  { value: 'MT', label: 'Mato Grosso' },
  { value: 'MS', label: 'Mato Grosso do Sul' },
  { value: 'MG', label: 'Minas Gerais' },
  { value: 'PA', label: 'Pará' },
  { value: 'PB', label: 'Paraíba' },
  { value: 'PR', label: 'Paraná' },
  { value: 'PE', label: 'Pernambuco' },
  { value: 'PI', label: 'Piauí' },
  { value: 'RJ', label: 'Rio de Janeiro' },
  { value: 'RN', label: 'Rio Grande do Norte' },
  { value: 'RS', label: 'Rio Grande do Sul' },
  { value: 'RO', label: 'Rondônia' },
  { value: 'RR', label: 'Roraima' },
  { value: 'SC', label: 'Santa Catarina' },
  { value: 'SP', label: 'São Paulo' },
  { value: 'SE', label: 'Sergipe' },
  { value: 'TO', label: 'Tocantins' }
]

export const emailValidation = (value: string): string | true => {
  if (!value) {
    return 'Email é necessário'
  }
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailRegex.test(value)) {
    return 'Por favor, insira um email válido'
  }
  return true
}

export const passwordValidation = (value: string): string | true => {
  if (!value) {
    return 'Senha é necessária'
  }
  if (value.length < 8) {
    return 'Senha deve ter pelo menos 8 caracteres'
  }
  if (value.length > 20) {
    return 'Senha deve ter no máximo 20 caracteres'
  }
  return true
}

export const confirmPasswordValidation = (password1: string, password2: string): string | true => {
  if (!password2) {
    return 'Confirmação de senha é necessária'
  }
  if (password2 !== password1) {
    return 'As senhas não coincidem'
  }
  return true
}

export const usernameValidation = (value: string): string | true => {
  if (!value) {
    return 'Username é necessário'
  }
  if (value.length < 3) {
    return 'Username deve ter pelo menos 3 caracteres'
  }
  if (value.length > 20) {
    return 'Username deve ter no máximo 20 caracteres'
  }
  return true
}

export const nameValidation = (value: string): string | true => {
  if (!value) {
    return 'Nome completo é necessário'
  }
  return true
}

export const requiredValidation = (value: string): string | true => {
  if (!value) {
    return 'Campo obrigatório'
  }
  return true
}

export const isValidCPF = (cpf: string): string | boolean => {
  // Verificar se há caracteres não numéricos
  if (/\D/.test(cpf)) return 'CPF deve conter apenas números.'

  // Remover caracteres não numéricos (por precaução)
  cpf = cpf.replace(/\D/g, '')

  // Verificar se o CPF tem 11 dígitos
  if (cpf.length !== 11) return 'CPF deve conter 11 dígitos.'

  // Verificar se todos os dígitos são iguais
  if (/^(\d)\1+$/.test(cpf)) return 'CPF não pode conter todos os dígitos iguais.'

  // Calcular os dígitos verificadores
  let sum = 0
  let remainder

  for (let i = 1; i <= 9; i++) {
    sum += parseInt(cpf.substring(i - 1, i)) * (11 - i)
  }
  remainder = (sum * 10) % 11
  if (remainder === 10 || remainder === 11) remainder = 0
  if (remainder !== parseInt(cpf.substring(9, 10))) return 'Dígito verificador 1 inválido.'

  sum = 0
  for (let i = 1; i <= 10; i++) {
    sum += parseInt(cpf.substring(i - 1, i)) * (12 - i)
  }
  remainder = (sum * 10) % 11
  if (remainder === 10 || remainder === 11) remainder = 0
  if (remainder !== parseInt(cpf.substring(10, 11))) return 'Dígito verificador 2 inválido.'

  return true
}

export const isValidPhoneNumber = (phoneNumber: string): string | boolean => {
  // Verificar se há caracteres não numéricos
  if (/\D/.test(phoneNumber)) return 'O número de telefone deve conter apenas números.'

  // Verificar se o número tem 11 dígitos
  if (phoneNumber.length !== 11) return 'O número de telefone deve conter 11 dígitos.'

  // Verificar se o número começa com 9 (padrão para celulares no Brasil)
  if (phoneNumber[2] !== '9') return 'O número de telefone deve começar com 9 após o DDD.'

  return true
}

export function isNotEmpty(value: any): boolean {
  // Verifica se o valor é uma string e não está vazio
  return typeof value === 'string' && value.trim().length > 0
}

export const validateNumberInput = (value: string): string | null => {
  if (!/^\d+$/.test(value)) {
    return 'O campo deve conter apenas números.'
  }
  return null
}

// Função para validar o CEP
export const isValidCEP = (value: string): boolean => {
  return /^[0-9]{5}-?[0-9]{3}$/.test(value)
}
