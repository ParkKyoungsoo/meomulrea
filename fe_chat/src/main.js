import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import * as firebase from 'firebase'
import router from './router'
import { store } from './store'
import AlertComponent from './components/Shared/Alert.vue'

Vue.config.productionTip = false
Vue.component('app-alert', AlertComponent)

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App),
  created () {
    firebase.initializeApp({
      apiKey: "AIzaSyBLLbDAcF_E4SIDDtT6sGd_BNHLtiudxZc",
      authDomain: "babygoat-aeb58.firebaseapp.com",
      databaseURL: "https://babygoat-aeb58.firebaseio.com",
      projectId: "babygoat-aeb58",
      storageBucket: "babygoat-aeb58.appspot.com",
      messagingSenderId: "320378947501",
      appId: "1:320378947501:web:9f4dddf54f047b380c4324",
      measurementId: "G-CYPY4K6VGB"
    })
  }
}).$mount('#app')
