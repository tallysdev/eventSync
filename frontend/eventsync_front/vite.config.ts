import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          // Split large libraries into separate chunks
          vue: ['vue'],
          vuetify: ['vuetify'],  // If using Vuetify
          axios: ['axios'],       // If axios is heavily used
          // Additional libraries or components can be split here
        },
      },
    },
    chunkSizeWarningLimit: 500,  // Adjust this value based on your needs
  },
});
