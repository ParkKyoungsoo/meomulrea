const state = {
  userAddress: [],
  isLogin: "",
};

const getters = {
  getUserInfo: function(state) {
    return state;
  },
  getIsLogin: function(state) {
    return state.isLogin;
  },
};

const mutations = {
  setUserInfo: function(state, payload) {
    console.log("setUserInfo called");
    state.userAddress = payload.userAddress;
  },
  setIsLogin: function(state, payload) {
    state.isLogin = payload.isLogin;
    console.log("setIsLogin called", state.isLogin);
  },
};

export default {
  strict: process.env.NODE_ENV !== "production",
  state: {
    ...state,
  },
  getters,
  mutations,
  namespaced: true,
};
