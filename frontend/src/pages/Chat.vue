<template>
  <v-main>
    <v-container fluid style="padding: 0;">
      <!-- <v-app> -->
      <!-- <v-app-bar app class="light-blue darken-1">
      <v-app-bar-nav-icon @click.native.stop="drawerToggle = !drawerToggle"></v-app-bar-nav-icon>
      <v-toolbar-title>
        <router-link to="/chat/0" tag="span" style="cursor: pointer">Vuetify Chat</router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items v-for="item in menuItems" v-bind:key="item.route">
        <v-btn text :key="item.title" :to="item.route">
          <v-icon left>{{ item.icon }}</v-icon>
          <div class="hidden-xs-only">{{ item.title }}</div>
        </v-btn>
      </v-toolbar-items>
    </v-app-bar> -->
      <!-- </v-app> -->
      <v-row no-gutters>
        <v-col sm="2" class="scrollable">
          <chats></chats>
        </v-col>
        <v-col sm="10" style="position: relative;">
          <div
            class="chat-container"
            v-on:scroll="onScroll"
            ref="chatContainer"
          >
            <message :messages="messages" @imageLoad="scrollToEnd"></message>
          </div>
          <!-- <emoji-picker :show="emojiPanel" @close="toggleEmojiPanel" @click="addEmojiToMessage"></emoji-picker> -->
          <div class="typer">
            <input
              type="text"
              placeholder="Type here..."
              v-on:keyup.enter="sendMessage"
              v-model="content"
            />
            <!-- <v-btn icon class="blue--text emoji-panel" @click="toggleEmojiPanel">
            <v-icon>mdi-emoticon-outline</v-icon>
          </v-btn> -->
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import Message from "../components/Message.vue";
//   import EmojiPicker from './parts/EmojiPicker.vue'
import Chats from "../components/Chats.vue";
import * as firebase from "firebase";

export default {
  data() {
    return {
      content: "",
      chatMessages: [],
      // emojiPanel: false,
      currentRef: {},
      loading: false,
      totalChatHeight: 0,
    };
  },
  props: ["id"],
  mounted() {
    this.loadChat();
    this.$store.dispatch("loadOnlineUsers");
  },
  components: {
    message: Message,
    //   'emoji-picker': EmojiPicker,
    chats: Chats,
  },
  computed: {
    messages() {
      return this.chatMessages;
    },
    username() {
      return this.$store.getters.user.username;
    },
    menuItems() {
      let items = [
        { icon: "mdi-face", title: "Register", route: "/register" },
        { icon: "mdi-lock-open", title: "Login", route: "/login" },
      ];
      let user = firebase.auth().currentUser;
      if (user) {
        items = [
          { icon: "mdi-forum", title: "Create a Chat", route: "/create" },
          { icon: "mdi-chat", title: "Chat List", route: "/discover" },
        ];
      }
      return items;
    },
    userIsAuthenticated() {
      return (
        this.$store.getters.user !== null &&
        this.$store.getters.user !== undefined
      );
    },
    onlineUsers() {
      return this.$store.getters.onlineUsers;
    },
    onNewMessageAdded() {
      const that = this;
      let onNewMessageAdded = function(snapshot, newMessage = true) {
        let message = snapshot.val();
        message.key = snapshot.key;
        /*eslint-disable */
        var urlPattern = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/gi;
        /*eslint-enable */
        message.content = message.content
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;")
          .replace(/"/g, "&quot;")
          .replace(/'/g, "&#039;");
        message.content = message.content.replace(
          urlPattern,
          "<a href='$1'>$1</a>"
        );
        if (!newMessage) {
          that.chatMessages.unshift(that.processMessage(message));
          that.scrollTo();
        } else {
          that.chatMessages.push(that.processMessage(message));
          that.scrollToEnd();
        }
      };
      return onNewMessageAdded;
    },
  },
  watch: {
    "$route.params.id"(newId, oldId) {
      this.currentRef.off("child_added", this.onNewMessageAdded);
      this.loadChat();
    },
  },
  methods: {
    loadChat() {
      this.totalChatHeight = this.$refs.chatContainer.scrollHeight;
      this.loading = false;
      if (this.id !== undefined) {
        this.chatMessages = [];
        let chatID = this.id;
        this.currentRef = firebase
          .database()
          .ref("messages")
          .child(chatID)
          .child("messages")
          .limitToLast(20);
        this.currentRef.on("child_added", this.onNewMessageAdded);
      }
    },
    onScroll() {
      let scrollValue = this.$refs.chatContainer.scrollTop;
      const that = this;
      if (scrollValue < 100 && !this.loading) {
        this.totalChatHeight = this.$refs.chatContainer.scrollHeight;
        this.loading = true;
        let chatID = this.id;
        let currentTopMessage = this.chatMessages[0];
        if (currentTopMessage === undefined) {
          this.loading = false;
          return;
        }
        firebase
          .database()
          .ref("messages")
          .child(chatID)
          .child("messages")
          .orderByKey()
          .endAt(currentTopMessage.key)
          .limitToLast(20)
          .once("value")
          .then(function(snapshot) {
            let tempArray = [];
            snapshot.forEach(function(item) {
              tempArray.push(item);
            });
            if (tempArray[0].key === tempArray[1].key) return;
            tempArray.reverse();
            tempArray.forEach(function(child) {
              that.onNewMessageAdded(child, false);
            });
            that.loading = false;
          });
      }
    },
    processMessage(message) {
      /*eslint-disable */
      // var imageRegex = /([^\s\']+).(?:jpg|jpeg|gif|png)/i
      /*eslint-enable */
      // if (imageRegex.test(message.content)) {
      //   message.image = imageRegex.exec(message.content)[0]
      // }
      // var emojiRegex = /([\u{1f300}-\u{1f5ff}\u{1f900}-\u{1f9ff}\u{1f600}-\u{1f64f}\u{1f680}-\u{1f6ff}\u{2600}-\u{26ff}\u{2700}-\u{27bf}\u{1f1e6}-\u{1f1ff}\u{1f191}-\u{1f251}\u{2934}-\u{1f18e}])/gu
      // if (emojiRegex.test(message.content)) {
      //   message.content = message.content.replace(emojiRegex, '<span class="emoji">$1</span>')
      // }
      return message;
    },
    sendMessage() {
      if (this.content !== "") {
        // this.$store.dispatch('sendMessage', { username: this.username, content: this.content, date: new Date().toString(), chatID: this.id })
        firebase
          .database()
          .ref("messages")
          .child(this.chatID)
          .child("messages")
          .push(this.content)
          .then((data) => {});
        this.content = "";
      }
    },
    scrollToEnd() {
      this.$nextTick(() => {
        var container = this.$el.querySelector(".chat-container");
        container.scrollTop = container.scrollHeight;
      });
    },
    scrollTo() {
      this.$nextTick(() => {
        let currentHeight = this.$refs.chatContainer.scrollHeight;
        let difference = currentHeight - this.totalChatHeight;
        var container = this.$el.querySelector(".chat-container");
        container.scrollTop = difference;
      });
    },
    // addEmojiToMessage (emoji) {
    //   this.content += emoji.value
    // },
    // toggleEmojiPanel () {
    //   this.emojiPanel = !this.emojiPanel
    // }
  },
};
</script>
<style scoped src="../assets/chat.css"></style>
