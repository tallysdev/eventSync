import { fileURLToPath, URL } from 'node:url'
import { defineConfig, configDefaults } from 'vitest/config'
import viteConfig from './vite.config'

export default defineConfig({
  ...viteConfig,
  test: {
    deps: {
      moduleDirectories: ['node_modules', 'src']
    },
    environment: 'jsdom',
    setupFiles: ['./src/tests/setupTests.ts'],
    exclude: [...configDefaults.exclude, 'e2e/*'],
    root: fileURLToPath(new URL('./', import.meta.url))
  }
})
