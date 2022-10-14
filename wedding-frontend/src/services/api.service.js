import axios from 'axios';
import authHeader from './authheader';
import { useAuthStore } from '@/stores';

export const API_URL = process.env.VUE_APP_BACKEND_URL;
export function request(){
  const request = axios.create({
    headers: authHeader()
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

  async updateAddress(address1, address2, city, postalCode, provinceOrState, country) {
    return request().post(
      API_URL + '/api/user/profile/', { address: {
          address1,
          address2,
          city,
          postalCode,
          provinceOrState,
          country,
        }},
    );
  }

  async setupPlusOne(email, first_name, last_name){
    return request().post(
      API_URL + '/api/user/setup-plus-one/',
      {
        email,
        first_name,
        last_name,
      },
    )
  }

  async getInboxContent() {
    return request().get(API_URL + '/api/inbox/message/')
  }

  async postInboxResponse(question, option, text="") {
    return request().post(
      API_URL + '/api/inbox/response/',
      {
        "question": question,
        "option": option,
        "text": text,
      }
    )
  }

  async getInfoContent() {
    return request().get(
      API_URL + '/api/info/'
    )
  }
  
  async getGalleryContent() {
    return request().get(
      API_URL + '/api/photo/'
    )
  }
  
}

export default new ApiService();
