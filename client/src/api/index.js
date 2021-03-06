import axios from 'axios';

const BASE_URL = 'http://localhost:5000';

export function fetchDelays() {
  return axios.get(`${BASE_URL}/delays`);
}

export function addDelay(payload, jwt) {
  return axios.post(`${BASE_URL}/delay`, payload, { headers: { Authorization: `Bearer: ${jwt}` } });
}

export function signin(userData) {
  return axios.post(`${BASE_URL}/auth/signin`, userData);
}

export function register(userData) {
  return axios.post(`${BASE_URL}/auth/register`, userData);
}

export function fetchFriends(jwt) {
  return axios.get(`${BASE_URL}/friends`, { headers: { Authorization: `Bearer: ${jwt}` } });
}
