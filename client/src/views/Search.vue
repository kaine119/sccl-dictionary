<template>
  <input type="text" v-model="query" v-on:keyup.enter="search()">
</template>

<script>
export default {
  name: 'Search',
  methods: {
    search() {
      this.$router.push({ name: 'results', params: { query: this.query } });
    },
  },
  data: () => ({
    query: '',
  }),
};
</script>
