
// Lista de siglas de estados válidos
// Adiciona um mapeamento de estados para CEPs padrões
export const defaultCEPs = {
  'AC': '69900-000',
  'AL': '57000-000',
  'AP': '68900-000',
  'AM': '69000-000',
  'BA': '40000-000',
  'CE': '60000-000',
  'DF': '70000-000',
  'ES': '29000-000',
  'GO': '74000-000',
  'MA': '65000-000',
  'MT': '78000-000',
  'MS': '79000-000',
  'MG': '30000-000',
  'PA': '66000-000',
  'PB': '58000-000',
  'PR': '80000-000',
  'PE': '50000-000',
  'PI': '64000-000',
  'RJ': '20000-000',
  'RN': '59000-000',
  'RS': '90000-000',
  'RO': '76800-000',
  'RR': '69300-000',
  'SC': '88000-000',
  'SP': '01000-000',
  'SE': '49000-000',
  'TO': '77000-000'
};

export const emailValidation = (value: string): string | true => {
  if (!value) {
    return 'Email é necessário';
  }
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(value)) {
    return 'Por favor, insira um email válido';
  }
  return true;
};

export const passwordValidation = (value: string): string | true => {
  if (!value) {
    return 'Senha é necessária';
  }
  if (value.length < 8) {
    return 'Senha deve ter pelo menos 8 caracteres';
  }
  if (value.length > 20) {
    return 'Senha deve ter no máximo 20 caracteres';
  }
  return true;
};

export const confirmPasswordValidation = (password: string) => (value: string): string | true => {
  if (!value) {
    return 'Confirmação de senha é necessária';
  }
  if (value !== password) {
    return 'As senhas não coincidem';
  }
  return true;
};

export const usernameValidation = (value: string): string | true => {
  if (!value) {
    return 'Username é necessário';
  }
  if (value.length < 3) {
    return 'Username deve ter pelo menos 3 caracteres';
  }
  if (value.length > 20) {
    return 'Username deve ter no máximo 20 caracteres';
  }
  return true;
};

export const nameValidation = (value: string): string | true => {
  if (!value) {
    return 'Nome completo é necessário';
  }
  return true;
};

export const requiredValidation = (value: string): string | true => {
  if (!value) {
    return 'Campo obrigatório';
  }
  return true;
}

// Função para validar se uma string não é vazia
export const isNotEmpty = (value: string): boolean => {
  return value.trim().length > 0;
};

// Função para validar se o número da rua é um número
export const isValidStreetNumber = (value: string): boolean => {
  return /^\d+$/.test(value);
};


// Função para validar o CEP
export const isValidCEP = (value: string): boolean => {
  return /^[0-9]{5}-?[0-9]{3}$/.test(value);
};


