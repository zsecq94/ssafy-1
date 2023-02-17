import Vue from 'vue'
import Vuex from 'vuex'
// import todo from './modules/todo'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    list: [
      {
        id: 1638771553377,
        content: 'Vue',
        dueDateTime: '2021-12-11T16:05',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 1638771553378,
        content: 'Vue Router',
        dueDateTime: '2021-12-11T16:05',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 1638771553379,
        content: 'Vuex',
        dueDateTime: '2021-12-11T16:05',
        isCompleted: true,
        isImportant: false,
      },
    ],
  },
  getters: {

  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.list.push(todoItem)
    }
  },
  actions: {
    createTodo(context, todoContent) {
      const index = this.state.list.length - 1
      const newDate = new Date()
      const saveDate = `${newDate.getFullYear()}-${newDate.getMonth()+1}-${newDate.getDate()}T00:00`
      const todoItem = {
        id: this.state.list[index].id + 1,
        content: todoContent,
        dueDateTime: saveDate,
        isCompleted: false,
        isImportant: false,
      }
      context.commit('CREATE_TODO', todoItem)
    }
  },
})
