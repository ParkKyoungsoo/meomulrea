<template>
  <!-- <div>
    <textarea class="ldj" id="chat-log" cols="100" rows="20"></textarea><br>
    <input class="ldj" id="chat-message-input" type="text" size="100"><br>
    <input class="ldj" id="chat-message-submit" @click="yhr()" v-on:keyup.enter="yhr()" type="button" value="Send">
  </div> -->
  <div class="chat">
  <ul>
    <li><img src="http://maxme-life.ru/tests/img2.jpg">
      <div class="message">Салют)</div>
    </li>
    
    
    <li><img src="http://maxme-life.ru/tests/img1.jpg">
      <div class="message">Добрый день,Макс!Пока не уехал,скинь заданице.)</div>
    </li>
    
    <li><img src="http://maxme-life.ru/tests/img2.jpg">
      <div class="message">Хорошо, только при одном условии, ты выполнишь все задание самостоятельно! Ладно?</div>
    </li>
    
    <li><img src="http://maxme-life.ru/tests/img1.jpg">
      <div class="message">Я постараюсь :)</div>
    </li>
  </ul>
  <input type="text" placeholder="Написать сообщение" /><button>Отправить</button>
</div>
</template>

<script>
export default {
    data(){
        return {
            roomName: "",
            chatSocket: ""
        }
    },
    created: function() {
        this.roomName = this.$route.params.roomName;
        this.chatSocket = new WebSocket(
            'ws://'
            + "127.0.0.1:8000"
            + '/ws/chat/'
            + this.roomName
            + '/'
        ) // ws://127.0.0.1:8000/ws/chat/roomName/
        console.log(this.chatSocket);
        console.log(this.roomName);
        this.chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            document.querySelector('#chat-log').value += (data.message + '\n');
        };
        this.chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };
    },
    methods: {
        yhr(){
            const messageInputDom = document.querySelector('#chat-message-input');
            const message = messageInputDom.value;
            this.chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInputDom.value = '';
        }
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

html{
  width:100%;
  height:100%;
  background:linear-gradient(145deg ,#072732,#215768);
}

.chat{
  font:12px Trebuchet MS;
  min-width:300px;
  width:300px;
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
  box-sizing:border-box;
   
}


.chat ul li:nth-child(odd) img{
  float:right;
}

.chat ul li:nth-child(odd) .message{
  margin-right:90px;
  margin-left:0;
  background:#def1ff;
}



.chat ul li:nth-child(even) .message{
  background:#daffb1;
}




.chat ul li:nth-child(odd) .message:before{
  content:"";
  width:0px;
  height:0px;
  position:absolute;
  right:0;
  top:0;
  margin-right:-15px;
  border-top:15px solid #def1ff;
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
  border-top:15px solid #daffb1;
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
}

</style>