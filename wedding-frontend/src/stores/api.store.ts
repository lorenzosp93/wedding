import type { GuestBook, GuestBookEntry, GuestBookError } from '@/models/guestbook.interface';
import type { Information, Message, Response, ResponseErrors } from '@/models/listObjects.interface';
import type { Gallery, Photo } from '@/models/gallery.interface';
import apiService from '@/services/api.service';
import type { AxiosError, AxiosResponse } from 'axios';
import { defineStore } from 'pinia';
import { useStorage, type RemovableRef } from '@vueuse/core'

export const INFOS_TTL = 60; // minutes
export const INBOX_TTL = 10; // minutes
export const GALLERY_TTL = 60; // minutes
export const GUESTBOOK_TTL = 5; // minutes

export const GALLERY_LIMIT = 16;
export const GUESTBOOK_LIMIT = 30;

interface GetContentOptions {
    force: boolean;
};
interface GetLimitOffsetContentOptions extends GetContentOptions{
    limit?: number;
    next?: boolean;
}

export const useInfoStore = defineStore({
    id: 'info',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        infos: useStorage('infos', []) as RemovableRef<Information[]>,
        loading: false as boolean,
        error: undefined as AxiosError | undefined,
        expiry: useStorage('infosExpiry', Date.now()) as RemovableRef<number>,
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
        async getInfo(): Promise<void> {
            if (this.expiry < Date.now()) {
                this.infos = [];
            }
            if (this.infos.length == 0) {
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
            if (!type) {
                type = this.infoTypes.find(t => t) ?? '';
            }
            this.activeType = type;
        },
        handleResponse(response: AxiosResponse<Information[]>) {
            this.infos = response.data;
            this.loading = false;
            this.setExpiry();
            this.activeType = this.infos.find(info => info)?.type;
        },
        setExpiry() {
            let expiry = new Date();
            expiry.setTime(
                expiry.getTime() + INFOS_TTL * 60 * 1000
            );
            this.expiry = expiry.valueOf();
        }
    },
});


export const useInboxStore = defineStore({
    id: 'inbox',
    state: () => ({
        inbox: useStorage('inbox', []) as RemovableRef<Message[]>,
        expiry: useStorage('inboxExpiry', Date.now()) as RemovableRef<number>,
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
        async getInbox(options: GetContentOptions = {force: false}): Promise<void> {
            if (this.expiry < Date.now()) {
                this.inbox = [];
            }
            if (this.inbox.length == 0 || options.force) {
                this.inboxLoading = true;
                apiService.getInboxContent().then(
                    (response: AxiosResponse<Message[]>) => {
                        this.inboxLoading = false;
                        this.inbox = response.data;
                        this.setExpiry()
                    }
                ).catch(
                    (error: AxiosError) => {
                        this.inboxLoading = false;
                        this.error = error;
                    }
                )
            }
        },
        async submitResponse(responses: Response[], activeUuid: string): Promise<void> {
            var calls: Promise<AxiosResponse>[] = [];
            let activeMessage = this.inbox.find(m => m.uuid == activeUuid);
            this.submitLoading = true;
            responses.forEach(
                (response: Response) => {
                    if (activeMessage?.questions.some(q => q.uuid == response.question && !q.response)) {
                        calls = [...calls, apiService.postInboxResponse({
                            question: response.question ?? '',
                            option: Array.isArray(response.option) ? response.option : response.option ? [response.option] : [],
                            text: response.text,
                        })];
                    }
                }
            )
            return Promise.allSettled(calls).then((responses: PromiseSettledResult<AxiosResponse>[]) => {
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
                this.getInbox({ force: true });
            });
        },
        async deleteResponses(activeUuid: string): Promise<void> {
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
                this.getInbox({ force: true });
            });
        },
        setExpiry() {
            let expiry = new Date();
            expiry.setTime(
                expiry.getTime() + INBOX_TTL * 60 * 1000
            );
            this.expiry = expiry.valueOf();
        }
    },
})


