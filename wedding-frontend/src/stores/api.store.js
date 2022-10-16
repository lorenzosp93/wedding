import { defineStore } from 'pinia';

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        messages: localStorage.getItem('messages'),
        infos: localStorage.getItem('infos'),
        gallery: localStorage.getItem('gallery'),
    }),
    actions: {
    }
});