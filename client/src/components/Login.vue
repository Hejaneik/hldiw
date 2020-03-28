<template>
  <section>
      <b-field label="Email">
          <b-input type="email" id="email" v-model="email"></b-input>
      </b-field>
      <b-field label="Password">
          <b-input type="password" id="password" v-model="password"></b-input>
      </b-field>
      <b-button type="is-primary" @click="authenticate">Login</b-button>
      <b-button type="is-primary" outlined @click="register">Register</b-button>
      <p>{{ errorMsg }}</p>
  </section>
</template>

<script>
import { EventBus } from '@/util';

export default {
  data() {
    return {
      email: '',
      password: '',
      errorMsg: '',
    };
  },
  methods: {
    autheticate() {
      this.$store.dispatch('login', { email: this.email, password: this.password })
        .then(() => this.$router.push('/'));
    },
    register() {
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
