<template>
  <div>
    <section>
      <b-table :data="records">
        <template slot-scope="props">
          <b-table-column field="name" label="Name">{{ props.row.name }}</b-table-column>
          <b-table-column field="time" label="Time">{{props.row.time}}</b-table-column>
          <b-table-column field="date" label="Date">{{props.row.date}}</b-table-column>
          <b-table-column field="excuse" label="Excuse">{{props.row.excuse}}</b-table-column>
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
    <add-record></add-record>
  </div>
</template>

<script>
import axios from 'axios';
import AddRecord from './AddRecord.vue';

export default {
  name: 'Records',
  components: {
    AddRecord,
  },
  data() {
    return {
      records: [],
    };
  },
  methods: {
    getRecords() {
      const path = 'http://localhost:5000/records';
      axios.get(path)
        .then((res) => {
          this.records = res.data.records;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
  },
  created() {
    this.getRecords();
  },
};
</script>

<style>
</style>
