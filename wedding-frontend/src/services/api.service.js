import axios from 'axios';
import authHeader from './authheader';
import { useAuthStore } from '@/stores';

export const API_URL = process.env.VUE_APP_BACKEND_URL;

export function getCSRFHeader() {
    const token = request().get(
      API_URL + '/api/shared/get-token/'
    ).then( response => response.data.token )
    return {'X-CSRFToken': token}
  }

export function request(post=false){
  var headers = {...authHeader()};
  headers = post ? {...headers, ...getCSRFHeader()} : headers;
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

  async updateAddress(address1, address2, city, postalCode, provinceOrState, country) {
    
    return request(true).post(
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
    return request(true).post(
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
    return request(true).post(
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
