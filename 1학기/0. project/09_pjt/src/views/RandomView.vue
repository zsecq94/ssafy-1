<template>
  <div >
    <button @click="randomNum" type="button" class="btn btn-success" style="width:300px; margin-top: 40px;">PICK</button>
    <div class="d-flex justify-content-center">
      <div id="div123" v-if="num">
        <img :src="imgSrc" alt=""><br>
        <b>{{movies[num].title}}</b>
      </div>
      <div id="div123" v-else-if="num===0">
        <img :src="imgSrc" alt=""><br>
        <b>{{movies[num].title}}</b>
      </div>
    </div>
    
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: 'RandomView',
  data(){
    return{
      movies: this.$store.state.movies,
      num: null
    }
  },
  computed:{
    imgSrc(){
      const homeSrc="https://image.tmdb.org/t/p/w500"
      return homeSrc+this.movies[this.num].poster_path
      }
  },
  methods: {
    randomNum() {
      var a = _.random(0, this.movies.length)
      this.num = a
    }
  }

}
</script>

<style>
#div123 {
  border: 1px solid darkgray;
}
img {
  width: 300px;
  
}
</style>