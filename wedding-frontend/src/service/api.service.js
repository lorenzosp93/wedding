import axios from 'axios';
import authHeader from './authheader';

const API_URL = process.env.VUE_APP_BACKEND_URL;
const request = axios.create({
  headers: authHeader()
})

class ApiService {
  getProfileContent() {
    return request.get(API_URL + '/api/user/profile');
  }

  updateAddress(address1, address2, city, postalCode, provinceOrState, country) {
    return request.post(
      API_URL + '/api/user/profile', { address: {
          address1,
          address2,
          city,
          postalCode,
          provinceOrState,
          country
        }},
    );
  }

  getInboxContent() {
    return request.get(API_URL + '/api/inbox')
  }

  
}

export default new ApiService();
