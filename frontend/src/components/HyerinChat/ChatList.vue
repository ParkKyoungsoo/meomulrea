<template>
  <v-container v-on:scroll="onScroll" ref="chatlistContainer">
    <v-row no-gutters>
      <v-col v-for="chat in chatList" :key="chat.room_name" cols="12" sm="4">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <!-- 채팅방 키값(왜 있는지는 모르겠음) -->
              <div class="overline mb-4">{{ chat.key }}</div>
              <!-- 방 제목 -->
              <v-list-item-title class="headline mb-1">{{
                chat.room_name
              }}</v-list-item-title>
              <!-- v-if 채팅방의 현재 인원수 -->
              <!-- <v-list-item-subtitle v-if="chat.usercount != null"
                > 참가인원 : {{ chat.usercount }} 명</v-list-item-subtitle
              > -->
              <!-- v-else 채팅방의 인원수가 로드되지 않았을 경우 -->
              <!-- <v-list-item-subtitle v-else
                >Loading user count...</v-list-item-subtitle
              > -->
            </v-list-item-content>
          </v-list-item>
          <v-card-actions>
            <!-- 카드를 클릭했을 때의 이벤트 -->
            <v-btn
              text
              @click="ldj_enterChat(chat)"
              v-if="!chat.isAlreadyJoined && chat.usercount != null"
              >참여하기</v-btn
            >
            <!-- 참여하고 있는 채팅방인 경우 -->
            <v-btn text disabled v-if="chat.isAlreadyJoined">Joined</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
// const baseURL = "http://127.0.0.1:8000/";

export default {
  props: {
    store_id: [],
  },
  data() {
    return {
      chatList: [],
      loading: false,
    };
  },
  mounted() {
    // 여기서 ldj_loadChats 호출
    this.ldj_loadChats();
  },
  computed: {
    ...mapGetters("server", ["getBaseURL"]),
  },
  methods: {
    ldj_loadChats() {
      // backend 요청
      // this.chatList = backend에서 전달받은 데이터
      axios
        .post(
          this.getBaseURL.baseURL + "api/chatroom/store_chatroom_list/",
          {
            store_id: this.store_id,
          },
          {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
          }
        )
        .then((res) => {
          console.log(res.data);
          // this.chats = res.data;
          if (res.data.message) {
            this.chatList = [];
          } else {
            this.chatList = res.data;
          }
        });
    },
    ldj_loadChats_On_Scrool(lastKey) {
      // backend 요청
      // this.chatList에 Append
    },
    ldj_enterChat(chat) {
      const key = chat.store_id + "_" + chat.user;
      this.$router.push("/hrchat/" + key + "/" + chat.room_name);
    },
    onScroll() {
      if (
        window.top.scrollY + window.innerHeight >=
          document.body.scrollHeight - 100 &&
        !this.loading
      ) {
        this.ldj_loadChats_On_Scrool(
          this.chatList[this.chatList.length - 1].key
        );
      }
    },
  },
  created() {
    window.addEventListener("scroll", this.onScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.onScroll);
  },
  // watch: {
  //   loadedChats: {
  //     deep: true,
  //     handler() {},
  //   },
  // },
};
</script>
