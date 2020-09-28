const state = {
  userAddress: "",
};

const getters = {
  getUserInfo: function(state) {
    return state;
  },
};

const mutations = {
  setUserInfo: function(state, payload) {
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
