<template>
  <v-main>
    <Header />
    <v-container>
      <h1>{{ this.storeInfo.store_name }}</h1>
      <v-card>
        <v-row>
          <v-col
            style="background-size:200px 200px;"
            :style="{ backgroundImage: `url(` + imgUrl + `)` }"
            lg="2"
            md="2"
          >
          </v-col>
          <v-col
            style="background-color: rgb(132, 245, 132); text-align: left;"
            lg="7"
            md="7"
          >
            <div>
              <img
                src="../assets/image/placeholder.png"
                style="width:15px;"
                alt=""
              />
              {{ this.storeInfo.address }}
            </div>
            <div>
              <img
                src="../assets/image/category.png"
                style="width:15px;"
                alt=""
              />
              {{ this.storeInfo.category }}
            </div>
            <div>
              <img src="../assets/image/money.png" style="width:15px;" alt="" />
              {{ this.storeInfo.min_price }}원
            </div>
            <div>
              <img src="../assets/image/clock.png" style="width:15px;" alt="" />
              {{ this.businessDay }} {{ this.startTime }} - {{ this.endTime }}
            </div>
            <div>평점 : {{ this.storeInfo.average_rating }}</div>
            <div style="display: flex; justify-content: start;">
              <!-- 영업일 : {{ this.businessDay }} -->
              <!-- <div>{{ this.storeInfo.mon == 0 ? "월" : null }}</div>
              <div>{{ this.storeInfo.tue == 0 ? "화" : null }}</div>
              <div>{{ this.storeInfo.wen == 0 ? "수" : null }}</div>
              <div>{{ this.storeInfo.thu == 0 ? "목" : null }}</div>
              <div>{{ this.storeInfo.fri == 0 ? "금" : null }}</div>
              <div>{{ this.storeInfo.sat == 0 ? "토" : null }}</div>
              <div>{{ this.storeInfo.sun == 0 ? "일" : null }}</div> -->
            </div>
          </v-col>
          <v-col style="background-color: rgb(245, 183, 132);" lg="3" md="3">
            <KakaoMap :storeData="this.storeInfo" />
          </v-col>
        </v-row>
      </v-card>
      <br />

      <!-- <v-card>
        <v-row>
          <v-col class="menu" @click="showContent(1)">메뉴</v-col>
          <v-col class="review" @click="showContent(2)">리뷰</v-col>
          <v-col class="party" @click="showContent(3)">파티만들기</v-col>
        </v-row>
        <v-row>
          <v-col>
            <review v-if="contentTrigger2" />
            <party v-if="contentTrigger3" />
          </v-col>
        </v-row>
      </v-card> -->
      <v-row>
        <v-tabs v-model="tab" fixed-tabs color="orange accent-4">
          <v-tab class="menu" @click="showContent(1)"
            ><img src="../assets/image/menu.png" alt="menu" width="35"
          /></v-tab>
          <v-tab class="review" @click="showContent(2)"
            ><img src="../assets/image/review.png" alt="review" width="35"
          /></v-tab>
          <v-tab class="party" @click="showContent(3)"
            ><img src="../assets/image/high-five.png" alt="party" width="35"
          /></v-tab>
        </v-tabs>
      </v-row>
      <v-row>
        <v-col>
          <review v-if="contentTrigger2" />
          <party v-if="contentTrigger3" />
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>
<script>
// import StoreData from "../assets/datas/all_store_encoding2.json";
import Header from "../components/Header.vue";
import review from "../components/review.vue";
import party from "../components/party.vue";
import axios from "axios";
import KakaoMap from "../components/KakaoMap.vue";

// const baseURL = "http://127.0.0.1:8000/";
const baseURL =
  "http://ec2-54-180-109-206.ap-northeast-2.compute.amazonaws.com/";

