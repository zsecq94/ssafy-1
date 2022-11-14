<template>
  <div>
    <input 
      type="text" 
      v-model.trim="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo: function () {
      // 2번 문제
      const title = this.title
      const is_completed = false
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/todos/',
        data: { title, is_completed }
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'TodoList' })
          // this.todos = res.data
        })
        .catch(err => {
          console.log(err)
        })      
    }
  }
}
</script>
