import apiService from '@/services/api.service';
import { defineStore } from 'pinia';

const INFOS_LIFETIME = 60 // minutes
const GALLERY_LIFETIME = 60 // minutes

export const useInfoStore = defineStore({
    id: 'info',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        infos: JSON.parse(localStorage.getItem('infos') ?? "[]"), 
        loading: false,
        error: null,
        infosExpiry: Date.parse(localStorage.getItem('infosExpiry') ?? new Date()),
        activeType: null,
    }),
    getters: {
        infosActiveType: (state) => {
            return state.infos.filter(info => {
                return (
                    info.type == state.activeType
                )
            })
        },
        infoTypes: (state) => {
            var infoTypes = [];
            state.infos.forEach(info => {
                if (!infoTypes.includes(info?.type)) {
                    infoTypes = [...infoTypes, info?.type];
                }
            })
            return infoTypes
        },
    },
    actions: {
        async getInfo () {
            if (this.infos.length == 0 || this.infosExpiry < Date.now()) {
                this.loading = true;
                apiService.getInfoContent().then(
                    (response) => {
                        this.infos = response.data;
                        this.loading = false;
                        this.infosExpiry = new Date();
                        this.infosExpiry.setTime(
                            this.infosExpiry.getTime() + INFOS_LIFETIME * 60 * 60 * 1000
                        );
                        this.activeType = this.infos.find(info => info)?.type;
                        localStorage.setItem('infos', JSON.stringify(this.infos));
                        localStorage.setItem('infosExpiry', JSON.stringify(this.infosExpiry));
                    }
                ).catch(
                    error => {
                        this.loading = false;
                        console.log(error)
                        this.error = error;
                    }
                );
            }
        },
        activateType (type) {
            this.activeType = type;
        },

    },
});

export const useInboxStore = defineStore({
    id: 'inbox',
    state: () => ({
        inbox: [],
        inboxLoading: false,
        responses: [],
        error: null,
        submitLoading: false,
        submitSuccess: false,
        submitError: null,
        deleteLoading: false,
        deleteSuccess: false,
        deleteError: null,
    }),
    actions: {
        async getInbox() {
            if(this.inbox.length == 0){
                this.inboxLoading = true;
                apiService.getInboxContent().then(
                    (response) => {
                        this.inboxLoading = false;
                        this.inbox = response.data;
                        this.responseSetup();
                    }
                ).catch(
                    error => {
                        this.inboxLoading = false;
                        this.error = error;
                    }
                )
            }
        },
        async submitResponse (responses, activeUuid) {
            this.submitLoading = true;
            const out = responses.some(
                response => {
                    if(this.inbox.find(m => m.uuid == activeUuid).questions.some(q => q.uuid == response.question && !q.response)){
                        apiService.postInboxResponse(
                            response.question,
                            Array.isArray(response.option) ? [...response.option] : [response.option],
                            response.text,
                        ).then(
                            () => {
                                return false;
                            }
                        ).catch(
                            error => {
                                this.submitError = [...(this.submitError ?? []), {q: response.question, e: error.response.data}];
                                return true;
                            }
                        )
                    }
                }
            )
            this.submitLoading = false;
            if (!out) {
                this.submitSuccess = true;
            }
        },
        async deleteResponses (activeUuid) {
            this.deleteLoading = true;
            const out = this.inbox.find(m => m.uuid == activeUuid).questions.some(
                question => {
                    apiService.deleteInboxResponse(
                        question.response.uuid
                    ).then(
                        () => {
                            return false;
                        }
                    ).catch(
                        error => {
                            this.deleteError = error;
                            return true;
                        }
                    )
                }
            );
            this.deleteLoading = false;
            if (!out) {
                this.deleteSuccess = true;
            }
        },
    },
})

export const useGalleryStore = defineStore({
    id: 'gallery',
    state: () => ({
        loading: false,
        error: null,
        gallery: JSON.parse(localStorage.getItem('gallery') ?? "[]"),
        galleryExpiry: Date.parse(localStorage.getItem('galleryExpiry') ?? new Date()),
    }),
    actions: {
        async getGalleryContent () {
            if (this.gallery.length == 0 || this.galleryExpiry < Date.now()) {
                this.loading = true;
                apiService.getGalleryContent().then(
                    (response) => {
                        this.gallery = response.data;
                        this.loading = false;
                        this.galleryExpiry = new Date()
                        this.galleryExpiry.setTime(
                            this.galleryExpiry.getTime() + GALLERY_LIFETIME * 60 * 60 * 1000
                        );
                        localStorage.setItem('gallery', JSON.stringify(this.gallery));
                        localStorage.setItem('galleryExpiry', JSON.stringify(this.galleryExpiry));
                    }
                ).catch(
                    error => {
                        this.error = error;
                    }
                )
            }
        },
    }
})