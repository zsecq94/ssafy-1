<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <router-link :to="{ name: 'Home' }"><button id="bt1">Home</button></router-link>
    <router-link :to="{ name: 'Nocolor'}"><button id="bt1">Start</button></router-link>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#bt1 {
  border: 1px solid #f1a324;
  background-color: white;
  width: 130px;
  height: 60px;
  margin: 40px;
}
#div1 {
  text-align: center;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, 
  rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
  width: 500px;
  height: 500px;
  margin: auto;
}
#img1 {
  margin: auto;
  width: 380px;
  height: 330px;
}
</style>
