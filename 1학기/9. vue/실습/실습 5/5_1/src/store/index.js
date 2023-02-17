import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: true,
        image: '<https://source.unsplash.com/featured/?americano>'
      },
      {
        title: '카페라떼',
        price: 4500,
        selected: true,
        image: '<https://source.unsplash.com/featured/?latte>'
      },
      {
        title: '라면',
        price: 1500,
        selected: true,
        image: '<https://source.unsplash.com/featured/?ramen>'
      }
    ],
    sizeList: [
      {
        name: 'small',
        price: 500,
        selected: true,
      },
      {
        name: 'medium',
        price: 1000,
        selected: true,
      },
      {
        name: 'large',
        price: 1500,
        selected: true,
      },
    ],
  },
  getters: {
  },
  mutations: {
    addOrder: function () {},
    updateMenuList: function (state, menu) {
      const index = state.menuList.indexOf(menu)
      state.menuList[index].selected = !state.menuList[index].selected
      console.log(state.menuList)
    },
    updateSizeList: function (state, size) {
      const index = state.sizeList.indexOf(size)
      state.sizeList[index].selected = !state.sizeList[index].selected
      console.log(state.sizeList)
    },
  },
  actions: {
  },
  modules: {
  }
})