<template>
  <div>
    <h1>모든 할일</h1>
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
  name: 'AllTodoPage',
  computed: {
    allTodo() {
      return this.$store.state.list
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
#pTag {
  border: solid gray 1px;
  border-radius: 10px;
  padding: 25px;
}
#inputTag {
  border: solid gray 1px;
  border-radius: 5px;
  margin-left: 10px;
}
</style>