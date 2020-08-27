import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieListView from '@/views/movies/MovieListView.vue'
import MovieDetailView from '@/views/movies/MovieDetailView.vue'

import ArticleListView from '@/views/articles/ArticleListView.vue'
import ArticleDetailView from '@/views/articles/ArticleDetailView.vue'
import ArticleCreateView from '@/views/articles/ArticleCreateView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'



Vue.use(VueRouter)

  const routes = [
  // movie
  {
    path: '/',
    name: 'MovieListView',
    component: MovieListView,
  },
  {
    path: '/movies/detail',
    name: 'MovieDetailView',
    component: MovieDetailView,
    props(route){
      return { movie_id: route.query.movie_id }
    },
  },
  // article
  {
    path: '/articles',
    name: 'ArticleListView',
    component: ArticleListView,
  },
  {
    path: '/articles/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView,
    props(route){
      return { 
        movie_id: route.query.movie_id,
        article_id: route.query.article_id
      }
    },
    beforeEnter: (to, from, next) => {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/accounts/login')
      } 
      else {
        next()
      }
    },
  },
  {
    path: '/articles/detail',
    name: 'ArticleDetailView',
    component: ArticleDetailView,
    props(route) {
      return { article_id: route.query.article_id }
    },
    beforeEnter: (to, from, next) => {
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/accounts/login')
      } 
      else {
        next()
      }
    },
  },
  // accounts
  {
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView,
  },
  {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView,
    beforeEnter: (to, from, next) => {
      // 1. 토큰 값을 가지고 있는가?
      if (Vue.$cookies.isKey('auth-token')) {
        next('/')
      } 
      else {
        next()
      }
    },
  },
  {
    path: '/accounts/profile',
    name: 'ProfileView',
    component: ProfileView,
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
