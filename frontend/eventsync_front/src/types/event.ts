export interface FormValuesEvent {
  name: string
  start_date: string
  end_date: string
  local: string
  min_quantity: number
  max_quantity: number
  hours_quantity: number
  event_type: string
  description: string
  status: string
}

export interface Event {
  id?: number
  name: string
  start_date: string
  end_date: string
  max_quantity: number
  min_quantity: number
  hours_quantity: number
  description: string
  status: 'upcoming' | 'ongoing' | 'completed'
  event_type: string
  local: number
}
