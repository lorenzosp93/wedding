import axios from 'axios';
import authHeader from './authheader';

const API_URL = process.env.VUE_APP_BACKEND_URL;
const request = axios.create({
  headers: authHeader()
}); 

// handle errors and redirect 401
request.interceptors.response.use(
  response => response,
  error => {
    if (error?.response?.status == 401) {
      localStorage.removeItem('token');
      this.$router.push('/login');
    }
    console.log(error);
    return Promise.reject(error)
  }
);
 
class ApiService {
  getProfileContent() {
    return request.get(API_URL + '/api/user/profile/')
  }

  updateAddress(address1, address2, city, postalCode, provinceOrState, country) {
    return request.post(
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

  setupPlusOne(email, first_name, last_name){
    return request.post(
      API_URL + '/api/user/setup-plus-one/',
      {
        email,
        first_name,
        last_name,
      },
    )
  }

  getInboxContent() {
    return request.get(API_URL + '/api/inbox/message/')
  }

  postInboxResponse(question, option, text="") {
    return request.post(
      API_URL + '/api/inbox/response/',
      {
        "question": question,
        "option": option,
        "text": text,
      }
    )
  }

  getInfoContent() {
    return request.get(
      API_URL + '/api/info/'
    )
  }
  
  getGalleryContent() {
    return request.get(
      API_URL + '/api/photo/'
    )
  }
  
}

export default new ApiService();
