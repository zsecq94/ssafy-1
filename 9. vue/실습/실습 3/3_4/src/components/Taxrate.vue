<template>
  <div>
    <!-- <h2 v-if="zeroV.length == 0">산출세액 : 0 만원</h2>
    <h2 v-if="1200>=incomeProps && incomeProps >= 0">산출세액 : {{ Math.ceil(incomeProps-(incomeProps*0.94)) }} 만원</h2>
    <h2 v-if="1200<incomeProps && incomeProps<=4600">산출세액 : {{ Math.ceil(incomeProps-(incomeProps*0.85)-108) }} 만원</h2>
    <h2 v-if="4600<incomeProps && incomeProps<=8800">산출세액 : {{ Math.ceil(incomeProps-(incomeProps*0.76)-522) }} 만원</h2>
    <h2 v-if="8800<incomeProps && incomeProps<=15000">산출세액 : {{ Math.ceil(incomeProps-(incomeProps*0.65)-1490) }} 만원</h2>
    <h2 v-if="15000<incomeProps && incomeProps<=30000">산출세액 : {{ Math.ceil(incomeProps-(incomeProps*0.62)-1940) }} 만원</h2>
    <h2 v-if="30000<incomeProps && incomeProps<=50000">산출세액 : {{ Math.ceil(incomeProps-(incomeProps*0.60)-2540) }} 만원</h2>
    <h2 v-if="50000<incomeProps && incomeProps<=10000">산출세액 : {{ Math.ceil(incomeProps-(incomeProps*0.58)-3540) }} 만원</h2>
    <h2 v-if="100000<incomeProps">산출세액 : {{ Math.ceil(incomeProps-(incomeProps*0.55)-6540) }} 만원</h2> -->
    <h2 v-if="incomeProps >= 0">산출세액 : {{ find(incomeProps) }} 만원</h2>
    <h2 v-if="incomeProps < 0">산출세액 : 0 만원</h2>
    <h2>세액감면 : (-) {{ absProps }} 만원</h2>
    <hr>
    <Finaltax 
    :income-props="resultNumber"
    :abs-props="absProps"/>
  </div>
</template>

<script>
import Finaltax from '@/components/Finaltax'

export default {
  name: 'Taxrate',
  components: {
    Finaltax,
  },
  props: {
    incomeProps: Number,
    absProps: Number,
  },
  data: function () {
    return {
      resultNumber: 0
    }
  },
  methods: {
    find: function (V) {
      var resultNumber = 0
      if (1200>=V && V >= 0) {
        this.resultNumber = Math.ceil(V-(V*0.94))
        return Math.ceil(V-(V*0.94))
      } else if (1200<V && V<=4600) {
        this.resultNumber = Math.ceil(V-(V*0.85)-108)
        return Math.ceil(V-(V*0.85)-108)
      } else if (4600<V && V<=8800) {
        this.resultNumber = Math.ceil(V-(V*0.76)-522)
        return Math.ceil(V-(V*0.76)-522)
      } else if (8800<V && V<=15000) {
        this.resultNumber = Math.ceil(V-(V*0.65)-1490)
        return Math.ceil(V-(V*0.65)-1490)
      } else if (15000<V && V<=30000) {
        this.resultNumber = Math.ceil(V-(V*0.62)-1940)
        return Math.ceil(V-(V*0.62)-1940)
      } else if (30000<V && V<=50000) {
        this.resultNumber = Math.ceil(V-(V*0.60)-2540)
        return Math.ceil(V-(V*0.60)-2540)
      } else if (50000<V && V<=100000) {
        this.resultNumber = Math.ceil(V-(V*0.58)-3540)
        return Math.ceil(V-(V*0.58)-3540)
      } else {
        this.resultNumber = Math.ceil(V-(V*0.55)-6540)
        return Math.ceil(V-(V*0.55)-6540)
      }
    }
  }
}
</script>

<style>

</style>