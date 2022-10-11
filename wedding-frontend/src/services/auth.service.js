import router from '@/router';
import axios from 'axios';

const API_URL = process.env.VUE_APP_BACKEND_URL;

class AuthService {
  login(email) {
    return axios
      .post(API_URL + '/auth/email/', {
        email: email
      }, {
        headers: {
            // 'content-type': 'multipart/form-data',
      }})
      .then(response => {
        if (response.status == 200) {
          router.push('/login/success')
        }
        return response.data;
      })
      .catch(error => {
        return error
      });
  }

  logout() {
    localStorage.removeItem('token');
  }

}

export default new AuthService();
