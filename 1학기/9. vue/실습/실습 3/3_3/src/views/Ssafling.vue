<template>
  <div id="div1">
    <br>
    <h2>1단계</h2>
    <button id="btn1" @click="Noleft">◀</button>
    <router-link :to="{ name: 'Ssafleaf'}"><button id="btn2">▶</button></router-link>
    <img id="img1" src="../assets/happling.png" alt="">
    <h1>해피드</h1>
  </div>
</template>

<script>
export default {
  name: 'Ssafling',
  methods: {
    Noleft() {
      alert('이전 진화 단계로 돌아갈 수 없습니다.')
    }
  }
}
</script>

<style>

</style>