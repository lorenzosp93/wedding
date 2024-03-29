import { defineConfig } from "vite";
import { resolve } from "node:path";
import path from "path";
import vue from "@vitejs/plugin-vue";
import viteCompression from "vite-plugin-compression";
import { VitePWA } from "vite-plugin-pwa";
import VueI18nPlugin from "@intlify/unplugin-vue-i18n/vite";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({
      isProduction: process.env.DEV === "false",
    }),
    viteCompression({
      filter: /\.(js|mjs|json|css|html|svg|webp|ttf|png|ico|txt)$/i,
    }),
    VueI18nPlugin({
      include: resolve(__dirname, "./src/i18n/locales/**"),
      strictMessage: false,
    }),
    VitePWA({
      strategies: "generateSW",
      registerType: "autoUpdate",
      workbox: {
        importScripts: ["/push-sw.js"],
        navigateFallbackDenylist: [/\/api\//],
        runtimeCaching: [
          {
            urlPattern: ({ url }) => {
              return url.pathname.startsWith("/api");
            },
            handler: "NetworkFirst" as const,
            method: "GET",
            options: {
              cacheName: "api-cache",
              cacheableResponse: {
                statuses: [0, 200],
              },
            },
          },
        ],
      },
      devOptions: {
        enabled: false,
      },
      includeAssets: [
        "favicon.ico",
        "favicon-16x16.ico",
        "favicon-32x32.ico",
        "apple-touch-icon.png",
      ],
      manifest: {
        name: "Priscilla & Lorenzo - wedding app",
        short_name: "PriscillaLorenzo",
        description:
          "The web application to keep track of Priscilla and Lorenzo's wedding",
        theme_color: "#D5B19B",
        icons: [
          {
            src: "pwa-192x192.png",
            sizes: "192x192",
            type: "image/png",
          },
          {
            src: "pwa-512x512.png",
            sizes: "512x512",
            type: "image/png",
            purpose: "any maskable",
          },
        ],
      },
    }),
  ],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    port: 8080,
  },
  build: {
    sourcemap: true,
  },
});
