<template>
  <div>
    <GenreListView
    @genre-select="onGenreSelect"
    />
    <RecommendView/>
    <div class="container">
      <div class="row">  
        <MovieListItem  v-for="movie in movies" :key="movie.id" :movie="movie"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from './MovieListItem.vue'
import GenreListView from '@/components/GenreListView.vue'
import RecommendView from '@/components/recommend/RecommendView.vue'

const SERVER_URL = process.env.SERVER_URL

export default {
  name: "MovieList",
  components: {
    MovieListItem,
    GenreListView,
    RecommendView,
  },
  data() {
    return {
      movies: [],
      genre: null,
    }
  },
  methods: {
    fetchMovies(genre) {
      if (genre) {
        axios.get(`${SERVER_URL}/movies/?genre=${genre.id}`)
        .then(response => {
          this.movies = response.data
          })
        .catch(error => console.log(error.response.data))
      } else {
        axios.get(`${SERVER_URL}/movies/`)
        .then(response => {
          this.movies = response.data
          })
        .catch(error => console.log(error.response.data))
      }
    },
    onGenreSelect(genre) {
      this.genre = genre
      this.fetchMovies(genre)
    },
    
  },
  created() {
    this.fetchMovies(null)
  },
}
</script>

<style scoped>

</style>