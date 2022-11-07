<template>
  <div>
    <p @click="selectSize">{{ size.name }}</p>
    <p>{{ size.price }}</p>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods: {
    selectSize() {
      // console.log(1234)
      this.$store.commit('updateSizeList', this.size)
    },
  }
}
</script>

<style>
</style>