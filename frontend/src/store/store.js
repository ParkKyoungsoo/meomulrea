import Vue from "vue";
import Vuex from "vuex";
import Location from "./Location";
import ShopList from "./ShopList";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    location: Location,
    shopList: ShopList,
  },
  plugins: [
    createPersistedState({
      paths: ["Location.state", "ShopList"],
    }),
  ],
});
