<template>
  <v-container v-on:scroll="onScroll" ref="chatlistContainer">
    <v-row no-gutters>
      <v-col v-for="(chat,index) in chatList" :index="index" :key="chat.room_name" cols="12" sm="4">
        <div class="chatlist">
          <img :src="url('../../assets/image/home'+index+'.png')" alt="" />
          <p class="title">{{chat.room_name}}</p>
          <div class="overlay"></div>
          <v-btn @click="mvtochatting(chat)">참가하기</v-btn>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
const baseURL = "http://127.0.0.1:8000/";

export default {
  props:{
    store_id: []
  },
  data() {
    return {
      chatList: [],
      loading: false,
    };
  },
  mounted() {
      // 여기서 ldj_loadChats 호출
      this.ldj_loadChats()
  },
  // computed: {
  //   user() {
  //     console.log("userInfo", this.$store.getters.user);
  //     return this.$store.getters.user;
  //   }
  // },
  methods: {
    ldj_loadChats(){
      // backend 요청
      // this.chatList = backend에서 전달받은 데이터
      axios.post(
        baseURL + "api/chatroom/store_chatroom_list/",
        {
          store_id : this.store_id
        },
        {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
        }
      )
      .then((res)=>{
        console.log(res.data);
        // this.chats = res.data;
        if(res.data.message){
          this.chatList = []
        }else{
          this.chatList = res.data
        }
        
      })
    },
    ldj_loadChats_On_Scrool(lastKey) {
      // backend 요청
      // this.chatList에 Append
    },
    mvtochatting(chat){
      const key = chat.store_id +"_" +  chat.user
      this.$router.push("/hrchat/" + key + '/' +chat.room_name);
    },
    onScroll() {
      if (window.top.scrollY + window.innerHeight >=document.body.scrollHeight - 100 && !this.loading) {
        this.ldj_loadChats_On_Scrool(this.chatList[this.chatList.length - 1].key);
      }
    },
  },
  created() {
    window.addEventListener("scroll", this.onScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.onScroll);
  },
  watch: {
    loadedChats: {
      deep: true,
      handler() {},
    },
  },
};
</script>

<style scoped>
.chatlist {
  position: relative;
  margin: 10%;
  width: 300px;
  height: 300px;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0);
  transition: background 0.5s ease;
}

.container:hover .overlay {
  display: block;
  background: rgba(0, 0, 0, .3);
}

img {
  position: absolute;
  width: 500px;
  height: 300px;
  left: 0;
}

.title {
  position: absolute;
  width: 500px;
  left: 0;
  top: 120px;
  font-weight: 700;
  font-size: 30px;
  text-align: center;
  text-transform: uppercase;
  color: white;
  z-index: 1;
  transition: top .5s ease;
}

.container:hover .title {
  top: 90px;
}

.button {
  position: absolute;
  width: 500px;
  left:0;
  top: 180px;
  text-align: center;
  opacity: 0;
  transition: opacity .35s ease;
}

.button a {
  width: 200px;
  padding: 12px 48px;
  text-align: center;
  color: white;
  border: solid 2px white;
  z-index: 1;
}

.container:hover .button {
  opacity: 1;
}

</style>
