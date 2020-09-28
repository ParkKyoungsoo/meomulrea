<template>
  <v-app>
    <Header />
    <v-main>
      <v-container>
        카테고리에 해당하는 가게 목록들
        <div>{{ $route.params.category }}</div>
        <div>{{ this.getLocation.dong }}</div>
        <v-btn @click="getStoreInfo">버튼</v-btn>
        <v-row>
          <v-col class="shopList">
            <v-card
              class="mx-auto"
              max-width="320"
              outlined
              v-for="(item, index) in this.getShopList.shopList"
              :key="index"
            >
              <v-col>
                <v-row justify="center">
                  <div>{{ item.store_name }}</div>
                </v-row>
                <v-row justify="center">
                  <v-list-item-avatar tile size="200" color="grey" />
                </v-row>
              </v-col>

              <v-card-actions>
                <v-btn
                  depressed
                  color="primary"
                  @click="goToShopDetail(item.store_id)"
                  >가게 보러가기</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-col>
          <v-col>
            <kakaoMap :storeData="loc" :category="category" />
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";
import kakaoMap from "../components/KakaoMap.vue";
import { mapGetters } from "vuex";
import Header from "../components/Header.vue";

const baseURL = "http://127.0.0.1:8000/";

export default {
  data() {
    return {
      data: {
        loc: 0,
        category: "",
        shopList: "",
      },
    };
  },
  components: {
    kakaoMap,
    Header,
  },

  computed: {
    ...mapGetters("location", ["getLocation"]),
    ...mapGetters("shopList", ["getShopList"]),
  },

  created: function() {
    this.loc = this.getLocation;
    this.category = this.$route.params.category;
    this.shopList = this.getShopList;
    console.log("shopList : ", this.shopList);
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
    test: function() {
      console.log("loc", this.loc);
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
};
</script>
<style>
.shopList {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
</style>
