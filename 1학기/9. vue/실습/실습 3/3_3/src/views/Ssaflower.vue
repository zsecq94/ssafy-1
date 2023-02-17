<template>
  <div id="div1">
    <br>
    <h2>3단계</h2>
    <button id="btn1" @click="Noleft">◀</button>
    <router-link :to="{ name: 'Home'}">
      <button id="btn2" @click="goHome">▶</button></router-link>
    <img id="img1" src="../assets/happlower.png" alt="">
    <h1>해플라워</h1>
  </div>
</template>

<script>
export default {
  name: 'Ssaflower',
  methods: {
    Noleft() {
      alert('이전 진화 단계로 돌아갈 수 없습니다.')
    },
    goHome() {
      alert('Home으로 돌아갑니다.')
    }
  }
}
</script>

<style>

</style>