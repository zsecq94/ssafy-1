<template>
  <div id="div1" @click="goApp">
    <img :src="thumbnails" alt="">
    {{ video.snippet.title }}
    <!-- {{video}} -->
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: Object,
    thumbnails: String,
  },
  methods: {
    goApp() {
      this.$emit('goApp', this.video)
    }
  }
}
</script>

<style>
#div1 {
  display: flex;
}
</style>