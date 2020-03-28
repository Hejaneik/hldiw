import axios from 'axios';

const BASE_URL = 'http://localhost:5000';

export function fetchDelays() {
  return axios.get(`${BASE_URL}/delays`);
}

export function addDelay(payload) {
  return axios.post(`${BASE_URL}/delay`, payload, { headers: { Authorization: `Bearer: ${jwt}` } });
}

export function signin(userData) {
  return axios.post(`${BASE_URL}/auth/signin`);
}

export function register(userData) {
  return axios.post(`${BASE_URL}/auth/register`);
}
