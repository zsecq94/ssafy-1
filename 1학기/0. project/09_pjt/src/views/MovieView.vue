<template>
  <div>
    <div class="container">
      <div class="row">
          <MovieCard 
          class="col-3"
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
          />
      </div>
    </div>

  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue';

export default {
  name: 'MovieView',
  
  components:{
    MovieCard,
  },
  computed:{
    movies(){
      return this.$store.state.movies
    }
  }
}
</script>

<style>

</style>
