<template>
  <v-app>
    <Header />
    <v-main>
      <v-container>
        <v-row>
          <v-flex>{{ $route.params.bigcategory }}</v-flex>
          <v-flex>{{ this.getLocation.dong }}</v-flex>
        </v-row>

        <v-row style="display: flex; align-items: center; text-align: center;">
          <div v-for="(item, index) in storeList" :key="index" :index="index">
            <v-row style="margin: 10px; width: fit-content;">
              <Card v-bind:storeData="item" />
            </v-row>
          </div>
        </v-row>
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
// const baseURL =
//   "http://ec2-54-180-109-206.ap-northeast-2.compute.amazonaws.com/";

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
    ...mapGetters("server", ["getBaseURL"]),
  },

  created: async function() {
    this.loc = this.getLocation;
    this.category = this.$route.params.bigcategory;
    await this.getStoreInfo();
  },

  methods: {
    test() {},
    async getStoreInfo() {
      await axios
        .post(
          this.getBaseURL.baseURL + "api/stores/store_bigcategory/",
          {
            bigcategory: this.category,
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