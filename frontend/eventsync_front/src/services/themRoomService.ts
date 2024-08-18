import api from '@/services/api'

export const fetchThemeRooms = (eventId: number) => {
    return api.get('themeRoom/', {
        params: { event_id: eventId }
    })

}

export const fetchThemeRoom = (id: number) => {
    return api.get(`themeRoom/${id}/`)
}

export const addThemeRoom = (formData: FormData) => {
    return api.post('themeRoom/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
    })
}

export const updateThemeRoom = (id: number, formData: FormData) => {
    return api.patch(`themeRoom/${id}/`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
    })
}

export const deleteThemeRoom = (id: number) => {
    return api.delete(`themeRoom/${id}/`)
}
