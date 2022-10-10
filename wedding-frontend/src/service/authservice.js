import axios from 'axios';

const API_URL = process.env.VUE_APP_BACKEND_URL;

class AuthService {
  login(email, token) {
    return axios
      .post(API_URL + '/auth/token/', {
        email: email,
        token: token
      }, {
        headers: {
            'content-type': 'multipart/form-data',
      }})
      .then(response => {
        if (response.data.token) {
          localStorage.setItem('token', JSON.stringify(response.data.token));
        }
        return response.data;
      });
  }

  logout() {
    localStorage.removeItem('token');
  }

}

export default new AuthService();
