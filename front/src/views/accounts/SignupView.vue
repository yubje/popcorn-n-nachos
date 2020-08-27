<template>
  <div class="signupbox">
    <div class="formbox">
      <div class="forms">
        <h1>Sign Up</h1>
        <!-- .prevent -> 제출 이벤트가 페이지를 다시 로드하지 않습니다. -->
        <form class="form" @submit.prevent="signup">
            <label for="id">ID: </label>
            <input id="id" type="text" placeholder="ID"  v-model="signupData.username"><br>

          <label for="pw1">Password: </label>
          <input id="pw1" type="password" placeholder="Password" v-model="signupData.password1"><br>

          <label for="pw2">Verify Password: </label>
          <input style="margin-bottom: 0 !important;" id="pw2" type="password" placeholder="Password" v-model="signupData.password2"><br>
          <small id="passwordHelpBlock" class="form-text text-muted m-0">
            Your password must be 8-20 characters long, contain letters and numbers, and must not contain spaces, special characters, or emoji.
          </small>

          
          <gb-button class="button" color="blue" size="small" type="submit">Sign Up</gb-button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignupView",
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null,
      }
    }
  },
  methods: {
    signup() {
      // console.log(this.signupData)
      // App.vue로 회원가입 정보를 가지고 submit-signup-data 이벤트를 emit
      this.$emit('submit-signup-data', this.signupData)
    },
  },
}
</script>

<style scoped>
.signupbox {
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
  padding: 2rem 3rem;
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
  margin-bottom: 1.5rem;
}
.form > button {
  width: 100%;
  height: 40px;
  border-radius: 0 !important; 
  padding: 0 !important;
  margin-top: 1.5rem;
}

.form-text {
  display: block;
  text-align: left;
}
</style>