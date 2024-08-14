export interface ThemeRoom {
    id?: number
    event?: number,
    star_time: string,
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
    audiences: string
}

// audiences = models.TextField()
// event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default='conference')