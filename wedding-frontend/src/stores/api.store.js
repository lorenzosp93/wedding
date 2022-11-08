import apiService from '@/services/api.service';
import { defineStore } from 'pinia';

const INFOS_LIFETIME = 30 // minutes

export const useInfoStore = defineStore({
    id: 'info',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        infos: [], 
        loading: false,
        error: null,
        infosExpiry: null,
        activeInfo: null,
        activeType: null,
    }),
    getters: {
        infosActiveType: (state) => {
            return state.infos.filter(info => {
                return info.type == state.activeType
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
                        this.activeInfo = this.infos.find(info => info);
                        this.activeType = this.activeInfo?.type;
                    }
                ).catch(
                    error => {
                        this.error = error;
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

export const useInboxStore = defineStore({
    id: 'inbox',
    state: () => ({
        inbox: [],
        responses: [],
        error: null,
        inboxExpiry: null,
        active: 0,
        submitLoading: false,
        submitSuccess: false,
        submitError: null,
        search: '',
        viewDetail: false,
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
        async getInbox() {
            this.loading = true;
            apiService.getInboxContent().then(
                (response) => {
                    this.inbox = response.data;
                    this.responseSetup();
                    this.loading = false;
                }
            ).catch(
                error => {
                    this.error = error;
                }
            )
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
        submitResponse () {
            this.submitLoading = true;
            const out = this.responses.some(
                response => {
                    if(this.activeMessage.questions.some(q => q.uuid == response.question && !q.response)){
                        apiService.postInboxResponse(
                            response.question,
                            Array.isArray(response.option) ? [...response.option] : [response.option],
                            response.text,
                        ).then(
                            () => false
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
            this.getInbox();
        },
        deleteResponses () {
            this.deleteLoading = true;
            const out = this.activeMessage.questions.some(
                question => {
                    apiService.deleteInboxResponse(
                        question.response.uuid
                    ).then(
                        () => false
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
                this.getInbox();
            }
        },
        setActive (n) {
            this.active = n;
            this.viewDetail = true;
        },
    },
})

export const useGalleryStore = defineStore({
    id: 'gallery',
    state: () => ({
        loading: false,
        error: null,
        gallery: [],
        galleryExpiry: null,
    }),
    actions: {
        async getGalleryContent () {
            if (!this.gallery || this.galleryExpiry < Date.now()) {
                this.loading = true;
                apiService.getGalleryContent().then(
                    (response) => {
                    this.gallery = response.data;
                    this.loading = false;
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