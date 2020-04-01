<template>
  <div class="login">
    <section>
      <div class="tile is-ancestor">
        <div class="tile is-vertical is-parent">
          <div class="tile is-child box">
            <article class="media">
              <div class="media-content">
                <div class="content">
                  <h1>Login</h1>
                  <p>Enter your username and password to log in</p>
                </div>
              </div>
              <figure class="media-right">
                <p class="image is-128x128">
                  <img src="https://bulma.io/images/placeholders/128x128.png" alt="Create Account" />
                </p>
              </figure>
            </article>
            <b-field horizontal label="Username">
              <b-input id="username" v-model="username"></b-input>
            </b-field>
            <b-field horizontal label="Password">
              <b-input type="password" id="password" v-model="password"></b-input>
            </b-field>
            <b-field horizontal>
              <div>
                <b-button class="btn" type="is-primary" @click="authenticate">Login</b-button>
                <b-button class="btn" type="is-primary"
                outlined @click="toRegister">Register</b-button>
              </div>
            </b-field>
          </div>
        </div>
      </div>
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

<style lang="scss" scoped>
@import "@/assets/scss/colors.scss";

.login {
  margin: 2% auto;
  max-width: 800px;
}
.btn {
  margin-right: 1%;
}
.media {
  margin-bottom: 3vh;
}
.field {
  margin: 3vh 0;
}
</style>
