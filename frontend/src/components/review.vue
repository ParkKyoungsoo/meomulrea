<template>
  <v-container fluid>
    <div class="review-top">
      <!-- <h3 style="text-align:left">리뷰({{ review_cnt }}개)</h3> -->
      <hr />
      <br />
    </div>
    <div
      class="review-write"
      style="border: 1px solid silver; margin-bottom:10px; border-radius: 0.4em"
    >
      <div
        style="margin:10px"
        v-show="!usertype == this.$route.params.store_user_id"
      >
        <v-rating
          v-model="rating"
          style="text-align:left"
          background-color="orange lighten-3"
          color="orange"
          dense="true"
          half-increments="true"
          hover="true"
        ></v-rating
        ><br />
        <v-textarea
          outlined
          name="input-7-4"
          label="리뷰를 남겨보세요."
          v-model="myReview"
          color="orange"
        ></v-textarea>
        <div class="text-right">
          <v-btn
            v-show="rating == 0 || myReview == 0"
            @click="msg()"
            color="gray"
            style="color:darkgray"
            >등록</v-btn
          >
          <v-btn
            v-show="rating > 0 && myReview != 0"
            @click="registerReview()"
            color="orange"
            >등록</v-btn
          >
        </div>
        <hr />
      </div>
    </div>
    <div class="review-sort" style="display:inline;">
      <v-row>
        <h2 style="text-align:left; width: fit-content;">
          리뷰({{ this.review_cnt }}개)
        </h2>
        <v-spacer></v-spacer>
        <!-- <v-bottom-navigation style="box-shadow:none; width: fit-content; height: fit-content;" :value="value" color="orange" >
          <span><v-btn>최신순</v-btn></span>
          <span style>|</span>
          <span @click="getReviewHighScore()" style="cursor:pointer;">높은 평점순</span>
          <span>|</span>
          <span @click="getReviewLowScore()" style="cursor:pointer;">낮은 평점순</span>
        </v-bottom-navigation> -->
        <span @click="getReview()" style="cursor:pointer;">최신순&nbsp;</span>

        <span @click="getReviewHighScore()" style="cursor:pointer;"
          >높은 평점순</span
        >

        <span @click="getReviewLowScore()" style="cursor:pointer;"
          >낮은 평점순</span
        >
      </v-row>
    </div>
    <div
      class="review-origin"
      v-for="(review, index) in reviews"
      :key="review.id"
    >
      <div style="border: 1px solid silver; border-radius: 0.4em">
        <article class="review review-1">
          <v-row>
            <h3
              v-if="review.user === null"
              class="review-title"
              style="display: inline"
            >
              {{ review.userid }}
            </h3>
            <h3 v-else class="review-title">{{ review.user.username }}</h3>
            <v-rating
              :value="review.score"
              readonly
              background-color="orange lighten-3"
              color="orange"
              dense="true"
              half-increments="true"
              small="true"
            ></v-rating
            ><br />
            <v-spacer></v-spacer>
            <p style="color: lightgray">{{ review.created_at.slice(0, 10) }}</p>
            <p
              v-show="review.userid === userId"
              @click="clickedDeleteReview(review.id)"
              style="cursor:pointer;"
            >
              <img
                src="../assets/image/delete.png"
                style="width:15px;"
                alt=""
              />
            </p>
          </v-row>
          <!-- <v-row>
              <v-rating :value="review.score" readonly background-color="orange lighten-3" color="orange" dense="true" half-increments="true" small="true"></v-rating>({{ review.score }})<br>
            </v-row> -->
          <p class="review-excerpt">{{ review.content }}</p>
          <v-row justify="center">
            <v-expansion-panels v-show="review.replyset.length == 0">
              <!-- v-show="review.replyset.length==0" -->
              <v-expansion-panel>
                <v-expansion-panel-header>답글 달기</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-textarea
                    outlined
                    v-model="myComment[index]"
                    name="input-7-4"
                    label="답글을 남겨보세요."
                    color="orange"
                  ></v-textarea>
                  <div class="text-right">
                    <!-- <v-btn @click="msgComment(myComment)" color="gray" style="color:darkgray">등록</v-btn> -->
                    <v-btn
                      v-show="myComment[index] != 0"
                      @click="registerComment(review.id, myComment[index])"
                      color="orange"
                      >등록</v-btn
                    >
                  </div>
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
          </v-row>

          <v-row class="comment">
            <div class="chat">
              <div class="chat-history">
                <div class="message-data"></div>
                <span class="message-data-name">사장님</span>
                <span class="message-data-time">{{
                  review.replyset.slice(-1)[0].created_at.substring(0, 10)
                }}</span>
                <div class="message my-message">
                  <span>{{ review.replyset.slice(-1)[0].content }}</span>
                  <span>
                    <img
                      src="../assets/image/delete.png"
                      style="width:15px; cursor: pointer"
                      alt=""
                      @click="
                        clickedDeleteComment(
                          review.id,
                          review.replyset.slice(-1)[0].id
                        )
                      "
                    />
                  </span>
                </div>
              </div>
            </div>
            <!-- <span>{{ review.replyset.slice(-1)[0].created_at.substring(0, 10) }}</span> -->
          </v-row>
        </article>
      </div>
      <br />
    </div>
  </v-container>
