<template>
  <div>
    <h1>로또</h1>
    <button @click="getNum">Get Lucky Numbers</button>
    <br>
    <p v-if="nums.length > 0">{{ nums }}</p>
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: 'TheLotto',
  data() {
    return {
      nums: []
    }
  },
  methods: {
    getNum() {
      this.nums = []
      var flag = true
      while (flag === true) {
        var a = _.random(1, 45)
        console.log(a)
        if (this.nums.includes(a) == false) {
          this.nums.push(a)
          console.log(this.nums)
        } if (this.nums.length === 6) {
          flag = false
        }
      }
      
    }
  }
}
</script>

<style>

</style>