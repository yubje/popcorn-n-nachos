<template>
  <div class="container mt-5">
    <div v-if="this.articles.length" class="article-box">
      <h1>Reviews</h1>
      <table class="table table-dark mt-5">
        <thead>
            <tr>
              <th scope="col" class="col-id">#</th>
              <th scope="col" class="col-movie">Movie</th>
              <th scope="col" class="col-title">Title</th>
              <th scope="col" class="col-user">Posted by</th>
              <th scope="col" class="col-date">Created at</th>
            </tr>
        </thead>
        <tbody
          v-for="article in articles" 
          :key="article.id"
          class="tbody"
        >
          <ArticleListItemView
            :article="article"
          />
        </tbody>
      </table>
    </div>
    <div v-else>
      <h5>No Reviews Yet</h5>
      <p>Be the first to write a review for this movie!</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleListItemView from '@/views/articles/ArticleListItemView.vue'
const SERVER_URL = process.env.SERVER_URL

export default {
  name: 'ArticleListView',
  data() {
    return {
      articles: [],
    }
  },
  components: {
    ArticleListItemView
  },
  props: {
    movie_id: {
      type: Number,
    },
  },
  methods: {
    fetchAllArticles() {
      axios.get(`${SERVER_URL}/articles/`)
      .then(response => this.articles = response.data)
      .catch(error => console.log(error.response.data))
    },
    fetchArticles() {
      axios.get(`${SERVER_URL}/articles/bymovie/${this.movie_id}/`)
        .then(response => {
          this.articles = response.data})
        .catch(error => console.log(error.response.data))
    },
  },

  // 사용자가 ListView.vue에 접근하자마자 글 목록 불러오는 함수 실행
  created() {
    if (!this.movie_id) {
      this.fetchAllArticles()
    } else {
      this.fetchArticles()
    }
  },
}
</script>

<style>


.article-box {
  padding: 5rem;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.2);
}

table {
  width: 100%;

}

th {
  color: #8EACC5 !important;
}
.table-dark {
  background-color: transparent !important;
}

.col-title {
  width: 45%;
}

.col-id{
 width: 3%;

}

.col-movie {
  width: 26%;

}

.col-user {
  width: 12%;

}

.col-date {
  width: 17%;

}
</style>

