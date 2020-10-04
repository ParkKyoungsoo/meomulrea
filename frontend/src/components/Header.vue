<template>
  <v-app-bar app style="box-shadow:none;">
    <v-toolbar-title>
      <router-link
        style="text-decoration: none; color: rgb(233,105,30); display:flex; align-items: center;"
        to="/home"
      >
        <img style="height:65px; width: 65px;" src="../assets/image/home.png" />
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
          style="margin:10px; margin-top:25px; width:250px;"
          color="rgb(233,105,30)"
          item-color="none"
        />
      </v-col>
    </v-toolbar-title>
    <button @click="findAddress(true)">추가하기</button>
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

<script src="http://dmaps.daum.net/map_js_init/postcode.v2.js"></script>
<script src="//dapi.kakao.com/v2/maps/sdk.js?appkey=48cbffa8392e1a7acffc1975347ec0d3&libraries=services"></script>

<script>
import user from "../assets/datas/user.json";
import { mapGetters, mapMutations } from "vuex";
import { EventBus } from "../utils/EventBus.js";
import * as firebase from "firebase";
import axios from "axios";

// const baseURL = "http://127.0.0.1:8000/";
const baseURL =
  "http://ec2-54-180-109-206.ap-northeast-2.compute.amazonaws.com/";

export default {
  data() {
    return {
      select: [],
      userInfo: "",
      showAddrModal: false,
      seletedAddress: "",
      isLogined: false,
      newAddress: "",
    };
  },
  components: {},
  computed: {
    ...mapGetters("location", ["getLocation"]),
    ...mapGetters("userInfo", ["getUserInfo"]),
  },

  watch: {
    newAddress: function(newVal, oldVal) {
      console.lof("watch", newVal);
    },
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

    addAddress: function() {
      console.log("addAddr Func", this.newAddress);
      axios
        .post(
          baseURL + "api/accounts/user_order/",
          {
            location: this.newAddress,
          },
          {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
          }
        ) // post > post
        .then((res) => {
          console.log(res.data);
        })
        .catch((res) => {
          console.log(res);
        }); // post > post > then
    },

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
        .post(baseURL + "api/accounts/user_order_list/", null, {
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

    findAddress() {
      new daum.Postcode({
        oncomplete: (data) => {
          var fullAddr = data.address;
          var extraAddr = "";

          if (data.addressType === "R") {
            if (data.bname !== "") {
              extraAddr += data.bname;
              console.log("bname : " + extraAddr);
            }
            if (data.buildingName !== "") {
              extraAddr +=
                extraAddr !== "" ? ", " + data.buildingName : data.buildingName;
              console.log("buildingName : " + extraAddr);
            }
            fullAddr += extraAddr !== "" ? " (" + extraAddr + ")" : "";
            this.newAddress = fullAddr;
          }
        },
      }).open();
      console.log("new Address is ", this.newAddress);
      this.addAddress();
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
