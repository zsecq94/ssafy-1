<template>
  <div id="div1">
    <br>
    <h2>2단계</h2>
    <button id="btn1" @click="Noleft">◀</button>
    <router-link :to="{ name: 'Ssaflower'}"><button id="btn2">▶</button></router-link>
    <img id="img1" src="../assets/happlossome.png" alt="">
    <h1>해플라썸</h1>
  </div>
</template>

<script>
export default {
  name: 'Ssafleaf',
  methods: {
    Noleft() {
      alert('이전 진화 단계로 돌아갈 수 없습니다.')
    }
  }
}
</script>

<style>

</style>