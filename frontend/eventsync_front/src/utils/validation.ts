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

export const isValidCPF = (cpf: string): string | boolean => {
  // Verificar se há caracteres não numéricos
  if (/\D/.test(cpf)) return 'CPF deve conter apenas números.';

  // Remover caracteres não numéricos (por precaução)
  cpf = cpf.replace(/\D/g, '');

  // Verificar se o CPF tem 11 dígitos
  if (cpf.length !== 11) return 'CPF deve conter 11 dígitos.';

  // Verificar se todos os dígitos são iguais
  if (/^(\d)\1+$/.test(cpf)) return 'CPF não pode conter todos os dígitos iguais.';

  // Calcular os dígitos verificadores
  let sum = 0;
  let remainder;

  for (let i = 1; i <= 9; i++) {
      sum += parseInt(cpf.substring(i - 1, i)) * (11 - i);
  }
  remainder = (sum * 10) % 11;
  if (remainder === 10 || remainder === 11) remainder = 0;
  if (remainder !== parseInt(cpf.substring(9, 10))) return 'Dígito verificador 1 inválido.';

  sum = 0;
  for (let i = 1; i <= 10; i++) {
      sum += parseInt(cpf.substring(i - 1, i)) * (12 - i);
  }
  remainder = (sum * 10) % 11;
  if (remainder === 10 || remainder === 11) remainder = 0;
  if (remainder !== parseInt(cpf.substring(10, 11))) return 'Dígito verificador 2 inválido.';

  return true;
}

export const isValidPhoneNumber = (phoneNumber: string): string | boolean => {
  // Verificar se há caracteres não numéricos
  if (/\D/.test(phoneNumber)) return 'O número de telefone deve conter apenas números.';

  // Verificar se o número tem 11 dígitos
  if (phoneNumber.length !== 11) return 'O número de telefone deve conter 11 dígitos.';

  // Verificar se o número começa com 9 (padrão para celulares no Brasil)
  if (phoneNumber[2] !== '9') return 'O número de telefone deve começar com 9 após o DDD.';

  return true;
}