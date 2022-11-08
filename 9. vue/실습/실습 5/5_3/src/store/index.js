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
        selected: false,
        image: 'https://source.unsplash.com/featured/?americano'
      },
      {
        title: '카페라떼',
        price: 4500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?latte'
      },
      {
        title: '라면',
        price: 1500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?ramen'
      }
    ],
    sizeList: [
      {
        name: 'small',
        price: 500,
        selected: false,
      },
      {
        name: 'medium',
        price: 1000,
        selected: false,
      },
      {
        name: 'large',
        price: 1500,
        selected: false,
      },
    ],
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state) {
      var num = 0
      state.orderList.forEach(V => {
        num += V.menu.price
        num += V.size.price
      });
      return num
    }
  },
  mutations: {
    addOrder: function (state) {
      const newMenu = {
      }
      state.menuList.forEach(element => {
        if (element.selected === true) {
          newMenu.menu = element
        }
      });    
      state.sizeList.forEach(element => {
        if (element.selected === true) {
          newMenu.size = element
        }
      });      
      state.orderList.push(newMenu)
    },
    updateMenuList: function (state, menu) {
      state.menuList.forEach(element => {
        if (element.selected === true) {
          element.selected = false
        }
      });
      const index = state.menuList.indexOf(menu)
      state.menuList[index].selected = !state.menuList[index].selected
      // console.log(state.menuList)
    },
    updateSizeList: function (state, size) {
      state.sizeList.forEach(element => {
        if (element.selected === true) {
          element.selected = false
        }
      });
      const index = state.sizeList.indexOf(size)
      state.sizeList[index].selected = !state.sizeList[index].selected
      // console.log(state.sizeList)
    },
  },
  actions: {
  },
  modules: {
  }
})