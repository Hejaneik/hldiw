<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">Login Page</h1>
          <h2 class="subtitle">{{ errorMsg }}</h2>
        </div>
      </div>
    </section>
    <section>
      <b-field label="Username">
        <b-input id="username" v-model="username"></b-input>
      </b-field>
      <b-field label="Password">
        <b-input type="password" id="password" v-model="password"></b-input>
      </b-field>
      <b-button type="is-primary" @click="authenticate">Login</b-button>
      <b-button type="is-primary" outlined @click="toRegister">Register</b-button>
    </section>
  </div>
</template>

<script>
import { EventBus } from '@/util';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMsg: '',
    };
  },
  methods: {
    authenticate() {
      this.$store
        .dispatch('login', { username: this.username, password: this.password })
        .then(() => this.$router.push('/friends'));
    },
    toRegister() {
      this.$router.push('/register');
    },
  },
  mounted() {
    EventBus.$on('failedAuthentication', (msg) => {
      this.errorMsg = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off('failedAuthentication');
  },
};
</script>

<style>
</style>
