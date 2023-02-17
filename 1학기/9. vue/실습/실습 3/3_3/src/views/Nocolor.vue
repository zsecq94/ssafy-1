<template>
  <div id="div1">
    <br>
    <h2>시작</h2>
    <router-link :to="{ name: 'Home' }"><button id="btn1">◀</button></router-link>
    <router-link :to="{ name: 'Ssafling' }"><button id="btn2">▶</button></router-link>
    <img id="img1" src="../assets/happeed.png" alt="">
    <h1>해피드</h1>
  </div>
</template>

<script>
export default {
  name: 'Nocolor',
}
</script>

<style>
#btn1 {
  float: left;

}
#btn2 {
  float: right;
}
</style>