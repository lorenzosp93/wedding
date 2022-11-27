import { defineStore } from 'pinia';
import { API_URL, request } from '@/services/api.service'
import i18n from '@/i18n';

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        token: localStorage.getItem('token'),
        profile: JSON.parse(localStorage.getItem('profile')),
        loading: false,
        error: null,
    }),
    actions: {
        async login(token) {
            // update pinia state
            this.token = token;
            this.loading = true;
            await request().get(API_URL + '/api/user/profile/').then((response) => {
                let profile = response.data.find(d => d);
                this.profile = profile;
                this.loading = false;
                localStorage.setItem('profile', JSON.stringify(profile));
                // store user details and jwt in local storage to keep user logged in between page refreshes
                localStorage.setItem('token', token);
                if (this.profile?.language){
                    i18n.global.locale.value = this.profile.language;
                    localStorage.setItem('lang', this.profile.language);
                }
            }).catch(
                error => {
                    this.loading = false;
                    console.log(error);
                    this.error = error;
                }
            )
        },
        logout() {
            this.token = null;
            this.profile = null;
            localStorage.clear();
            this.$router.push('/login')
        },
    }
});