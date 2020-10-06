<template>
  <div>
    <v-main>
      <!-- <div> -->
      <v-col>
        <Header />
      </v-col>
      <!-- <v-col style="border: 1px solid black; margin-top: 100px;">
        <textarea class="ldj" id="chat-log" cols="100" rows="20"></textarea><br>
        <input class="ldj" id="chat-message-input" type="text" size="100"><br>
        <input class="ldj" id="chat-message-submit" @click="yhr()" v-on:keyup.enter="yhr()" type="button" value="Send">
        </v-col> -->
        <!-- <v-col style="border: 1px solid red;"> -->
        <!-- <div class="chat">
        <ul>
            <li><img src="http://maxme-life.ru/tests/img2.jpg">
            <div class="message">메시지1</div>
            </li>
            
            
            <li><img src="http://maxme-life.ru/tests/img1.jpg">
            <div class="message">메시지2</div>
            </li>
            
            <li><img src="http://maxme-life.ru/tests/img2.jpg">
            <div class="message">Хорошо, только при одном условии, ты выполнишь все задание самостоятельно! Ладно?</div>
            </li>
            
            <li><img src="http://maxme-life.ru/tests/img1.jpg">
            <div class="message">Я постараюсь :)</div>
            </li>
        </ul>
        <input type="text" placeholder="Написать сообщение" /><button>Отправить</button>
        </div> -->
      <v-col>
        <div class="chat">
          <div style="float: left;">
            <div class="chat_header">
              <!-- <img class="chat_avatar" src="http://www.naturaloil.ph/wp-content/uploads/2015/11/John_Doe.jpg"/>채팅방이름 -->
              <!-- <div class="chat_status">ONLINE</div> -->
              {{ roomName }}
            </div>
            <button @click="exit()">나가기</button>
          </div>
          <div class="chat_s">
            <div v-for="(chatting, index) in chattings" :key="index">
              <div v-if="$cookies.get('nickname') === chatting.nickname" style="float:right;"> {{ chatting.nickname }}
                <div class="chat_bubble-2">{{ chatting.msg }}</div>
              </div>
              <div v-else>
                <div style="float:left; width:60%;">
                  {{ chatting.nickname }}
                  <div class="chat_bubble-1">{{ chatting.msg }}</div>
                </div>
              </div>
            </div>
                <!-- <div class="chat_bubble-1">Hi</div> -->
                <!-- <div class="chat_bubble-1">How are you?</div>
                <div class="chat_bubble-2">Fine. What about you?</div>
                <div class="chat_bubble-1">I'm great. Wanna meet?</div>
                <div class="chat_bubble-2">Sure</div>
                <div class="chat_bubble-2">I'll see you soon</div>
                <div class="chat_bubble-1">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla volutpat augue ac ultrices malesuada. Fusce varius urna id dignissim vestibulum. Integer rutrum, purus sit amet tincidunt molestie, diam dui pulvinar nulla, rhoncus facilisis elit mi sit amet lorem.</div>
                <div class="chat_bubble-2">Huh?</div>
                <div class="chat_bubble-1">Just Testing &#x1F609;</div> -->
          </div>
          <div class="chat_input">
            <input
              placeholder="메시지를 작성하세요"
              class="chat_text"
              v-model="message"
            />
            <v-btn
              class="chat_submit fa fa-send"
              @click="yhr()"
              v-on:keyup.enter="yhr()"
              >전송</v-btn
            >
            <!-- onkeypress="if(event.keyCode === 13){add()}" -->
            <!-- onclick="add()" -->
          </div>
        </div>
      </v-col>
    </v-main>
  </div>
</template>

<script>
import Header from "../components/Header.vue";
import { mapGetters } from "vuex";
export default {
  components: {
    Header,
  },
  data() {
    return {
      roomName: "",
      roomNumber: "",
      chatSocket: "",
      message: "",
      chattings: [],
    };
  },
  created() {
    this.roomNumber = this.$route.params.roomNumber; // 채팅방 uid
    this.roomName = this.$route.params.roomName; // 채팅방 이름
    this.chatSocket = new WebSocket( // 웹소켓에 연결하는 부분
      "ws://" +
        // "ec2-54-180-109-206.ap-northeast-2.compute.amazonaws.com" +
        "127.0.0.1:8000" +
        "/ws/chat/" +
        this.roomNumber +
        "/"
    ); // ws://127.0.0.1:8000/ws/chat/roomName/
    console.log(this.chatSocket);

    // 이벤트 등록. onmessage -> chatSocket에 메세지가 도착했을 때 일어날 이벤트를 여기에 작성.
    this.chatSocket.onmessage = (e) => {
      const data = JSON.parse(e.data);
      const nickname = data.message.split("&&&&")[0];
      const msg = data.message.split("&&&&")[1];
      this.chattings.push({ nickname: nickname, msg: msg });
      // document.querySelector('#chat-log').value += (nickname+" ) "+ msg + '\n');
      console.log(this.chattings);
    };
    this.chatSocket.onclose = function() {
      console.error("Chat socket closed unexpectedly");
    };
  },
  computed: { ...mapGetters("server", ["getBaseURL"]) },
  methods: {
    exit() {
      location.href = "/home";
    },
    yhr() {
      // const messageInputDom = document.querySelector('#chat-message-input');
      // this.message = messageInputDom.value; // message : 채팅창에 입력한 텍스트
      // message = 닉네임 + "&&&&" + message
      this.message = this.$cookies.get("nickname") + "&&&&" + this.message;
      this.chatSocket.send(
        JSON.stringify({
          message: this.message,
        })
      );
      // messageInputDom.value = '';
      this.message = "";
    },
  }
}
</script>

