<template>
  <v-main>
    <v-container>
      가게 상세 정보
      <div style="display: flex;">
        <div style="background-color: rgb(132, 192, 245);">
          <div>가게 썸네일</div>
          <div>평점 : {{ this.storeInfo.average_rating }}</div>
        </div>
        <div style="background-color: rgb(132, 245, 132);">
          <div>{{ this.storeInfo.store_name }}</div>
          <div>{{ this.storeInfo.address }}</div>
          <div>최소 주문 금액 : {{ this.storeInfo.min_price }} 원</div>
          <div style="display: flex; justify-content: center;">
            휴무일 :
            <div>{{ this.storeInfo.mon == 1 ? "월" : null }}</div>
            <div>{{ this.storeInfo.tue == 1 ? "화" : null }}</div>
            <div>{{ this.storeInfo.wen == 1 ? "수" : null }}</div>
            <div>{{ this.storeInfo.thu == 1 ? "목" : null }}</div>
            <div>{{ this.storeInfo.fri == 1 ? "금" : null }}</div>
            <div>{{ this.storeInfo.sat == 1 ? "토" : null }}</div>
            <div>{{ this.storeInfo.sun == 1 ? "일" : null }}</div>
          </div>
        </div>
        <div style="background-color: rgb(245, 183, 132);">
          지도표시구역
        </div>
      </div>
      <div>{{ this.storeInfo }}</div>
    </v-container>
  </v-main>
</template>
<script>
import StoreData from "../assets/datas/all_store_encoding2.json";

export default {
  data() {
    return {
      storeInfo: "",
    };
  },
  created() {
    this.getStoreDetail();
  },
  methods: {
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
