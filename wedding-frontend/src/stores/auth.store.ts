import { defineStore } from 'pinia';
import apiService from '@/services/api.service'
import type { Profile, User, UserError } from '@/models/auth.interface';
import type { AxiosError, AxiosResponse } from 'axios';
import i18n from '@/i18n';
import router from '@/router';
import { useNotificationStore } from '@/stores/notification.store'


export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        token: localStorage.getItem('token') as string,
        profile: JSON.parse(localStorage.getItem('profile') ?? "null") ?? undefined as Profile | undefined,
        loading: false as boolean,
        error: undefined as AxiosError | undefined,
        registerError: undefined as UserError | undefined,
    }),
    actions: {
        async login(token: string) {
            // update pinia state
            this.token = token;
            this.loading = true;
            apiService.getUserProfile().then((response: AxiosResponse<Profile[]>) => {
                let profile = response.data.find((d: Profile) => d);
                this.profile = profile;
                this.loading = false;
                localStorage.setItem('profile', JSON.stringify(profile));
                // store user details and jwt in local storage to keep user logged in between page refreshes
                localStorage.setItem('token', token);
                if (profile?.language) {
                    i18n.global.locale.value = profile.language;
                    localStorage.setItem('lang', profile.language);
                }
                const notificationStore = useNotificationStore();
                notificationStore.checkIsSubscribed();
            }).catch(
                (error: AxiosError) => {
                    this.loading = false;
                    console.log(error);
                    this.error = error;
                }
            )
        },
        logout () {
            this.token = '';
            this.profile = undefined;
            localStorage.clear();
            router.push({name: 'login'});
        },
        register (user: User) {
            this.loading = true;
            apiService.registerUser(user).then((response: AxiosResponse<string>) => {
                this.loading = false;
                router.push({name: 'login', query: {
                    email: user.email,
                    message: response.data,
                }});
            }).catch((error: AxiosError<UserError> ) => {
                this.loading = false;
                console.log(error);
                this.registerError = error?.response?.data;
            })
        }
    }
});