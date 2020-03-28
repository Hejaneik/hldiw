import Vue from 'vue';
import Vuex from 'vuex';

// AJAX methods from api here
import {
  fetchDelays, addDelay, signin, register,
} from '@/api';
import { isValidJwt, EventBus } from '@/util';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    delays: [],
    jwt: '',
    user: {},
  },
  getters: {
    // reusable data accessor
    isAuthenticated(state) {
      return isValidJwt(state.jwt.token);
    },
  },
  mutations: {
    setDelays(state, payload) {
      state.delays = payload.delays;
    },
    setUserData(state, payload) {
      // eslint-disable-next-line
      console.log('setUserData payload = ', payload);
      state.userData = payload.userData;
    },
    setJwt(state, payload) {
      // eslint-disable-next-line
      console.log('setJwt payload = ', payload);
      localStorage.token = payload.jwt.token;
      state.jwt = payload.jwt;
    },
  },
  actions: {
    loadDelays(context) {
      return fetchDelays()
        .then(res => context.commit('setDelays', { delays: res.data }));
    },
    submitDelay(context, delay) {
      return addDelay(delay, context.state.jwt.token);
    },
    login(context, userData) {
      context.commit('setUserData', { userData });
      return signin(userData)
        .then(res => context.commit('setJwt', { jwt: res.data }))
        .catch((err) => {
          // eslint-disable-next-line
          console.log('Error Authenticating: ', err);
          EventBus.$emit('failedAuthentication', err);
        });
    },
    register(context, userData) {
      context.commit('setUserData', { userData });
      return register(userData)
        .then(context.dispatch('login', { userData }))
        .catch((err) => {
          // eslint-disable-next-line
          console.log('Error Registering: ', err);
          EventBus.$emit('failedRegsitering', err);
        });
    },
  },
});
