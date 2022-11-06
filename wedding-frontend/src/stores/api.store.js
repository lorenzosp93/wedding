import apiService from '@/services/api.service';
import { defineStore } from 'pinia';
const INFOS_LIFETIME = 30 // minutes

export const useInfoStore = defineStore({
    id: 'info',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        infos: null,
        loading: false,
        error: null,
        infosExpiry: null,
        activeInfo: null,
        activeType: null,
    }),
    actions: {
        async getInfo () {
            if (!this.infos || this.infosExpiry < Date.now()) {
                this.loading = true;
                apiService.getInfoContent().then(
                    (response) => {
                        this.infos = response.data;
                        this.loading = false;
                        let now = new Date()
                        this.infosExpiry = now.setTime(
                            now.getTime + INFOS_LIFETIME * 60 * 60 * 1000
                        );
                    }
                ).catch(
                    error => {
                        console.log(error);
                        this.error = error;
                    }
                ).then(
                    () => {
                        if (this.infos) {
                            this.activeInfo = this.infos.find(info => info);
                            this.activeType = this.activeInfo?.type;
                        }
                    }
                );
            }
        },
        activateType (type) {
            this.activeType = type;
            this.activeInfo = this.infos.find(info => info.type == this.activeType);
        }
    },
});