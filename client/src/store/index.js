import Vue from 'vue';
import Vuex from 'vuex';

// AJAX methods from api here
import { fetchDelays, addDelay } from '@/api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    delays: [],
    jwt: '',
  },
  mutations: {
    setDelays(state, payload) {
      state.delays = payload.delays;
    },
  },
  actions: {
    loadDelays(context) {
      return fetchDelays()
        .then(res => context.commit('setDelays', { delays: res.data }));
    },
    submitDelay(context, delay) {
      return addDelay(delay);
    },
  },
  modules: {
  },
});
