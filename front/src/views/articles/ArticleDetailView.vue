<template>
<div class="container mt-5">
  <div class="d-flex flex-column justify-content-between mb-5">
    <div class="poster-background" :style="{ 'backgroundImage': `url(${this.backdropUrl})`}" >
      <div class="gradient d-flex flex-column justify-content-between">
        <div class="d-flex">
          <div class="text-div col-8 text-left">
            <h2 class="text mb-0">{{ article.title }}</h2><br>
            <p class="my-0">{{ movie_title }}</p>
          </div>
          <div class="text-div col-4 d-flex justify-content-end align-items-start">
            <router-link :to="{name : 'ArticleCreateView', query : { article_id : this.article_id, movie_id: this.article.movie }}">
              <gb-button
                color="black"
                class="m-1"
              >edit</gb-button>
            </router-link>
            <router-view />
            <gb-button
                color="black"
                class="m-1"
                @click="deleteArticle"
              >delete</gb-button>
            <!-- </div> -->
          </div>
        </div>
        <div class="d-flex text-div mt-3">
          <p class="m-1">Posted by <b>{{ article.user.username }}</b></p>
          <p class="m-1"> |  created at: {{ article.created_at.substring(0, 10) }}</p>
          <p class="m-1"> |  updated at: {{ article.updated_at.substring(0, 10) }}</p>
        </div>
      </div>
    </div>
    <div class="articlebox">
      <div class="contents text-left">
        <a>{{ article.content }}</a>
      </div>
      <gb-divider color="blue" class="my-2"></gb-divider>
      <div>
        <CommentCreateView 
          :article_id="article_id"
          :movie_id="article.movie"
        />
        <CommentListView
          :article_id="article_id"
          :movie_id="this.article.movie"
        />
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import CommentCreateView from '@/components/comments/CommentCreateView.vue'
import CommentListView from '@/components/comments/CommentListView.vue'
const SERVER_URL = process.env.SERVER_URL

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      article: {},
      movie_title: '',
      backdrop_path: '',
    }
  },
  components: {
    CommentCreateView,
    CommentListView,
  },  
  props: {
    article_id: {
      type: Number,
    },
  },
  methods: {
    fetchArticle() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}/articles/${this.article_id}/`, null, requestHeader)
        .then(response => {
          this.article = response.data
          this.fetchMovie()
          })
        .catch(error => console.log(error.response.data))
    },

    fetchMovie() {
      axios.get(`${SERVER_URL}/movies/${this.article.movie}/`)
      .then(response => {
        this.movie_title = response.data.title
        this.backdrop_path = response.data.backdrop_path
        })
      .catch(error => console.log(error.response.data))
    },
    
    deleteArticle() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.delete(`${SERVER_URL}/articles/${this.article_id}/update_delete/`, requestHeader)
      .then(()=> {
        this.$router.push({ name: 'MovieDetailView', query: {movie_id : this.article.movie }})
      })
      .catch(error => console.log(error.response.data))
    },
  },
  computed: {
    backdropUrl() {
      return `https://image.tmdb.org/t/p/original/${this.backdrop_path}`
    }
  },
  
  created() {
    this.fetchArticle()
  }

}
</script>
<style scoped>

.poster-background {
  min-height: 200px;
  background-size: 100%;
  background-position: center;
  margin: 0;
  padding: 0;

}

.gradient{
  min-height: 200px;
  background: linear-gradient(to top, rgba(0,0,0,1) 30%, rgba(0,0,0,0));
  /* margin: 2rem auto; */
  word-break: break-all !important;
  text-align: left;
}

.article-header{
  display: inline-block;
}

.articlebox {
  height: 100%;
  padding: 5rem;
  background-color: white !important;
  color: #171E29 !important;
  
}

.text-left {
  word-break: break-all !important;
}

.text-div {
  padding: 2rem;
}

.contents {
  padding: 3rem .5rem 5rem .5rem;
}
</style>

