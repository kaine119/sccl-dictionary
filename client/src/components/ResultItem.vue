<template>
  <router-link v-bind:to="resultURL">
    <li class="mdl-list__item mdl-list__item--two-line mdl-js-ripple-effect">
      <span class="mdl-list__item-primary-content">
        <i class="material-icons mdl-list__item-avatar">text_format</i>
        <span>{{ title }}</span>
        <span class="mdl-list__item-sub-title">{{ synopsis }}</span>
      </span>
    </li>
  </router-link>
</template>

<script>
require('mdl/material.min.css');
require('mdl');

export default {
  props: ['title', 'synopsis', 'itemid'],
  computed: {
    resultURL() {
      return ''.concat('/definition/', this.itemid);
    },
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>
