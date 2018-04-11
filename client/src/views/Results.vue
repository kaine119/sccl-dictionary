<template>
  <div class="mdl-grid">
    <div class="mdl-cell mdl-cell--4-col mdl-cell--hide-phone"></div>
    <div class="mdl-cell mdl-cell--4-col">
      <div class="mdl-shadow--2dp" id="results-card">
        <h1>Results for {{ query }}</h1>
        <ul class="mdl-list">
          <ResultItem v-for="result in results" v-bind:key="result.id"
                v-bind:title="result.name"
                v-bind:itemid="result.id"
                synopsis="This is a test." />
      </ul>
      </div>
    </div>
  </div>
</template>

<script>
import ResultItem from '@/components/ResultItem.vue';

require('mdl/material.min.css');
require('mdl');

export default {
  name: 'Results',
  props: ['query'],
  data: () => ({
    results: [],
  }),
  components: {
    ResultItem,
  },
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

<style scoped>
#results-card {
  padding-left: 20px;
  padding-right: 20px;
}
</style>
