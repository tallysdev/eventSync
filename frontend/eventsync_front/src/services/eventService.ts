import api from '@/services/api'
import { useAuthStore } from '@/stores/auth'

export const fetchEvents = (page: number, pageSize: number) => {
  return api.get('events/', {
    params: { page, page_size: pageSize }
  })
}

export const addEvent = (formData: FormData) => {
  const { token } = useAuthStore()
  return api.post('events/', formData, {
    headers: { Authorization: `Bearer ${token}` }
  })
}

export const fetchLocations = () => {
  return api.get('locals/');
  
}