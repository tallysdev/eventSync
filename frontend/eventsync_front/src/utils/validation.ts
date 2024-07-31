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