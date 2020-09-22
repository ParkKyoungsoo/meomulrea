<template>
  <v-container>
    <v-main>
      <div class="cont">
        <div class="cont_center_left">
          <div v-if="nm_page === 0" class="start">
            <div>
              <h2>일반회원</h2>
              <v-btn rounded color="primary" dark @click="mvpage(true)"
                >시작하기</v-btn
              >
            </div>
          </div>
          <div v-if="nm_page === 1" class="start">
            <div>
              <div>
                <button @click="reset(true)">
                  <i class="material-icons">&#xE5C4;</i>
                </button>
                <h2>일반회원</h2>
              </div>
              <v-text-field v-model="nm_email" label="이메일"></v-text-field>
              <v-text-field
                v-model="nm_password"
                label="비밀번호"
                :messages="[err]"
              ></v-text-field>
              <v-btn rounded color="rgb(233, 105, 30)" dark @click="nm_login()"
                >로그인</v-btn
              >
              <v-btn rounded color="primary" dark @click="mvpage(true)"
                >회원등록</v-btn
              >
            </div>
          </div>
          <div v-if="nm_page === 2" class="start">
            <div>
              <div>
                <button @click="reset(true)">
                  <i class="material-icons">&#xE5C4;</i>
                </button>
                <h2>일반회원</h2>
              </div>
              <v-text-field v-model="nm_email" label="이메일"></v-text-field>
              <v-text-field v-model="nm_name" label="이름"></v-text-field>
              <v-text-field v-model="nm_nickname" label="닉네임"></v-text-field>
              <v-text-field
                v-model="nm_password"
                label="비밀번호"
              ></v-text-field>
              <v-text-field
                v-model="nm_password_confirm"
                label="비밀번호"
              ></v-text-field>
              <v-text-field
                v-model="nm_address"
                label="주소"
                readonly="readonly"
                @click="findAddress()"
              ></v-text-field>
              <v-container fluid style="height:fit-content;">
                <v-layout style="height:fit-content;" row>
                  <v-radio-group v-model="nm_gender" row>
                    <v-flex xs4>
                      <label for="nm_gender">성별</label>
                    </v-flex>
                    <v-flex xs4>
                      <v-radio label="FEMALE" value="F"></v-radio>
                    </v-flex>
                    <v-flex xs4>
                      <v-radio label="MALE" value="M"></v-radio>
                    </v-flex>
                  </v-radio-group>
                </v-layout>
              </v-container>
              <v-btn rounded color="primary" dark @click="nm_signup()"
                >회원가입</v-btn
              >
            </div>
          </div>
        </div>
        <div class="cont_center_right">
          <div v-if="biz_page === 0" class="start">
            <div>
              <h2>사업자회원</h2>
              <v-btn rounded color="primary" dark @click="mvpage(false)"
                >시작하기</v-btn
              >
            </div>
          </div>
          <div v-if="biz_page === 1" class="start">
            <div>
              <div>
                <button @click="reset(false)">
                  <i class="material-icons">&#xE5C4;</i>
                </button>
                <h2>사업자회원</h2>
              </div>
              <v-text-field
                v-model="biz_email"
                label="사업자번호"
              ></v-text-field>
              <v-text-field
                v-model="biz_password"
                label="비밀번호"
              ></v-text-field>
              <v-btn rounded color="rgb(233, 105, 30)" dark @click="biz_login()"
                >로그인</v-btn
              >
              <v-btn rounded color="primary" dark @click="mvpage(false)"
                >사업자등록</v-btn
              >
            </div>
          </div>
          <div v-if="biz_page === 2" class="start">
            <div>
              <div>
                <button @click="reset(false)">
                  <i class="material-icons">&#xE5C4;</i>
                </button>
                <h2>사업자회원</h2>
              </div>
              <v-text-field
                v-model="biz_email"
                label="사업자번호"
              ></v-text-field>
              <v-file-input accept="image/*" label="사진"></v-file-input>
              <v-text-field v-model="biz_name" label="업주명"></v-text-field>
              <v-text-field
                v-model="biz_password"
                label="비밀번호"
              ></v-text-field>
              <v-text-field
                v-model="biz_password_confirm"
                label="비밀번호"
              ></v-text-field>
              <v-text-field
                v-model="nm_address"
                label="사업장주소"
                readonly="readonly"
                @click="findAddress()"
              ></v-text-field>
              <v-btn rounded color="primary" dark @click="biz_signup()"
                >회원가입</v-btn
              >
            </div>
          </div>
        </div>
      </div>
    </v-main>
  </v-container>
</template>

<script>
import axios from "axios";
const baseURL = "http://127.0.0.1:8000/";
export default {
  name: "LogIn",
  data() {
    return {
      nm_page: 0,
      nm_email: "",
      nm_name: "",
      nm_nickname: "",
      nm_password: "",
      nm_password_confirm: "",
      nm_address: "",
      nm_gender: "",

      biz_page: 0,
      biz_email: "",
      biz_name: "",
      biz_password: "",
      biz_password_confirm: "",
      biz_address: "",

      err: "",
    };
  },
  watch: {
    nm_email: function() {
      this.nm_nickname = this.nm_email;
    },
  },
  methods: {
    findAddress() {
      console.log("findADDRESS");
    },
    nm_login() {
      axios
        .post(baseURL + "account/login/", {
          email: this.nm_email,
          password: this.nm_password,
        })
        .then((res) => {
          console.log(res);
          this.err = "";
        })
        .catch(() => {
          console.log("err");
          this.err = "이메일과 비밀번호를 다시 확인해주세요.";
        });
    },
    nm_signup() {
      axios
        .post(baseURL + "account/signup/", {
          username: this.nm_name,
          email: this.nm_email,
          password1: this.nm_password,
          password2: this.nm_password_confirm,
        })
        .then(() => {
          console.log("then");
        })
        .catch(() => {
          console.log("catch");
        });
    },
    reset(nm) {
      if (nm) {
        this.nm_page -= 1;
        this.nm_email = "";
        this.nm_name = "";
        this.nm_nickname = "";
        this.nm_password = "";
        this.nm_password_confirm = "";
        this.nm_address = "";
        this.nm_gender = "";
      } else {
        this.biz_page -= 1;
        this.biz_email = "";
        this.biz_name = "";
        this.biz_password = "";
        this.biz_password_confirm = "";
        this.biz_address = "";
      }
    },
    mvpage(nm) {
      if (nm) {
        this.nm_page += 1;
        this.nm_email = "";
        this.nm_name = "";
        this.nm_nickname = "";
        this.nm_password = "";
        this.nm_password_confirm = "";
        this.nm_address = "";
        this.nm_gender = "";
      } else {
        this.biz_page += 1;
        this.biz_email = "";
        this.biz_name = "";
        this.biz_password = "";
        this.biz_password_confirm = "";
        this.biz_address = "";
      }
    },
  },
};
</script>
<style scoped src="../assets/login.css"></style>
