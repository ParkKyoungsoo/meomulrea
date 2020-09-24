import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

import Login from "./pages/LogIn.vue";
import Content from "./pages/Content.vue";
import StoreList from "./pages/StoreList.vue";
import StoreDetail from "./pages/StoreDetail.vue";
import Create from "./components/Create.vue";

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
      path: "/create",
      name: "CreateChat",
      component: Create,
    },
  ],
});
