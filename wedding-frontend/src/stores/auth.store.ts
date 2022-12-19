import { defineStore } from 'pinia';
import { API_URL, request } from '@/services/api.service'
import i18n from '@/i18n';
import type { Profile } from '@/models/auth.interface';
import type { AxiosError, AxiosResponse } from 'axios';
import router from '@/router';

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        token: localStorage.getItem('token') as string,
        profile: JSON.parse(localStorage.getItem('profile') ?? 'null') as Profile | undefined,
        loading: false as boolean,
        error: undefined as AxiosError | undefined,
    }),
    actions: {
        async login(token: string) {
            // update pinia state
            this.token = token;
            this.loading = true;
            await request().get(API_URL + '/api/user/profile/').then((response: AxiosResponse<Profile[]>) => {
                let profile = response.data.find((d: Profile) => d);
                this.profile = profile;
                this.loading = false;
                localStorage.setItem('profile', JSON.stringify(profile));
                // store user details and jwt in local storage to keep user logged in between page refreshes
                localStorage.setItem('token', token);
                if (this.profile?.language) {
                    i18n.global.locale.value = this.profile.language;
                    localStorage.setItem('lang', this.profile.language);
                }
            }).catch(
                (error: AxiosError) => {
                    this.loading = false;
                    console.log(error);
                    this.error = error;
                }
            )
        },
        logout() {
            this.token = '';
            this.profile = undefined;
            localStorage.clear();
            router.push('/login')
        },
    }
});