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
        <v-select :items="userAddress" label="주소를 선택해주세요" dense solo />
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

export default {
  data: () => ({
    userAddress: user.nm_address,
    showAddrModal: false,
  }),
  components: {},
};
</script>
<style>
.address {
  margin-top: 25px;
}
</style>
