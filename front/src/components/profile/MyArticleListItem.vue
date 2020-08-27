<template>
  <div id="main" :style="{ 'backgroundImage': `url(${this.backdropUrl})`}" >
    <div id="gradient">
      <div class="mb-5">
        <h2 id="articleTitle" @click="gotoArticleDetail">{{ myArticle.title }}</h2>
        <h5>{{ mymovie.title }}</h5>
      </div>
      <div>Post Date: {{ myArticle.created_at.substring(0, 10) }}  |   {{ myArticle.updated_at.substring(0, 10) }}</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.SERVER_URL

export default {
  name: "MyArticleListItem",
  data() {
    return {
      mymovie: {},
    }
  },
  props: {
    myArticle: {
      type: Object,
    }
  },
  methods: {
    getMovie() {
      axios.get(`${SERVER_URL}/movies/${this.myArticle.movie}/`)
        .then(response => {
          this.mymovie = response.data
        })
        .catch(error => console.log(error.response.data))
    },
    gotoArticleDetail() {
      this.$router.push({name: 'ArticleDetailView', query: {article_id: this.myArticle.id}})
    }
  },
  computed: {
    backdropUrl() {
      return `https://image.tmdb.org/t/p/original/${this.mymovie.backdrop_path}`
    },
  },
  created() {
    this.getMovie()
  }
}
</script>

<style scoped>

#main{
  background-size: 100%;
  background-position: center;

}

#gradient{
  background: linear-gradient(to right, rgba(0,0,0,1) 30%, rgba(0,0,0,0));
  margin: 2rem auto;
  padding: 3rem ;
  word-break: break-all !important;
  text-align: left;
}

h5 {
  color: #313D4F;
}

h2{
  margin-bottom: 1rem auto;
}

h2:hover{
  cursor:pointer;
  text-decoration-line: underline;
}

</style>