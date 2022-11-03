<template>
  <div>
    <h2>상담 신청 현황</h2>
    <h3>상담 선생님</h3>
    <p>성함 : <span v-for="(name, index) in nameCreate[0]" :key="index">{{name}} </span></p>
    <hr id="hr2">
    <h3>예약 현황</h3>
    <p>시간들 : <span v-for="(time, index) in timeCreate[0]" :key="index">{{time}} </span></p>
    <hr id="hr2">
    <img id="img1" src="../assets/ssafy-logo.png" alt="asd">
  </div>
</template>

<script>
export default {
  name: 'Mylist',
  props: {
    timeCreate: null,
    nameCreate: null,
  },
  methods: {
    clear: function () {
      console.log('clear1')
      if (this.timeCreate.length > 0 ||this.nameCreate.length > 0) {
        this.timeCreate = null
        this.nameCreate = null
      }
    }
  }
}
</script>

<style>
#hr2 {
  margin: 20px;
  margin-left: 50px;
  margin-right: 50px;
}
#img1 {
  margin-bottom: 50px;
}
</style>