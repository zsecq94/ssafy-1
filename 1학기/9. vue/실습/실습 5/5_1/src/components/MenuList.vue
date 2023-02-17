<template>
  <div class="menu-list">
    <h1>1. 음료를 고르세요.</h1>
    <!-- {{ menuList }} -->
    <MenuListItem
      v-for="menu in menuList" :key="menu.title"
      :menu="menu"
    />
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem'

export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    menuList: function () {
      return this.$store.state.menuList
    },
  },
  methods: {
    selectMenu: function () {},
  },
}
</script>

<style>

</style>