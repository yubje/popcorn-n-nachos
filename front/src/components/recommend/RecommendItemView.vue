<template>
  <div class="card p-0 border-0 m-0">
    <img :src="backdropUrl" class="card-img-top" :alt="movie.id"> 
    <div class="overlay" @click="gotoMovieDetail">
      <div class="description">
        <p class="title"><b>{{ movie.title }}</b></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecommendItemView',
  props: {
    movie: {
      type: Object,
    }
  },
  computed: {
    backdropUrl() {
      if (this.movie.backdrop_path) {
        return `https://image.tmdb.org/t/p/w780/${this.movie.backdrop_path}`
      } else {
        return "https://picsum.photos/id/1015/780/440"
      }
    },
  },
  methods: {
    gotoMovieDetail() {
      this.$router.push({ name: 'MovieDetailView', query: {movie_id : this.movie.id }})
    },
  },

}
</script>

<style scoped>
.card {
  display: block !important;
  width: 100% !important;
}

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
  display: inline-block;
  height: 100%;
  cursor: pointer;
  
}

.card .overlay .description {
  position: absolute;
  top: 50%;
  left: 50%;
  text-align: center;

}

.card .overlay .description .title {
  position: relative;
  right: 50%;
}

</style>