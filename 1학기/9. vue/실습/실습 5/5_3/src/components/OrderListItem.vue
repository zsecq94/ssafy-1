<template>
  <div id="divT">
    <img :src=img alt="" id="img">
    <p id="p1">{{ order.menu.title }}</p>
    <p id="p2">사이즈: {{ order.size.name }}</p>
    <p id="p3">가격: {{ order.size.price + order.menu.price }}원</p>
  </div>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  data() {
    return {
      img: this.order.menu.image
    }
  },
  computed: {
    // totalPrice: function () {
    // },
  },
}
</script>

<style>
#img {
  width : 30px;
  height : 30px;
}
#divT {
  display: flex;
}
</style>