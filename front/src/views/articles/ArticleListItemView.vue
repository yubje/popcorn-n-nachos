<template>
  <tr class="table-row">
    <th scope="row">{{ article.id }}</th>
    <td class="col-movie-item">{{ this.movie.title }}</td>
    <td class="col-title-item">
      <h5>
        <router-link 
          class="text-white text-decoration-none"
          :to="{ name: 'ArticleDetailView', query : { article_id : article.id }}"
        >
          {{ article.title }}
        </router-link>
      </h5>
      <router-view />
    </td>
    <td>{{ article.user.username }}</td>
    <td>{{ article.created_at.substring(0, 10) }}</td>
  </tr>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.SERVER_URL
export default {
  name: 'ArticleListItemView',
  data() {
    return {
      movie: {},
      movie_id: this.article.movie,
    }
  },
  props: {
    article: {
      type: Object,
    },
  },
  methods: {
    fetchMovie() {
      axios.get(`${SERVER_URL}/movies/${this.movie_id}/`)
      .then(response => {
        this.movie = response.data
        })
      .catch(error => console.log(error.response.data))
    },
  },
  created() {
    this.fetchMovie()
  },
}
</script>

<style scoped>
.table-row:hover {
  overflow: hidden;
  background: rgba(142, 172, 197, 0.1);
  text-align: center;
  vertical-align: middle;
}

th {
  vertical-align: middle;
}


td {
  vertical-align: middle;
}

.col-movie-item {
  text-align: left;
}

.col-title-item {
  word-break: break-all !important;
  text-align: left;
}

</style>

