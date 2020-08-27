import Vue from 'vue'
import App from './App.vue'
import router from './router'
// vue-cookeis
import VueCookies from 'vue-cookies'
// vue dark mode
import VueDarkMode from "@growthbunker/vuedarkmode"
// vue-paginate
// import Paginate from 'vuejs-paginate' 

Vue.use(VueCookies)
Vue.use(VueDarkMode)
// Vue.component('paginate', Paginate)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
