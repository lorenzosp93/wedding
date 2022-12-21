import router from '@/router';
import axios, { type AxiosResponse } from 'axios';

const API_URL = import.meta.env.VITE_APP_BACKEND_URL;

export async function login (email: string) {
  return axios.post(
    API_URL + '/api/auth/email/', {
    email: email
  })
  .then(() => {
    router.push({ name: 'login-success', query: { email: email } });
  })
  .catch(error => {
    console.log(error.message);
    throw error;
  })
};

export async function get_token(email: string, token: string): Promise<void | AxiosResponse<string>> {
  return axios
    .get(`${API_URL}/api/shared/magic-auth/?email=${email}&token=${token}&api=1`)
    .then(response => {
      let token = response.data.token;
      router.push({ name: 'home', query: { token: token } });
    })
};
