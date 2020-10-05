import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

import Login from "./pages/LogIn.vue";
import Content from "./pages/Content.vue";
import StoreList from "./pages/StoreList.vue";
import StoreDetail from "./pages/StoreDetail.vue";
import Create from "./components/Chat/Create.vue";
// import Chat from "./components/Chat/Chat.vue";
import ChatList from "./components/Chat/ChatList";
import Signin from "@/components/User/Signin";
import test from "@/components/test.vue";
import HyerinChat from "./pages/HyerinChat.vue";

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/home",
      name: "Home",
      component: Content,
    },
    {
      path: "/",
      name: "Login",
      component: Login,
    },
    {
      path: "/storelist/:bigcategory",
      name: "storelist",
      component: StoreList,
    },
    {
      path: "/storedetail/:storeid",
      name: "storedetail",
      component: StoreDetail,
    },
    // {
    //   path: "/chat",
    //   name: "chat",
    //   component: Chat,
    // },
    {
      path: "/create/:storeid",
      name: "CreateChat",
      component: Create,
    },
    {
      path: "/discover",
      name: "JoinChat",
      component: ChatList,
    },
    {
      path: "/loginChat",
      name: "Signin",
      component: Signin,
    },
    {
      path: "/test",
      name: "test",
      component: test,
    },
    {
      path: "/hrchat/:roomNumber/:roomName",
      name: "HyerinChat",
      component: HyerinChat,
    },
  ],
});
