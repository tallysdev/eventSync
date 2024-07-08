import { config } from '@vue/test-utils'
import { createVuetify } from 'vuetify'
import 'vuetify/styles'

const vuetify = createVuetify()


config.global.plugins = [vuetify]
