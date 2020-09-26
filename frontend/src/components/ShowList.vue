<template>
  <v-card class="mx-auto" max-width="320" outlined>
    <v-col>
      <v-row justify="center">
        <div>{{ storeData.category }}</div>
      </v-row>
      <v-row justify="center">
        <v-list-item-avatar tile size="200" color="grey" />
      </v-row>
    </v-col>

    <v-card-actions>
      <v-btn depressed color="primary" @click="goToShop">가게 보러가기</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    storeData: {},
  },

  methods: {
    goToShop: function() {
      this.$router.push("/storelist/" + this.storeData.category);
    },
    mvpage: function(){
      this.$router.push("/chat");
    }
  },
};
</script>
