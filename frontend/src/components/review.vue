<template>
  <v-container fluid>
    <div class="review-top">
      <h3 style="text-align:left">리뷰({{ review_cnt }}개)</h3>
      <hr>
      <br>
    </div>
    <div class="review-stats" style="background-color:yellow">
      <p>Review stats</p>
    </div>
    <div class="review-write" style="border: 1px solid silver; margin-bottom:10px">
      <div style="margin:10px 10px 0 10px">
        <v-rating v-model="rating" background-color="orange lighten-3" color="orange" dense="true" half-increments="true" hover="true"></v-rating><br>
        <v-textarea solo name="input-7-4" label="리뷰를 남겨보세요." v-model="myReview"></v-textarea>
        <div class="text-right" style="pt-0; mb-5">
          <v-btn @click="registerReview()" style="text-align:right;" color="orange">등록</v-btn>
        </div>
        <hr>
      </div>
    </div>
    <div class="review-sort" style="background-color:yellow">
      <span>최신순</span> | 
      <span>높은 평점순</span> | 
      <span>낮은 평점순</span>
      <v-select :items="items" label="최신순" dense solo width=5></v-select>
    </div>
    <div class="review-origin" v-for="review in reviews" :key="review.id">
      <div style="border: 1px solid silver">
        <article class="review review-1">
          <v-container>
            <v-row>
              <v-rating :value="review.score" readonly background-color="orange lighten-3" color="orange" dense="true" half-increments="true" small="true"></v-rating>({{ review.score }})<br>
            </v-row>
            <v-row>
              <v-col-3><h3 v-if="review.user===null" class="review-title" style="display: inline">{{ review.userid }}</h3>
              <h3 v-else class="review-title">{{ review.user.username }}</h3></v-col-3>
              <v-col-9><p style="color: lightgray">{{ timeForToday(review.reg_time) }}</p></v-col-9>
        </v-row>
       </v-container>
      <p class="review-excerpt">{{ review.content }}</p>
      <!-- </h3> -->
        </article>
      </div>
      <br>
    </div>
  </v-container>
</template>

<script>
import axios from 'axios';
const baseURL = "http://127.0.0.1:8000/api/";
// const baseURL = "http://j3b304.p.ssafy.io/";

export default {
  data () {
    return {
      rating: 0,
      reviews: "",
      review_cnt: 0,
      myReview: "",
      items: ['최신순', '높은 평점 순', '낮은 평점 순'],
    }
  },
  created() {
    this.getReview()
  },

  methods: {
    getReview() {
      axios.post(baseURL + "reviews/store_review_list/", {
        storeid: 148
      },
      {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      })
      .then(res => {
        console.log(res)
        console.log('getreview' + res.data)
        this.reviews = res.data
        this.review_cnt = res.data.length
        
      })
      .catch(err => {
        console.log("리뷰 안온다" + err)
      })
    }, // getReview

    registerReview() {
      if (this.myReview.length == 0) {
        alert("리뷰를 작성해주세요.")
      }
      // if (this.rating == 0) {
      //   alert("평점을 매겨주세요.")
      // }
      axios.post(baseURL + "reviews/create_review/", {
        storeid: 148,
        content: this.myReview,
        score: this.rating,
      },
      {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      })
      .then(res => {
        console.log(res)
        alert("리뷰가 등록되었습니다.")
        this.getReview()

      })
      .catch(err => {
        console.log(err)
      })
      this.reviews = ""
    },
    // 시간 체크
    timeForToday(value) {
      const today = new Date();
      const timeValue = new Date(value);

      const betweenTime = Math.floor((today.getTime() - timeValue.getTime()) / 1000 / 60);

      if (betweenTime < 1) return '방금 전';
      if (betweenTime < 60) return `${betweenTime}분 전`;

      const betweenTimeHour = Math.floor(betweenTime / 60);
      if (betweenTimeHour < 24) return `오늘`;

      const betweenTimeDay = Math.floor(betweenTime / 60 / 24);
      if (betweenTimeDay < 365) return `${betweenTimeDay}일 전`;
      // return value
      return `${Math.floor(betweenTimeDay / 365)}년 전`;
    },
  },
}
</script>

<style scoped>
* {
  position: relative;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  border: none;
}

p {
  font-size: 0.9em;
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
  padding: 20px 10px;
  text-align: left;
}
/* .review:hover {
  border-color: gainsboro;
  background: #f0f0f0;
} */
.review-title {
  margin-bottom: 5px;
  padding-bottom: 5px;
  border-bottom: 1px solid gainsboro;
}
.review a {
  text-decoration: none;
}


</style>
