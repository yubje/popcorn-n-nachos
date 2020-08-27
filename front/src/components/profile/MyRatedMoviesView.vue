<template>
  <div>
    <h4 class="mt-5 mb-3" style="text-align:left;">My Rated Movies</h4>
    <div v-for="myrate in myRates" :key="myrate.id">
      <MyRatedMoviesItem :myrate="myrate"/>
    </div>
  </div>
</template>

<script>
import MyRatedMoviesItem from '@/components/profile/MyRatedMoviesItem.vue'


export default {
  name: 'MyRatedMoviesView',
  data() {
    return {
      myRatedMovies: [],
    }
  },
  props: {
    myRates: {
      type: Array,
    }
  },
  components: {
    MyRatedMoviesItem,
  },
  methods: {
    
  },
}
  
</script>

<style> 
</style>