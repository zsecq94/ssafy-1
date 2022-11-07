// App.vue

<template>
  <div id="app">
    <p>Counter: {{ cnt1 }}</p>
    <p>Counter x2: {{ cnt2 }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  data() {
    return {
      counter: 1,
    }
  },
  methods: {
    increase() {
      const newCnt1 = this.counter
      this.$store.dispatch('increase', newCnt1)
    },
    decrease: function () {
      const newCnt1 = this.counter
      this.$store.dispatch('decrease', newCnt1)
    },
  },
  computed: {
    cnt1() {
      return this.$store.state.cnt
    },
    cnt2() {
      return this.$store.getters.cnt2
    }
  },
}
</script>

<style>
</style>