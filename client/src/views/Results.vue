<template>
  <div id="container">
    <h1>Results for {{ query }}</h1>
    <router-link v-bind:to="resultURL(result.id)" v-for="result in results" v-bind:key="result.id">
      <div>
          <p>{{ result.name }}</p>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'Results',
  props: ['query'],
  data: () => ({
    results: [],
  }),
  mounted() {
    // stub
    this.results = [
      { name: 'test1', id: 1 },
      { name: 'test2', id: 2 },
      { name: 'test3', id: 3 },
    ];
  },
  methods: {
    resultURL: resultId => ''.concat('/definition/', resultId),
  },
};
</script>

<style>
</style>
