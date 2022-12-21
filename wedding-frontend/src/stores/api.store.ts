import type { Gallery, Information, Message, Photo, Question, Response, ResponseErrors } from '@/models/listObjects.interface';
import apiService from '@/services/api.service';
import type { AxiosError, AxiosResponse } from 'axios';
import { defineStore } from 'pinia';

const INFOS_TTL = 60 // minutes
const GALLERY_TTL = 60 // minutes

export const useInfoStore = defineStore({
    id: 'info',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        infos: JSON.parse(localStorage.getItem('infos') ?? "[]") as Information[],
        loading: false as boolean,
        error: undefined as AxiosError | undefined,
        infosExpiry: Date.parse(
            localStorage.getItem('infosExpiry') ?? ''
        ) as number,
        activeType: undefined as string | undefined,
    }),
    getters: {
        infosActiveType: (state): Information[] => {
            return state.infos.filter(info => {
                return (
                    info.type == state.activeType
                )
            })
        },
        infoTypes: (state): string[] => {
            var infoTypes: string[] = [];
            state.infos.forEach(info => {
                if (!infoTypes.includes(info?.type)) {
                    infoTypes = [...infoTypes, info?.type];
                }
            })
            return infoTypes
        },
    },
    actions: {
        async getInfo(): Promise<AxiosResponse<Information[]> | void> {
            if (this.infos.length == 0 || this.infosExpiry < Date.now()) {
                this.loading = true;
                apiService.getInfoContent().then(
                    (response: AxiosResponse<Information[]>) => {
                        this.handleResponse(response);
                    }
                ).catch(
                    (error: AxiosError) => {
                        this.loading = false;
                        console.log(error);
                        this.error = error;
                    }
                );
            }
        },
        activateType(type: string) {
            this.activeType = type;
        },
        handleResponse(response: AxiosResponse<Information[]>) {
            this.infos = response.data;
            this.loading = false;
            this.setExpiry();
            this.activeType = this.infos.find(info => info)?.type;
            this.persistInfo();
        },
        persistInfo() {
            localStorage.setItem('infos', JSON.stringify(this.infos));
            localStorage.setItem('infosExpiry', this.infosExpiry.toString());
        },
        setExpiry() {
            let infosExpiry = new Date();
            infosExpiry.setTime(
                infosExpiry.getTime() + INFOS_TTL * 60 * 1000
            );
            this.infosExpiry = infosExpiry.valueOf();
        }
    },
});


export const useInboxStore = defineStore({
    id: 'inbox',
    state: () => ({
        inbox: [] as Message[],
        inboxLoading: false as boolean,
        responses: [] as Array<Response>,
        error: undefined as AxiosError | undefined,
        submitLoading: false as boolean,
        submitSuccess: false as boolean,
        submitError: [] as Array<ResponseErrors>,
        deleteLoading: false as boolean,
        deleteSuccess: false as boolean,
        deleteError: [] as Array<ResponseErrors>,
    }),
    actions: {
        async getInbox(force: boolean = false): Promise<AxiosResponse<Message[]> | void> {
            if (this.inbox.length == 0 || force) {
                this.inboxLoading = true;
                apiService.getInboxContent().then(
                    (response: AxiosResponse<Message[]>) => {
                        this.inboxLoading = false;
                        this.inbox = response.data;
                    }
                ).catch(
                    (error: AxiosError) => {
                        this.inboxLoading = false;
                        this.error = error;
                    }
                )
            }
        },
        async submitResponse(responses: Response[], activeUuid: string) {
            var calls: Promise<AxiosResponse>[] = [];
            let activeMessage = this.inbox.find(m => m.uuid == activeUuid);
            this.submitLoading = true;
            responses.forEach(
                response => {
                    if (activeMessage?.questions.some(q => q.uuid == response.question && !q.response)) {
                        calls = [...calls, apiService.postInboxResponse({
                            question: response.question ?? '',
                            option: Array.isArray(response.option) ? response.option : response.option ? [response.option] : '',
                            text: response.text,
                        })];
                    }
                }
            )
            Promise.allSettled(calls).then((responses: PromiseSettledResult<AxiosResponse>[]) => {
                this.submitLoading = false;
                responses.forEach((response: PromiseSettledResult<AxiosResponse>, idx: number) => {
                    if (response.status == 'rejected') {
                        this.submitError = [
                            ...this.submitError,
                            {
                                q: activeMessage?.questions[idx].uuid ?? '',
                                e: response.reason.response.data
                            }
                        ];
                    };
                })
                if (responses.every(response => response.status == 'fulfilled')) {
                    this.submitSuccess = true;
                    this.submitError = [];
                }
                this.getInbox(true);
            });
        },
        async deleteResponses(activeUuid: string): Promise<AxiosResponse | void> {
            var calls: Promise<AxiosResponse>[] = [];
            let activeMessage = this.inbox.find(m => m.uuid == activeUuid);
            this.deleteLoading = true;
            this.submitSuccess = false;
            activeMessage?.questions.forEach(
                question => {
                    calls = [...calls, apiService.deleteInboxResponse(
                        question.response?.uuid ?? ''
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
                                q: activeMessage?.questions[idx].uuid ?? '',
                                e: response.reason.response.data
                            }
                        ];
                    };
                })
                if (responses.every(response => response.status == 'fulfilled')) {
                    this.deleteSuccess = true;
                    this.deleteError = [];
                }
                this.getInbox(true);
            });
        },
    },
})

export const useGalleryStore = defineStore({
    id: 'gallery',
    state: () => ({
        loading: false as boolean,
        error: undefined as AxiosError | undefined | null,
        gallery: JSON.parse(localStorage.getItem('gallery') ?? "[]") as Photo[],
        galleryExpiry: Date.parse(
            localStorage.getItem('galleryExpiry') ?? ''
        ) as number,
        next: localStorage.getItem('galleryNext') as string | null,
    }),
    actions: {
        async getGalleryContent(force: boolean = false): Promise<AxiosResponse<Gallery> | void> {
            if (this.gallery.length == 0 || this.galleryExpiry < Date.now() || force) {
                this.loading = true;
                apiService.getGalleryContent(this.next).then(
                    (response: AxiosResponse<Gallery>) => {
                        this.handleResponse(response, force);
                    }
                ).catch(
                    (error: AxiosError) => {
                        this.error = error;
                    }
                )
            }
        },
        handleResponse(response: AxiosResponse<Gallery>, force: boolean): void {
            let gallery = new Set([...this.gallery, ...response.data.results]);
            this.gallery = Array.from(gallery);
            this.next = response.data.next;
            this.loading = false;
            this.setExpiry();
            this.persistGallery(force);
        },
        persistGallery(force: boolean): void {
            if (!force) { // set properties for persistence upon refresh
                localStorage.setItem('gallery', JSON.stringify(this.gallery));
                localStorage.setItem('galleryExpiry', this.galleryExpiry.toString());
                localStorage.setItem('galleryNext', this.next ?? '');
            }
        },
        setExpiry(): void {
            let galleryExpiry = new Date();
            galleryExpiry.setTime(
                galleryExpiry.getTime() + GALLERY_TTL * 60 * 1000
            );
            this.galleryExpiry = galleryExpiry.valueOf();
        },
    },
})




