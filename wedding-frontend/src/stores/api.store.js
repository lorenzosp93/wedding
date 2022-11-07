import apiService from '@/services/api.service';
import { defineStore } from 'pinia';
const INFOS_LIFETIME = 30 // minutes

export const useInfoStore = defineStore({
    id: 'info',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        infos: null, loading: false,
        error: null,
        infosExpiry: null,
        activeInfo: null,
        activeType: null,
    }),
    getters: {
        infosActiveType: (state) => {
            return state.infos?.filter(info => {
                return info.type == state.activeType
            })
        },
        infoTypes: (state) => {
            var infoTypes = [];
            state.infos?.forEach(info => {
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

export const useInboxStore = defineStore({
    id: 'inbox',
    state: () => ({
        inbox: null,
        responses: [],
        error: null,
        inboxExpiry: null,
        active: 0,
        submitLoading: false,
        submitSuccess: false,
        search: '',
        viewDetail: false,
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
                    console.log(error);
                    this.error = error;
                }
            )
        },
        async responseSetup () {
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
                Array.isArray(response.option) ? response.option : response.option ? [response.option] : [],
                response.text,
                ).then(
                () => false
                )
            }
            }
        )
        this.submitLoading = false;
        if (!out) {
            this.submitSuccess = true;
        }
        },
        setActive (n) {
            this.active = n;
            this.viewDetail = true;
        },
    },
})
