import { defineStore } from 'pinia';
import { API_URL, request } from '@/services/api.service'

const i18n = () => import('@/i18n')

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        token: localStorage.getItem('token'),
        profile: JSON.parse(localStorage.getItem('profile')),
        languages: JSON.parse(localStorage.getItem('languages')),
        loading: false,
        error: null,
    }),
    actions: {
        async login(token) {
            // update pinia state
            this.token = token;
            this.loading = true;
            request().get(API_URL + '/api/user/profile/').then((response) => {
                let profile = response.data.find(d => d);
                this.profile = profile;
                this.loading = false;
                localStorage.setItem('profile', JSON.stringify(profile));
                if (this.profile?.language){
                    i18n().then(
                        i18n => i18n.default.global.locale = this.profile?.language
                    ).finally(
                    localStorage.setItem('lang', this.profile?.language)
                    );
                }
            }).catch(
                error => {
                    console.log(error);
                    this.error = error;
                }
            )
            // store user details and jwt in local storage to keep user logged in between page refreshes
            localStorage.setItem('token', token);
        },
        logout() {
            this.token = null;
            localStorage.clear();
            this.$router.push('/login')
        },
        async getLanguages() {
            request().get(API_URL + '/api/shared/get-languages/').then(
                response => {
                    this.languages = response.data;
                    localStorage.setItem('languages', JSON.stringify(this.languages));
                }
            ).catch(error => console.log(error))
        },
        async updateLanguage() {
            this.loading = true;
            request(true).put(
                `${API_URL}/api/user/profile/${this.profile.id}/`,
                {
                    'language': this.profile.language
                }
            ).then(
                () => {
                    this.loading = false;
                    localStorage.setItem('profile', JSON.stringify(this.profile));
                    i18n().then(
                        i18n => {
                            i18n.default.global.locale = this.profile.language;
                        }
                    ).finally(
                        localStorage.setItem('lang', this.profile.language)
                    );
                }
            ).catch(
                error => {
                    console.log(error);
                    this.error = error;
                }
            )
        }
    }
});