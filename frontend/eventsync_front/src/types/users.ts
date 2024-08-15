export interface User {
    email: string
    password: string
}
  
export interface AuthState {
    user: User | null
    token: string | null
    rtoken: string | null
    profile: Profile | null
}

export interface Profile {
    id: number
    name: string
    is_staff: boolean
    birth_date: string
    is_active: boolean
    date_joined: string
    cpf: string
    phone: String
    email: string
}