export const useGalleryStore = defineStore({
    id: 'gallery',
    state: () => ({
        loading: false as boolean,
        error: undefined as AxiosError | undefined | null,
        gallery: useStorage('gallery', []) as RemovableRef<Photo[]>,
        expiry: useStorage('galleryExpiry', Date.now()) as RemovableRef<number>,
        next: useStorage('galleryNext', '') as RemovableRef<string>,
    }),
    actions: {
        async getGalleryContent(options: GetLimitOffsetContentOptions): Promise<void> {
            if (this.expiry < Date.now()) {
                this.gallery = [];
                this.next = '';
            }
            if (this.gallery.length == 0 || options.force) {
                this.loading = true;
                apiService.getGalleryContent({
                    overrideLink: this.next,
                    limit: options.limit ?? GALLERY_LIMIT,
                }).then(
                    (response: AxiosResponse<Gallery>) => {
                        this.handleResponse(response, options.next);
                    }
                ).catch(
                    (error: AxiosError) => {
                        this.error = error;
                    }
                )
            }
        },
        handleResponse(response: AxiosResponse<Gallery>, next: boolean | undefined): void {
            let gallery = new Set([...this.gallery, ...response.data.results]);
            this.gallery = Array.from(gallery);
            this.next = response.data.next ?? '';
            this.loading = false;
            if (!next) {
                this.setExpiry();
            }
        },
        setExpiry(): void {
            let galleryExpiry = new Date();
            galleryExpiry.setTime(
                galleryExpiry.getTime() + GALLERY_TTL * 60 * 1000
            );
            this.expiry = galleryExpiry.valueOf();
        },
    },
})

export const useGuestBookStore = defineStore({
    id: 'guestbook',
    state: () => ({
        entries: useStorage('guestbookEntries', []) as RemovableRef<GuestBookEntry[]>,
        expiry: useStorage('entriesExpiry', Date.now()) as RemovableRef<number>,
        next: useStorage('guestbookNext', '') as RemovableRef<string>,
        loading: false as boolean,
        error: undefined as AxiosError | undefined,
        submitLoading: false as boolean,
        submitSuccess: false as boolean,
        submitError: undefined as GuestBookError | undefined,
        deleteLoading: false as boolean,
        deleteSuccess: false as boolean,
        deleteError: undefined as GuestBookError | undefined,
    }),
    actions: {
        async getEntries(options: GetLimitOffsetContentOptions): Promise<void> {
            if (this.expiry < Date.now()) { 
                this.entries = [];
                this.next = '';
            };
            if (this.entries.length == 0 || options.force) {
                this.loading = true;
                apiService.getGuestBookContent({ limit: options.limit ?? GUESTBOOK_LIMIT, overrideLink: options.next ? this.next : ''}).then(
                    (response: AxiosResponse<GuestBook>) => {
                        this.handleResponse(response, options.force, options.next);
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
        async submitEntry(text: string): Promise<void> {
            this.submitLoading = true;
            apiService.postGuestBookEntry(text).then((_) => {
                this.submitError = undefined;
                this.submitLoading = false;
                this.getEntries({ force: true });
            }).catch((error: AxiosError<GuestBookError>) => {
                this.submitError = error?.response?.data;
            })
        },
        async deleteEntry(uuid: string): Promise<void> {
            this.deleteLoading = true;
            apiService.deleteGuestBookContent(uuid).then((_) => {
                this.deleteLoading = false;
                this.getEntries({ force: true });
            }).catch((error: AxiosError<GuestBookError>) => {
                this.deleteError = error?.response?.data;
            })
        },
        handleResponse(response: AxiosResponse<GuestBook>, force: boolean, next: boolean | undefined) {
            this.loading = false;
            if (next) {
            let entries = new Set([...this.entries, ...response.data.results]);
            this.entries = Array.from(entries);
            } else {
                this.entries = response.data.results;
            }
            this.next = response.data.next ?? '';
            if (!next) {
                this.setExpiry();
            }
        },
        setExpiry() {
            let expiry = new Date();
            expiry.setTime(
                expiry.getTime() + GUESTBOOK_TTL * 60 * 1000
            );
            this.expiry = expiry.valueOf();
        }
    }
})



