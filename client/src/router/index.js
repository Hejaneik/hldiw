import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

import Ping from '../components/Ping.vue';
import Delays from '../components/Delays.vue';
import Friends from '../components/Friends.vue';

import NotFound from '../components/NotFound.vue';

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
    path: '/delays',
    name: 'Delays',
    component: Delays,
  },
  {
    path: '/friends',
    name: 'Friends',
    component: Friends,
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
