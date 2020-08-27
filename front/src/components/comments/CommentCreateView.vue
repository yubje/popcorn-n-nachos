<template>
  <div>
    <div v-if="!this.comment">
      <div class="inputbox d-flex flex-column m-3">
        <input class="textbox" v-model="commentData.content"><br>
        <button 
          @click="createComment"
          class="btn btn-sm d-flex justify-content-end m-1"
          >SUBMIT</button>
      </div>
    </div>

    <div v-else>
      <div class="inputbox d-flex flex-column m-3">
        <textarea class="textbox" v-model="comment.content" value="comment.content"></textarea><br>
        <button 
          @click="updateComment"
          class="btn btn-sm d-flex justify-content-end m-1"
          >SUBMIT</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.SERVER_URL

export default {
  name: 'CommentCreateView',
  data() {
    return {
      commentData :{
        content: null,
        article: this.article_id,
        movie: this.movie_id,
      }
    }
  },
  props: {
    article_id: {
      type: Number,
    },
    movie_id: {
      type: Number,
    },
    comment: {
      type: Object,
    }
  },
  // 로그인 하지 않은 유저가 댓글을 작성하려고 할 때 
  // 로그인 창으로 이동
  created() {
    if (!this.$cookies.isKey('auth-token')) {
      this.$router.push({ name: 'LoginView' })
      }
  },

  methods: {
    createComment() {
      // 토큰 정보 가져오기(?)
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.commentData.movie = this.movie_id
      // url, body, header
      axios.post(`${SERVER_URL}/articles/${this.article_id}/comments_create/`, this.commentData, requestHeader)
        // 글작성 완료했다면 목록으로 이동
        .then(() => this.$router.go())
        .catch(error => console.log(error.response.data))
    },
    updateComment() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.put(`${SERVER_URL}/articles/${this.article_id}/${this.comment.id}/update_delete/`, this.comment, requestHeader)
        // 글작성 완료했다면 목록으로 이동
        .then(() => this.$router.go())
        .catch(error => console.log(error.response.data))

    },
  },
  
}
</script>

<style scoped>
div {
  vertical-align: center;
}

.inputbox {
  border: 1px solid #8EACC5;
  border-radius: 5px;
  height: 100px;
}
.textbox {
  width: 100%;
  padding: 10px;
  border: 0px none;
  box-shadow: none;
  background-color: transparent;
}

.textbox:focus {
  outline: none;
}

</style>