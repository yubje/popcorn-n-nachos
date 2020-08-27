<template>
<div>
  <div id="multi-item" class="carousel slide carousel-multi-item mt-3 mb-5" data-ride="carousel" >
    <!--control-->
    <a class="carousel-control-prev" href="#multi-item" data-slide="prev"><i
        class="fas fa-chevron-left"></i></a>
    <a class="carousel-control-next" href="#multi-item" data-slide="next"><i
        class="fas fa-chevron-right"></i></a>

    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#multi-item" data-slide-to="0" class="active"></li>
      <li data-target="#multi-item" data-slide-to="1"></li>
    </ol>

    <div class="carousel-inner" role="listbox">
      <div class="carousel-item active">
        <div class="card-group d-flex">
          <div
            v-for="movie in former" 
            :key="movie.id"
            class="inline"
          >
            <RecommendItemView :movie="movie"/>
          </div>
        </div>
      </div>
    
      <div class="carousel-item">
        <div class="card-group">    
          <div 
            v-for="movie in latter" 
            :key="movie.id"
            class="inline"
          >
            <RecommendItemView :movie="movie"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import RecommendItemView from '@/components/recommend/RecommendItemView.vue'
const SERVER_URL = process.env.SERVER_URL

export default {
  name: 'RecommendView',
  data() {
    return {
      recommendMovies: [],
      former: [],
      latter: [],
    }
  },
  components: {
    RecommendItemView,
  },
  methods: {
    recommend() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }

      axios.get(`${SERVER_URL}/accounts/recommend/`, null, requestHeader)
        .then(response =>{
          this.recommendMovies = response.data
          this.former = response.data.slice(0, 5)
          this.latter = response.data.slice(5, 10)
        })
        .catch(error => console.log(error.data))
    },

  },

  created() {
    this.recommend()
  }

}
</script>

<style scoped>
#recommend {
    position: fixed;
    right:0;
    z-index: 100;
}

#recommend > {
    background-color: rgba(255,255,255,0.5);
}

.inline {
  
  display: inline-block;
  width: 20%;

}


</style>