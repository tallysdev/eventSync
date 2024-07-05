import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import { fa } from 'vuetify/iconsets/fa'
import '@mdi/font/css/materialdesignicons.css'
import '@fortawesome/fontawesome-free/css/all.css'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import { myTheme } from './plugins/vuetify/MyTheme'

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    sets: {
      fa
    }
  },
  theme: {
    defaultTheme: 'myTheme',
    themes: {
      myTheme
    }
  }
})

const app = createApp(App)
app.use(vuetify)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
// Use the plugin
app.use(pinia)
app.use(router)

app.mount('#app')
