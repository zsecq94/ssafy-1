<template>
  <div>
    <h2>종합소득금액: {{ incomeProps }} 만원</h2>
    <h2>종합소득공제:  만원</h2>
    <h2>과세표준:  만원</h2>
  </div>
</template>

<script>
export default {
  name: 'Taxrate',
  props: {
    incomeProps: Number,
    absProps: Number,
  },
}
</script>

<style>

</style>