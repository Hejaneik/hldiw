import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

import Ping from '../components/Ping.vue';
import Delays from '../components/Delays.vue';
import Friends from '../components/Friends.vue';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';

import NotFound from '../components/NotFound.vue';

import store from '@/store';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
  },
  {
    path: '/delays',
    name: 'Delays',
    component: Delays,
  },
  {
    path: '/friends',
    name: 'Friends',
    component: Friends,
    beforeEnter(to, from, next) {
      if (!store.getters.isAuthenticated) {
        next('/login');
      } else {
        next();
      }
    },
  },
  // all new routes before this one, default route to display error messages
  {
    path: '*',
    component: NotFound,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
