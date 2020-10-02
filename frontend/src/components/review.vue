<template>
  <v-container fluid>
    <div class="review-top">
      <!-- <h3 style="text-align:left">리뷰({{ review_cnt }}개)</h3> -->
      <hr>
      <br>
    </div>
    <div class="review-stats" style="background-color:yellow">
      <p>Review stats</p>
    </div>
    <div class="review-write" style="border: 1px solid silver; margin-bottom:10px; border-radius: 0.4em">
      <div style="margin:10px">
        <v-rating v-model="rating" style="text-align:left" background-color="orange lighten-3" color="orange" dense="true" half-increments="true" hover="true"></v-rating><br>
        <v-textarea solo name="input-7-4" label="리뷰를 남겨보세요." v-model="myReview"></v-textarea>
        <div class="text-right">
          <v-btn @click="registerReview()" color="orange">등록</v-btn>
        </div>
        <hr>
      </div>
    </div>
    <div class="review-sort" style="display:inline;">
      <v-row>
        <h3 style="text-align:left;">리뷰({{ review_cnt }}개)</h3>
        <v-spacer></v-spacer>
        <span>최신순 | </span> 
        <span> 높은 평점순 | </span> 
        <span> 낮은 평점순</span>
      </v-row>
    </div>
    <div class="review-origin" v-for="review in reviews" :key="review.id">
      <div style="border: 1px solid silver; border-radius: 0.4em">
        <article class="review review-1">
            <v-row>
              <h3 v-if="review.user===null" class="review-title" style="display: inline">{{ review.userid }}</h3>
              <h3 v-else class="review-title">{{ review.user.username }}</h3>
              <v-rating :value="review.score" readonly background-color="orange lighten-3" color="orange" dense="true" half-increments="true" small="true"></v-rating><br>
              <p style="color: lightgray">{{ review.reg_time.slice(0, 10) }}</p>
              <p v-show="review.userid == userId" @click="clickedDeleteBtn(review.id)" style="cursor:pointer;"><img src="../assets/image/delete.png" style="width:15px;" alt=""></p>
            </v-row>
            <!-- <v-row>
              <v-rating :value="review.score" readonly background-color="orange lighten-3" color="orange" dense="true" half-increments="true" small="true"></v-rating>({{ review.score }})<br>
            </v-row> -->
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
      if (this.myReview.length == 0 || this.rating == 0) {
        if (this.myReview.length == 0) {
          alert("리뷰를 작성해주세요.")
        }
        if (this.rating < 1) {
          alert("평점을 매겨주세요.")
        }
        this.getReview()
      }
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

    clickedDeleteBtn(reviewId) {
      console.log("review.id"+reviewId)
      var answer = confirm("리뷰를 삭제하시겠습니까?");
      if(answer) { // true
        axios.delete(baseURL + `reviews/${reviewId}/`,
          {
              headers:{
                Authorization: `Token ${this.$cookies.get('auth-token')}`
              }
          },
        )
        .then((res) => {
            alert("게시글이 삭제 되었습니다.");
            this.getReview();
        })
        .catch((err) => {
            alert("게시글 삭제 실패!");
            console.log("삭제 실패")
        });
      }
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
.review a {
  text-decoration: none;
}


</style>
