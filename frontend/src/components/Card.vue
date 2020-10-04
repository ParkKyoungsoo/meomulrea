<template>
  <div class="flip">
    <div class="front" :style="{ backgroundImage: `url(` + imgUrl + `)` }">
      <h1 class="text-shadow">{{ this.storeData.store_name }}</h1>
    </div>
    <div class="back">
      <h2>{{ this.storeData.store_name }}</h2>
      <p>별점 : {{ parseInt(this.storeData.average_rating) }}</p>
      <v-btn @click="goToShopDetail()"
        >가게보러가기</v-btn>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { mapGetters } from "vuex";
// const baseURL = "http://j3b304.p.ssafy.io/";
const baseURL =
  "http://ec2-54-180-109-206.ap-northeast-2.compute.amazonaws.com/";

export default {
  props: {
    storeData: {},
  },
  data() {
    return {
      imgUrl: "",
      data: {
        category: "",
      },
      storeId: "",
    };
  },
  components: {},
  created: function() {
    // this.imgUrl = require("../assets/image/storelist/" +
    //   this.storeData.store_name.replace(/(\s*)/g, "") +
    //   ".jpg");
    // console.log(this.imgUrl);
    
    console.log("created!!", this.storeData.store_id);
  },

  methods: {
    
    goToShopDetail() {
      this.storeId = this.storeData.store_id
      this.$router.push("/storedetail/" + this.storeId);
    },
    showShopList: function() {
      axios
        .post(
          baseURL + "api/stores/store_category/",
          {
            category: this.$route.params.category,
          },
          {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
          }
        ) // post > post
        .then((res) => {
          this.userInfo = res.data;
        })
        .catch((res) => {
          console.log("user Address error", res);
        }); // post > post > then
    },
  },
};
</script>

<style lang="scss" scoped src="../assets/css/Card.scss"></style>>
