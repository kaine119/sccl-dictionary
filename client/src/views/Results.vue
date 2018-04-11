<template>
  <div class="mdl-grid">
    <div class="mdl-cell mdl-cell--4-col mdl-cell--hide-phone"></div>
    <div class="mdl-cell mdl-cell--4-col">
      <div class="mdl-shadow--2dp" id="results-card">
        <h1>Results for {{ currentQuery }}</h1>

        <ul v-if="currentResults.length > 0" class="mdl-list">
          <ResultItem v-for="result in currentResults" v-bind:key="result.id"
                v-bind:title="result.word"
                v-bind:itemid="result.id"
                v-bind:synopsis="result.pos" />
        </ul>
        <div v-else>
          <h3>Loading...</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import ResultItem from '@/components/ResultItem.vue';

require('mdl/material.min.css');
require('mdl');

export default {
  name: 'Results',
  props: ['query'],
  data: () => ({
  }),
  components: {
    ResultItem,
  },
  methods: {
    resultURL: resultId => ''.concat('/definition/', resultId),
  },
  computed: {
    ...mapGetters(['currentResults', 'currentQuery']),
  },
};
</script>

<style scoped>
#results-card {
  padding: 20px;

}
</style>
