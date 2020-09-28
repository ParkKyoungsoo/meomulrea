<template>
  <v-app id="app">
    <!-- <Header /> -->
    <router-view />
  </v-app>
</template>

<script>
// import Header from "./components/Header.vue";

export default {
  name: "App",
  components: {
    // Header,
  },
};
</script>
<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  /* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  font-family: 'Do Hyeon', 'Jua', sans-serif;
  /* font-family: 'Jua', sans-serif; */
  text-align: center;
  /* color: #2c3e50; */
}
</style>
