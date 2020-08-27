<template>
  <div class="container articlebox">
    <!-- id가 아직 없다면 = 후기 생성 -->
    <div v-if="!this.article_id" class="formbox d-flex flex-column">
      <h1>New Post</h1>
      <gb-divider color="blue"></gb-divider>
      <label class="label" for="title"><b>Title</b></label>
      <input v-model="articleData.title" id="title" type="text" placeholder="Title"><br>

      <label class="label"  for="content"><b>Content</b></label>
      <textarea v-model="articleData.content" id="content" cols="30" rows="10" placeholder="Content"></textarea><br>

      <div class="d-flex justify-content-end">
        <gb-button class="button" color="blue" type="submit" @click="createArticle">Submit</gb-button>
      </div>
    </div>
    <!-- id가 존재한다면 = 글 수정 -->
    <div v-else class="formbox">
      <h1>Edit Post</h1>

      <label for="title">title: </label>
      <input v-model="articleData.title" id="title" type="text" value="articleData.title"><br>

      <label for="content">content</label><br>
      <textarea v-model="articleData.content" id="content" value="articleData.content" cols="30" rows="10"></textarea><br>

      <gb-button class="button" color="blue" size="small" type="submit" @click="updateArticle">Submit</gb-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.SERVER_URL

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      articleData :{
        title: null,
        content: null,
        movie: this.movie_id,

      }
    }
  },
  props: {
    movie_id: {
      type: Number,
    },
    article_id: {
      type: Number,
    }
  },
  // 로그인 하지 않은 유저가 글을 작성하려고 할 때 
  // 로그인 창으로 이동
  created() {
    if (!this.$cookies.isKey('auth-token')) {
      this.$router.push({ name: 'LoginView' })
      
      } else {
        this.fetchArticle()
      }
  },

  methods: {
    createArticle() {
      // 토큰 정보 가져오기(?)
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.articleData.movie = this.movie_id
      // url, body, header
      axios.post(`${SERVER_URL}/articles/create/`, this.articleData, requestHeader)
        // 글작성 완료했다면 목록으로 이동
        .then(() => {
          this.$router.push('/articles')
        })
        .catch(error => console.log(error.response.data))
    },

    fetchArticle() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER_URL}/articles/${this.article_id}/`, null, requestHeader)
        .then(response => {
          this.articleData = response.data
          })
        .catch(error => console.log(error.response.data))
    },

    updateArticle() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.put(`${SERVER_URL}/articles/${this.article_id}/update_delete/`, this.articleData, requestHeader)
      .then(() => {
        this.$router.push({name: 'MovieDetailView', query: { movie_id: this.movie_id}})
      })
      .catch(error => console.log(error.response.data))
    },
  },
}
</script>

<style scoped>
.articlebox {
  width: 80%;
  height: 100%;
  margin-top: 5rem;
  padding: 5rem;
  background-color: white;
  color: #171E29;
}

.formbox {
  display: block;
  text-align: left;
}

.label {
  margin-right: 3rem;
}

.formbox > input {
  width: 100%;
  border: 1px solid #A9C7DF;
  height: 40px;
  padding: 0.5rem;
  margin-bottom: 2rem;
}

.formbox > textarea {
  width: 100%;
  border: 1px solid #A9C7DF;
  height: 300px;
  padding: 0.5rem;
  margin-bottom: 2rem;
}

</style>