import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

import Login from "./pages/LogIn.vue";
import Content from "./pages/Content.vue";
import StoreList from "./pages/StoreList.vue";
import StoreDetail from "./pages/StoreDetail.vue";
import Create from "./components/Chat/Create.vue";
import Chat from "./components/Chat/Chat.vue";
import ChatList from "./components/Chat/ChatList";

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/",
      name: "Home",
      component: Content,
    },
    {
      path: "/storelist/:category",
      name: "storelist",
      component: StoreList,
    },
    {
      path: "/storedetail/:storeid",
      name: "storedetail",
      component: StoreDetail,
    },
    {
      path: "/chat",
      name: "chat",
      component: Chat,
    },
    {
      path: "/create",
      name: "CreateChat",
      component: Create,
    },
    {
      path: "/chat/:id",
      name: "Chat",
      component: Chat,
      props: true,
    },
    {
      path: "/discover",
      name: "JoinChat",
      component: ChatList,
    },
  ],
});
