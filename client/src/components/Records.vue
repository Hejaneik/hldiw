<template>
  <section>
    <b-table :data="data">
      <b-table-colum id="name" label="Name"></b-table-colum>
      <b-table-colum id="time" label="Time"></b-table-colum>
      <b-table-colum id="date" label="Date"></b-table-colum>
      <b-table-colum id="excuse" label="Excuse"></b-table-colum>
    </b-table>
  </section>
</template>

<script>
export default {
  name: 'Records',
  data() {
      return []
  },
};
</script>

<style>
</style>
