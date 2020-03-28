<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">Register Page</h1>
          <h2 class="subtitle">{{ errorMsg }}</h2>
        </div>
      </div>
    </section>
    <section>
      <b-field label="Email">
        <b-input type="email" id="email" v-model="email"></b-input>
      </b-field>
      <b-field label="First Name">
        <b-input id="firstName" v-model="firstName"></b-input>
      </b-field>
      <b-field label="Last Name">
        <b-input id="lastName" v-model="lastName"></b-input>
      </b-field>
      <b-field label="Username">
        <b-input id="username" v-model="username"></b-input>
      </b-field>
      <b-field label="Password">
        <b-input type="password" id="password" v-model="password"></b-input>
      </b-field>
      <b-button type="is-primary" @click="register">Register</b-button>
      <b-button type="is-primary" outlined @click="toLogin">Login</b-button>
    </section>
  </div>
</template>

<script>
import { EventBus } from '@/util';

export default {
  data() {
    return {
      email: '',
      firstName: '',
      lastName: '',
      username: '',
      password: '',
      errorMsg: '',
    };
  },
  methods: {
    toLogin() {
      this.$router.push('/login');
    },
    register() {
      this.$store.dispatch('register', {
        email: this.email,
        first_name: this.firstName,
        last_name: this.lastName,
        username: this.username,
        password: this.password,
      })
        .then(() => this.$router.push('/'));
    },
  },
  mounted() {
    EventBus.$on('failedRegistering', (msg) => {
      this.errorMsg = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off('failedRegistering');
  },
};
</script>

<style>
</style>
