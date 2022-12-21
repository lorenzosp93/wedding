import axios, { type AxiosInstance, type AxiosResponse, type RawAxiosRequestHeaders } from 'axios';
import authHeader from './authheader';
import { useAuthStore } from '@/stores';
import type { Gallery, Information, Message, Response, Subscription } from '@/models/listObjects.interface';
import type { User, Profile } from '@/models/auth.interface';

export const API_URL = import.meta.env.VITE_APP_BACKEND_URL;
const GALLERY_LIMIT = 16 // images per load

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

export function axiosInstanceFactory(): AxiosInstance {
  var headers = { ...authHeader() };
  headers = { ...headers, ...getCSRFHeader() };
  const request = axios.create({
    headers: headers
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


class ApiService {

  async setupPlusOne(invitee: User): Promise<AxiosResponse> {
    return axiosInstanceFactory().post(
      API_URL + '/api/user/setup-plus-one/',
      invitee,
    )
  }

  async registerUser(invitee: User): Promise<AxiosResponse> {
    return axiosInstanceFactory().post(
      API_URL + '/api/user/register-user/',
      invitee,
    )
  }

  async getUserSubscription(): Promise<AxiosResponse<Subscription[]>> {
    return axiosInstanceFactory().get(
      `${API_URL}/api/user/subscription/`
    )
  }

  async getUserProfile(): Promise<AxiosResponse<Profile[]>> {
    return axiosInstanceFactory().get(API_URL + '/api/user/profile/')
  }

  async getInboxContent(): Promise<AxiosResponse<Message[]>> {
    return axiosInstanceFactory().get(API_URL + '/api/inbox/message/')
  }

  async postInboxResponse(response: Response): Promise<AxiosResponse> {
    return axiosInstanceFactory().post(
      API_URL + '/api/inbox/response/',
      response
    )
  }

  async deleteInboxResponse(response_uuid: string): Promise<AxiosResponse> {
    return axiosInstanceFactory().delete(
      `${API_URL}/api/inbox/response/${response_uuid}/`
    )
  }

  async getInfoContent(): Promise<AxiosResponse<Information[]>> {
    return axiosInstanceFactory().get(
      API_URL + '/api/info/'
    )
  }

  async getGalleryContent(overrideLink: string | null = null): Promise<AxiosResponse<Gallery>> {
    return axiosInstanceFactory().get(
      overrideLink ?? API_URL + '/api/photo/?limit=' + GALLERY_LIMIT
    )
  }

  async postUserSubscription(subscription: PushSubscriptionJSON | undefined): Promise<AxiosResponse> {
    return axiosInstanceFactory().post(
      `${API_URL}/api/user/subscription/`,
      subscription
    )
  }

}

export default new ApiService();
