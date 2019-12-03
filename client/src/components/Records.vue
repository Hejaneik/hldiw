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
  </div>
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
