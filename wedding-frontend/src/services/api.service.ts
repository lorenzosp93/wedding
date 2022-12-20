import axios, { type AxiosInstance, type AxiosResponse, type RawAxiosRequestHeaders } from 'axios';
import authHeader from './authheader';
import { useAuthStore } from '@/stores';
import type { Gallery, Information, Message } from '@/models/listObjects.interface';

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

export function axiosInstanceFactory(post: boolean = false): AxiosInstance {
  var headers = { ...authHeader() };
  headers = post ? { ...headers, ...getCSRFHeader() } : headers;
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

  async setupPlusOne(email: string, first_name: string, last_name: string): Promise<AxiosResponse> {
    return axiosInstanceFactory(true).post(
      API_URL + '/api/user/setup-plus-one/',
      {
        email,
        first_name,
        last_name,
      },
    )
  }

  async getInboxContent(): Promise<AxiosResponse<Message[]>> {
    return axiosInstanceFactory().get(API_URL + '/api/inbox/message/')
  }

  async postInboxResponse(question: string, option: string[] | string, text: string = ""): Promise<AxiosResponse> {
    return axiosInstanceFactory(true).post(
      API_URL + '/api/inbox/response/',
      {
        "question": question,
        "option": option,
        "text": text,
      }
    )
  }

  async deleteInboxResponse(response: string): Promise<AxiosResponse> {
    return axiosInstanceFactory().delete(
      `${API_URL}/api/inbox/response/${response}/`
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

}

export default new ApiService();
