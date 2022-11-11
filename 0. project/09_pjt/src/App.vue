<template>
  <div id="app">
    <div>
      <nav class="navbar">
        <div class="container-fluid">
          <div>
            <img src="./assets/ssafy-logo.png" alt="..." style="width: 40px; height: 30px;">
          </div>
          <div>
            <router-link :to="{ name: 'movie' }">MOVIE</router-link>
            <router-link :to="{ name: 'random' }">RANDOM</router-link>
            <router-link :to="{ name: 'watch' }">WATCH</router-link>
          </div>
        </div>
      </nav>
    </div>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      movies: [],
    }
  },
  methods:{
    onGetVideo(){
      axios({
        method:'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated?api_key=936dc8401bd304eab508a23e5dc38aa9&language=ko-KR',
        params:{
          api_key:process.env.VUE_APP_TMDP_API_KEY,
          language:"ko",
        }
      })
        .then((res) => {
          this.movies = res.data.results
          this.$store.dispatch('getMovies',this.movies)
          this.movies=[]
        })
        .catch((error) => {console.log(error)})
    }
  },
  created(){
    this.onGetVideo()
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
}
/* #rl1 {
  float: right;
} */
/* nav {
  padding: 30px;
} */

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin: 20px;
}

nav a.router-link-exact-active {
  color: #42b983;
}

/* #divTag {
  float: right;
} */
nav{
  background-color: skyblue;
}
</style>
