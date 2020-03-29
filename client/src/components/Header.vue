<template>
  <header>
    <div id="nav">
      <router-link id="logo" tag="p" to="/">HLDIW</router-link>
      <span></span>
      <router-link class="navitem" to="/">Dashboard</router-link>
      <router-link class="navitem" to="/delays">Delays</router-link>
      <router-link class="navitem" to="/friends">Friends</router-link>
      <router-link class="navitem" to="/about">About</router-link>
      <router-link class="navbutton" tag="button" to="/login">Login</router-link>
      <router-link class="navbutton" tag="button" to="/register">Register</router-link>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style lang="scss">
header {
  width: 100%;
  position: sticky;
  top: 0;
}

#nav {
  background-color: $secondary;
  text-align: left;
  /* min-height: 6vh; */
  width: 100%;
  display: flex;
}

#logo {
  margin: auto 0;
  color: #ffffff;
  font-family: Arial;
  font-size: 1.5em;
  display: inline-block;
  padding-left: 3%;
  cursor: pointer;
}

a,
button {
  font-family: "Montserrat", sans-serif;
  color: #dadada;
  text-decoration: none;
  font-size: 1.2em;
  font-weight: 500;
  padding: 10px 3% 10px 0;
  height: 100%;
  display: inline-block;
  box-sizing: border-box;
  transition: all 0.3s ease 0s;
}

span {
  flex-grow: 2;
}

.navitem a:hover {
  color: #00c8f5;
}

.nav-style {
  list-style: none;
}

button {
  background-color: rgba(0, 179, 219, 1);
  /* background-color: #00b3db; */
  color: #292929;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease 0s;
  padding: 5px 25px;
  font-size: 1em;
  margin: auto 5% auto 0;
}

button:hover {
  background-color: rgba(0, 179, 219, 0.8);
  color: #292929;
}

.navbutton {
  color: #292929 !important;
}

.router-link-exact-active {
  /* background-color: #444444; */
  color: #00a8ce;
}

#logo {
    color: #ffffff !important;
}
</style>
