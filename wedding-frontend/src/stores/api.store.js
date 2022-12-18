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
                            this.infosExpiry.getTime() + INFOS_LIFETIME * 60 * 1000
                        );
                        this.activeType = this.infos.find(info => info)?.type;
                        localStorage.setItem('infos', JSON.stringify(this.infos));
                        localStorage.setItem('infosExpiry', this.infosExpiry.toJSON());
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
        async getInbox(force) {
            if(this.inbox.length == 0 || force){
                this.inboxLoading = true;
                apiService.getInboxContent().then(
                    (response) => {
                        this.inboxLoading = false;
                        this.inbox = response.data;
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
            var calls = [];
            let activeMessage = this.inbox.find(m => m.uuid == activeUuid);
            this.submitLoading = true;
            responses.forEach(
                response => {
                    if(activeMessage.questions.some(q => q.uuid == response.question && !q.response)){
                        calls = [...calls, apiService.postInboxResponse(
                            response.question,
                            Array.isArray(response.option) ? response.option : response.option ? [response.option] : null,
                            response.text,
                        )];    
                    }
                }
            )
            Promise.allSettled(calls).then(responses => {
                this.submitLoading = false;
                responses.forEach((response, idx) => {
                    if (response.status == 'rejected') {
                        this.submitError = [
                            ...(this.submitError ?? []),
                            {
                                q: activeMessage.questions[idx].uuid,
                                e: response.reason.response.data
                            }
                        ];
                    };
                })
                if (responses.every(response => response.status == 'fulfilled')) {
                    this.submitSuccess = true;
                    this.submitError = null;
                }
                this.getInbox(true);
            });
        },
        async deleteResponses (activeUuid) {
            var calls = [];
            let activeMessage = this.inbox.find(m => m.uuid == activeUuid);
            this.deleteLoading = true;
            this.submitSuccess = false;
            activeMessage.questions.forEach(
                question => {
                    calls = [...calls, apiService.deleteInboxResponse(
                        question.response.uuid
                    )];
                }
            );
            Promise.allSettled(calls).then(responses => {
                this.deleteLoading = false;
                responses.forEach((response, idx) => {
                    if (response.status == 'rejected') {
                        this.deleteError = [
                            ...(this.deleteError ?? []),
                            {
                                q: activeMessage.questions[idx].uuid,
                                e: response.reason.response.data
                            }
                        ];
                    };
                })
                if (responses.every(response => response.status == 'fulfilled')) {
                    this.deleteSuccess = true;
                    this.deleteError = null;
                }
                this.getInbox(true);
            });
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
        next: localStorage.getItem('galleryNext'),
    }),
    actions: {
        async getGalleryContent (force=null) {
            if (this.gallery.length == 0 || this.galleryExpiry < Date.now() || force) {
                this.loading = true;
                apiService.getGalleryContent(this.next).then(
                    (response) => {
                        this.gallery = [...this.gallery, ...response.data.results];
                        this.next = response.data.next;
                        this.loading = false;
                        this.galleryExpiry = new Date()
                        this.galleryExpiry.setTime(
                            this.galleryExpiry.getTime() + GALLERY_LIFETIME * 60 * 1000
                        );
                        if (!force) { // set properties for persistence upon refresh
                            localStorage.setItem('gallery', JSON.stringify(this.gallery));
                            localStorage.setItem('galleryExpiry', this.galleryExpiry.toJSON());
                            localStorage.setItem('galleryNext', this.next);
                        }
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