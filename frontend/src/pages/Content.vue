<template>
  <v-main class="content">
    <v-container style="width: 80%;">
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
            <v-flex>기온 : {{ locationData.main.temp - 273.15 }} &deg;C</v-flex>
            <v-flex>습도 : {{ locationData.main.humidity }} %</v-flex>
            <v-flex>기압 : {{ locationData.main.pressure }}</v-flex>
            <v-flex>날씨 : {{ locationData.weather[0].main }}</v-flex>
            <v-flex>풍향 : {{ locationData.wind.deg }} &deg;</v-flex>
            <v-flex>풍속 : {{ locationData.wind.speed }} m/s</v-flex>
            <v-flex>구름 : {{ locationData.clouds.all + "%" }}</v-flex>
          </v-row>
        </v-col>
      </v-layout>
      <div class="advertise" align="center" justify="center">
        광고영역
        <Carousel :storeData="tmpData" />
      </div>
      <v-layout>
        <v-flex> 현재 {{ this.getLocation.dong }}에서 인기있는 음식은? </v-flex>
      </v-layout>
      <div class="shopList">
        <div
          v-for="(item, index) in tmpData"
          :key="index"
          s
          style="margin: 10px;"
        >
          <ShowList :storeData="item" />
        </div>
      </div>
    </v-container>
  </v-main>
</template>

<script>
import Carousel from "../components/Carousel";
import axios from "axios";
import tmpData from "../assets/datas/store.json";
import ShowList from "../components/ShowList";
import { mapMutations, mapGetters } from "vuex";
import test from "../components/Addr2Code.vue";
import { EventBus } from "../utils/EventBus.js";

export default {
  components: {
    test,
    Carousel,
    ShowList,
  },

  data() {
    return {
      polling: null,
      lat: 0,
      lng: 0,
      locationData: "",
      tmpData: tmpData,
    };
  },

  created() {
    this.pollData();
    // this.getLocation();
    EventBus.$on("addressChange", () => {
      this.getWeather();
    });
  },
  computed: {
    ...mapGetters("location", ["getLocation"]),
  },
  beforeMount() {
    this.getWeather();
  },
  methods: {
    ...mapMutations(("location", ["setLocation"])),
    getWeather: function() {
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
          console.log(this.locationData);
        })
        .catch((ex) => {
          console.log("ERR!!!!! : ", ex);
        });
    },

    pollData() {
      this.polling = setInterval(() => {
        console.log("hihi");
        this.getWeather();
      }, 60000);
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

<style>
.content {
  border: 1px solid black;
  background-color: #ffe6e6;
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
}
</style>
