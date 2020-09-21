<template>
  <div id="tmp" class="content">
    <h2>본문영역</h2>
    <div class="weather">
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
    </div>
    <div class="advertise">
      광고영역
      <Carousel :storeData="tmpData" />
    </div>
    <div class="recommandFood">
      추천음식 구역
      <CarouselStore :storeData="tmpData" />
      <div style="display: flex;">
        <router-link tag="button" to="/">우리동네 매장 보러가기</router-link>
        <button>배달파티 보러가기</button>
      </div>
    </div>
    <div class="recommandFood">
      추천음식 구역2
      <div class="recommnadTopFood">
        <div class="foodThumbnail">추천음식 썸네일</div>
        <div style="display: flex;">
          <router-link tag="button" to="/"> 우리동네 매장 보러가기</router-link>
          <button>배달파티 보러가기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Carousel from "./Carousel";
import CarouselStore from "./CarouselStore";
import axios from "axios";
import tmpData from "../assets/datas/store.json";

export default {
  components: {
    Carousel,
    CarouselStore,
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
    axiosTest: function() {
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

    getLocation: function() {
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
