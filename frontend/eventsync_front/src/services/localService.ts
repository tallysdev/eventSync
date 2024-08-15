import api from '@/services/api'

export const fetchLocations = (page: number, pageSize: number) => {
  return api.get('locals/', {
    params: { page, page_size: pageSize }
  })
}

export const addLocal = (formData: FormData) => {
  return api.post('locals/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })
}

export const fetchLocal = () => {
  return api.get('locals');
}