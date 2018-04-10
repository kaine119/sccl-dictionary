<template>
  <div id="app">
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
      <header class="mdl-layout__header">
        <div class="mdl-layout-icon" v-show="notHome">
          <button class="mdl-layout-icon mdl-button mdl-js-button mdl-button--icon"
                  v-on:click="back">
            <i class="material-icons">arrow_back</i>
          </button>
        </div>
        <div class="mdl-layout__header-row">
          <span class="mdl-layout-title">Dictionary</span>
        </div>
      </header>
      <div class="mdl-layout__content">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
require('mdl/material.min.css');
require('material-icons/iconfont/material-icons.css');
require('mdl');

export default {
  name: 'App',
  computed: {
    notHome() {
      return this.$route.name !== 'search';
    },
  },
  methods: {
    back() {
      this.$router.go(-1);
    },
  },
};
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
}
</style>
