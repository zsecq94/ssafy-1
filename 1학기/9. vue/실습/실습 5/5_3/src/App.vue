<template>
  <div id="app">
    <h1 id="hTag">Coffee Order App</h1>
    <div id="main_container">
      <div id="one_container">
        <MenuList/>
      </div>
      <div id="two_container">
        <SizeList/>
      </div>
    </div>
    <br>
    <hr>
    <br>
    <button  @click="addOrder">장바구니 담기</button>
    <OrderList/>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OrderList,
  },
  methods: {
    addOrder() {
      this.$store.commit('addOrder')
    }
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
#app {
  width: 700px;
  height: 330px;
}
#main_container {
  width: 700px;
  height: 330px;
  background-color:darkgrey ;
  border-radius: 20px;
}
#one_container {
  float: left;
  margin: 10px;
  padding: 10px;
  height: 300px;
  background-color: white;
  border-radius: 20px;
}
#two_container {
  float: right;
  margin: 10px;
  padding: 10px;
  height: 300px;
  background-color: white;
  border-radius: 20px;
}
#hTag {
  text-align: center;
  margin-bottom: 20px;
}
</style>
