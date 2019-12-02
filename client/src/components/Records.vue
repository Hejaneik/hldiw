<template>
  <section>
    <b-table :data="records">
      <template slot-scope="props">
        <b-table-colum field="name" label="Name">{{props.rows.name}}</b-table-colum>
        <b-table-colum field="time" label="Time">{{props.rows.time}}</b-table-colum>
        <b-table-colum field="date" label="Date">{{props.rows.date}}</b-table-colum>
        <b-table-colum field="excuse" label="Excuse">{{props.rows.excuse}}</b-table-colum>
      </template>
<!-- TODO remove airbnb for better linting -->
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
</template>

<script>
export default {
  name: 'Records',
  data() {
    const records = [
      {
        name: 'Max Mustermann',
        time: '20 min',
        date: 'heute',
        excuse: 'lorem ipsum',
      },
    ];
    return { records };
  },
};
</script>

<style>
</style>
