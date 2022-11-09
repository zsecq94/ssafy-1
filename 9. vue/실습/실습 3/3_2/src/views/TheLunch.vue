<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="pickLunch">Pick Lunch</button>
    <br>
    {{ pick }}
    <br>
    <h3>로또를 뽑아보자</h3>
    <button @click="goToLotto">Pick Lotto</button>
  </div>
</template>

<script>
export default {
  name: 'TheLunch',
  data() {
    return {
      list: [
        '라면', '국밥', '김밥', '랍스터', '대게', '짜장면', '짬뽕', '볶음밥'
      ],
      pick: null,
    }
  },
  methods: {
    goToLotto() {
      this.$router.push({name : 'lotto'})
    },
    pickLunch() {
      this.pick = this.list[Math.floor(Math.random() * this.list.length)];
    }
  }
}
</script>

<style>

</style>