<template>
  <div>
    <div class="card" style="width: 18rem; margin-top: 10px;">
      <img :src="imgSrc" class="card-img-top align-self-center" alt="..." style=" height: 300px; ">
      <div class="card-body">
        <b>{{movie.title}} </b>
        <p>{{a}}</p>
      </div>
    </div>   
  </div>
</template>

<script>
import _ from 'lodash'

export default {
name:'MovieCard',
data(){
  return {
    a: ''
  }
},
props:{
  movie:Object
},
computed:{
  imgSrc(){
    const homeSrc="https://image.tmdb.org/t/p/w500"
    return homeSrc+this.movie.poster_path
  }
},
methods: {
  truncate() {
    const a = _.truncate(this.movie.overview, {
      'length': 50,
      'omission':'...'
    })
    this.a = a
  }
},
created(){
  this.truncate()
}
}
</script>

<style>

</style>