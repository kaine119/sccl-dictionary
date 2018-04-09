import Vue from 'vue';
import Router from 'vue-router';
import Search from '@/views/Search.vue';
import Results from '@/views/Results.vue';
import Definition from '@/views/Definition.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'search',
      component: Search,
    },
    {
      path: '/results',
      name: 'results',
      component: Results,
      props: true,
    },
    {
      path: '/definition/:id',
      name: 'definition',
      component: Definition,
      params: true,
    },
  ],
});
