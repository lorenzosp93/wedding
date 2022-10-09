import {createApp} from 'vue'
import App from './App.vue'
import './index.css'
import {gsap} from "gsap";
import {createRouter, createWebHistory} from 'vue-router';

import LandingPage from './components/LandingPage.vue'
import TheHome from './components/TheHome.vue'
import TheEvents from './components/events/TheEvents.vue'
import TheInbox from './components/inbox/TheInbox.vue'
import TheInfo from './components/information/TheInfo.vue'
import TheProfile from './components/profile/TheProfile.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/landing', component: LandingPage},
        {path: '/', component: TheHome},
        {path: '/events', component: TheEvents},
        {path: '/inbox', component: TheInbox},
        {path: '/info', component: TheInfo},
        {path: '/profile', component: TheProfile},
    ]
})

const myApp = createApp(App);

myApp.use(router);

myApp.config.globalProperties.$gsap = gsap;

myApp.mount('#app');

