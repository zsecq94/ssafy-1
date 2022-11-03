<template>
  <div id="app">
    <div id="div1">
      <Timetable @create-time="createTime"
      @create-name="createName"/>
    </div>
    <div id="div2">
      <Mylist :time-create="times" :name-create="names"/>
    </div>
  </div>
</template>

<script>
import Timetable from '@/components/Timetable'
import Mylist from '@/components/Mylist'


export default {
  name: 'App',
  components: {
    Timetable,
    Mylist,
  },
  data: function () {
    return {
      times: [],
      names: [],
    }
  },
  methods: {
    createTime: function (time) {
      this.times.push(time)
    },
    createName: function (name) {
      this.names.push(name)
    }
  }

}
</script>

<style>
#div1 {
  width: 450px;
  float: left;
}
#div2 {
  width: 450px;
  float: left;
  background-color: #658DC63D;
}
#app {
  /* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  margin-top: 60px;
  color: #424242;
}
</style>
