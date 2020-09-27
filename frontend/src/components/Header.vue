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
          :items="userInfo"
          item-text="location"
          return-object
          dense
          solo
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
import { mapGetters, mapMutations } from "vuex";
import { EventBus } from "../utils/EventBus.js";
import * as firebase from "firebase";
import axios from "axios";

const baseURL = "http://127.0.0.1:8000/";

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
  },

  watch() {},
};
</script>
<style>
.address {
  margin-top: 25px;
}
</style>
