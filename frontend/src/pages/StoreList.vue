<template>
  <v-main>
    <v-container>
      카테고리에 해당하는 가게 목록들
      <div>{{ $route.params.category }}</div>
      <!-- <div>{{ this.$store.getters["location/getLocation"] }}</div> -->
      <v-row>
        <v-col>
          <v-row>
            1-1
          </v-row>
          <v-row>
            1-2
          </v-row>
        </v-col>
        <v-col>
          <kakaoMap :storeData="loc" />
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import axios from "axios";
import kakaoMap from "../components/KakaoMap.vue";
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      loc: 0,
    };
  },
  components: {
    kakaoMap,
  },

  computed: {
    ...mapGetters("location", ["getLocation"]),
  },

  created: function() {
    this.loc = this.getLocation;
  },

  methods: {
    test: function() {
      console.log("loc", this.loc);
    },
    showShopList: function() {
      axios({
        method: "GET",
        url: ``,
        params: {
          page: 1,
          pagesize: 5,
        },
      })
        .then((response) => {
          this.locationData = response.data;
          console.log(this.locationData);
        })
        .catch((ex) => {
          console.log("ERR!!!!! : ", ex);
        });
    },
  },
};
</script>
