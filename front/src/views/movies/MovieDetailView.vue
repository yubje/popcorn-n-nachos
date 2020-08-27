<template>
  <div>
    <div id="header" :style="{ 'backgroundImage': `url(${this.backdropUrl})`}">
      <div id="movieDescript" class="row" >
        <div id="movieinfo" class="container">
          <div class="d-flex flex-row" >
            <img :src="posterUrl" class="poster card-img-top d-inline mx-3" style="width:300px;">
            <div id="inner" class="m-3 d-inline py-2 d-flex flex-column" style="flex:1;">
              <div>
              <h1 class="d-inline mr-3">{{ movie.title }}</h1> <gb-heading tag="h3" class="d-inline">({{ movie.original_title }})</gb-heading>
              </div>
              <gb-divider color="grey" class="mt-1 mb-3"></gb-divider>
              <div id="under" class="my-3 d-flex flex-column justify-content-between" style="flex:1;">
                <div>Genre :
                  <span v-for="genre in this.genres" :key="genre.name"> {{ genre.name }} </span>  
                </div>
                <div>Release Date : {{ movie.release_date }}</div>
                <div>Popularity : {{ movie.popularity }}</div>
                <div>Votes : {{ movie.vote_count }} Votes, Average : {{ movie.vote_average }}</div>
                <div>Language : {{ movie.original_language }}</div>
                <div v-if="movie.adult">R-rated</div>
                <div class="d-flex justify-content-between">
                  <RateView :movie_id="movie_id" />
                    <router-link :to="{ name: 'ArticleCreateView', query: {movie_id : movie.id} }">
                    <gb-button color="orange">New Post</gb-button>
                  </router-link>
                  <router-view/>
                </div>
              </div>
            </div>
          </div>

          <div class="container p-3 mt-3" style="text-align:left">
            <p>{{ movie.overview }}</p>
          </div>
        </div>
      </div>
    </div>
    <div id="reviewList" class="container" style="">
      <ArticleListView :movie_id="movie_id"/>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import ArticleListView from '@/views/articles/ArticleListView.vue'
import RateView from '@/components/RateView.vue'

const SERVER_URL = process.env.SERVER_URL

export default {
  name: 'MovieDetailView',
  components: {
    ArticleListView,
    RateView,
  },
  data() {
    return {
      movie: {},
      genres: [],
      backdropUrl: '',
    }
  },
  props: {
    movie_id: {
      type: Number,
    },
  },
  methods: {
    fetchMovie() {
      axios.get(`${SERVER_URL}/movies/${this.movie_id}/`)
      .then(response => {

        this.movie = response.data
        this.getbackDropUrl()
        })
      .catch(error => console.log(error.response.data))
    },
    changeGenre() {
      axios.get(`${SERVER_URL}/movies/${this.movie_id}/genre/`)
      .then(response => {
        this.genres = response.data
      })
      .catch(error=> console.log(error.response.data))
    },
    getbackDropUrl() {
      this.backdropUrl = `https://image.tmdb.org/t/p/original/${this.movie.backdrop_path}`
    },
    
  },
  computed: {
    posterUrl() {
      return `https://image.tmdb.org/t/p/w780/${this.movie.poster_path}`
    },
    // backdropUrl() {
    //   return `https://image.tmdb.org/t/p/original/${this.movie.backdrop_path}`
    // },
  },
  created() {
    this.fetchMovie()
    this.changeGenre()

    

  },
}
</script>

<style scoped>
#header {
  background-size: 100%;
}

#movieDescript {
  background-color: rgba(0,0,0,0.8);
  /* margin-top: 5em;
  margin-bottom: 5em; */
}

#movieinfo {
  /* background-color: rgba(0,0,0,0.5); */
  margin-top: 5em;
  margin-bottom: 5em;
}

#inner {
  text-align: left;
}


</style>