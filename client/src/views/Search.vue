<template>
  <div class="mdl-grid">
    <div class="mdl-cell mdl-cell--4-col mdl-cell--hide-phone"></div>
    <div class="mdl-cell mdl-cell--8ol mdl-cell--4-col-phone" id="grid-cell">
      <div class="mdl-card mdl-shadow--2dp" id="search-card">
        <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label mdl-shadow--" id="search-query">
          <input id="query" type="text" class="mdl-textfield__input"
                 v-model="query" v-on:keyup.enter="search()">
          <label for="query" class="mdl-textfield__label">Search</label>
        </div>
        <button class="mdl-button mdl-js-button mdl-button--raised" v-on:click="search()">Search</button>
      </div>
    </div>
  </div>
</template>

<script>
// mdl stuff
require('mdl/material.min.css');
require('mdl');

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
  mounted() {
    /* eslint-disable no-undef */
    componentHandler.upgradeElement(document.getElementById('search-query'));
    /* eslint-enable */
  },
};
</script>

<style scoped>
#search-query {
  margin: auto;
}
#search-card {
  width: 100%;
  height: 50px;
}

</style>
