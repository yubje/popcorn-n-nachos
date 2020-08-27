<template>
  <div>
    <div class="navbar navbar-expand-lg navbar-light justify-content-between p-0">
      <b>{{ comment.user.username }}</b>
      <ul class="navbar-nav ml-auto">
        <li class="nav-item dropdown">
          <a class="nav-link" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <i class="fas fa-ellipsis-v"></i>
          </a>
          <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
            <button
              class="dropdown-item"
              @click="onUpdateSelect()"
            >update</button>
            <button
              class="dropdown-item"
              @click="deleteComment()"
            >delete</button>
          </div>
        </li>
      </ul>
    </div>
    <div>
      <p class="px-3 text-left">{{ comment.content }}</p>
      <p class="px-3 text-left">created at: {{ comment.created_at.slice(0, 10) }}  |  upated at: {{ comment.updated_at.slice(0, 10) }}</p>
    </div>
    <gb-divider color="orange" class="my-1"></gb-divider>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.SERVER_URL

export default {
  name: 'CommentListItemView',
  props: {
    comment: {
      type: Object,
    },
    article_id: {
      type: Number,
    }
  },

  methods: {
    deleteComment() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.delete(`${SERVER_URL}/articles/${this.article_id}/${this.comment.id}/update_delete/`,  requestHeader)
      .then(() => {
        this.$router.go()
      })
      .catch(error => console.log(error.response.data))
    },
    onUpdateSelect() {
      this.$emit('comment-update', this.comment)
    },
  },

}
</script>

<style scoped>
div {
  background-color: white;
}
</style>