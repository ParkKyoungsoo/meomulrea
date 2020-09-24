<template>
  <div id="map" style="height: 50vh;">
    map
  </div>
</template>
<script>
export default {
  props: {
    storeData: {
      lat: 0,
      lng: 0,
    },
  },
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
  },

  methods: {
    initMap() {
      var container = document.getElementById("map");
      var options = {
        center: new kakao.maps.LatLng(this.storeData.lat, this.storeData.lng),
        level: 3,
      };
      var map = new kakao.maps.Map(container, options); //마커추가하려면 객체를 아래와 같이 하나 만든다.
      var marker = new kakao.maps.Marker({ position: map.getCenter() });
      marker.setMap(map);
    },
    addScript() {
      const script = document.createElement("script");
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=a7bd2d0df8f5ae53b0c5e106842b94fd&libraries=services";
      document.head.appendChild(script);
    },
  },
};
</script>
