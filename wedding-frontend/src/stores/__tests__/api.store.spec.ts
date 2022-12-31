import { describe, it, expect, vi, beforeEach, type Mock } from 'vitest'
import { createPinia, setActivePinia } from 'pinia';
import {
  useInfoStore,
  useInboxStore,
  useGalleryStore,
  useGuestBookStore,
  GALLERY_LIMIT,
  GUESTBOOK_LIMIT,
} from "../api.store";
import apiService from '@/services/api.service';
import type { Information, Message, Response } from '@/models/listObjects.interface';
import type { AxiosResponse } from 'axios';

let axiosResponse = {
  data: [], status: 200, statusText: 'fulfilled', headers: {}, config: {}
} as AxiosResponse;

let testInfo = [{
    uuid: 'abc123',
    content: 'someTestContent',
    subject: 'someTestSubject',
    type: 'Events',
    picture: 'https://link.to.pic',
    thumbnail: 'https://link.to.thumb',
},{
    uuid: 'abc321',
    content: 'someOtherTestContent',
    subject: 'someOtherTestSubject',
    type: 'Travel',
    picture: 'https://link.to.pic',
    thumbnail: 'https://link.to.thumb',
}] as Information[];

describe('Info store test', () => {

  beforeEach(() => {
    const pinia = createPinia();
    setActivePinia(pinia);
  });

  it('Gets Infos', () => {
    let store = useInfoStore();

    let res = vi.spyOn(apiService, 'getInfoContent').mockResolvedValue({
      ...axiosResponse,
      data: testInfo,
    });

    store.getInfo().then(() => {
      expect(res).toBeCalled();
      expect(store.infos).toStrictEqual(testInfo);
      expect(store.activeType).toBe('Events');
      expect(store.expiry).toBeGreaterThan(Date.now());
      expect(store.infoTypes).toStrictEqual(['Events', 'Travel']);
      expect(store.infosActiveType).toStrictEqual([testInfo[0]]);
    })
  })
})

let testInbox = [{
    uuid: 'abc123',
    content: 'someTestContent',
    subject: 'someTestSubject',
    questions: [{
      uuid: 'cba321',
      content: 'someQuestionTestContent',
      subject: 'someQuestionTestContent',
      options: [{
        uuid: 'acb231',
        content: 'someOptionContent',
        question: 'cba321',
      }],
      response: null,
      multi_select: true,
      free_text: true,
      mandatory: true,
      message: 'abc123',
    }],
    
},{
    uuid: 'abc321',
    content: 'someOtherTestContent',
    subject: 'someOtherTestSubject',
    questions: [],
}] as Message[];

let testResponse = {
    option: ['acb231'],
    text: 'someTextResponse',
    question: 'cba321',
} as Response;

describe('Inbox store test', () => {

  beforeEach(() => {
    const pinia = createPinia();
    setActivePinia(pinia);
  });

  it('Gets inbox', () => {
    let store = useInboxStore();

    let res = vi.spyOn(apiService, 'getInboxContent').mockResolvedValue({
      ...axiosResponse,
      data: testInbox,
    })

    store.getInbox().then(() => {
      expect(res).toBeCalled();
      expect(store.inbox).toStrictEqual(testInbox);
      expect(store.expiry).toBeGreaterThan(Date.now());
    })
  })

  it('Submits responses', () => {
    let store = useInboxStore();

    let res = vi.spyOn(apiService, 'postInboxResponse').mockResolvedValue(axiosResponse);
    let res1 = vi.spyOn(store, 'getInbox').mockResolvedValue();

    store.submitResponse([testResponse, testResponse], testInbox[0].uuid).finally(() => {
      expect(res).toBeCalledTimes(2);
      expect(store.submitSuccess).toBe(true);
      expect(res1).toBeCalledWith({ force: true });
    })
  })

})