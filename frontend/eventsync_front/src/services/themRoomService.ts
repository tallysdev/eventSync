import api from '@/services/api'
import { useAuthStore } from '@/stores/auth'

export const fetchThemeRooms = (eventId: number) => {
    return api.get('themeRoom/', {
        params: { event_id: eventId }
    })
}

export const fetchThemeRoom = (id: number) => {
    return api.get(`themeRoom/${id}/`)
}

export const addThemeRoom = (formData: FormData) => {
    const { token } = useAuthStore()
    return api.post('themeRoom/', formData, {
        headers: { Authorization: `Bearer ${token}` }
    })
}

export const updateThemeRoom = (id: number, formData: FormData) => {
    const { token } = useAuthStore()
    return api.patch(`themeRoom/${id}/`, formData, {
        headers: { Authorization: `Bearer ${token}` }
    })
}

export const deleteThemeRoom = (id: number) => {
    const { token } = useAuthStore()
    return api.delete(`themeRoom/${id}/`, {
        headers: { Authorization: `Bearer ${token}` }
    })
}
