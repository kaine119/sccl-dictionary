<template>
  <div class="mdl-grid">
    <div class="mdl-cell--2-col mdl-cell--hide-phone"></div>
    <div class="mdl-cell--8-col mdl-card mdl-shadow--2dp">
      <div v-if="definitionToDisplay.id">
        <h1>{{ definitionToDisplay.word }}</h1>
        <p>{{ definitionToDisplay.definition }}</p>
      </div>
      <div id="loading" v-else>
        <h3>Loading...</h3>
      </div>
    </div>
  </div>

</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'Definition',
  computed: {
    ...mapGetters(['definitionToDisplay']),
  },
  mounted() {
    this.$store.dispatch('getDefinition', { id: this.$route.params.id });
  },
};
</script>

<style scoped>
  .mdl-card {
    padding: 3em;
    width: 100%;
  }
</style>
