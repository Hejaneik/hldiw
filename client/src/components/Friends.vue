<template>
  <div>
    <section>
      <b-table :data="friends">
        <template slot-scope="props">
          <b-table-column field="username" label="Username">{{props.row.username}}</b-table-column>
          <b-table-column field="id" label="ID">{{props.row.id}}</b-table-column>
          <b-table-column field="name" label="Name">{{props.row.first_name}} {{props.row.last_name}}
          </b-table-column>
          <b-table-column field="since" label="User since">{{props.row.user_since}}</b-table-column>
        </template>

        <template slot="empty">
          <section class="section">
            <div class="content has-text-grey has-text-centered">
              <p>
                <b-icon icon="emoticon-sad" size="is-large"></b-icon>
              </p>
              <p>Nothing here.</p>
            </div>
          </section>
        </template>
      </b-table>
    </section>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Friends',
  computed: mapState({
    friends: state => state.friends,
  }),
  beforeMount() {
    this.$store.dispatch('loadFriends');
  },
};
</script>

<style>
</style>
