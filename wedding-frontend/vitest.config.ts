import { mergeConfig } from 'vite';
import { defineConfig } from 'vitest/config';
import viteConfig from './vite.config';

export default defineConfig(
    mergeConfig(viteConfig, { // extending app vite config
        test: {
            globals: true,
            environment: 'jsdom',
      },
      root: ".",
    })
);
