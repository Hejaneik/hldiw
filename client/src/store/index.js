import Vue from 'vue';
import Vuex from 'vuex';

// AJAX methods from api here
import {
  fetchDelays, addDelay, signin, register, fetchFriends,
} from '@/api';
import { isValidJwt, EventBus } from '@/util';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    delays: [],
    jwt: '',
    user: {},
    friends: [],
  },
  getters: {
    // reusable data accessor
    isAuthenticated(state) {
      // eslint-disable-next-line
      console.log(state.jwt.token);
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
    setFriends(state, payload) {
      state.friends = payload.friends;
    },
  },
  actions: {
    loadDelays(context) {
      return fetchDelays()
        .then(res => context.commit('setDelays', { delays: res.data }));
    },
    loadFriends(context) {
      return fetchFriends(context.state.jwt.token)
        .then(res => context.commit('setFriends', { friends: res.data }));
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
          EventBus.$emit('failedRegistering', err);
        });
    },
  },
});
