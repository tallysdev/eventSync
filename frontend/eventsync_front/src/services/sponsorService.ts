import api from '@/services/api'
import { useAuthStore } from '@/stores/auth'


export const fetchSponsors = (page: number, pageSize: number) => {
  return api.get('sponsors/', {
    params: { page, page_size: pageSize }
  })
}

export const addSponsor = (formData: FormData) => {
  // TODO: add authentication
  const { token } = useAuthStore()
  return api.post('sponsors/', formData, {
    headers: { 'Content-Type': 'multipart/form-data', Authorization: `Bearer ${token}` }
  })
}
