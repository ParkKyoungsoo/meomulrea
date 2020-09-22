<template>
  <v-card class="mx-auto" max-width="320" outlined>
    <v-list-item three-line>
      <v-list-item-content>
        <div>{{ storeData.name }}</div>
      </v-list-item-content>
      <v-list-item-avatar tile size="200" color="grey" />
    </v-list-item>

    <v-card-actions>
      <v-btn text>가게 보러가기</v-btn>
      <v-btn text>파티 구하러가기</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    storeData: {},
  },
};
</script>
