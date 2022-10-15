import { defineStore } from 'pinia';
import { API_URL, request } from '@/services/api.service'

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        token: localStorage.getItem('token'),
        profile: null,
    }),
    actions: {
        async login(token) {
            // update pinia state
            this.token = token;
            request().get(API_URL + '/api/user/profile/').then((response) => {
                this.profile = response.data[0];
            })

            // store user details and jwt in local storage to keep user logged in between page refreshes
            localStorage.setItem('token', token);
        },
        logout() {
            this.token = null;
            localStorage.removeItem('token');
            this.$router.push('/login')
        }
    }
});