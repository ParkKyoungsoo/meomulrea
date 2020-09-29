<template>
  <v-main>
    <Header/>
    <div class="advertise" align="center" justify="center">
      <Carousel :storeData="recommendedDate"/> 
    </div>
    <v-container class="content">
      <div style="width: 80%;">
        <v-layout class="weather">
          오늘의 날씨
            <v-btn icon color="green" @click="getWeather">
              <v-icon>mdi-cached</v-icon>
            </v-btn>
            <v-flex>지역 : {{ this.getLocation.dong }} </v-flex>
            <v-flex>기온 : {{ parseInt(locationData.main.temp - 273.15) }} &deg;C</v-flex>
            <v-flex>습도 : {{ locationData.main.humidity }} %</v-flex>
            <v-flex>날씨 : <img style="width:25px; height:25px;" :src="require('../assets/image/' + weatherimg)" :alt=weatherimg></v-flex>
            <v-flex>구름 : {{ locationData.clouds.all + "%" }}</v-flex>
        </v-layout>
      <v-layout>
        <v-flex> 오늘은 뭐먹지? </v-flex>
      </v-layout>
      <div class="shopList">
        <carousel-3d :controls-visible="true">
          <slide v-for="(item, index) in recommendedDate" :key="index" :index="index">
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
import { EventBus } from "../utils/EventBus.js";
import Header from "../components/Header.vue";

// const baseURL = "http://127.0.0.1:8000/";
const baseURL = "http://j3b304.p.ssafy.io/";

Vue.use(Carousel3d);

export default {
  components: {
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
      weatherimg: "",
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
          if(this.locationData.weather[0].main==='Clear')
            this.weatherimg = 'Clear.png';
          else if(this.locationData.weather[0].main==='Clouds'){
            this.weatherimg = 'Clouds.png';
          }
          else if(this.locationData.weather[0].main==='wind')
            this.weatherimg = 'wind.png';
          else if(this.locationData.weather[0].main==='rain')
            this.weatherimg = 'rain.png';
          else if(this.locationData.weather[0].main==='snow')
            this.weatherimg = 'snow.png';
          console.log(this.weatherimg)
        })
        .catch(() => {
          // .catch((ex) => {
          // console.log("ERR!!!!! : ", ex);
        });
    },

    getCategory() {
      console.log('getCategory')
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
.content {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  height: fit-content;
  padding: 0;
}
.weather {
  text-align: right;
}
.weatherInfo {
  display: flex;
}
.shopList {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  height: fit-content;
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
