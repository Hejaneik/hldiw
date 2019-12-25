<template>
  <section>
    <button class="is-primary button is-medium" @click="isComponentModalActive=true">
      Add Delay</button>
    <b-modal
      :active.sync="isComponentModalActive"
      has-modal-card
      trap-focus
      aria-role="dialog"
      aria-modal
    >
      <modal-form></modal-form>
    </b-modal>
  </section>
</template>

<script>
const ModalForm = {
  props: ['name', 'time', 'date', 'excuse'],
  template: `
          <form action="">
            <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">Add Delay</p>
            </header>
            <section class="modal-card-body">
                <b-field label="Name">
                <b-input type="text" :value="name" placeholder="Name" required></b-input>
                </b-field>
                <b-field label="Time">
                <b-input type="text" :value="time" placeholder="Time" required></b-input>
                </b-field>
                <b-field label="Date">
                <b-input type="text" :value="date" placeholder="Date" required></b-input>
                </b-field>
                <b-field label="Excuse">
                <b-input type="text" :value="excuse" placeholder="Excuse" required></b-input>
                </b-field>
            </section>
            <footer class="modal-card-foot">
                <button class="button" type="button" @click="$parent.close()">Close</button>
                <button class="button is-primary">Add Delay</button>
            </footer>
            </div>
        </form>
    `,
};

export default {
  name: 'AddDelay',
  components: {
    ModalForm,
  },
};
</script>

<style>
</style>
