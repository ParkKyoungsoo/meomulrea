const state = {
  // 로컬 <-> 서버 전환시 이 URL만 바꿔주면 됩니다.
  baseURL: "http://127.0.0.1:8000/",
  // baseURL: "http://ec2-54-180-109-206.ap-northeast-2.compute.amazonaws.com/",
};

const getters = {
  getBaseURL: function(state) {
    return state;
  },
};

export default {
  strict: process.env.NODE_ENV !== "production",
  state: {
    ...state,
  },
  getters,
  namespaced: true,
};
