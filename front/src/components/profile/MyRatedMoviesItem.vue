<template>
  <div>
    <div class="card mb-3 border border-0 rounded-0 d-flex" style="width:100%; background-color:black;">
      <div class="row no-gutters">
        <div class="col-2">
          <img :src="posterUrl" class="card-img rounded-0" >
        </div>
        <div class="card-body d-flex flex-column justify-content-between">
          <div>
            <div class="d-flex justify-content-between">
              <h2 id="movieTitle" class="card-title" @click="gotoMovieDetail">
                {{ mymovie.title }}
              </h2>
              <div class="stardiv">
                <star-rating 
                  border-color="#FFC02A"
                  v-model="myrate.rate"
                  :inline="true"
                  :read-only="true"
                  active-color="#FFC02A"
                  :star-size="30"
                  :show-rating="false"
                ></star-rating>
              </div>
            </div>
            <h4 style="text-align:left;">{{ mymovie.original_title }}</h4>
          </div>
          <div class="card-text text-muted" style="text-align:left;">
            {{ mymovie.release_date }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'
const SERVER_URL = process.env.SERVER_URL

export default {
  name: "MyRatedMoviesItem",
  data(){
    return {
      mymovie: {},
    }
  },
  props: {
    myrate: {
      type: Object,
    }
  },
  components: {
    StarRating
  },
  methods: {
    getMovie() {
      axios.get(`${SERVER_URL}/movies/${this.myrate.movie}/`)
        .then(response => {
          this.mymovie = response.data
        })
        .catch(error => console.log(error.response.data))
    },
    gotoMovieDetail() {
      this.$router.push({ name: 'MovieDetailView', query: {movie_id : this.mymovie.id }})
    },
  },
  created() {
    this.getMovie()
  },
  computed: {
    posterUrl() {
      return `https://image.tmdb.org/t/p/w780/${this.mymovie.poster_path}`
    },
  }

}
</script>

<style>
#movieTitle:hover {
  cursor: pointer;
  text-decoration-line: underline;
}
</style>