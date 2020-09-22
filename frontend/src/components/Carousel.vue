<template>
  <div class="content">
    <carousel
      :per-page="1"
      :navigate-to="someLocalProperty"
      :mouse-drag="false"
      :autoplay="true"
      :autoplayTimeout="5000"
      :navigationEnabled="true"
      :loop="true"
    >
      <slide v-for="(item, index) in storeData" :key="index">
        <img :src="item.image" alt="item.name" />
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

<style></style>
