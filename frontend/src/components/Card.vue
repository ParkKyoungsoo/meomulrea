<template>
<v-container>
    <v-row style="margin-left: 71px;">
        <div v-for="(item, index) in this.getShopList.shopList" :key="index" :index="index">
            <v-row style="margin: 10px; width: fit-content;" >
                <div class="con">
                    <div class="card-border" style="background-image: url(https://source.unsplash.com/HgxVSzUHDRY/320x460);">
                    <div class="card">
                        <div class="content">
                        <h2 class="title">{{item.store_name}}</h2>
                        <p class="text">별점 : {{item.average_rating}}</p>
                        <v-btn class="text">가게보러가기</v-btn>
                        </div>
                    </div>
                    </div>
                </div>
            </v-row>
        </div>
    </v-row>
</v-container>
</template>
<script>
import axios from "axios";
import { mapGetters } from "vuex";
const baseURL = "http://j3b304.p.ssafy.io/";
export default {
    data() {
    return {
      data: {
        category: "",
        shopList: "",
      },
    };
  },
  components: {
  },

  computed: {
    ...mapGetters("shopList", ["getShopList"]),
  },
  created: function() {
    // this.loc = this.getLocation;
    // this.category = this.$route.params.category;
    this.shopList = this.getShopList;
    console.log("shopList : ", this.shopList);
  },

  methods: {
    getStoreInfo() {
      console.log(this.$cookies.get("auth-token"));
      axios
        .post(
          baseURL + "stores/store_list/",
          {
            category: this.category,
            user_location: this.getLocation.dong,
          },
          {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
          }
        ) // post > post
        .then((res) => {
          console.log(res.data);
        })
        .catch((res) => {
          console.log(res);
        }); // post > post > then
    },

    goToShopDetail: function(shopId) {
      this.$router.push("/storedetail/" + shopId);
    },
    showShopList: function() {
      axios
        .post(
          baseURL + "stores/store_category/",
          {
            category: this.$route.params.category,
          },
          {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`,
            },
          }
        ) // post > post
        .then((res) => {
          this.userInfo = res.data;
        })
        .catch((res) => {
          console.log("user Address error", res);
        }); // post > post > then
    },
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;800;900&display=swap');
/* 
:root {
  --d: 700ms;
  --e: cubic-bezier(0.19, 1, 0.22, 1);
} */
body{
  /* display: flex; */
  /* justify-content: center; */
  /* align-items: center; */
  min-height: 100vh;
  background-image: radial-gradient( circle farthest-corner at 1.3% 2.8%,  rgba(239,249,249,1) 0%, rgba(182,199,226,1) 100.2% );
}

.con {
  /* display: flex; */
  /* justify-content: center; */
  /* align-items: center; */
  /* justify-content: space-around; */
  /* width: 1100px; */
  max-width: fit-content;
}

.card {  
  position: relative;
  display: flex;
  align-items: flex-end;
  /* width: 100%; */
  max-width: 100%;
  height: 100%;
  color: whitesmoke;
  cursor: pointer;
  overflow: hidden;
  z-index: 10;
  pointer-events: auto;
}

.card-border {
  position: relative;
  width: 320px;
  height: 460px;
  z-index: 9;
  pointer-events: none;
}

.card-border:after,
.card-border:before {
  content: "";
  left: -20px;
  bottom: -20px;
  right:-20px;
  top: -20px;
  position: absolute;
  transition: transform 0.3s ease-in-out;
}

.card-border:before {
  transform: scaleY(0);
}

.card-border:after {
  transform: scaleX(0);
}

/* .card-border:nth-child(1) .card{ */
  /* background-image: url(https://source.unsplash.com/HgxVSzUHDRY/320x460); */
/* } */

.card-border:nth-child(1):before {
  border-left: 6px solid #241f57;
  border-right: 6px solid #241f57;
}

.card-border:nth-child(1):after {
  border-bottom: 6px solid #241f57;
  border-top: 6px solid #241f57;
}


.card-border:hover:before {
  transform: scaleY(1);
}

.card-border:hover:after {
  transform: scaleX(1);
}

.content {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 1rem;
  transition: transform var(--d) var(--e);
  z-index: 1;
  transform: translateY(calc(100% - 4.5rem));
}


.content:after{
  content: '';
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 200%;
  pointer-events: none;
  background-image: linear-gradient(
    to bottom,
    hsla(0, 0%, 0%, 0) 0%,
    hsla(0, 0%, 0%, 0.009) 11.7%,
    hsla(0, 0%, 0%, 0.034) 22.1%,
    hsla(0, 0%, 0%, 0.072) 31.2%,
    hsla(0, 0%, 0%, 0.123) 39.4%,
    hsla(0, 0%, 0%, 0.182) 46.6%,
    hsla(0, 0%, 0%, 0.249) 53.1%,
    hsla(0, 0%, 0%, 0.320) 58.9%,
    hsla(0, 0%, 0%, 0.394) 64.3%,
    hsla(0, 0%, 0%, 0.468) 69.3%,
    hsla(0, 0%, 0%, 0.540) 74.1%,
    hsla(0, 0%, 0%, 0.607) 78.8%,
    hsla(0, 0%, 0%, 0.668) 83.6%,
    hsla(0, 0%, 0%, 0.721) 88.7%,
    hsla(0, 0%, 0%, 0.762) 94.1%,
    hsla(0, 0%, 0%, 0.790) 100%
  );
  transform: translateY(-50%);
  transition: transform calc(var(--d) * 2) var(--e);
  opacity: 0;
}

.card:hover .content {
  transform: translateY(0);
}
.card:hover .content::after {
  opacity: 1;
}

.content > *:not(.title) {
  opacity: 0;
  transform: translateY(1rem);
  transition: transform var(--d) var(--e), opacity var(--d) var(--e);
}

.card:hover .content {
  transform: translateY(0);
  opacity: 1;
  transform: translateY(0);
  transition-delay: calc(var(--d) / 8);
}

.card:hover .content > *:not(.title) {
  opacity: 1;
  transform: translateY(0);
  transition-delay: calc(var(--d) / 8);
}

.title{
  width: 100%;
  font-size: 1.6rem;
  z-index: 2;
  margin-bottom: 1rem;
}

.text {
  font-size: 1rem;
  line-height: 1.8rem;
  z-index: 2;
}


</style>