<template>
  <div>
    <v-btn @click='mvtopage()'>
      <v-icon left>mdi-forum</v-icon>
      <div class="hidden-xs-only">파티만들기</div>
    </v-btn>
    <v-btn text to="/discover">
      <v-icon left>mdi-chat</v-icon>
      <div class="hidden-xs-only">파티찾기</div>
    </v-btn>
    <div>
      <ChatList />
    </div>
  </div>
</template>
<script>
// import ChatList from "./Chat/ChatList.vue";
import ChatList from "./HyerinChat/ChatList.vue";

export default {
  props:{
    storeInfo: []
  },

  components: {
    ChatList,
  },
  methods:{
    mvtopage(){
      console.log(this.storeInfo.store_id)
      this.$router.push('/create/'+this.storeInfo.store_id)
    }
  }

};
</script>
