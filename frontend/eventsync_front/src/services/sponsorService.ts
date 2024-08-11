// services/sponsorService.ts
import api from '@/services/api'

export const fetchSponsors = (page: number, pageSize: number) => {
  return api.get('sponsors/', {
    params: { page, page_size: pageSize }
  })
}

export const addSponsor = (formData: FormData) => {
  // TODO: add authentication
  return api.post('sponsors/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })
}
