<template>
  <div id="ratings"> 
    <star-rating 
      v-model="rating"
      :inline="true"
      @rating-selected="Rate()"
      :show-rating='false'
      active-color="#FFB610"
      boder-color="#FFB610"
      :star-size="40"
    ></star-rating>
    <i class="far fa-times-circle fa-2x text-danger" v-on:click.self="deleteRate"></i>
  </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'
const SERVER_URL = process.env.SERVER_URL

export default {
  name: 'RateView',
  data(){
    return {
      rateData: {
        movie: this.movie_id,
        rate: this.rating,
      },
      ori_rate: 0,
      rating: this.ori_rate,

    }
  },
  props: {
    movie_id: {
      type: Number,
    },
  },
  components: {
    StarRating
  },
  methods: {
    Rate() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.rateData.rate = this.rating
      axios.post(`${process.env.SERVER_URL}/movies/${this.movie_id}/rate/${this.ori_rate}/`, this.rateData, requestHeader)
        .then(response =>
          console.log(response.data)
        )
        .catch(error => console.log(error.response.data))
    },
    fetchRate() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}/movies/${this.movie_id}/rate_info/`, null, requestHeader)
      .then(response => {
        if (!response.data.rate) {
          this.ori_rate = 0
        } else {
          this.ori_rate = response.data.rate
          this.rating = response.data.rate
        }
        })
      .catch(err => {console.log(err)})
    },
    deleteRate() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      
      axios.delete(`${SERVER_URL}/movies/${this.movie_id}/rate_delete/`, requestHeader)
      .then(response => {
        console.log(response)
        this.$router.push({ name: 'MovieDetailView', query: {movie_id : this.movie_id }})
      })
      .catch(error => console.log(error.response.data))
    },
    // rateStar(star) {
    //   if (typeof star === 'number' && star <= this.maxStars && star >= 0) {
    //     this.stars = this.stars === star ? star - 1 : star
    //   }
    // }

  },
  created() {
    this.fetchRate()
  }
}
</script>

<style scoped>
div > i {
  display: inline-flex;
  vertical-align: bottom;
  margin-left: 10px;
}

</style>