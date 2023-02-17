<template>
  <div id="app">
    <h1>SSAFY TUBE</h1>
    <div>
      <iframe id="player" type="text/html" width="640" height="360" 
      :src="videoSrc" frameborder="0"></iframe>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  components: {
  },
  data: function () {
    return {
      selectedVideo: ''
    }
  },
  methods: {
    isSelected: function () {
      return Object.keys(this.selectedVideo).length
    }
  },
  computed: {
    videoSrc: function () {
      if (this.isSelected()) {
        return "http://www.youtube.com/embed/" + this.selectedVideo.id.videoId
      }
      return ''
    },
  },
  created: function () {
    axios({
      method: 'get',
      url: 'https://www.googleapis.com/youtube/v3/search',
      params: {
        key: process.env.VUE_APP_YOUTUBE_API_KEY,
        q: '코딩노래',
        part: 'snippet',
        type: 'video'
      }
    })
      .then((res) => {
        this.selectedVideo = res.data.items[0]
        console.log(this.selectedVideo.id.videoId)
      })
      .catch((error) => {console.log(error)})
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
