<template>
  <div @click="updateTodoStatus"
      :class="{'is-completed' : input.isCompleted}">
    <span>
    {{ input.inputData }}
  </span>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
<script>

export default {
  name: 'WatchListItem',
  props: {
    input: Object
  },
  methods: {
    updateTodoStatus() {
        this.$store.dispatch('updateTodoStatus', this.input)
    },
  }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
    background-color: darkgrey;
    color: gray
  }
</style>