import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

import Login from "./components/LogIn.vue";
import Content from "./components/Content.vue";
import StoreList from "./components/StoreList.vue";
import StoreDetail from "./components/StoreDetail.vue";

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
  ],
});
