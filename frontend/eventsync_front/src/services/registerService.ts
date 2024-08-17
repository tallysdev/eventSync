import api from '@/services/api'
import { type RegisterUser } from '@/types/users'

export const registerUserInDB = (user: RegisterUser) => {
  return api.post('register/', user)
}
