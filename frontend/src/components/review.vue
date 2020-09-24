<template>
  <v-container>
    <div style="display: flex;">
      <v-text-field></v-text-field>
      <v-btn @click="registerReview">리뷰 쓰기</v-btn>
    </div>
    <div style="text-align: left;">
      <v-list-item two-line>
        <v-list-item-content>
          <v-list-item-title>유저 닉네임</v-list-item-title>
          <v-list-item-subtitle>리뷰 내용</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-list-item two-line>
        <v-list-item-content>
          <v-list-item-title>유저 닉네임</v-list-item-title>
          <v-list-item-subtitle>리뷰 내용</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-list-item two-line>
        <v-list-item-content>
          <v-list-item-title>유저 닉네임</v-list-item-title>
          <v-list-item-subtitle>리뷰 내용</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-list-item two-line>
        <v-list-item-content>
          <v-list-item-title>유저 닉네임</v-list-item-title>
          <v-list-item-subtitle>리뷰 내용</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-list-item two-line>
        <v-list-item-content>
          <v-list-item-title>유저 닉네임</v-list-item-title>
          <v-list-item-subtitle>리뷰 내용</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </div>
  </v-container>
</template>

<script>
export default {
  methods: {
    registerReview() {
      console.log("axios요청!!");
    },
  },
};
</script>
