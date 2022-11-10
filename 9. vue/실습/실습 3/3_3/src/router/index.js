import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Nocolor from '../views/Nocolor.vue'
import Ssafling from '../views/Ssafling.vue'
import Ssafleaf from '../views/Ssafleaf.vue'
import Ssaflower from '../views/Ssaflower.vue'
import NotFound from '../views/NotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/happeed',
    name: 'Nocolor',
    component: Nocolor
  },
  {
    path: '/happling',
    name: 'Ssafling',
    component: Ssafling
  },
  {
    path: '/happlossome',
    name: 'Ssafleaf',
    component: Ssafleaf
  },
  {
    path: '/happlossome',
    name: 'Ssaflower',
    component: Ssaflower
  },
  {
    path: '/notfound',
    name: 'NotFound',
    component: NotFound
  },
  {
    path: '*',
    redirect: '/notfound'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
