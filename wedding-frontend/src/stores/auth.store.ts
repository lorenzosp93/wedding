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
        success: false as boolean,
    }),
    actions: {
        setupPlusOne(plusOne: User) {
            this.loading = true;
            return apiService.setupPlusOne(plusOne).then(
                (response:AxiosResponse<string>) => {
                    this.error = undefined;
                    this.loading = false;
                    this.success = true;
                    this.getProfile();
                    return response
                },
                (error: AxiosError<UserError>) => {
                    this.loading = false;
                    this.registerError = error?.response?.data;
                    throw error
                }
            );
        },
        async getProfile () {
            this.loading = true;
            return apiService.getUserProfile().then((response: AxiosResponse<Profile[]>) => {
                let profile = response.data.find((d: Profile) => d);
                this.profile = profile;
                this.loading = false;

                localStorage.setItem('profile', JSON.stringify(profile));

                if (profile?.language) {
                    i18n.global.locale.value = profile.language;
                    localStorage.setItem('lang', profile.language);
                }
            }).catch(
                (error: AxiosError) => {
                    this.loading = false;
                    console.log(error);
                    this.error = error;
                }
            )
        },
        async login(token: string) {
            this.token = token;
            await this.getProfile().then(_ => {
                localStorage.setItem('token', token);
                const notificationStore = useNotificationStore();
                notificationStore.checkIsSubscribed();
            });
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
                this.success = true;
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