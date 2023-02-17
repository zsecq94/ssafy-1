<template>
  <div>
    <p>연봉 입력 (만원): 
      <input 
        type="number"
        v-model.number="incomeMoney"
      ></p>
    <p>세액감면액 (만원):
      <input 
        type="number"
        v-model.number="asdMoney"
      ></p>
    <hr>
    <h2>종합소득금액: {{ incomeMoney }} 만원</h2>
    <h2>종합소득공제: (-) 150 만원</h2>
    <h2 v-if="incomeMoney-150 > 0">과세표준: {{incomeMoney - 150}} 만원</h2>
    <h2 v-if="incomeMoney-150 <= 0">과세표준: 만원</h2>
    <hr>
    <Taxrate 
    :income-props="incomeMoney-150"
    :abs-props="asdMoney"/>
  </div>
</template>

<script>
import Taxrate from '@/components/Taxrate'

export default {
  name: 'Income',
  components: {
    Taxrate,
  },
  data: function () {
    return {
      incomeMoney: null,
      asdMoney: null,
    }
  },
}
</script>

<style>

</style>