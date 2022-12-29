import axios, { type AxiosInstance, type AxiosResponse, type RawAxiosRequestHeaders } from 'axios';
import authHeader from './authheader';
import { useAuthStore } from '@/stores';
import type { Information, Message, Response, Subscription } from '@/models/listObjects.interface';
import type { Gallery } from '@/models/gallery.interface';
import type { User, Profile } from '@/models/auth.interface';
import type { GuestBook, GuestBookEntry } from '@/models/guestbook.interface';


export const API_URL = import.meta.env.VITE_APP_BACKEND_URL;

function getCookie(name: string): string {
  let cookieValue = '';
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

export function getCSRFHeader(): RawAxiosRequestHeaders {
  return { 'X-CSRFToken': getCookie('csrftoken') }
}

function axiosInstanceFactory(): AxiosInstance {
  var headers = { ...authHeader() };
  headers = { ...headers, ...getCSRFHeader() };
  const request = axios.create({
    headers: headers,
    baseURL: API_URL,
  })
  request.interceptors.response.use(
    response => response,
    error => {
      if ([401, 403].includes(error?.response?.status)) {
        const auth = useAuthStore()
        auth.logout();
      }
      console.log(error);
      return Promise.reject(error)
    }
  );
  return request
}

interface LimitOffsetOptions {
  overrideLink?: string;
  limit: number;
};

class ApiService {

  async setupPlusOne(invitee: User): Promise<AxiosResponse> {
    return axiosInstanceFactory().post(
      '/api/user/setup-plus-one/',
      invitee,
    )
  }

  async registerUser(invitee: User): Promise<AxiosResponse> {
    return axiosInstanceFactory().post(
      '/api/user/register-user/',
      invitee,
    )
  }

  async getUserSubscription(): Promise<AxiosResponse<Subscription[]>> {
    return axiosInstanceFactory().get(
      '/api/user/subscription/'
    )
  }

  async getUserProfile(): Promise<AxiosResponse<Profile[]>> {
    return axiosInstanceFactory().get('/api/user/profile/')
  }

  async getInboxContent(): Promise<AxiosResponse<Message[]>> {
    return axiosInstanceFactory().get('/api/inbox/message/')
  }

  async postInboxResponse(response: Response): Promise<AxiosResponse> {
    return axiosInstanceFactory().post(
      '/api/inbox/response/',
      response
    )
  }

  async deleteInboxResponse(response_uuid: string): Promise<AxiosResponse> {
    return axiosInstanceFactory().delete(
      `/api/inbox/response/${response_uuid}/`
    )
  }

  async getInfoContent(): Promise<AxiosResponse<Information[]>> {
    return axiosInstanceFactory().get(
      '/api/info/'
    )
  }

  async getGalleryContent(options: LimitOffsetOptions): Promise<AxiosResponse<Gallery>> {
    let overrideLink = options.overrideLink?.length ? options.overrideLink : null
    return axiosInstanceFactory().get(
      overrideLink ?? `/api/photo/?limit=${options.limit}`
    )
  }

  async postUserSubscription(subscription: PushSubscriptionJSON | undefined): Promise<AxiosResponse> {
    return axiosInstanceFactory().post(
      '/api/user/subscription/',
      subscription
    )
  }

  async getGuestBookContent(options: LimitOffsetOptions): Promise<AxiosResponse<GuestBook>> {
    let overrideLink = options.overrideLink?.length ? options.overrideLink : null
    return axiosInstanceFactory().get(
      overrideLink ?? `/api/guestbook/entry/?limit=${options.limit}`
    )
  }

  async postGuestBookEntry(text: string): Promise<AxiosResponse<GuestBookEntry>> {
    return axiosInstanceFactory().post(
      '/api/guestbook/entry/',
      { text: text }
    )
  }

  async deleteGuestBookContent(uuid: string): Promise<AxiosResponse<GuestBookEntry[]>> {
    return axiosInstanceFactory().delete(
      `/api/guestbook/entry/${uuid}/`
    )
  }

}

export default new ApiService();
