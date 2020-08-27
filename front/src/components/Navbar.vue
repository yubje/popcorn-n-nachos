<template>
<div>
  <nav class="navbar navbar-expand-lg sticky-top">
    <a class="navbar-brand text-white">
      <router-link class="text-white text-decoration-none" :to="{ name: 'MovieListView' }">POPCORN & NACHOS</router-link>
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item navitem" >
          <router-link class="nav-link text-decoration-none" :to="{ name: 'MovieListView' }">Movies</router-link>
        </li>

        <li class="nav-item navitem" >
          <router-link class="nav-link text-decoration-none" :to="{ name: 'ArticleListView' }">Reviews</router-link>
        </li>

        <li class="nav-item navitem" >
          <router-link class="nav-link text-decoration-none" v-if="!isLoggedIn" to="/accounts/login">Login</router-link> 
        </li>

        <li class="nav-item" >
          <router-link class="nav-link text-decoration-none" v-if="!isLoggedIn" to="/accounts/signup">Sign Up</router-link>
        </li>

        <li class="nav-item" >
          <router-link class="nav-link text-decoration-none" v-if="isLoggedIn" to="/accounts/logout" @click.native="logout">Logout</router-link>
        </li>

        <li class="nav-item" >
          <router-link class="nav-link text-decoration-none" v-if="isLoggedIn" :to="{ name: 'ProfileView' }">Profile</router-link>
        </li>
      </ul>
    </div>
  </nav>
  <gb-divider color="black" margin="0" class="mb-0"></gb-divider>
</div>
</template>

<script>

export default {
  name: 'Navbar',
  props: {
    isLoggedIn: {
      type: Boolean,
    }
  },
 
  methods: {
    logout() {
      this.$emit('submit-logout-data')
    },
  },
}


</script>

<style scoped>
.navbar {
  background-color: #171E29;
  min-height: 80px;
}


#nav a:hover{
  color : #313D4F;
}

#nav a:hover{
  color: #222C3C;
}


#watflix {
  padding-left: 30px;
  padding-right: 40px;
  font-size: 30px;
  
}

</style>