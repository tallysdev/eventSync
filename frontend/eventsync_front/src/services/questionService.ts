import api from '@/services/api'

export const addQuestions = (formData: FormData) => {
  return api.post('questions/', formData, {
    headers: { 'Content-Type': 'multipart/question-data' }
  })
}
