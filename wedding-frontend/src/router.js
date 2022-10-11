import { createRouter, createWebHistory } from 'vue-router';

import TheLanding from './components/auth/TheLanding.vue'
import LoginPage from './components/auth/LoginPage.vue'
// Lazy load
const LoginSuccess = () => import('./components/auth/LoginSuccess.vue')
const TheHome = () => import('./components/TheHome.vue')
const TheNavbar = () => import('./components/shared/TheNavbar.vue')
const TheInbox = () => import('./components/inbox/TheInbox.vue')
const TheInfo = () => import('./components/information/TheInfo.vue')
const TheGallery = () => import('./components/gallery/TheGallery.vue')
const TheProfile = () => import('./components/profile/TheProfile.vue')
const NotFound = () => import('./components/shared/NotFound.vue')

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {name: 'landing', path: '/landing', component: TheLanding},
        {name: 'login', path: '/login', component: LoginPage},
        {name: 'login-success', path: '/login/success', component: LoginSuccess},
        {name: 'home', path: '/', components: {default: TheHome, TheNavbar}, },
        {name: 'inbox', path: '/inbox', components: {default: TheInbox, TheNavbar}, },
        {name: 'info', path: '/info', components: {default: TheInfo, TheNavbar}, },
        {name: 'gallery', path: '/gallery', components: {default: TheGallery, TheNavbar}, },
        {name: 'profile', path: '/profile', components: {default: TheProfile, TheNavbar}, },
        {name: 'notFound', path: '/:notFound(.*)', components: {default: NotFound, TheNavbar}},

    ]
})

router.beforeEach((to, _, next) => {
    const publicPages = ['/landing', '/login', '/login/success'];
    const authRequired = !publicPages.includes(to.path);
    const token = to?.query["token"];
    if (token){
      localStorage.setItem('token', token)
    }
    
    const loggedIn = !!localStorage.getItem('token');
    // trying to access a restricted page + not logged in
    // redirect to login page
    if (authRequired && !loggedIn) {
      next('/login');
    } else {
      next();
    }
  });

export default router; 
