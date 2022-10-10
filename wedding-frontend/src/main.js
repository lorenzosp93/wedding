import createApp from 'vue'
import VueAxios from 'vue-axios';
import axios from 'axios';
import gsap from "gsap";
import App from './App.vue'
<<<<<<< HEAD
import {createRouter, createWebHistory} from 'vue-router';
import VueAxios from 'vue-axios';
import axios from 'axios';
import gsap from "gsap";
import { createI18n } from 'vue-i18n';
import './index.css'

import TheLanding from './components/auth/TheLanding.vue'
import TheHome from './components/TheHome.vue'
import TheNavbar from './components/shared/TheNavbar.vue'
import TheEvents from './components/events/TheEvents.vue'
import TheInbox from './components/inbox/TheInbox.vue'
import TheInfo from './components/information/TheInfo.vue'
import TheProfile from './components/profile/TheProfile.vue'
import NotFound from './components/shared/NotFound.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {name: 'landing', path: '/landing', component: TheLanding},
        {name: 'home', path: '/', components: {default: TheHome, TheNavbar}, meta: {requiresAuth: true}},
        {name: 'events', path: '/events', components: {default: TheEvents, TheNavbar}, meta: {requiresAuth: true}},
        {name: 'inbox', path: '/inbox', components: {default: TheInbox, TheNavbar}, meta: {requiresAuth: true}},
        {name: 'info', path: '/info', components: {default: TheInfo, TheNavbar}, meta: {requiresAuth: true}},
        {name: 'profile', path: '/profile', components: {default: TheProfile, TheNavbar}, meta: {requiresAuth: true}},
        {name: 'notFound', path: '/:notFound(.*)', components: {default: NotFound, TheNavbar}},

    ]
})

// router.beforeEach((to, from, next) => {
//     if (to.matched.some(record => record.meta.requiresAuth)) {
//       // this route requires auth, check if logged in
//       // if not, redirect to login page.
//       if (!store.getters.isLoggedIn) {
//         next({ name: 'Login' })
//       } else {
//         next() // go to wherever I'm going
//       }
//     } else {
//       next() // does not require auth, make sure to always call next()!
//     }
//   })

const i18n = createI18n({
    locale:
      localStorage.getItem('lang') ||
      // Detect user's browser language
      i18n.detectLanguage(),
    fallbackLocale: 'en',
    // Load selected lang's .json file
    messages: i18n.loadLocaleMessages()
  })

const myApp = createApp(App);

myApp.use(router);
myApp.use(VueAxios, axios);
myApp.use(i18n);
=======
import createI18n from 'vue-i18n';
import router from './router.js'
// import service from './service'
// import store from './store'
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
  // .use(store)
  // .use(service)
  .use(VueAxios, axios)
  .use(i18n);
>>>>>>> ebce308 (squash commits)

myApp.config.globalProperties.$gsap = gsap;

myApp.mount('#app');
