import type { FormValuesEvent } from '@/types/event'
import { ref } from 'vue'


// Snackbar states
export const snackbar = ref(false)
export const snackbarText = ref('')
export const snackbarColor = ref('')

const showSnackbar = (message: string, type: string) => {
  snackbarText.value = message
  snackbarColor.value = type === 'success' ? 'green' : 'red'
  snackbar.value = true
}

export const validateFields = (formValues: FormValuesEvent): boolean => {
  const { name, start_date, end_date, local, min_quantity, max_quantity, hours_quantity, event_type, description, status } = formValues

  const fields = [
    { value: name, message: 'Nome do Evento é obrigatório' },
    { value: start_date, message: 'Data de Início do Evento é obrigatória' },
    { value: end_date, message: 'Data de Fim do Evento é obrigatória' },
    { value: local, message: 'Local do Evento é obrigatório' },
    { value: min_quantity && min_quantity > 0, message: 'Quantidade Mínima de Participantes é obrigatória e deve ser maior que 0' },
    { value: max_quantity && max_quantity > 0, message: 'Quantidade Máxima de Participantes é obrigatória e deve ser maior que 0' },
    { value: hours_quantity && hours_quantity > 0, message: 'Quantidade de Horas é obrigatória e deve ser maior que 0' },
    { value: event_type, message: 'Tipo do Evento é obrigatório' },
    { value: description, message: 'Descrição do Evento é obrigatória' },
  ]

  for (const field of fields) {
    if (!field.value) {
      showSnackbar(field.message, 'error')
      return false
    }
  }
  return true
}

export const validateNumberInput = (event: KeyboardEvent) => {
  const key = event.key
  if (!/[0-9]/.test(key)) {
    event.preventDefault()
  }
}
