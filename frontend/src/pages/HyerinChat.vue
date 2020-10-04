<template>
  <div>
    <textarea class="ldj" id="chat-log" cols="100" rows="20"></textarea><br>
    <input class="ldj" id="chat-message-input" type="text" size="100"><br>
    <input class="ldj" id="chat-message-submit" @click="yhr()" v-on:keyup.enter="yhr()" type="button" value="Send">
  </div>
</template>

<script>
export default {
    data(){
        return {
            roomName: "",
            chatSocket: "",
            message: ""
        }
    },
    created: function() {
        this.roomName = this.$route.params.roomName; // 채팅방 이름 
        this.chatSocket = new WebSocket( // 웹소켓에 연결하는 부분 
            'ws://'
            + "127.0.0.1:8000"
            + '/ws/chat/'
            + this.roomName
            + '/'
        ) // ws://127.0.0.1:8000/ws/chat/roomName/
        console.log(this.chatSocket);
        console.log(this.roomName);
        
        // 이벤트 등록. onmessage -> chatSocket에 메세지가 도착했을 때 일어날 이벤트를 여기에 작성.
        this.chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            const nickname = data.message.split("&&&&")[0]
            const msg = data.message.split("&&&&")[1]
            document.querySelector('#chat-log').value += (nickname+" ) "+ msg + '\n');
        };
        this.chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };
    },
    methods: {
        yhr(){
            const messageInputDom = document.querySelector('#chat-message-input');
            this.message = messageInputDom.value; // message : 채팅창에 입력한 텍스트 
            // message = 닉네임 + "&&&&" + message
            this.message = "어피치"+"&&&&"+ this.message
            this.chatSocket.send(JSON.stringify({
                'message': this.message
            }));
            messageInputDom.value = '';
        }
    }
}
</script>

<style>
.ldj {
    background-color: aliceblue !important;
    border: black !important;
}
.ldj:focus{
    background-color: aliceblue !important;
    border: black !important;
}


</style>