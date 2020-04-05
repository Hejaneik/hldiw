<template>
  <b-navbar type="is-primary">
    <template slot="brand">
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        <img
          src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
          alt="Lightweight UI components for Vue.js based on Bulma"
        />
      </b-navbar-item>
    </template>
    <template slot="start">
      <b-navbar-item tag="router-link" :to="{ path: '/' }">Dashboard</b-navbar-item>
      <b-navbar-item tag="router-link" :to="{ path: '/delays' }">Delays</b-navbar-item>
      <b-navbar-dropdown label="Social" hoverable="true">
        <b-navbar-item tag="router-link" :to="{ path: '/friends' }">Friends</b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/addfriend' }">Add Friend</b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/contact' }">Contact</b-navbar-item>
      </b-navbar-dropdown>
      <b-navbar-item tag="router-link" :to="{ path: '/about' }">About</b-navbar-item>
    </template>

    <template slot="end">
      <b-navbar-item tag="div">
        <div class="buttons">
          <router-link :to="{ path: '/register' }">
            <a class="button is-purple">
              <strong>Sign up</strong>
            </a>
          </router-link>
          <router-link :to="{ path: '/login' }">
          <a class="button is-light">
            <strong>Log in</strong>
          </a>
          </router-link>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style lang="scss">
// .navbar {
//   border-bottom: 3px solid;
//   border-color: $white;
// }

.button {
  margin-left: 7px;
}
</style>
