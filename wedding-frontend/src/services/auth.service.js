import router from '@/router';
import axios from 'axios';

const API_URL = process.env.VUE_APP_BACKEND_URL;

class AuthService {
  login(email) {
    return axios
      .post(API_URL + '/auth/email/', {
        email: email
      }, )
      .then( response => {
        console.log(response);
        if(response.status == 200){
          router.push('/login/success');
        }
      })
      .catch(error => {
        console.log(error.message);
        throw error;
      });
  }

  logout() {
    localStorage.removeItem('token');
    router.push('/login');
  }

}

export default new AuthService();
