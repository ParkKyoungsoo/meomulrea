const state = {
  userAddress: "",
};

const getters = {
  getUserInfo: function(state) {
    console.log("userInfo getter!!");
    return state;
  },
};

const mutations = {
  setUserInfo: function(state, payload) {
    console.log("userInfo setter!!");
    state.userAddress = payload.userAddress;
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
