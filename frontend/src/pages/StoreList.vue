<template>
  <v-app>
    <Header />
    <v-main>
      <v-container>
        <v-row>
          <v-flex>{{ $route.params.category }}</v-flex>
          <v-flex>{{ this.getLocation.dong }}</v-flex>
        </v-row>

        <v-row style="display: flex; align-items: center; text-align: center;">
          <div v-for="(item, index) in storeList" :key="index" :index="index">
            <v-row style="margin: 10px; width: fit-content;">
              <Card :storeData="item" />
            </v-row>
          </div>
          <!-- <v-col>
                <v-row justify="center">
                  <div>{{ item.store_name }}</div>
                </v-row>
                <v-row justify="center">
                  <v-list-item-avatar tile size="200" color="grey" />
                </v-row>
              </v-col> -->

          <!-- <v-card-actions>
                <v-btn
                  depressed
                  color="primary"
                  @click="goToShopDetail(item.store_id)"
                  >가게 보러가기</v-btn
                >
              </v-card-actions> -->
          <!-- </v-card> -->
          <!-- </v-col> -->
          <!-- <v-col> -->
        </v-row>
        <!-- <v-row> -->
        <!-- </v-col> -->
        <!-- </v-row> -->
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";
// import kakaoMap from "../components/KakaoMap.vue";
import { mapGetters } from "vuex";
import Header from "../components/Header.vue";
import Card from "../components/Card.vue";

// const baseURL = "http://127.0.0.1:8000/";
const baseURL =
  "http://ec2-54-180-109-206.ap-northeast-2.compute.amazonaws.com/";

export default {
  data() {
    return {
      storeList: "",
      data: {
        loc: 0,
        category: "",
      },
    };
  },
  components: {
    // kakaoMap,
    Header,
    Card,
  },

  computed: {
    ...mapGetters("location", ["getLocation"]),
  },

  created: function() {
    this.loc = this.getLocation;
    this.category = this.$route.params.category;
    this.getStoreInfo();
  },

  methods: {
    getStoreInfo() {
      console.log(this.$cookies.get("auth-token"));
      axios
        .post(
          baseURL + "api/stores/store_list/",
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
          this.storeList = res.data;
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
        });
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
