import axios from 'axios';

const BASE_URL = 'http://localhost:5000';

export function fetchDelays() {
  return axios.get(`${BASE_URL}/delays`);
}

export function addDelay(payload) {
  return axios.post(`${BASE_URL}/delay`, payload);
}
