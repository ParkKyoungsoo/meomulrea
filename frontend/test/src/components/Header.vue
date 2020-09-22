<template>
  <div class="header">
    <h1>헤더 영역</h1>
    <div class="flexbox">
      <div class="leftSide">
        <router-link style="text-decoration: none; color: black;" to="/">
          Home
        </router-link>
      </div>
      <div class="center">
        <select>
          <option disabled value="">주소를 선택해 주세요.</option>
          <option v-for="(addr, index) in userAddress" :key="index">
            {{ addr }}
          </option>
        </select>
        <button @click="showAddrModal = true">추가하기</button>
      </div>
      <div class="rightSide">
        <router-link style="text-decoration: none; color: black;" to="/Login">
          Login
        </router-link>
      </div>
    </div>
  </div>
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
.header {
  border: 1px solid black;
  background-color: #e9691e;
}
.flexbox {
  display: flex;
}

.leftSide {
  justify-content: flex-start;
}
.center {
  justify-content: center;
}
.rightSide {
  justify-content: flex-end;
}
</style>