export default {
  components: {
    Header,
    KakaoMap,
    review,
    party,
  },
  data() {
    return {
      storeInfo: "",
      contentTrigger1: true,
      contentTrigger2: false,
      contentTrigger3: false,
      startTime: "",
      endTime: "",
      days: [],
      businessDay: "",
      imgUrl: "",
    };
  },
  created() {
    this.getStoreDetail();
  },
  methods: {
    changeStartTime(time) {
      // P0DT0H~
      if (time[5] == "H") {
        // P0DT0H0M~
        if (time[7] == "M") {
          this.startTime =
            "0" + time.substring(4, 5) + ":" + time.substring(6, 7) + "0";
        }
        // P0DT0H00M~
        else {
          this.startTime = time.substring(4, 5) + ":" + time.substring(6, 8);
        }
      }
      // P0DT00H~
      else {
        // P0DT00H0M~
        if (time[8] == "M") {
          this.startTime =
            time.substring(4, 6) + ":" + time.substring(7, 8) + "0";
        }
        // P0DT00H00M~
        else {
          this.startTime = time.substring(4, 6) + ":" + time.substring(7, 9);
        }
      }
    },

    changeEndTime(time) {
      if (time[5] == "H") {
        if (time[7] == "M") {
          this.endTime =
            "0" + time.substring(4, 5) + ":" + time.substring(6, 7) + "0";
        } else {
          this.endTime = time.substring(4, 5) + ":" + time.substring(6, 8);
        }
      } else {
        if (time[8] == "M") {
          this.endTime =
            time.substring(4, 6) + ":" + time.substring(7, 8) + "0";
        } else {
          this.endTime = time.substring(4, 6) + ":" + time.substring(7, 9);
        }
      }
      if (this.endTime == "00:00") this.endTime = "24:00";
    },

    getBusinessDay(day) {
      // 0: 휴무
      if (day.mon == 1 ? this.days.push("월") : this.days.push(0));
      if (day.tue == 1 ? this.days.push("화") : this.days.push(0));
      if (day.wed == 1 ? this.days.push("수") : this.days.push(0));
      if (day.thu == 1 ? this.days.push("목") : this.days.push(0));
      if (day.fri == 1 ? this.days.push("금") : this.days.push(0));
      if (day.sat == 1 ? this.days.push("토") : this.days.push(0));
      if (day.sun == 1 ? this.days.push("일") : this.days.push(0));

      if (!this.days.includes(0)) {
        this.businessDay = "매일";
      }
      for (var d in this.days) {
        if (this.days[d] != 0) this.businessDay += this.days[d] + ",";
      }
      if (this.businessDay == "월,화,수,목,금") this.businessDay = "평일";
      else if (this.businessDay == "토,일") this.businessDay = "주말";
      else
        this.businessDay = this.businessDay.substring(
          0,
          this.businessDay.length - 1
        );
    },

    getStoreDetail() {
      axios
        .post(baseURL + `api/stores/${this.$route.params.storeid}/`, null, {
          headers: {
            Authorization: `Token ${this.$cookies.get("auth-token")}`,
          },
        }) // post > post
        .then((res) => {
          console.log("res Data", res.data);
          this.storeInfo = res.data;
          this.imgUrl = require("../assets/image/storelist/" +
            this.storeInfo.store_name.replace(/(\s*)/g, "") +
            ".jpg");
          this.changeStartTime(res.data.start_time);
          this.changeEndTime(res.data.end_time);
          this.getBusinessDay(res.data);
        })
        .catch((res) => {
          console.log("user Address error", res);
        }); // post > post > then
    },

    showContent(num) {
      if (num == 1) {
        this.contentTrigger1 = true;
        this.contentTrigger2 = false;
        this.contentTrigger3 = false;
      } else if (num == 2) {
        this.contentTrigger1 = false;
        this.contentTrigger2 = true;
        this.contentTrigger3 = false;
      } else if (num == 3) {
        this.contentTrigger1 = false;
        this.contentTrigger2 = false;
        this.contentTrigger3 = true;
      }
    },
    // getStoreDetail() {
    //   for (var i = 0; i < StoreData.data.length; i++) {
    //     if (StoreData.data[i].store_id == this.$route.params.storeid) {
    //       this.storeInfo = StoreData.data[i];
    //     }
    //   }
    // },
  },
};
</script>
<style></style>
