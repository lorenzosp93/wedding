import axios from 'axios';
import authHeader from './authheader';
import { useAuthStore } from '@/stores';

const GALLERY_LIMIT = 16 // images per load

function getCookie(name) {
  let cookieValue = null;
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
export const API_URL = import.meta.env.VITE_APP_BACKEND_URL;
export function getCSRFHeader() {
  return {'X-CSRFToken': getCookie('csrftoken')}
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

  async deleteInboxResponse(response) {
    return request().delete(
      `${API_URL}/api/inbox/response/${response}/`
    )
  }

  async getInfoContent() {
    return request().get(
      API_URL + '/api/info/'
    )
  }
  
  async getGalleryContent(overrideLink=null) {
    return request().get(
      overrideLink ?? API_URL + '/api/photo/?limit=' + GALLERY_LIMIT
    )
  }
  
}

export default new ApiService();
