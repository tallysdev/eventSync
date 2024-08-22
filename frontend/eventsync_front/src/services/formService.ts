import api from '@/services/api'

export const addForm = (formData: FormData) => {
  return api.post('forms/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })
}
