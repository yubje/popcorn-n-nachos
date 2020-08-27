<template>
  <div class="my-3">
    <nav class="navbar navbar-expand-lg m-auto row justify-content-between w-100">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav m-auto">
          <li class="nav-link active col genrelist"
            @click="onGenreSelect(null)"
          >All</li>
          <div v-for="genre in genres" :key="genre.id">
            <li class="category nav-link list-unstyled text-decoration-none col genrelist"
            @click="onGenreSelect(genre)"
            >{{ genre.name }}
            </li>
          </div>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.SERVER_URL

export default {
  name: 'GenreListView',
  data() {
    return {
      genres: {},
    }
  },
  methods: {
    getGenres() {
      axios.get(`${SERVER_URL}/movies/genre_list/`)
        .then(response => {
          this.genres = response.data
        })
        .catch(error => console.log(error.data))
    },
    onGenreSelect(genre) {
      this.$emit('genre-select', genre)
    },
    
  },
  created() {
    this.getGenres()
  },
}
</script>

<style>

.navbar {
  background-color: #171E29;
}
/* li:hover {
  cursor: !point;
} */

.genrelist {
  color: #A9C7DF;
}

.genrelist:hover { 
  text-decoration-line: underline !important;
}

li:hover{
  cursor:pointer;
}

</style>     