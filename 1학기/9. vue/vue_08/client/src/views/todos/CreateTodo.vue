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
      if (!title) {
        alert('입력해 주세요')
        return
      }

      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/todos/',
        data: {title,}
      })
      .then(() => {
        this.$router.push({name: 'TodoList'})
      })
      .catch(error => console.log(error))
    }
  }
}
</script>
