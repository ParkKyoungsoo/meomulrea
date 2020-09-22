<template>
  <v-app-bar app color="indigo" dark>
    <v-toolbar-title>
      <router-link style="text-decoration: none; color: white" to="/">
        Home
      </router-link>
    </v-toolbar-title>
    <v-col cols="12" sm="4" justify="center" align="center">
      <v-select :items="userAddress" label="주소를 선택해주세요" dense solo />
    </v-col>
    <button @click="showAddrModal = true">추가하기</button>
    <v-toolbar-title>
      <router-link style="text-decoration: none; color: white" to="/Login">
        Login
      </router-link>
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
export default {
  data: () => ({
    userAddress: [1, 2, 3, 4, 5],
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