<style>
/* .ldj {
    background-color: aliceblue !important;
    border: black !important;
}
.ldj:focus{
    background-color: aliceblue !important;
    border: black !important;
} */

/* html{
  width:100%;
  height:100%;
  background:linear-gradient(145deg ,#072732,#215768);
} */

/* .chat{
  width: 80%;
  margin:auto auto;
}


.chat ul{
  margin:0;
  padding:0;
  border-bottom:2px solid #9c9c9c;
  padding-bottom:15px;
  margin-bottom:15px;
}


.chat ul li{
  width:100%;
  list-style-type:none;
  margin:5px 0;
  position:relative;
  display:inline-block;
}

.chat ul li img{
  float:left;
   border-radius:50px;
  box-shadow:0 2px 15px rgba(0,0,0,.5);
}
.chat ul li .message{
  margin-left:90px;
  background:blue;
  position:relative;
  min-height:25px;
  margin-top:35px;
  padding:10px;
  width: fit-content;
  box-sizing:border-box;
   
}


.chat ul li:nth-child(odd) img{
  float:right;
}

.chat ul li:nth-child(odd) .message{
  float: right;
  margin-right:90px;
  margin-left:0;
  background-color: rgba(233,105,30,0.3);
}



.chat ul li:nth-child(even) .message{
  background:rgba(0,0,0,0.3);
}




.chat ul li:nth-child(odd) .message:before{
  content:"";
  width:0px;
  height:0px;
  position:absolute;
  right:0;
  top:0;
  margin-right:-15px;
  border-top: 15px solid rgba(233,105,30,0.3);
  border-right:15px solid transparent;
}
.chat ul li:nth-child(even) .message:before{
  content:"";
  width:0px;
  height:0px;
  position:absolute;
  left:0;
  top:0;
  margin-left:-15px;
  border-top:15px solid rgba(0,0,0,0.3);
  border-left:15px solid transparent;
}



.chat input[type="text"]{
  width:70%; 
  margin:0; 
  border:0;
  padding:6px;
  background:#e5ecff;
  font:italic 12px Trebuchet MS;
  box-sizing:border-box;
}
.chat button{
  box-sizing:border-box;
  width:30%;padding:6px;font:12px Trebuchet MS; color:white;
  background:#84adfc;
  margin:0;
  border:0;
} */

@import "https://fonts.googleapis.com/css?family=Montserrat";
/* body{
    width:100%;
    height:100%;
    margin:0;
    padding:0;
    background:url(http://kriswhitewrites.com/wp-content/uploads/2013/06/landscape-mountains-snow-sky.jpg);
    background-size:cover;
    background-position:bottom
    } */
.chat {
  width: 80%;
  margin: auto auto;
  margin-top: 25px;
  height: 100%;
  border: 1px solid black;
  /* box-shadow:0 0 30px -5px grey; */
  /* margin:10vh calc(50vw - 200px); */
  background: #fafafa;
  position: relative;
  /* font-family:'Montserrat',sans-serif */
}
.chat_header {
  padding: 15px;
  border-bottom: 4px solid teal;
  background: #f0f0f0;
  color: teal;
}
/* .chat_status{
    font-size:11px;
    margin:4px 0 -4px
    } */
/* .chat_avatar{
    border: 1px solid black;
    float:right;
    width:fit-content;
    border-radius:50%;
    margin-top:-3px
} */
.chat_input {
  bottom: 0;
  /* width:calc(100% - 8px); */
  width: 100%;
  /* padding:10px 4px 6px; */
  background: #c8c8c8;
}
.chat_text {
  width: calc(85% - 10px);
  padding: 10px;
  /* box-sizing:border-box; */
  margin: 0 5px 5px;
  vertical-align: top;
  font-family: "Montserrat", sans-serif;
}
.chat_submit {
  width: calc(15% - 5px);
  padding: 10px;
  box-sizing: border-box;
  margin: 0 5px 5px 0;
  vertical-align: top;
  border: 1px solid teal;
  cursor: pointer;
  color: teal;
  border-radius: 0 8px 8px 0;
  transition: all 0.4s;
}
.chat_submit:hover {
  background: teal;
  color: #fff;
}
.chat_bubble-1,
.chat_bubble-2 {
  padding: 10px;
  margin: 13px 17px;
  width: 200px;
  font-size: 14px;
}
.chat_bubble-1 {
  border: 1px solid teal;
  border-radius: 12px 12px 12px 0;
}
.chat_bubble-2 {
  border: 1px solid grey;
  border-radius: 12px 12px 0 12px;
  margin-left: 160px;
}
.chat_s {
  max-height: calc(75vh - 86px - 29px);
  overflow-y: scroll;
  padding: 15px 0 0;
}
::-webkit-scrollbar {
  width: 13px;
}
::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 0 4px #fff;
  background: rgba(0, 0, 0, 0.2);
}
</style>
