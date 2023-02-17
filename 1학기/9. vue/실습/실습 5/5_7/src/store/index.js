import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    cnt: 0,
  },
  getters: {
    cnt2(state) {
      return state.cnt * 2
    }
  },
  mutations: {
    INCREASE(state, num) {
      state.cnt += num
    },
    DECREASE(state, num) {
      state.cnt -= num
    }
  },
  actions: {
    increase(context, num) {
      context.commit('INCREASE', num)
    },
    decrease(context, num) {
      context.commit('DECREASE', num)
    }
  },
  modules: {
  }
})
