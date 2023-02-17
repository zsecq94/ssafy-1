<template>
  <div>
    <h1>SSAFY TUBE</h1>
    <input type="text" @keyup.enter="onInput">
  </div>
</template>

<script>

export default {
  name: 'SearchBar',
  methods: {
    onInput(event) {
      this.$emit('onSearchInput', event.target.value)
    }
  }
}
</script>

<style>

</style>