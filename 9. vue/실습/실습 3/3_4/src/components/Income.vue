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
    <Taxrate :income-props="incomeMoney"
    :abs-props="asdMoney"/>
    <hr>
    <Taxrate/>
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