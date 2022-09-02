import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import { gsap } from "gsap";

const myApp = createApp(App);

myApp.config.globalProperties.$gsap = gsap;

myApp.mount('#app');
