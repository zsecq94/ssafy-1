import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/MovieView.vue'
import RandomView from '../views/RandomView.vue'
import WatchListView from '../views/WatchListView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movie',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/random',
    name: 'random',
    component: RandomView
  },
  {
    path: '/watch',
    name: 'watch',
    component: WatchListView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
