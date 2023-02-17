<template>
  <div>
    <h1>모든 할일</h1>
    <hr>
    <p id="pTag" v-for="(todo, index) in allTodo" :key="index">
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
  }
}
</script>

<style>
#pTag {
  border: solid gray 1px;
  border-radius: 10px;
  padding: 25px;

}
</style>