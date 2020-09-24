<template>
  <v-app-bar app color="indigo" dark>
    <v-toolbar-title>
      <router-link style="text-decoration: none; color: white;" to="/">
        Home
      </router-link>
    </v-toolbar-title>
    <v-spacer />
    <v-toolbar-title>
      <v-col>
        <v-select
          v-model="seletedAddress"
          @change="changeAddress"
          :items="userAddress"
          return-object
          dense
          solo
        />
      </v-col>
    </v-toolbar-title>
    <button @click="showAddrModal = true">추가하기</button>
    <v-spacer />
    <v-toolbar-title>
      <router-link style="text-decoration: none; color: white;" to="/Login">
        Login
      </router-link>
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
import user from "../assets/datas/user.json";
import { EventBus } from "../utils/EventBus.js";

export default {
  data: () => ({
    userAddress: user[0].nm_address,
    showAddrModal: false,
    seletedAddress: "",
  }),
  components: {},
  computed: {
    options: () => user[0].nm_address,
  },
  created() {
    console.log("userAddress", user[0]);
  },
  methods: {
    changeAddress: function() {
      EventBus.$emit("addressChange", this.seletedAddress);
    },
  },
};
</script>
<style>
.address {
  margin-top: 25px;
}
</style>
