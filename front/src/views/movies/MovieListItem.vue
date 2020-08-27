<template>
  <div class="col-12 col-sm-6 col-md-3 my-3">
    <div id="postercard" @click="gotoMovieDetail" class="card h-100 border-0 rounded-0 shadow-lg " style="margin-bottom: 10px;">
      <img :src="posterUrl" class="card-img-top border-0 rounded-0">
      <div class="card-body d-flex flex-column justify-content-between">
        <div class="d-flex justify-content-between">
          <h6 class="card-title">{{ movie.title }}</h6>
          <div style="margin-left: 10px;">
            <gb-badge color='orange' :filled="true">
              <b>
                {{ movie.vote_average }}
              </b>
            </gb-badge>
          </div>
        </div>
        <div class="card-text">
          <span class="text-muted" v-for="genre in genreObjects" :key="genre.id">
            <small>{{ genre.name }} </small>
          </span>
        </div>
      </div>

      <!-- overlay Rate -->
      <div class="overlay" style="text-align:center;">
        <div class="stardiv">
        <star-rating 
          border-color="#FFC02A"
          v-model="rating"
          :inline="true"
          :read-only="true"
          active-color="#FFC02A"
          :star-size="30"
          :show-rating="false"
        ></star-rating>
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
  name: "MovieListItem",
  data() {
    return {
      genreObjects: {},
      myRate : 0,
      rating: this.myRate,
    }
  },
  props: {
    movie: {
      type: Object
    },
    
  },
  components: {
    StarRating
  },
  methods: {
    getGenres() {
      axios.get(`${SERVER_URL}/movies/${this.movie.id}/get_genres/`)
        .then(response => {
          this.genreObjects = response.data
        })
        .catch(error => console.log(error))
    },
    gotoMovieDetail() {
      this.$router.push({ name: 'MovieDetailView', query: {movie_id : this.movie.id }})
    },
    getRate() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}/movies/${this.movie.id}/rate_info/`, null, requestHeader)
        .then(response => {
          if (!response.data.rate) {
            
            this.myRate = 0
          } else {
            this.myRate = response.data.rate
            this.rating = response.data.rate
          }
          })
        .catch(error => console.log(error))
    },
    Rate() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.rateData.rate = this.rating
      axios.post(`${SERVER_URL}/movies/${this.movie_id}/rate/${this.myRate}/`, this.rateData, requestHeader)
        .then(() => {})
        .catch(error => console.log(error.response.data))
    }
  },
  computed: {
    posterUrl() {
      return `https://image.tmdb.org/t/p/w780/${this.movie.poster_path}`
    },
  },
  created() {
    if (this.$cookies.isKey('auth-token')) {
      this.getRate()
    }
    this.getGenres()
  }
}
</script>

<style scoped>
.card .overlay{
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  overflow: hidden;
  width: 100%;
  height: 0;
  color: #fff;
  background: rgba(0, 0, 0, 0.6);
  text-align: center;
  
}

.card:hover .overlay{
  display: block;
  height: 100%;
  vertical-align: middle;
}

.card-body {
  background-color: black;
}


.card-title {
  text-align: left;
}

.card-text {
  text-align: left;
}

.stardiv {
  position:absolute; 
  top: 50%; 
  left:50%; 
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);        
}

#postercard:hover{
  cursor: pointer;
}
</style>