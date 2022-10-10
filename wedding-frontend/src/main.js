import createApp from 'vue'
import VueAxios from 'vue-axios';
import axios from 'axios';
import gsap from "gsap";
import App from './App.vue'
import createI18n from 'vue-i18n';
import router from './router.js'
import service from './service'
import store from './store'
import './index.css'


const i18n = createI18n({
    locale:
      localStorage.getItem('lang') ||
      // Detect user's browser language
      i18n.detectLanguage(),
    fallbackLocale: 'en',
    // Load selected lang's .json file
    messages: i18n.loadLocaleMessages()
  })


const myApp = createApp(App)
  .use(router)
  .use(store)
  .use(service)
  .use(VueAxios, axios)
  .use(i18n);

myApp.config.globalProperties.$gsap = gsap;

myApp.mount('#app');
