import {createRouter, createWebHistory} from 'vue-router';

import TheLanding from './components/auth/TheLanding.vue'
import LoginPage from './components/auth/LoginPage.vue'
import LoginSuccess from './components/auth/LoginSuccess.vue'
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
        {name: 'login', path: '/login', component: LoginPage},
        {name: 'login-success', path: '/login/success', component: LoginSuccess},
        {name: 'home', path: '/', components: {default: TheHome, TheNavbar}, meta: {requiresAuth: true}},
        {name: 'events', path: '/events', components: {default: TheEvents, TheNavbar}, meta: {requiresAuth: true}},
        {name: 'inbox', path: '/inbox', components: {default: TheInbox, TheNavbar}, meta: {requiresAuth: true}},
        {name: 'info', path: '/info', components: {default: TheInfo, TheNavbar}, meta: {requiresAuth: true}},
        {name: 'profile', path: '/profile', components: {default: TheProfile, TheNavbar}, meta: {requiresAuth: true}},
        {name: 'notFound', path: '/:notFound(.*)', components: {default: NotFound, TheNavbar}},

    ]
})

export default router ;