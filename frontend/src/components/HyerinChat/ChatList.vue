<template>
  <v-container v-on:scroll="onScroll" ref="chatlistContainer">
    <v-row no-gutters>
      <v-col v-for="chat in chats" :key="chat.name" cols="12" sm="4">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">{{ chat.key }}</div>
              <v-list-item-title class="headline mb-1">{{
                chat.name
              }}</v-list-item-title>
              <v-list-item-subtitle v-if="chat.userCount != null"
                >{{ chat.userCount }} members have joined this
                chat.</v-list-item-subtitle
              >
              <v-list-item-subtitle v-else
                >Loading user count...</v-list-item-subtitle
              >
            </v-list-item-content>
          </v-list-item>
          <v-card-actions>
            <v-btn
              text
              @click="enterChat(chat)"
              v-if="!chat.isAlreadyJoined && chat.userCount != null"
              >Join</v-btn
            >
            <v-btn text disabled v-if="chat.isAlreadyJoined">Joined</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
const baseURL = "http://127.0.0.1:8000/";
// const baseURL =
//   "http://ec2-54-180-109-206.ap-northeast-2.compute.amazonaws.com/";

export default {
  data() {
    return {
      loadedChats: [],
      loading: false,
    };
  },

  created:async function(){
    await this.getPartys();
    window.addEventListener("scroll", this.onScroll);
  },

  methods: {
    async getPartys(){
      await axios.post(
        baseURL + "api/chatroom/store_chatroom_list/",
        {
          store_id : 15544
        },
        {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
        }
      )
      .then((res)=>{
        console.log(res.data);
        this.chats = res.data;
      })
    },

    enterChat(chat) { // 채팅방에 들어가기 - 수정해야댐 

      this.$router.push("/hrchat/" + chat.store_id);
     
    },
  
    getUserCountForChat(chat) { // 채팅참여자 조회 
      
    },
  },

  destroyed() {

    window.removeEventListener("scroll", this.onScroll);

  },

};
</script>
