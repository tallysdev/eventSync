export const formatDate = (date: string) => {
  return new Date(date).toLocaleDateString(undefined, {
    weekday: 'long',
    hour: '2-digit',
    minute: '2-digit'
  })
}
