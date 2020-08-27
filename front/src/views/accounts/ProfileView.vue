<template>
  <div class="container mt-5">
    <MyInfoView @gotPersonalInfo="gotPersonalInfo" />
    <gb-divider color="grey"></gb-divider>
    <MyRatedGenresView :personalInfo="personalInfo" />
  </div>
</template>

<script>

import MyInfoView from '@/components/profile/MyInfoView.vue'
import MyRatedGenresView from '@/components/profile/MyRatedGenresView.vue'

export default {
  name: 'ProfileView',
  data() {
    return {
      personalInfo: {},
    }
  },
  components: {
    MyInfoView,
    MyRatedGenresView,

  },
  methods: {
    gotPersonalInfo(info) {
      this.personalInfo = info
    }
  },
  
}
</script>

<style>

</style>