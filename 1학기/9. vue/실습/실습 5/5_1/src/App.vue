<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <MenuList/>
    <SizeList/>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
</style>
