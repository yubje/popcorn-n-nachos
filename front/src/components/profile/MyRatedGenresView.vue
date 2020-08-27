<template>
  <div>
    <h2 class="mb-5" style="text-align:left;">My Top 3 Genre Preferences</h2>
    
    <div v-for="(percent, genre_name) in myGenres" :key="genre_name">
      <gb-progress-bar :progress=percent :details=percent :title=genre_name class="mb-5">
      </gb-progress-bar>
    </div>
    <gb-divider color="grey"></gb-divider>
    <div class="d-flex row">
      <div class="col-6">
        <div class="col-2"></div>
        <gb-button color="orange" :full-width="true" @click="changeMovieStatus" style="height: 80px;">My Rated Movies</gb-button>
        <div class="col-2"></div>
      </div>
      <div class="col-6">
        <div class="col-2"></div>
        <gb-button color="blue" :full-width="true" @click="changeReviewStatus(); getArticles();" style="height: 80px;">My Written Reviews</gb-button>
        <div class="col-2"></div>
      </div>
    </div>
    <MyRatedMoviesView v-show="showRatedMovies" :myRates="myRates" />
    <MyArticleListView v-show="showWrittenReviews" :myArticles="myArticles" />
  
  </div>
</template>

<script>
import axios from 'axios'
import MyRatedMoviesView from '@/components/profile/MyRatedMoviesView.vue'
import MyArticleListView from '@/components/profile/MyArticleListView.vue'

const SERVER_URL = process.env.SERVER_URL

export default {
  name: 'MyRatedGenresView',

  data() {
    return {
      myRates: {},
      myGenres: {},
      myArticles: [],
      showRatedMovies: false,
      showWrittenReviews: false,
    }
  },
  props: {
    personalInfo: {
      type: Object,
    }
  },

  components: {
    MyRatedMoviesView,
    MyArticleListView,
  },

  methods: {
    getRates() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}/accounts/get_rates/`, requestHeader)
        .then(response => {
          this.myRates = response.data
          this.computeGenres()
        })
        .catch(error => console.log(error.response.data))
    },
    computeGenres() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}/accounts/compute_genres/`, this.myRates, requestHeader)
        .then(response => {
          this.myGenres = response.data
        })
        .catch(error => console.log(error.response.data))
    },
    getArticles() {
      axios.get(`${SERVER_URL}/articles/byuser/${this.personalInfo.id}/`)
        .then(response => {
          this.myArticles = response.data
        })
        .catch(error => console.log(error.response.data))
    },
    changeMovieStatus() {
      this.showRatedMovies = true
      this.showWrittenReviews = false
    },
    changeReviewStatus() {
      this.showRatedMovies = false
      this.showWrittenReviews = true
    }
    
  },
  created() {
    this.getRates()
  },
 
}
</script>

<style>

</style>