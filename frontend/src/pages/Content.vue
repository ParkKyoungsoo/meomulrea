<template>
  <v-main>
    <Header />
    <div class="advertise" align="center" justify="center">
      <!-- <Carousel :storeData="recommendedDate" /> -->
      <v-carousel
        cycle
        height="30vh"
        hide-delimiter-background
        show-arrows-on-hover
      >
        <v-carousel-item v-for="(slide, i) in advertise" :key="i">
          <v-sheet>
            <img
              :src="require(`@/assets/adverties/${slide}.png`)"
              style="width: 1523px; height: 226px;"
            />
          </v-sheet>
        </v-carousel-item>
      </v-carousel>
    </div>
    <v-container class="content">
      <div>
        <!-- <v-layout class="weather">
          <v-btn icon color="green" @click="getWeather">
            <v-icon>mdi-cached</v-icon>
          </v-btn>
          오늘의 날씨(<img
            style="width:30px; height:30px;"
            :src="require('../assets/image/' + weatherimg)"
            :alt="weatherimg"
          />)

          <v-flex>지역 : {{ this.getLocation.dong }} </v-flex>
          <v-flex
            >기온 :
            {{ parseInt(locationData.main.temp - 273.15) }} &deg;C</v-flex
          >
          <v-flex>습도 : {{ locationData.main.humidity }} %</v-flex>
          <v-flex>구름 : {{ locationData.clouds.all + "%" }}</v-flex>
        </v-layout> -->
        <v-layout>
          <v-flex> 오늘은 뭐먹지? </v-flex>
        </v-layout>
        <v-layout style="display: flex; justify-content: center;">
          <carousel-3d
            v-if="recommendedDate.length > 4"
            controls-visible="true"
          >
            <slide
              v-for="(item, index) in recommendedDate"
              :key="index"
              :index="index"
            >
              <figure>
                <img :src="require(`@/assets/menu/${item[1]}.jpg`)" />
                <figcaption @click="gotoShop(item[2])">
                  <h2>{{ index + 1 }}위 : {{ item[1] }}</h2>
                </figcaption>
              </figure>
            </slide>
          </carousel-3d>
        </v-layout>
        <v-layout>
          <v-row
            style="display: flex; align-items: center; text-align: center; justify-content: center;"
          >
            <div
              v-for="(item, index) in foodCategory"
              :key="index"
              :index="index"
            >
              <v-row style="margin: 10px; width: fit-content;">
                <FoodCard :categoryData="item" />
              </v-row>
            </div>
          </v-row>
        </v-layout>
      </div>
    </v-container>
  </v-main>
</template>

<script>
import Vue from "vue";
import Carousel from "../components/Carousel";
import { Carousel3d, Slide } from "vue-carousel-3d";
import axios from "axios";
// import ShowList from "../components/ShowList";
import { mapMutations, mapGetters } from "vuex";
import { EventBus } from "../utils/EventBus.js";
import Header from "../components/Header.vue";
import category from "../assets/category/category.json";
import FoodCard from "../components/FoodCard.vue";
import coverflow from "vue-coverflow";

// const baseURL = "http://127.0.0.1:8000/";
// const baseURL =
//   "http://ec2-54-180-109-206.ap-northeast-2.compute.amazonaws.com/";

// Vue.use(Carousel3d);

export default {
  components: {
    // Carousel,
    Header,
    Carousel3d,
    Slide,
    FoodCard,
  },

  data() {
    return {
      polling: null,
      lat: 0,
      lng: 0,
      locationData: "",
      recommendedDate: [],
      weatherimg: "",
      advertise: ["1", "2", "3", "4"],
    };
  },
  created() {
    this.pollData();

    // this.getLocation();
    EventBus.$on("addressChange", () => {
      this.getWeather();
    });

    axios
      .post(this.getBaseURL.baseURL + "api/main/", null, {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      }) // post > post
      .then((res) => {
        this.recommendedDate = res.data.data;
        console.log(this.recommendedDate);
      })
      .catch((res) => {
        console.log(res);
      }); // post > post > then
  },
  computed: {
    ...mapGetters("location", ["getLocation"]),
    user() {
      return this.$store.getters.user;
    },
    foodCategory() {
      return category;
    },
    ...mapGetters("server", ["getBaseURL"]),
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
          if (this.locationData.weather[0].main === "Clear")
            this.weatherimg = "Clear.png";
          else if (this.locationData.weather[0].main === "Clouds") {
            this.weatherimg = "Clouds.png";
          } else if (this.locationData.weather[0].main === "wind")
            this.weatherimg = "wind.png";
          else if (this.locationData.weather[0].main === "rain")
            this.weatherimg = "rain.png";
          else if (this.locationData.weather[0].main === "snow")
            this.weatherimg = "snow.png";
        })
        .catch(() => {
          // .catch((ex) => {
          // console.log("ERR!!!!! : ", ex);
        });
    },

    getCategory() {
      axios({
        method: "GET",
        url: this.getBaseURL.baseURL + "api/main/",
      })
        .then((response) => {
          this.recommendedDate = response.data.data;
        })
        .catch((ex) => {});
    },

    pollData() {
      this.polling = setInterval(() => {
        this.getWeather();
      }, 60000);
    },

    gotoShop(index) {
      this.$router.push("/storelist/" + index);
    },

    // mouseOver() {

    // }

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
