import api from '@/services/api'

export const fetchEvents = (page: number, pageSize: number) => {
  return api.get('events/', {
    params: { page, page_size: pageSize }
  })
}

export const addEvent = (formData: FormData) => {
  return api.post('events/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })
}

export const fetchLocations = () => {
  return api.get('http://127.0.0.1:8000/eventsync/api/v1/locals');
}