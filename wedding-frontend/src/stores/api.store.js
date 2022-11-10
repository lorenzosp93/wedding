import apiService from '@/services/api.service';
import { defineStore } from 'pinia';

const INFOS_LIFETIME = 60 // minutes
const INBOX_LIFETIME = 30 // minutes
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
        search: '',
        viewDetail: false,
        active: 0,
    }),
    getters: {
        infosActiveType: (state) => {
            return state.infos.filter(info => {
                return (
                    (info.type == state.activeType)
                    && 
                    ((info.subject + info.content).toLowerCase()
                    .search(state.search.toLowerCase()) != -1)
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
        activeInfo: (state) => {
            return state.infosActiveType[state.active]
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
                        console.log(error)
                        this.error = error;
                    }
                );
            }
        },
        activateType (type) {
            this.active = 0;
            this.activeType = type;
        },

    },
});

export const useInboxStore = defineStore({
    id: 'inbox',
    state: () => ({
        inbox: JSON.parse(localStorage.getItem('inbox') ?? "[]"),
        responses: [],
        error: null,
        inboxExpiry: Date.parse(localStorage.getItem('inboxExpiry') ?? new Date()),
        active: 0,
        submitLoading: false,
        submitSuccess: false,
        submitError: null,
        search: '',
        deleteLoading: false,
        deleteSuccess: false,
        deleteError: null,
    }),
    getters: {
        activeMessage: (state) => {
            return state.inbox ? state.inbox[state.active] : null
        },
        searchedInbox: (state) => {
            if (!state.search) {
                return state.inbox
            }
            return state.inbox.filter(message => {
                return (message.subject + message.content).toLowerCase()
                .search(state.search.toLowerCase()) != -1
            })
        }
    },
    actions: {
        async getInbox(force=false) {
            if(this.inbox.length == 0 | force | this.inboxExpiry < Date.now()){
                this.loading = true;
                apiService.getInboxContent().then(
                    (response) => {
                        this.inbox = response.data;
                        this.responseSetup();
                        this.loading = false;
                        this.inboxExpiry = new Date()
                        this.inboxExpiry.setTime(
                            this.inboxExpiry.getTime() + INBOX_LIFETIME * 60 * 60 * 1000
                        );
                        localStorage.setItem('inbox', JSON.stringify(this.inbox));
                        localStorage.setItem('inboxExpiry', JSON.stringify(this.inboxExpiry));
                    }
                ).catch(
                    error => {
                        this.error = error;
                    }
                )
            }
        },
        async responseSetup () {
            this.responses = [],
            this.inbox.forEach(message => {
                if (message.questions.length){
                message.questions.forEach(question => {
                    this.responses = [...this.responses, {
                    question: question.uuid,
                    option: question?.response?.option ?? (question.multi_select ? [] : null),
                    text: question?.response?.text ?? '',
                    }]
                })
                }
            })
        },
        async submitResponse () {
            this.submitLoading = true;
            const out = this.responses.some(
                response => {
                    if(this.activeMessage.questions.some(q => q.uuid == response.question && !q.response)){
                        apiService.postInboxResponse(
                            response.question,
                            Array.isArray(response.option) ? [...response.option] : [response.option],
                            response.text,
                        ).then(
                            () => {
                                this.getInbox(true);
                                return false;
                            }
                        ).catch(
                            error => {
                                this.submitError = [...(this.submitError ?? []), {q: response.question, e: error}];
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
        async deleteResponses () {
            this.deleteLoading = true;
            const out = this.activeMessage.questions.some(
                question => {
                    apiService.deleteInboxResponse(
                        question.response.uuid
                    ).then(
                        () => {
                            this.getInbox(true);
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