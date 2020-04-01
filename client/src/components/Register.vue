<template>
  <div class="register">
    <!-- <section class="hero is-primary" is-medium>
      <div class="hero-body">
        <div class="container">
          <h1 class="title">Register</h1>
          <h2 class="subtitle">{{ errorMsg }}</h2>
        </div>
      </div>
    </section>-->
    <section>
      <div class="tile is-ancestor">
        <div class="tile is-vertical is-parent">
          <div class="tile is-child box">
            <article class="media">
              <div class="media-content">
                <div class="content">
                  <h1>Create Account</h1>
                  <p>Please fill in the following form to create an account</p>
                </div>
              </div>
              <figure class="media-right">
                <p class="image is-128x128">
                  <img src="https://bulma.io/images/placeholders/128x128.png" alt="Create Account" />
                </p>
              </figure>
            </article>
            <b-field class="field" horizontal label="Email">
              <b-input type="email" id="email" v-model="email" expanded required></b-input>
            </b-field>
            <b-field horizontal label="Name">
              <b-input
                id="firstName"
                placeholder="First Name"
                v-model="firstName"
                expanded
                required
              ></b-input>
              <b-input id="lastName" placeholder="Last Name"
              v-model="lastName" expanded required></b-input>
            </b-field>
            <b-field horizontal label="Username">
              <b-input id="username" v-model="username" expanded required></b-input>
            </b-field>
            <b-field horizontal label="Password">
              <b-input type="password" id="password" v-model="password" expanded required></b-input>
            </b-field>
            <b-field horizontal>
              <div>
                <b-button class="btn" type="is-primary" @click="register">Register</b-button>
                <b-button class="btn" type="is-primary" outlined @click="toLogin">Login</b-button>
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
      this.$store
        .dispatch('register', {
          email: this.email,
          first_name: this.firstName,
          last_name: this.lastName,
          username: this.username,
          password: this.password,
        })
        .then(() => this.$router.push('/friends'));
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

<style lang="scss" scoped>
@import "@/assets/scss/colors.scss";

.register {
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
