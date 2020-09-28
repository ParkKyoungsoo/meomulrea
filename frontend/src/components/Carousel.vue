<template>
  <div class="content" style="width:100%;">
    <carousel  :per-page="1" :mouse-drag="false" :autoplay="true" :autoplayTimeout="5000" :loop="true" :autoplayHoverPause="true" :paginationPosition="bottom-overlay">
      <slide v-for="(item, index) in storeData" :key="index">
        <!-- <img :src="item.store_id" alt="item.store_id" /> -->
        <img height="150vh!important" width="1550vh" src="../assets/image/background.jpg">
      </slide>
    </carousel>
  </div>
</template>

<script>
import Vue from "vue";
import VueCarousel from "vue-carousel";

Vue.use(VueCarousel);

export default {
  props: {
    storeData: {},
  },
  components: {},
  data: () => ({}),
};
</script>

<style>
.carousel-item img {
        height:100vh!important ;
    }
</style>
