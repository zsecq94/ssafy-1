<template>
  <div>
    <h1>오늘 할일</h1>
    <span><button @click="createTodo">+</button>
    <input 
      id="inputTag" 
      type="text"
      v-model.trim="todoContent"
      @click="clearInput"
    ></span>
    <hr>
    <p id="pTag" 
    v-for="(todo, index) in allTodo" 
    :key="index">
      {{ todo.content }}
    </p>
  </div>
</template>

<script>
export default {
  computed: {
    allTodo() {
      const result = []
      const newDate = new Date()
      this.$store.state.list.forEach(V => {
        if (isNaN(V.dueDateTime[10])) {
          const test2 = V.dueDateTime.slice(0, 10)
          const test = `${newDate.getFullYear()}-${newDate.getMonth()+1}-${newDate.getDate()}`
          if (test2 === test) {
            result.push(V)
          }
        } else {
          const test2 = V.dueDateTime.slice(0, 9)
          const test = `${newDate.getFullYear()}-${newDate.getMonth()+1}-${newDate.getDate()}`
          if (test2 === test) {
            result.push(V)
          }
        }
      });
      return result
    }
  },
  data() {
    return {
      todoContent: '할 일을 작성해주세요!',
    }
  },
  methods: {
    createTodo() {
      if (this.todoContent) {
        this.$store.dispatch('createTodo', this.todoContent)
      }
      this.todoContent = '할 일을 작성해주세요!'
    },
    clearInput() {
      this.todoContent = null
    }
  }
}
</script>

<style>

</style>