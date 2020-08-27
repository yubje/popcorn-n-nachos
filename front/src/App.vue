<template>
  <div id="app">
    <div id="nav">
      <Navbar
        :isLoggedIn="isLoggedIn"
        @submit-logout-data="logout"
      />
    </div>
    <router-view
      @submit-login-data="login"
      @submit-signup-data="signup"
    />
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from '@/components/Navbar.vue'


const SERVER_URL = process.env.SERVER_URL

export default {
  name: "App",
  data() {
    return {
      isLoggedIn: false,
    }
  },
  components: {
    Navbar,
  },
  methods: {
    // 쿠키설정
    setCookie(key) {
      // key: 'auth-token', value: key
      this.$cookies.set('auth-token', key)
      // 로그인 완료 표시 
      this.isLoggedIn = true
    },
    
    signup(signupData) {
      // 회원가입 정보를 url로 요청
      axios.post(`${SERVER_URL}/rest-auth/signup/`, signupData)
        .then(response => {
          // 1. 키 값 넘겨주기
          this.setCookie(response.data.key)
         // 2. 로그인 끝나면 메인 화면 이동
          this.$router.push('/')
        })
        .catch(error => console.log(error.response.data))
    },

    login(loginData) {
      // 로그인 정보를 url로 요청
      axios.post(`${SERVER_URL}/rest-auth/login/`, loginData)
        .then(response => {
          this.setCookie(response.data.key)
          this.$router.push('/')
        })
        .catch(error => console.log(error.response.data))
    },
    logout() {
      // 'auth-token'의 이름을 가진 key 가져오기
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      // url, body, header
      axios.post(`${SERVER_URL}/rest-auth/logout/`, null, requestHeader)
        .then(() => {
          // 캐시 삭제
          this.$cookies.remove('auth-token')
          // 상태 변경
          this.isLoggedIn = false
          // 목록으로 이동
          this.$router.push('/')
        })
        .catch(error => console.log(error.response.data))
    },
  },
  // 로그인 여부 확인
  mounted() {
    if (this.$cookies.isKey('auth-token')) {
      this.isLoggedIn = true
    } else {
      this.isLoggedIn = false
    }
  },
}

</script>

<style>
#app {
  font-family: Heebo, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffff;
  background-color: #171E29;
  min-height: 100%;
  

}


#nav a {
  font-weight: bold;
  color : #313D4F;
}

#nav a.router-link-exact-active {
  color: #0093EE;
}
</style>
