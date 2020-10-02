<template>
<v-container>
    <v-row style="display: flex; align-items: center; text-align: center;">
        <div v-for="(item, index) in this.getShopList.shopList" :key="index" :index="index">
            <v-row style="margin: 10px; width: fit-content;">
                <div class="flip">
                  <div class="front" :style="{ backgroundImage: `url(`+imgUrl[index]+`)` }">
                    <h1 class="text-shadow">{{item.store_name}}</h1>
                  </div>
                  <div class="back">
                    <h2>{{item.store_name}}</h2>
                    <p>별점 : {{item.average_rating}}</p>
                    <v-btn @click="goToShopDetail(item.shopId)">가게보러가기</v-btn>
                  </div>
              </div>
            </v-row>
        </div>
    </v-row>
</v-container>
</template>
<script>
import axios from "axios";
import { mapGetters } from "vuex";
const baseURL = "http://j3b304.p.ssafy.io/";
export default {
    data() {
    return {
      imgUrl: [],
      data: {
        category: "",
        shopList: "",
      },
    };
  },
  components: {
  },

  computed: {
    ...mapGetters("shopList", ["getShopList"]),
  },
  created: function() {
    // this.loc = this.getLocation;
    // this.category = this.$route.params.category;
    this.shopList = this.getShopList;
    for(var i=0;i<6;i++){
      this.imgUrl.push(require('../assets/image/storelist/'+this.shopList.shopList[i].store_name.replace(/(\s*)/g, "")+'.jpg'));
    }
    console.log(this.imgUrl)
  },

  methods: {
    getStoreInfo() {
      console.log(this.$cookies.get("auth-token"));
      axios
        .post(
          baseURL + "stores/store_list/",
          {
            category: this.category,
            user_location: this.getLocation.dong,
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

    goToShopDetail: function(shopId) {
      this.$router.push("/storedetail/" + shopId);
    },
    showShopList: function() {
      axios
        .post(
          baseURL + "stores/store_category/",
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
}
</script>

<style lang="scss" scoped src="../assets/css/Card.scss">
</style>>