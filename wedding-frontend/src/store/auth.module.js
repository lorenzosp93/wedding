import AuthService from '../services/auth.service';

const token = JSON.parse(localStorage.getItem('token'));
const initialState = token
  ? { status: { loggedIn: true }, token }
  : { status: { loggedIn: false }, token: null };

export const auth = {
  namespaced: true,
  state: initialState,
  actions: {
    logout({ commit }) {
      AuthService.logout();
      commit('logout');
    },
  },
  mutations: {
    logout(state) {
      state.status.loggedIn = false;
      state.token = null;
    },
  }
};