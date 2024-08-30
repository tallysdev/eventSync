export interface ThemeRoom {
    id?: number
    event?: number,
    start_time: string,
    name: string,
    speaker: string,
    start_date: string,
    end_date: string,
    max_quantity: number,
    min_quantity: number,
    hours_quantity: number,
    description: string
    local: number,
    status: string,
    event_type: string,
    audiences: string,
}