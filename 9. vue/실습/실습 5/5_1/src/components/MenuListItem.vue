<template>
  <div>
    <h4 @click="selectMenu">{{ menu.title }}</h4>
    <p>{{ menu.price }}</p>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    selectMenu() {
      // console.log(1234)
      this.$store.commit('updateMenuList', this.menu)
    },
  }
}
</script>

<style>
</style>