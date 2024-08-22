import api from '@/services/api'
import { useAuthStore } from '@/stores/auth'
import { AxiosError } from 'axios'

export const fetchEvents = (
  page: number = 1,
  pageSize: number = 10,
  status?: string,
  type?: string,
  name?: string
) => {
  return api.get('events/', {
    params: { page, page_size: pageSize, status, event_type: type, name }
  })
}

export const fetchEvent = (id: number) => {
  return api.get(`events/${id}/`)
}

export const addEvent = (formData: FormData) => {
  const { token } = useAuthStore()
  return api.post('events/', formData, {
    headers: { Authorization: `Bearer ${token}` }
  })
}

export const fetchLocations = () => {
  return api.get('locals')
}

export const fetchLocal = (id: number) => {
  return api.get(`locals/${id}/`)
}

export const signupForEvent = async (eventId: number, userId: number) => {
  const { token } = useAuthStore()
  try {
    const response = await api.post(`events/registration/`, null, {
      params: { event_id: eventId, user_id: userId },
      headers: { Authorization: `Bearer ${token}` }
    })
    return response
  } catch (error) {
    const axiosError = error as AxiosError

    console.error('Error signing up for event:', axiosError.response?.data || axiosError.message)
    throw error
  }
}

export const cancelSubscription = async (eventId: number, userId: number) => {
  const { token } = useAuthStore()
  try {
    const response = await api.delete(`events/registration/${eventId}/${userId}/`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    return response
  } catch (error) {
    const axiosError = error as AxiosError

    console.error(
      'Error canceling subscription for event:',
      axiosError.response?.data || axiosError.message
    )
    throw error
  }
}

export const checkUserSubscription = async (eventId: number, userId: number) => {
  const { token } = useAuthStore()
  try {
    const response = await api.get(`events/registration/${eventId}/${userId}/`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    return response
  } catch (error) {
    const axiosError = error as AxiosError

    console.error(
      'Error checking subscription status:',
      axiosError.response?.data || axiosError.message
    )
    throw error
  }
}

export const fetchMyEvents = (
  page: number = 1,
  pageSize: number = 10,
  status?: string,
  type?: string,
  name?: string
) => {
  const { token } = useAuthStore()
  return api.get('eventsorganized/', {
    params: { page, page_size: pageSize, status, event_type: type, name },
    headers: { Authorization: `Bearer ${token}` } 
  })
}

export const fetchEventsPresence = (
  page: number = 1,
  pageSize: number = 10,
  status?: string,
  type?: string,
  name?: string
) => {
  const { token } = useAuthStore()
  return api.get('eventspresence/', {
    params: { page, page_size: pageSize, status, event_type: type, name },
    headers: { Authorization: `Bearer ${token}` } 
  })
}

export const updateEvent = (formData: FormData, eventId: number) => {
  const { token } = useAuthStore()
  return api.patch(`events/${eventId}/`, formData, {
    headers: { Authorization: `Bearer ${token}` }
  })
}

export const deleteEvent = async (eventId: number) => {
  const { token } = useAuthStore()
  try {
    const response = await api.delete(`events/${eventId}/`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    return response
  } catch (error) {
    const axiosError = error as AxiosError

    console.error(
      'Error deleting event:',
      axiosError.response?.data || axiosError.message
    )
    throw error
  }
}

export const getOrganizer = (eventid: number) => {
  const { token } = useAuthStore()
  return api.get(`organizer/${eventid}/`, {
    headers: { Authorization: `Bearer ${token}` }
  })
}