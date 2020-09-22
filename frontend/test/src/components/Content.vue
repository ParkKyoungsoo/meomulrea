<template>
  <v-main class="content">
    <v-container>
      <h2>본문영역</h2>
      <v-layout class="weather">
        날씨 영역
        <button @click="axiosTest">날씨 테스트</button>
        <div class="weatherInfo">
          <div>지역 : {{ locationData.name }}</div>
          <div>기온 : {{ locationData.main.temp - 273.15 }} &deg;C</div>
          <div>습도 : {{ locationData.main.humidity }} %</div>
          <div>기압 : {{ locationData.main.pressure }}</div>
          <div>날씨 : {{ locationData.weather[0].main }}</div>
          <div>풍향 : {{ locationData.wind.deg }} &deg;</div>
          <div>풍속 : {{ locationData.wind.speed }} m/s</div>
          <div>구름 : {{ locationData.clouds.all + "%" }}</div>
        </div>
      </v-layout>
      <div class="advertise">
        광고영역
        <Carousel :storeData="tmpData" />
      </div>
      <v-layout>
        <v-flex> 현재 [위치]에서 인기있는 음식은? </v-flex>
      </v-layout>
      <div style="display: flex">
        <div v-for="(item, index) in tmpData" :key="index">
          <ShowList :storeData="item" />
        </div>
      </div>
    </v-container>
  </v-main>
</template>

<script>
import Carousel from "./Carousel";
import axios from "axios";
import tmpData from "../assets/datas/store.json";
import ShowList from "./ShowList";

export default {
  components: {
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
    this.getLocation();
  },

  beforeMount() {
    this.axiosTest();
  },

  methods: {
    axiosTest: function () {
      axios({
        method: "GET",
        url: `http://api.openweathermap.org/data/2.5/weather?lat=${this.lat}&lon=${this.lng}&appid=5da983044710640f1d38176a055c7f66`,
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
        this.axiosTest();
      }, 60000);
    },

    getLocation: function () {
      if (navigator.geolocation) {
        // GPS를 지원하면
        navigator.geolocation.getCurrentPosition(
          (position) => {
            this.lat = position.coords.latitude;
            this.lng = position.coords.longitude;
            console.log(this.lat + " " + this.lng);
          },
          (error) => {
            console.error(error);
          },
          {
            enableHighAccuracy: false,
            maximumAge: 0,
            timeout: Infinity,
          }
        );
      } else {
        alert("GPS를 지원하지 않습니다");
      }
    },
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
  width: 80%;
}
.weather {
  text-align: left;
}
.weatherInfo {
  display: flex;
}
.foodThumbnail {
  width: 50%;
  height: 200px;
  border: 1px solid black;
}
.recommnadTopFood {
  border: 1px solid black;
}
</style>
