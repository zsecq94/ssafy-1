<template>
  <div id="app">
    <SearchBar @onSearchInput='onSearchInput'/>
    <VideoDetail
    v-if="isSelected"
    :video="video" />
    <VideoList :videos="videos"
    @goApp="goApp"
    />
  </div>
</template>

<script>
import axios from 'axios'

import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'
import SearchBar from './components/SearchBar.vue'

export default {
  name: 'App',
  components: {
    VideoList,
    VideoDetail,
    SearchBar,
  },
  data() {
    return {
      searchWord: '',
      videos: [],
      video: null
    }
  },
  methods: {
    onSearchInput(searchInputData) {
      this.searchWord = searchInputData
      axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params: {
          key: process.env.VUE_APP_YOUTUBE_API_KEY,
          q: this.searchWord,
          part: 'snippet',
          type: 'video'
        }
      })
        .then((res) => {
          this.videos = res.data.items
          console.log(this.selectedVideo.id.videoId)
        })
        .catch((error) => {console.log(error)})
    },
    goApp(video) {
      this.video = video
      console.log(video)
    },
    isSelected: function () {
      return Object.keys(this.video).length
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: blue;
  margin-top: 60px;
}
</style>
