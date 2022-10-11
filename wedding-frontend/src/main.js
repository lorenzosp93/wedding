import { createApp } from 'vue'
import { VueAxios } from 'vue-axios';
import { axios } from 'axios';
import { gsap } from "gsap";
import i18n from './i18n'
import router from './router'
import App from './App.vue'
import './index.css'

const myApp = createApp(App)
  .use(router)
  .use(VueAxios, axios)
  .use(i18n);

myApp.config.globalProperties.$gsap = gsap;

myApp.mount('#app');
