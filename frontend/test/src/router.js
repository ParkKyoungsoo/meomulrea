import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

import Login from "./components/Login.vue";
import Content from "./components/Content.vue";
import ShowList from "./components/ShowList.vue";

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
      path: "/showlist/:foodid",
      name: "showlist",
      component: ShowList,
    },
  ],
});
