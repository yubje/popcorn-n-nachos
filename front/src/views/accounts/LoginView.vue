<template>
  <div class="loginbox">
    <div class="formbox">
      <div class="forms">
        <h1 class="mt-4">Login</h1>
        <form class="form" @submit.prevent="login">
          <label for="id">ID: </label>
          <input id="id" type="text" placeholder="ID" v-model="loginData.username"><br>

          <label for="pw">Password: </label>
          <input id="pw" type="password" placeholder="Password" v-model="loginData.password"><br>
          
          <gb-button class="button" color="blue" size="small" type="submit">Login</gb-button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'LoginView',
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login() {
      // 로그인 정보를 가지고 App.vue에 submit-login-data 이벤트 emit
      this.$emit('submit-login-data', this.loginData)
    }
  },
}
</script>

<style scoped>
.loginbox {
  position: absolute;
  top: 25%;
  left: 50%;
}

.formbox {
  position: relative;
  right: 50%;
  bottom: 50%;
  width: 500px;
  height: 500px;
  padding: 3rem;
  background-color: white;
  color: #171E29;
}


.form > label {
  display: block;
  text-align: left;
  margin-bottom: 0.5rem;
}
.form {
  vertical-align: middle;
}
.form > input {
  width: 100%;
  border: 1px solid #A9C7DF;
  height: 40px;
  padding: 0.5rem;
  margin-bottom: 2rem;
}
.form > button {
  width: 100%;
  height: 40px;
  border-radius: 0 !important; 
  padding: 0 !important;
  margin-top: 1.5rem;
}
</style>