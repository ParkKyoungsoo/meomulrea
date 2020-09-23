import Vue from "vue";
import Vuex from "vuex";
import Location from "./Location";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    location: Location,
  },
  plugins: [
    createPersistedState({
      paths: ["Location.state"],
    }),
  ],
});
