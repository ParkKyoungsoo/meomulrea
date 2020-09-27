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
          v-model="select"
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
      <div
        v-if="
          $cookies.get('auth-token') === null ||
            $cookies.get('auth-token') === ''
        "
      >
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

const baseURL = "http://127.0.0.1:8000/";

export default {
  data() {
    return {
      select: user[0].nm_address[0],
      userAddress: user[0].nm_address,
      showAddrModal: false,
      seletedAddress: "",
      isLogined: false,
    };
  },
  components: {},
  computed: {
    options: () => user[0].nm_address,
  },
  created() {
    this.getUserAddress();
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
    logout() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.$cookies.remove("auth-token");
          this.$router.push("/");
        });
    },
    getUserAddress() {
      axios
        .post(baseURL + "accounts/user_order_list/", {
          headers: {
            Authorization: this.$cookies.get("auth-token"),
          },
        }) // post > post
        .then((res) => {
          console.log("user Address is", res.data);
        }); // post > post > then
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
