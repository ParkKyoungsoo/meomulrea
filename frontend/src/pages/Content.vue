<template>
  <v-main>
    <Header />
    <div
      class="advertise"
      align="center"
      justify="center"
      style="border: 1px solid black;"
    >
      <Carousel :storeData="recommendedDate" />
    </div>
    <v-container class="content">
      <div style="width:80%;">
        <h2>본문영역</h2>
        <test />
        <v-layout class="weather">
          <v-col>
            <v-row>
              날씨 영역
              <v-btn icon color="green" @click="getWeather">
                <v-icon>mdi-cached</v-icon>
              </v-btn>
            </v-row>
            <v-row align="center" justify="center">
              <v-flex>지역 : {{ this.getLocation.dong }} </v-flex>
              <v-flex
                >기온 : {{ locationData.main.temp - 273.15 }} &deg;C</v-flex
              >
              <v-flex>습도 : {{ locationData.main.humidity }} %</v-flex>
              <v-flex>기압 : {{ locationData.main.pressure }}</v-flex>
              <v-flex>날씨 : {{ locationData.weather[0].main }}</v-flex>
              <v-flex>풍향 : {{ locationData.wind.deg }} &deg;</v-flex>
              <v-flex>풍속 : {{ locationData.wind.speed }} m/s</v-flex>
              <v-flex>구름 : {{ locationData.clouds.all + "%" }}</v-flex>
            </v-row>
          </v-col>
        </v-layout>
        <v-layout>
          <v-flex> 오늘은 뭐먹지? </v-flex>
        </v-layout>
        <div class="shopList">
          <carousel-3d :controls-visible="true">
            <slide
              v-for="(item, index) in recommendedDate"
              :key="index"
              :index="index"
            >
              <figure>
                <img :src="item.src" :alt="item[1]" />
                <!-- <img src="../assets/image/background.jpg"> -->
                <figcaption @click="gotoShop(item[1])">
                  <h2>{{ index + 1 }}위</h2>
                </figcaption>
              </figure>
            </slide>
          </carousel-3d>
        </div>
      </div>
    </v-container>
  </v-main>
</template>

<script>
import Vue from "vue";
import Carousel from "../components/Carousel";
import { Carousel3d, Slide } from "vue-carousel-3d";
import axios from "axios";
import recommendedDate from "../assets/datas/recommend_result_1.json";
// import ShowList from "../components/ShowList";
import { mapMutations, mapGetters } from "vuex";
// import Addr2Code from "../components/Addr2Code.vue";
import { EventBus } from "../utils/EventBus.js";
import Header from "../components/Header.vue";

// const baseURL = "http://127.0.0.1:8000/";
const baseURL = "http://j3b304.p.ssafy.io/";

Vue.use(Carousel3d);

export default {
  components: {
    // Addr2Code,
    Carousel,
    Header,
    Carousel3d,
    Slide,
  },

  data() {
    return {
      polling: null,
      lat: 0,
      lng: 0,
      locationData: "",
      recommendedDate: "",
    };
  },

  created() {
    this.pollData();
    // this.getLocation();
    EventBus.$on("addressChange", () => {
      this.getWeather();
    });
    this.getCategory();
  },
  computed: {
    ...mapGetters("location", ["getLocation"]),
    user() {
      return this.$store.getters.user;
    },
  },

  beforeMount() {
    this.getWeather();
  },

  methods: {
    test() {
      console.log(recommendedDate);
    },
    ...mapMutations(("location", ["setLocation"])),
    getWeather: function() {
      console.log("weather function called!!");
      axios({
        method: "GET",
        url: `http://api.openweathermap.org/data/2.5/weather?lat=${this.getLocation.lat}&lon=${this.getLocation.lng}&appid=5da983044710640f1d38176a055c7f66`,
        params: {
          page: 1,
          pagesize: 5,
        },
      })
        .then((response) => {
          this.locationData = response.data;
          // console.log(this.locationData);
        })
        .catch(() => {
          // .catch((ex) => {
          // console.log("ERR!!!!! : ", ex);
        });
    },

    getCategory() {
      axios({
        method: "GET",
        url: baseURL + "main/",
      })
        .then((response) => {
          console.log(response.data.data);
          this.recommendedDate = response.data.data;
        })
        .catch((ex) => {
          console.log(ex);
        });
    },

    pollData() {
      this.polling = setInterval(() => {
        this.getWeather();
      }, 60000);
    },

    gotoShop(index) {
      console.log("gotoShop : " + index);
      this.$router.push("/storelist/" + index);
    },

    // getLocation: function() {
    //   if (navigator.geolocation) {
    //     // GPS를 지원하면
    //     navigator.geolocation.getCurrentPosition(
    //       (position) => {
    //         this.lat = position.coords.latitude;
    //         this.lng = position.coords.longitude;
    //         this.$store.commit("location/setLocation", {
    //           lat: this.lat,
    //           lng: this.lng,
    //         });
    //         console.log(
    //           "lat",
    //           this.$store.state.lat,
    //           this.lat,
    //           "lng",
    //           this.$store.state.lng,
    //           this.lng
    //         );
    //       },
    //       (error) => {
    //         console.error(error);
    //       },
    //       {
    //         enableHighAccuracy: false,
    //         maximumAge: 0,
    //         timeout: Infinity,
    //       }
    //     );
    //   } else {
    //     alert("GPS를 지원하지 않습니다");
    //   }
    // },
  },

  beforeDestroy() {
    clearInterval(this.polling);
  },
};
</script>

<style lang="scss" scoped>
.container {
  margin: 0px;
  max-width: 1600px;
  min-height: 690px;
  /* background-image: url('../assets/image/background.jpg'); */
  /* // background: url('../assets/image/background.jpg');
  // background: rgba(233, 105, 30, 0.3);
  // -webkit-font-smoothing: antialiased;
  // -moz-osx-font-smoothing: grayscale;
  // background: linear-gradient(180deg, rgba(255,255,255,1) 0%, rgba(233,105,30,0.8) 100%);
  // background: url('../assets/image/cloud.jpg');
  // background-size: 100%; */
}
.content {
  /* // border: 1px solid black; */
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
.weather {
  text-align: left;
}
.weatherInfo {
  display: flex;
}
.shopList {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
figure {
  padding: 0;
  margin: 0;
}
figure figcaption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  text-align: center;
  color: #fff;
  padding: 10px;
  background-color: black;
  opacity: 0.5;
}
</style>
