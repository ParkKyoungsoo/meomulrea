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
.ldj {
    background-color: aliceblue !important;
    border: black !important;
}
.ldj:focus{
    background-color: aliceblue !important;
    border: black !important;
}


</style>