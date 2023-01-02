import { defineStore } from "pinia";
import type { Profile, User, UserError } from "@/models/auth.interface";
import type { AxiosError, AxiosResponse } from "axios";
import i18n from "@/i18n";
import router from "@/router";
import { useNotificationStore } from "@/stores";
import { useStorage, type RemovableRef } from "@vueuse/core";

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    // initialize state from local storage to enable user to stay logged in
    token: useStorage("token", "") as RemovableRef<string | undefined>,
    profile: useStorage("profile", { id: 0 } as Profile) as RemovableRef<
      Profile | undefined
    >,
    loading: false as boolean,
    error: undefined as AxiosError | undefined,
    registerError: undefined as UserError | undefined,
    success: false as boolean,
  }),
  actions: {
    async setupPlusOne(plusOne: User) {
      this.loading = true;
      let service = await import("@/services/api.service");
      return service.apiService.setupPlusOne(plusOne).then(
        (_: AxiosResponse<string>) => {
          this.error = undefined;
          this.loading = false;
          this.success = true;
          this.getProfile();
        },
        (error: AxiosError<UserError>) => {
          this.loading = false;
          this.registerError = error?.response?.data;
          return Promise.reject(error);
        }
      );
    },
    async getProfile() {
      this.loading = true;
      let service = await import("@/services/api.service");
      return service.apiService
        .getUserProfile()
        .then((response: AxiosResponse<Profile[]>) => {
          this.loading = false;
          let profile = response.data.find((d: Profile) => d);
          if (profile) {
            this.profile = profile;
            if (profile?.language) {
              i18n.global.locale.value = profile.language;
              localStorage.setItem("lang", profile.language);
            }
          }
        })
        .catch((error: AxiosError) => {
          this.loading = false;
          console.log(error);
          this.error = error;
        });
    },
    async login(token: string) {
      this.token = token;
      await this.getProfile().then(() => {
        const notificationStore = useNotificationStore();
        notificationStore.checkIsSubscribed();
      });
    },
    logout() {
      this.token = undefined;
      this.profile = undefined;
      localStorage.clear();
      router.push({ name: "login" });
    },
    async register(user: User) {
      this.loading = true;
      let service = await import("@/services/api.service");
      return service.apiServicePublic
        .registerUser(user)
        .then((response: AxiosResponse<string>) => {
          this.success = true;
          this.loading = false;
          router.push({
            name: "login",
            query: {
              email: user.email,
              message: response.data,
            },
          });
        })
        .catch((error: AxiosError<UserError>) => {
          this.loading = false;
          this.registerError = error?.response?.data;
        });
    },
  },
});
