<template>
  <div>
    <div
      v-for="comment in comments" 
      :key="comment.id"
      class="d-flex flex-column text-dark"
    >
      <div v-if="updateR.id!==comment.id">
        <CommentListItemView
          :comment="comment"
          :article_id="article_id"
          @comment-update="updateRequest"
        />
      </div>
  
      <div v-else>
        <CommentCreateView
          :movie_id="movie_id"
          :article_id="article_id"
          :comment="comment"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentListItemView from '@/components/comments/CommentListItemView.vue'
import CommentCreateView from '@/components/comments/CommentCreateView.vue'

const SERVER_URL = process.env.SERVER_URL

export default {
  name: 'CommentListView',
  data() {
    return {
      comments: [],
      updateR: false,

    }
  },
  components: {
    CommentListItemView,
    CommentCreateView,
  },

  props: {
    article_id: {
      type: Number,
    },
    movie_id: {
      type: Number,
    },
  },

  methods: {
    fetchComments() {
      axios.post(`${SERVER_URL}/articles/${this.article_id}/comments_list/`)
      .then(response => {
        this.comments = response.data
        })
      .catch(error => console.log(error.response.data))
    },
    updateRequest(comment) {
      this.updateR = comment
    }
  },

  // 사용자가 ListView.vue에 접근하자마자 글 목록 불러오는 함수 실행
  created() {
    this.fetchComments()
  },
  mounted() {
    this.fetchComments()
  },
}
</script>

<style scoped>
div {
  background-color: white;
}
</style>