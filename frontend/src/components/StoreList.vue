<template>
  <v-main>
    <v-container>
      카테고리에 해당하는 가게 목록들
      <div>{{ $route.params.category }}</div>
      <v-row>
        <v-col>
          <v-row>
            1-1
          </v-row>
          <v-row>
            1-2
          </v-row>
        </v-col>
        <v-col>지도가 들어갈 예정</v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import axios from "axios";

export default {
  components: {},
  methods: {
    showShopList: function() {
      axios({
        method: "GET",
        url: ``,
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
  },
};
</script>
