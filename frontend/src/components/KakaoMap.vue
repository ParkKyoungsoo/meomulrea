<template>
  <div id="map" style="height: 50vh;">
    map
  </div>
</template>
<script>
import all_store_encoding2 from "../assets/datas/all_store_encoding2.json";
import { mapGetters, mapMutations } from "vuex";

export default {
  props: {
    storeData: {},
    category: null,
  },
  created() {
    console.log("child", this.storeData);
  },
  computed: {
    ...mapGetters("location", ["getLocation"]),
    ...mapGetters("shopList", ["getShopList"]),
  },
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
  },

  methods: {
    ...mapMutations(("shopList", ["setShopList"])),

    initMap() {
      console.log("storeInfo", this.storeData);

      var container = document.getElementById("map");
      var options = {
        center: new kakao.maps.LatLng(
          console.log("lat", this.storeData.latitude),
          console.log("lng", this.storeData.longitude),
          this.storeData.latitude,
          this.storeData.longitude
        ),
        level: 7,
      };
      var map = new kakao.maps.Map(container, options); //마커추가하려면 객체를 아래와 같이 하나 만든다.
      var marker = new kakao.maps.Marker({ position: map.getCenter() });
      marker.setMap(map);

      // var imageSrc =
      //   "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
      // var imageSize = new kakao.maps.Size(24, 35);
      // var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

      // for (var i = 0; i < all_store_encoding2.data.length; i++) {
      //   if (
      //     all_store_encoding2.data[i].address.includes(this.getLocation.dong) &&
      //     all_store_encoding2.data[i].category.includes(this.category)
      //   ) {
      //     var latlng = new kakao.maps.LatLng(
      //       all_store_encoding2.data[i].latitude,
      //       all_store_encoding2.data[i].longitude
      //     );
      //     var title = all_store_encoding2.data[i].store_name;

      //     marker = new kakao.maps.Marker({
      //       map: map, // 마커를 표시할 지도
      //       position: latlng, // 마커를 표시할 위치
      //       title: title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
      //       image: markerImage, // 마커 이미지
      //     });
      //     storeList.push(all_store_encoding2.data[i]);
      //   }
      // }
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
