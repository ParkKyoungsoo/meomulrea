<template>
  <v-app-bar app color="rgb(233, 105, 30)" dark>
    <v-toolbar-title>
      <router-link style="text-decoration: none; color: white;" to="/home">
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
          dense
          solo
        />
      </v-col>
    </v-toolbar-title>
    <button @click="showAddrModal = true">추가하기</button>
    <v-spacer />
    <v-toolbar-title>
      <div v-if="$cookies.get('auth-token')===null || $cookies.get('auth-token')===''">
        <router-link style="text-decoration: none; color: white;" to="/">
          Login
        </router-link>
      </div>
        <button @click="logout()">logout</button>
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
import user from "../assets/datas/user.json";
import { mapMutations } from "vuex";
import { EventBus } from "../utils/EventBus.js";
import * as firebase from "firebase";

export default {
  data(){
    return{
    userAddress: user[0].nm_address,
    showAddrModal: false,
    seletedAddress: "",
<<<<<<< HEAD
    isLogined: false,
  }),
=======
    }
  },
>>>>>>> f7a99b280509a0bf51f34498e4923d844ffe53e1
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
<<<<<<< HEAD
    logout() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.$cookies.remove("auth-token");
          this.$router.push("/login");
        });
=======
    logout(){
      firebase.auth().signOut().then(()=>{
        this.$cookies.remove('auth-token');
        this.$router.push('/')
      })
>>>>>>> f7a99b280509a0bf51f34498e4923d844ffe53e1
    },
  },

  watch() {},
};
</script>
<style>
.address {
  margin-top: 25px;
}
</style>
