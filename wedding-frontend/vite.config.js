/* eslint-disable no-undef */
import { defineConfig } from 'vite'
import { resolve, dirname } from 'node:path'
import { fileURLToPath } from 'url'
import vue from '@vitejs/plugin-vue'
import vueI18n from '@intlify/vite-plugin-vue-i18n'
import viteCompression from 'vite-plugin-compression'
import { VitePWA } from 'vite-plugin-pwa'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueI18n({
      include: resolve(dirname(fileURLToPath(import.meta.url)), './src/i18n/locales/**'),
    }),
    viteCompression(),
    VitePWA({
      registerType: 'autoUpdate',
      workbox: {
        navigateFallbackDenylist: [/\/api\//],
      },
      devOptions: {
        enabled: process.env.ENV === 'true',
      },
      includeAssets: [
          'favicon.ico',
          'favicon-16x16.ico',
          'favicon-32x32.ico',
          'apple-touch-icon.png',
      ],
      manifest: {
        name: 'Priscilla & Lorenzo - wedding app',
        short_name: 'PriscillaLorenzo',
        description: "The web application to keep track of Priscilla and Lorenzo's wedding",
        theme_color: '#D5B19B',
        icons: [
          {
            src: 'pwa-192x192.png',
            sizes: '192x192',
            type: 'image/png',
          },
          {
            src: 'pwa-512x512.png',
            sizes: '512x512',
            type: 'image/png',
            purpose: 'any maskable'
          }
        ]
      },
    })
  ],
  resolve: {
      alias: {
          "@": fileURLToPath(new URL('./src', import.meta.url)),
      },
  },
  server: {
      port: 8080,
  },
  build: {
    sourcemap: true,
  }
})
