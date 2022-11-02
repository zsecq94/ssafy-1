<template>
  <div>
    <h2>결정세액 : {{ incomeProps-absProps }} 만원</h2>
  </div>
</template>

<script>
export default {
  name: 'Finaltax',
  props: {
    incomeProps: Number,
    absProps: Number,
  }
}
</script>

<style>

</style>