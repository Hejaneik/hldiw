<template>
  <div>
    <section>
      <b-table :data="delays">
        <template slot-scope="props">
          <b-table-column field="name" label="Name">{{props.row.name}}</b-table-column>
          <!-- rework the following line -->
          <b-table-column field="time" label="Time">{{props.row.delay}} min</b-table-column>
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

    <!-- TODO add post functionality -->
    <section>
      <button class="is-primary button is-medium"
      @click="isComponentModalActive=true">Add Delay</button>
      <b-modal
        :active.sync="isComponentModalActive"
        has-modal-card
        v-bind:trap-focus="false"
        aria-role="dialog"
        aria-modal
        v-bind="addDelayForm"
      >
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">Add Delay</p>
          </header>
          <section class="modal-card-body">
            <b-field label="Name">
              <b-input type="text" v-model="addDelayForm.name"
              placeholder="Name" required></b-input>
            </b-field>
            <b-field label="Delay">
              <b-input type="text" v-model="addDelayForm.delay"
              placeholder="Delay" required></b-input>
            </b-field>
            <b-field label="Date">
              <!-- <b-input type="text" v-model="addDelayForm.date"
              placeholder="Date" required></b-input> -->
              <b-datetimepicker
                rounded
                v-model="addDelayForm.date"
                placeholder="Click to select..."
                icon="calendar-today"
                required
                editable
                position="is-top-right"
              ></b-datetimepicker>
            </b-field>
            <b-field label="Excuse">
              <b-input type="text" v-model="addDelayForm.excuse"
              placeholder="Excuse" required></b-input>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <button class="button" type="button" @click="close()">Close</button>
            <button class="button is-primary" @click="submit()">Add Delay</button>
          </footer>
        </div>
      </b-modal>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';

const BASE_URL = 'http://localhost:5000';
// import ModalForm from './ModalForm.vue';

export default {
  name: 'Delays',
  components: {
    // ModalForm,
  },
  data() {
    return {
      addDelayForm: {
        name: '',
        delay: '',
        date: new Date(),
        excuse: '',
      },
      isComponentModalActive: false,
    };
  },
  methods: {
    // TODO add loading animation before delays are fetched
    // TODO rework the following methods
    getDelays() {
      const path = `${BASE_URL}/delays`;
      axios
        .get(path)
        .then((res) => {
          this.delays = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    addDelay(payload) {
      const path = `${BASE_URL}/delay`;
      axios
        .post(path, payload)
        .then(() => {
          this.getDelays();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getDelays();
        });
    },
    initForm() {
      this.addDelayForm.name = '';
      this.addDelayForm.delay = '';
      this.addDelayForm.time = '';
      this.addDelayForm.excuse = '';
    },
    submit() {
      this.isComponentModalActive = false;
      const payload = {
        // TODO add ID of posting person
        owner_id: 1,
        // TODO add person id or something like that
        name: this.addDelayForm.name,
        delay: this.addDelayForm.delay,
        date: this.addDelayForm.date,
        excuse: this.addDelayForm.excuse,
      };
      // this.addDelay(payload);
      this.$store.dispatch('submitDelay', payload);
      this.initForm();
    },
    close() {
      this.isComponentModalActive = false;
      this.initForm();
    },
  },
  created() {
    this.getDelays();
  },
  computed: mapState({
    delays: state => state.delays,
  }),
  beforeMount() {
    this.$store.dispatch('loadDelays');
  },
};
</script>

<style>
/* needed in order to have the datetimepicker overflowing the modal */
.modal .animation-content .modal-card {
  overflow: visible !important;
}

.modal-card-body {
  overflow: visible !important;
}
</style>
