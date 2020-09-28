<template>
  <v-app-bar app style="box-shadow:none;">
    <v-toolbar-title>
      <router-link style="text-decoration: none; color: rgb(233,105,30);" to="/home">
        Home
      </router-link>
    </v-toolbar-title>
    <v-spacer />
    <v-toolbar-title>
      <v-col>
        <v-select 
          v-model="seletedAddress"
          @change="changeAddress"
          :items="userAddress"
          return-object
          style="margin:10px; margin-top:25px; width:250px;"
          color="rgb(233,105,30)"
          item-color="none"
        />
      </v-col>
    </v-toolbar-title>
    <button @click="showAddrModal = true">추가하기</button>
    <v-spacer />
    <v-toolbar-title>
      <div v-if="$cookies.get('auth-token')===null || $cookies.get('auth-token')===''">
        <button @click="login()">login</button>
      </div>
      <div v-else>
        <button @click="logout()">logout</button>
      </div>
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
import user from "../assets/datas/user.json";
import { mapMutations } from "vuex";
import { EventBus } from "../utils/EventBus.js";
import * as firebase from 'firebase';

export default {
  data(){
    return{
    userAddress: user[0].nm_address,
    showAddrModal: false,
    seletedAddress: "",
    }
  },
  components: {},
  computed: {
    options: () => user[0].nm_address,
  },
  methods: {
    ...mapMutations(("location", ["setLocation"])),
    changeAddress: function() {
      EventBus.$emit("addressChange", this.seletedAddress);
      this.$store.commit("location/setLocation", {
        lat: this.lat,
        lng: this.lng,
      });
    },
    logout(){
      firebase.auth().signOut().then(()=>{
        this.$cookies.remove('auth-token');
        this.$router.push('/')
      })
    },
    login(){
      this.$router.push('/')
    }
  },
};
</script>
<style>
.address {
  margin-top: 25px;
}
button{
  color: rgb(233,105,30);
}
</style>