</template>

<script>
import axios from "axios";
<<<<<<< HEAD
import { mapGetters } from "vuex";
// const this.getBaseURL.baseURL = "http://127.0.0.1:8000/";
// const this.getBaseURL.baseURL =
=======
const baseURL = "http://127.0.0.1:8000/";
// const baseURL =
>>>>>>> 13137fe2bbbcda1fd17cec668902ead08db6eb4a
//   "http://ec2-54-180-109-206.ap-northeast-2.compute.amazonaws.com/";

export default {
  data() {
    return {
      show: false,
      rating: 0,
      reviews: "",
      review_cnt: 0,
      myReview: "",
      flag: 1,
      myComment: [],
      usertype: "",
    };
  },

  created() {
    this.getReview();
  },

  computed: {
    ...mapGetters("server", ["getBaseURL"]),
  },

  methods: {
    getReview() {
      this.flag = 1;
      // this.value = 1;
      axios
        .post(
          this.getBaseURL.baseURL + "api/reviews/store_review_list/",
          {
            storeid: this.$route.params.storeid,
          },
          {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
          }
        )
        .then((res) => {
          console.log("최신순 리뷰 여기요", res.data);
          this.reviews = res.data;
          this.review_cnt = res.data.length;
          this.usertype = res.data.user_id;
        })
        .catch((err) => {
          console.log("리뷰 안온다" + err);
        });
    },

    getReviewHighScore() {
      // this.value=3;
      this.flag = 2;
      axios
        .post(
          this.getBaseURL.baseURL + "api/reviews/sort_review_high_score/",
          {
            storeid: this.$route.params.storeid,
          },
          {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
          }
        )
        .then((res) => {
          this.reviews = res.data;
          this.review_cnt = res.data.length;
        });
    },

    getReviewLowScore() {
      this.flag = 3;
      axios
        .post(
          this.getBaseURL.baseURL + "api/reviews/sort_review_low_score/",
          {
            storeid: this.$route.params.storeid,
          },
          {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
          }
        )
        .then((res) => {
          this.reviews = res.data;
          this.review_cnt = res.data.length;
        });
    },

    msg() {
      if (this.myReview.length == 0 && this.rating == 0) {
        alert("평점과 리뷰를 평가해주세요.");
        return;
      } else if (this.myReview.length == 0) {
        alert("최소 한 글자 이상 작성해주세요.");
        return;
      } else if (this.rating == 0) {
        alert("평점을 매겨주세요.");
        return;
      }

      if (this.flag == 1) {
        this.getReview();
      } else if (this.flag == 2) {
        this.getReviewHighScore();
      } else {
        this.getReviewLowScore();
      }
    },

    msgComment() {
      alert("답글을 남겨주세요.");
    },

    registerReview() {
      // this.value=2;
      axios
        .post(
          this.getBaseURL.baseURL + "api/reviews/create_review/",
          {
            storeid: this.$route.params.storeid,
            content: this.myReview,
            score: this.rating,
          },
          {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
          }
        )
        .then((res) => {
          console.log("새로운 리뷰" + res.data);
          alert("리뷰가 등록되었습니다.");
          if (this.flag == 1) {
            this.getReview();
          } else if (this.flag == 2) {
            this.getReviewHighScore();
          } else {
            this.getReviewLowScore();
          }
        })
        .catch((err) => {
          console.log(err.response);
        });
      this.myReview = "";
      this.rating = 0;
    },

    clickedDeleteReview(reviewId) {
      var answer = confirm("리뷰를 삭제하시겠습니까?");
      if (answer) {
        // true
        axios
          .delete(this.getBaseURL.baseURL + `api/reviews/${reviewId}/`, {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
          })
          .then((res) => {
            alert("리뷰가 삭제 되었습니다.");
            if (this.flag == 1) {
              this.getReview();
            } else if (this.flag == 2) {
              this.getReviewHighScore();
            } else {
              this.getReviewLowScore();
            }
          })
          .catch((err) => {
            alert("리뷰 삭제 실패!");
          });
      }
    },

    // 사장님 답글 등록
    registerComment(idx, content) {
      axios
        .post(
          this.getBaseURL.baseURL + `api/reviews/${idx}/create_reply/`,
          {
            content: content,
          },
          {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
          }
        )
        .then((res) => {
          this.getReview();
        })
        .catch((err) => {
          console.log("답글ㄴㄴ", err.response);
        });
    },

    clickedDeleteComment(reviewId, commentId) {
      var answer = confirm("답글을 삭제하시겠습니까?");
      if (answer) {
        // true
        axios
          .post(
            this.getBaseURL.baseURL +
              `api/reviews/${reviewId}/reply/${commentId}/`,
            {
              storeid: this.$route.params.storeid,
            },
            {
              headers: {
                Authorization: `Token ${this.$cookies.get("auth-token")}`,
              },
            }
          )
          .then((res) => {
            alert("답글이 삭제 되었습니다.");
            if (this.flag == 1) {
              this.getReview();
            } else if (this.flag == 2) {
              this.getReviewHighScore();
            } else {
              this.getReviewLowScore();
            }
          })
          .catch((err) => {
            console.log(err.response);
            alert("답글 삭제 실패!");
            console.log(this.$route.params.storeid);
          });
      }
    },
  },
};
</script>

