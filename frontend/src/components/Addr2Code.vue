<template>
  <div id="map">
    <input v-model="address" />
    <button @click="searchAddr">조회</button>
    <div>{{ this.getLocation }}</div>
    <div>{{ lat }} | {{ lng }}</div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      address: "유성구 구암동",
      lat: 0,
      lng: 0,
    };
  },
  computed: {
    ...mapGetters("location", ["getLocation"]),
  },
  mounted() {
    window.kakao && window.kakao.maps ? null : this.addScript();
  },

  methods: {
    addScript() {
      let script = document.createElement("script");
      /* global kakao */

      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=a7bd2d0df8f5ae53b0c5e106842b94fd&libraries=services";
      document.head.appendChild(script);
    },

    searchAddr() {
      var geocoder = new kakao.maps.services.Geocoder();

      geocoder.addressSearch(this.address, (result, status) => {
        if (status === kakao.maps.services.Status.OK) {
          console.log(result);
          this.$store.commit("location/setLocation", {
            lat: result[0].y,
            lng: result[0].x,
            dong: result[0].address.region_3depth_name,
          });
          this.lat = result[0].y;
          this.lng = result[0].x;
        }
      });
    },
  },
};
</script>
