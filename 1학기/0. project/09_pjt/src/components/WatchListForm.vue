<template>
  <div>
    <input type="text" v-model="inputData">
    <button style="background-color:transparent;" @click="saveMovie">Add</button>
  </div>
</template>

<script>
export default {
  name:'WatchListForm',
  data() {
    return {
      inputData: '',
    }
  },
  methods: {
    saveMovie() {
      this.$store.dispatch('getInputData',this.inputData)
      this.inputData = ''
    }
  },

}
</script>

<style>

</style>