<style scoped>
* {
  position: relative;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  border: none;
}
h2,
h3 {
  font-size: 1em;
}
span {
  font-size: 0.8em;
}
p {
  font-size: 0.7em;
  color: #444;
  line-height: 1.3em;
}
a {
  text-decoration: none;
}
.wrapper {
  width: 800px;
  background: white;
  margin: 0 auto;
  padding: 0;
  position: relative;
}

/*
 * PAGE CONTENT STYLES
 */
.content {
  padding: 20px 0;
  width: 60%;
  float: left;
}
.review {
  margin-bottom: 30px;
  border: 2px solid transparent;
  box-sizing: border-box;
  margin: -10px;
  padding: 20px;
  text-align: left;
}
/* .review:hover {
  border-color: gainsboro;
  background: #f0f0f0;
} */
/* .review-title {
  margin-bottom: 5px;
  padding-bottom: 5px;
  border-bottom: 1px solid gainsboro;
} */
/* .review a {
  text-decoration: none;
} */

.chat {
  width: 1500px;
  float: left;
  /* background: #F2F5F8; */
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
  color: #434651;
}

.chat .chat-about {
  float: left;
  padding-left: 10px;
  margin-top: 6px;
}
.chat .chat-with {
  font-weight: bold;
  font-size: 16px;
}
.chat .chat-history .message-data {
  margin-bottom: 15px;
}
.chat .chat-history .message-data-time {
  color: #a8aab1;
  padding-left: 6px;
}
.chat .chat-history .message {
  color: black;
  padding: 18px 20px;
  line-height: 26px;
  font-size: 16px;
  border-radius: 7px;
  width: 90%;
  position: relative;
}
.chat .chat-history .message:after {
  bottom: 100%;
  left: 7%;
  border: solid transparent;
  content: " ";
  height: 0;
  width: 0;
  position: absolute;
  pointer-events: none;
  border-bottom-color: #ededed;
  border-width: 10px;
  margin-left: -10px;
}
.chat .chat-history .my-message {
  background: #ededed;
}

/* .chat .chat-message {
  padding: 30px;
} */
.chat .chat-message textarea {
  width: 100%;
  border: none;
  padding: 10px 20px;
  font: 14px/22px "Lato", Arial, sans-serif;
  margin-bottom: 10px;
  border-radius: 5px;
  resize: none;
}
/* .chat .chat-message, .chat .chat-message   {
  font-size: 16px;
  color: gray;
  cursor: pointer;
} */

.align-left {
  text-align: left;
}
/* 
.align-right {
  text-align: right;
} */

/* .float-right {
  float: right;
} */

.clearfix:after {
  visibility: hidden;
  display: block;
  font-size: 0;
  content: " ";
  clear: both;
  height: 0;
}
</style>
