<template>
  <v-app>
    <Header />
    <v-main>
      <v-container>
        가게 상세 정보
        <v-card>
          <v-row>
            <v-col style="background-color: rgb(132, 192, 245);" lg="2" md="2">
              <div>
                <div>가게 썸네일</div>
                <div>평점 : {{ this.storeInfo.average_rating }}</div>
              </div>
            </v-col>
            <v-col
              style="background-color: rgb(132, 245, 132); text-align: left;"
              lg="7"
              md="7"
            >
              <div>{{ this.storeInfo.store_name }}</div>
              <div>{{ this.storeInfo.address }}</div>
              <div>최소 주문 금액 : {{ this.storeInfo.min_price }} 원</div>
              <div style="display: flex; justify-content: start;">
                휴무일 :
                <div>{{ this.storeInfo.mon == 1 ? "월" : null }}</div>
                <div>{{ this.storeInfo.tue == 1 ? "화" : null }}</div>
                <div>{{ this.storeInfo.wen == 1 ? "수" : null }}</div>
                <div>{{ this.storeInfo.thu == 1 ? "목" : null }}</div>
                <div>{{ this.storeInfo.fri == 1 ? "금" : null }}</div>
                <div>{{ this.storeInfo.sat == 1 ? "토" : null }}</div>
                <div>{{ this.storeInfo.sun == 1 ? "일" : null }}</div>
              </div>
            </v-col>
            <v-col style="background-color: rgb(245, 183, 132);" lg="3" md="3">
              지도표시구역
            </v-col>
          </v-row>
        </v-card>
        <br />
        <v-card>
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
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>
<script>
import StoreData from "../assets/datas/all_store_encoding2.json";
import review from "../components/review.vue";
import party from "../components/party.vue";
import Header from "../components/Header.vue";

export default {
  components: {
    review,
    party,
    Header,
  },
  data() {
    return {
      storeInfo: "",
      contentTrigger1: true,
      contentTrigger2: false,
      contentTrigger3: false,
    };
  },
  created() {
    this.getStoreDetail();
  },
  methods: {
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
    getStoreDetail() {
      for (var i = 0; i < StoreData.data.length; i++) {
        if (StoreData.data[i].store_id == this.$route.params.storeid) {
          this.storeInfo = StoreData.data[i];
        }
      }
    },
  },
};
</script>
<style></style>
