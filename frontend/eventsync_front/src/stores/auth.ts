import { defineStore } from 'pinia'
import api from '@/services/api'
import { jwtDecode, type JwtPayload } from 'jwt-decode'
import {type User, type AuthState, type Profile} from '../types/users'


export const useAuthStore = defineStore({
  persist: true,
  id: 'auth',
  state: (): AuthState => ({
    user: null,
    token: null,
    profile: null,
    rtoken: null,
  }),

  getters: {
    getUser: (state): Profile | null => state.profile,
    isAuthenticated: (state): boolean => !!state.token,
    hasAdminPerm: (state): boolean => !!state.profile?.is_staff,
    hasProfile: (state): boolean => !!state.profile,
  },
  actions: {
    async login(user: User) {
      try {
        const resp = await api.post('login/', {
          email: user.email,
          password: user.password
        })
        if (resp.status === 200) {
          const access_token = resp.data.access
          const refresh_token = resp.data.refresh
          this.setToken(access_token)
          this.setRefreshToken(refresh_token)
          localStorage.setItem('token', access_token)
          localStorage.setItem('refresh_token', refresh_token)
          localStorage.setItem('email', user.email)
          await this.setProfile(resp.data.access)
        }
      } catch (err) {
        alert(err)
      }
    },
    logout() {
      this.clearTokens()
      this.clearProfile()
      localStorage.removeItem('token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('email')
      localStorage.removeItem('profile')
    },
    checkAuth() {
      const token = localStorage.getItem('token')
      if (token && token !== this.token) {
        this.setToken(token)
      }
      if (!isSignedIn()) {
        this.logout()
      }
    },
    async setProfile(token: string) {
      type customJwtPayload = JwtPayload & { user_id: number }
      const payload = jwtDecode<customJwtPayload>(token)
      const userID: number = payload.user_id
      try {
        const resp = await api.get(`users/${userID}/`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        if (resp.status === 200) {
          const profile = resp.data
          this.profile = profile
          localStorage.setItem('profile', JSON.stringify(profile))
        }
      } catch (err) {
        console.error('Erro ao obter perfil do usuário:', err)
      }
    },

    setToken(token: string) {
      this.token = token
    },

    setRefreshToken(token: string) {
      this.rtoken = token
    },
    clearTokens() {
      this.token = null
      this.rtoken = null
    },
    clearProfile() {
      this.profile = null
    }
  }
})

function isSignedIn() {
  const token = localStorage.getItem('token')

  if (!token)
    // Se não existe o token no LocalStorage
    return false // significa que o usuário não está assinado.

  try {
    const { exp: expiration } = jwtDecode<{ exp: number }>(token)
    const isExpired = !!expiration && Date.now() > expiration * 1000

    if (isExpired)
      // Se o token tem uma data de expiração e
      return false // essa data é menor que a atual o usuário
    // não está mais assinado.
    return true
  } catch (_) {
    // O "jwt-decode" lança erros pra tokens inválidos.
    return false // Com um token inválido o usuário não está assinado.
  }
}
