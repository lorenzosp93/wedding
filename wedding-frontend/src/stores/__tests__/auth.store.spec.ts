import { describe, it, expect, vi, beforeEach, type Mock } from 'vitest'
import { setActivePinia, createPinia } from 'pinia';
import { useAuthStore } from "../auth.store";
import type { Profile } from '@/models/auth.interface';
import type { Subscription } from '@/models/listObjects.interface';
import type { AxiosError, AxiosResponse } from 'axios';
import apiService from '@/services/api.service';
import router from '@/router';

vi.mock('@/router', () => ({
  default: {
    push: vi.fn(),
  }
}))

vi.mock('@/i18n', () => ({
  default: {
    global: {
      locale: {
        value: vi.fn(),
      }
    }
  }
}))

let testProfile = {
  id: 1,
  user: {
    first_name: 'testName',
    last_name: 'testLastName',
    email: 'test@mail.com',
  },
  type: 'family',
  language: 'it',
  plus: 1,
  parent: null,
  childs: [],
} as Profile;

let testSubscription = {
  endpoint:'https://abc.com',
  keys: {
    p256dh: 'abc123',
    auth: 'abc',
  }
} as Subscription;

let axiosResponse = {
 data: [], status: 200, statusText: 'success', headers: {}, config: {}
} as AxiosResponse

describe('Auth store test', () => {

  beforeEach(() => {
    const pinia = createPinia();
    setActivePinia(pinia);
  });

  it('Register user', () => {
    let store = useAuthStore();

    let res = vi.spyOn(apiService, 'registerUser').mockResolvedValue(axiosResponse)

    store.register(testProfile.user).then(() => {
      expect(store.success).toBe(true);
      expect(res).toBeCalledWith(testProfile.user);
      expect(router.push as Mock).toBeCalled();
    });
    
  });

  it('Register user fail', () => {
    let store = useAuthStore();

    let res = vi.spyOn(apiService, 'registerUser').mockImplementation(async (_) => {
      throw { response: { data: 'someError' } } as AxiosError
    });

    store.register(testProfile.user).then(() => {
      expect(res).toBeCalled();
      expect(store.registerError).toBe('someError');
    })
    
  })
  it('Get profile', () => {
    let store = useAuthStore();

    vi.spyOn(apiService, 'getUserProfile').mockResolvedValue({
      ...axiosResponse,
      data: [testProfile],
    });

    store.getProfile().then(() => {
      expect(store.profile).toStrictEqual(testProfile);
    })

  })

  it('Login user', () => {
    let store = useAuthStore();

    let token: string = 'abc';

    let res = vi.spyOn(store, 'getProfile').mockResolvedValue();

    let res1 = vi.spyOn(apiService, 'getUserSubscription').mockResolvedValue({
      ...axiosResponse,
      data: [testSubscription],
    })

    store.login(token).then(() => {
      expect(res).toBeCalled();
      expect(res1).toBeCalled();
      expect(store.profile).toStrictEqual(testProfile);

    });
  })

  it('Logout user', () => {
    let store = useAuthStore();
    store.logout();
    expect(store.token).toBe(undefined);
    expect(store.profile).toBe(undefined);
    expect(router.push as Mock).toBeCalledWith({name: 'login'});
  })

  it('Setup plus one', () => {
    let store = useAuthStore();

    let res = vi.spyOn(store, 'getProfile')
    let res1 = vi.spyOn(apiService, 'setupPlusOne').mockResolvedValue(axiosResponse)

    store.setupPlusOne(testProfile.user).then(() => {
      expect(res).toBeCalled();
      expect(res1).toBeCalledWith(testProfile.user);
      expect(store.success).toBe(true);
    });
  })

  it('Setup plus one fail', () => {
    let store = useAuthStore();

    let res = vi.spyOn(store, 'getProfile')
    let res1 = vi.spyOn(apiService, 'setupPlusOne').mockImplementation(async (_) => {
      throw { response: { data: 'someError' } } as AxiosError
    });

    expect(store.setupPlusOne(testProfile.user).then(() => {
      expect(res).toBeCalledTimes(0);
      expect(store.registerError).toBe('someError');
    })).rejects.toThrowError();
    
  })
})