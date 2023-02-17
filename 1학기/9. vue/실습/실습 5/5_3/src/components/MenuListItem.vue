<template>
  <div :class="{'selected' : menu.selected}" id="divTag">
    <img :src=img alt="" id="img">
    <h4 @click="selectMenu">{{ menu.title }}</h4>
    <p>{{ menu.price }}</p>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  data() {
    return {
      img: this.menu.image
    }
  },
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
#img {
  width : 30px;
  height : 30px;
}
.selected {
  background-color: greenyellow;
}
</style>