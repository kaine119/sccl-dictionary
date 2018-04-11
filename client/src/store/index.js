import Vue from 'vue';
import Vuex from 'vuex';

import { fetchQueryResults, fetchDefinitionByID } from '../api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentQuery: '',
    currentQueryResults: [],
    currentDefinition: {},
  },
  /* eslint-disable no-param-reassign */
  mutations: {
    changeQuery(state, { newQuery }) {
      state.currentQuery = newQuery;
    },
    setQueryResults(state, { queryResults }) {
      state.currentQueryResults = queryResults;
    },
    setDefinition(state, { definition }) {
      state.currentDefinition = definition;
    },
    setWord(state, { word }) {
      state.currentDefinition.word = word;
    },
  },
  /* eslint-enable */
  getters: {
    currentQuery: state => state.currentQuery,
    currentResults: state => state.currentQueryResults,
    definitionToDisplay: state => state.currentDefinition,
  },
  actions: {
    getQueryResults({ commit, state }) {
      // pings the server for search query and stores results in $store.currentResults.
      commit('setQueryResults', { queryResults: [] });
      fetchQueryResults(state.currentQuery)
        .then((queryResults) => {
          commit('setQueryResults', { queryResults });
        });
    },
    getDefinition({ commit }, { id }) {
      fetchDefinitionByID(id)
        .then((definition) => {
          commit('setDefinition', { definition });
        });
    },
  },
});
