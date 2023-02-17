<template>
  <div>
    <h2>예약 페이지</h2>
    <h3>선생님 선택</h3>
    <div id="div1">
      <button id="btn1" @click="save2('Eric')">Eric</button><button id="btn2" @click="save3('Tony')">Tony</button>
    </div>
    <hr id="hr1">
    <h3>시간 선택</h3>
    <div id="div3" v-for="(time, index) in times" :key="index">
      <button id="btn3" @click="save">{{time}}</button>
    </div>
    <button id="btn99" @click="create">예약 확정</button>
  </div>
</template>

<script>
export default {
  name: 'Timetable',
  data: function () {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30",
        "12:00","12:30","13:00","13:30","14:00","14:30",
        "15:00","15:30","16:00","16:30","17:00","17:30",
      ],
      timesave: [],
      namesave: [],
    }
  },
  methods: {
    save: function (v) {
      console.log(v.target.innerText)
      console.log(this.timesave)
      if (this.timesave.length >= 5) {
        alert('5타임까지만 신청할 수 있습니다.')
      } else if (this.timesave.includes(v.target.innerText)) {
        v.target.style.backgroundColor = 'white'
        const index = this.timesave.indexOf(v.target)
        console.log(index)
        this.timesave.splice(index)        
      } else {
        v.target.style.backgroundColor = '#658DC63D'
        this.timesave.push(v.target.innerText)
      }
    },
    save2: function (name) {
      const element = document.getElementById('btn1')
      if (this.namesave.includes(name)) {
        element.style.backgroundColor = 'white'
        const index = this.namesave.indexOf(name)
        this.namesave.splice(index)
      } else {
        this.namesave.push(name)
        element.style.backgroundColor = '#658DC63D'
        console.log(name)
      }
    },
    save3: function (name) {
      const element = document.getElementById('btn2')
      if (this.namesave.includes(name)) {
        element.style.backgroundColor = 'white'
        const index = this.namesave.indexOf(name)
        this.namesave.splice(index)
      } else {
        this.namesave.push(name)
        element.style.backgroundColor = '#658DC63D'
        console.log(name)
      }
    },
    create: function () {
      if (this.timesave.length <= 0) {
        alert('시간을 선택해 주세요!')
      } else if (this.namesave.length <= 0) {
        alert('선생님을 선택해 주세요!')
      } else {
      this.$emit('create-time', this.timesave)
      this.$emit('create-name', this.namesave)
      this.namesave = []
      this.timesave = []
      }
    },
  }
}
</script>

<style>
#btn4 {
  float: left;
  align-items: center;
  justify-content: center;
  width: 60px;
  height: 30px;
  border: 1px solid white;
  background-color: #658DC63D;
  cursor: pointer;
}
#btn99 {
  align-items: center;
  justify-content: center;
  width: 75px;
  height: 30px;
  border: 1px solid #0f4c81;
  background-color: white;
  cursor: pointer;
  margin-top: 50px;
}
#btn1 {
  align-items: center;
  justify-content: center;
  width: 75px;
  height: 30px;
  border: 1px solid #0f4c81;
  background-color: white;
  cursor: pointer;
}
#btn2 {
  margin-left: 30px;
  align-items: center;
  justify-content: center;
  width: 75px;
  height: 30px;
  border: 1px solid #0f4c81;
  background-color: white;
  cursor: pointer;
}
#btn3 {
  float: left;
  align-items: center;
  justify-content: center;
  width: 60px;
  height: 30px;
  border: 1px solid white;
  background-color: white;
  cursor: pointer;
}
#hr1 {
  margin-top: 70px;
  margin-left: 70px;
  margin-right: 70px;
}
#div3 {
  margin-left: 40px;
}
.color {
  background-color: #0f4c81;
}
</style>