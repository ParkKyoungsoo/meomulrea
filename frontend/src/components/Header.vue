<template>
  <v-app-bar app style="box-shadow:none;">
    <v-toolbar-title>
      <router-link style="text-decoration: none; color: rgb(233,105,30); display:flex; align-items: center;" to="/home">
        <img style="height:65px; width: 65px;" src="../assets/image/home.png">
      </router-link>
    </v-toolbar-title>
    <v-spacer/>
    <v-toolbar-title>
      <v-col>
        <v-select
          v-model="select"
          @change="changeAddress"
          :items="userInfo"
          item-text="location"
          return-object
          style="margin:10px; margin-top:25px; width:250px;"
          color="rgb(233,105,30)"
          item-color="none"
        />
      </v-col>
    </v-toolbar-title>
    <button @click="showAddrModal = true">추가하기</button>
    <button @click="test">버어튼</button>
    <v-spacer />
    <v-toolbar-title>
      <div
        v-if="
          $cookies.get('auth-token') === null ||
            $cookies.get('auth-token') === ''
        "
      >
        <button @click="login()"><h2>login</h2></button>
      </div>
      <div v-else>
        <button @click="logout()"><h2>logout</h2></button>
      </div>
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
import user from "../assets/datas/user.json";
import { mapGetters, mapMutations } from "vuex";
import { EventBus } from "../utils/EventBus.js";
import * as firebase from "firebase";
import axios from "axios";

const baseURL = "http://127.0.0.1:8000/";
// const baseURL = "http://j3b304.p.ssafy.io/";

export default {
  data() {
    return {
      select: "",
      userInfo: "",
      showAddrModal: false,
      seletedAddress: "",
      isLogined: false,
    };
  },
  components: {},
  computed: {
    ...mapGetters("location", ["getLocation"]),
    ...mapGetters("userInfo", ["getUserInfo"]),
  },

  created() {
    this.getUserAddress();
    console.log("Token ", this.$cookies.get("auth-token"));
    this.select = this.getUserInfo.location;
  },

  mounted() {
    window.kakao && window.kakao.maps ? null : this.addScript();
  },

  methods: {
    test() {
      console.log("test console", this.userInfo[0].location);
    },

    ...mapMutations(("location", ["setLocation"])),
    ...mapMutations(("userInfo", ["setUserInfo"])),

    changeAddress: function() {
      // EventBus.$emit("addressChange", this.select.location);
      // this.$store.commit("location/setLocation", {
      //   lat: this.lat,
      //   lng: this.lng,
      // });
      this.searchAddr();
      this.$store.commit("userInfo/setUserInfo", {
        userAddress: this.select.location,
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
        .post(baseURL + "accounts/user_order_list/", null, {
          headers: {
            Authorization: `Token ${this.$cookies.get("auth-token")}`,
          },
        }) // post > post
        .then((res) => {
          this.userInfo = res.data;
        })
        .catch((res) => {
          console.log("user Address error", res);
        }); // post > post > then
    },

    addScript() {
      let script = document.createElement("script");
      /* global kakao */

      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=a7bd2d0df8f5ae53b0c5e106842b94fd&libraries=services";
      document.head.appendChild(script);
    },

    searchAddr() {
      var geocoder = new kakao.maps.services.Geocoder();

      geocoder.addressSearch(this.select.location, (result, status) => {
        if (status === kakao.maps.services.Status.OK) {
          console.log("result", result);
          this.$store.commit("location/setLocation", {
            lat: result[0].y,
            lng: result[0].x,
            dong: result[0].address.region_3depth_name,
          });
        }
      });
    },
    login() {
      this.$router.push("/");
    },
  },

  watch() {},
};
</script>
<style>
.address {
  margin-top: 25px;
}
button {
  color: rgb(233, 105, 30);
}
</style>
