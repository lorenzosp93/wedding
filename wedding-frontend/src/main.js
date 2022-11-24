import { createPinia } from 'pinia';
import router from '@/router'
import i18n from '@/i18n'
import { createApp } from 'vue'
import VueAxios from 'vue-axios';
import axios from 'axios';
import App from './App.vue'
import Shepherd from 'shepherd.js';

import './index.css'

const pinia = createPinia()
pinia.use(({ store }) => {
  store.$router = router
});

const myApp = createApp(App)
  .use(pinia)
  .use(router)
  .use(VueAxios, axios)
  .use(i18n);

myApp.config.globalProperties.$shepherd = Shepherd;

myApp.mount('#app');
