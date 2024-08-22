import api from '@/services/api'
import { type Local } from '@/types/local'
import { useAuthStore } from '@/stores/auth'

export const fetchLocations = (page: number, pageSize: number) => {
  return api.get('locals/', {
    params: { page, page_size: pageSize }
  })
}

export const addLocal = (formData: FormData) => {
  const { token } = useAuthStore()
  return api.post('locals/', formData, {
    headers: { Authorization: `Bearer ${token}` }
  })
}

export const fetchLocal = () => {
  return api.get('locals')
}

export const updateLocal = async (local: Local) => {
  const { token } = useAuthStore()
  return api.put(`locals/${local.id}/`, local, {
    headers: { Authorization: `Bearer ${token}` }
  })
}

export const deleteLocal = async (id: number) => {
  const { token } = useAuthStore()
  return api.delete(`locals/${id}/`, {
    headers: { Authorization: `Bearer ${token}` }
  })
}
