import { defineConfig } from 'astro/config';
import auth from 'auth-astro';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [auth(), tailwind()],
  output: 'server' // ВАЖНО: для работы авторизации нужно SSR
});