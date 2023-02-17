import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies:[],
    inputData: []
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state,movies){
      state.movies.push(movies)
    },
    GET_INPUT_DATA(state, inputData) {
      const inputDataObj = {
        inputData: inputData,
        isCompleted: false
      }
      console.log(state.inputData)
      state.inputData.push(inputDataObj)
    },
    UPDATE_TODO_STATUS(state, inputData) {
      state.inputData = state.inputData.map((input) => {
        // console.log(input)
        if (input == inputData) {
          input.isCompleted = !input.isCompleted
        }
        return input
      })
    },
  },
  actions: {
    getMovies(context, movies){
      context.commit('GET_MOVIES',movies)
    },
    getInputData(context, inputData) {
      context.commit('GET_INPUT_DATA', inputData)
    },
    updateTodoStatus(context, inputData) {
      context.commit('UPDATE_TODO_STATUS', inputData)
    },
  },
  modules: {
  }
})
