<template>
  <div style="text-align:left;">
    <h2>Personal Info</h2>
    <p>ID: {{ info.id }}</p>
    <p>USERNAME: {{info.username}}</p>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.SERVER_URL

export default {
  name : 'MyInfoView',

  data() {
    return {
      info: {
        id: '',
        username: '',
      }
    }
  },

  methods: {
    getmyInfo() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}/accounts/myinfo/`, requestHeader)
        .then(response => {
          this.info = response.data
          this.$emit('gotPersonalInfo', this.info)
        })
        .catch(error => console.log(error.response.data))
    }
  },

  created() {
    this.getmyInfo()
  },

}
</script>

<style>

</style>