/* eslint-disable no-undef */
import { defineConfig } from 'vite'
import { resolve, dirname } from 'node:path'
import { fileURLToPath } from 'url'
import vue from '@vitejs/plugin-vue'
import vueI18n from '@intlify/vite-plugin-vue-i18n'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        vueI18n({
            include: resolve(dirname(fileURLToPath(import.meta.url)), './src/i18n/locales/**'),
        })
    ],
    resolve: {
        alias: {
            "@": fileURLToPath(new URL('./src', import.meta.url)),
        },
    },
    server: {
        port: 8080,
    }
  })
