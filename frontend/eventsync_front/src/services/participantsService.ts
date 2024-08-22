import api from '@/services/api'
import { useAuthStore } from '@/stores/auth'
import { AxiosError } from 'axios'

export const fetchParticipants = async (eventId: number) => {
  try {
    const response = await api.get(`participants/${eventId}/`)
    return response
  } catch (error) {
    const axiosError = error as AxiosError
    console.error('Error fetching participants:', axiosError.response?.data || axiosError.message)
    throw error
  }
}
