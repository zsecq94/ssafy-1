<template>
  <div>
    <h1>중요 할일</h1>
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
  name: 'ImportantTodoPage',
  computed: {
    allTodo() {
      const result = []
      this.$store.state.list.forEach(element => {
        if (element.isImportant === true) {
          result.push(element)
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