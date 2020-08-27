<template>
  <div>
    <h4 class="mt-5 mb-3" style="text-align:right;">My Written Reviews</h4>
    <div v-for="myArticle in myArticles" :key="myArticle.id">
      <MyArticleListItem :myArticle="myArticle" />
    </div>
  </div>
</template>

<script>
import MyArticleListItem from '@/components/profile/MyArticleListItem.vue'

export default {
  name: "MyArticleListView",
  props: {
    myArticles: {
      type: Array,
    }
  },
  components: {
    MyArticleListItem
  },
}
</script>

<style>

</style>