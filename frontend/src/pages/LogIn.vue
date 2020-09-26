<template>
  <v-main>
    <v-container>
      <div class="cont">
        <div class="cont_center_left">
          <div v-if="nm_page === 0" class="start">
            <div>
              <h2>일반회원</h2>
              <v-btn rounded color="rgb(0,0,0)" dark @click="mvpage(true)"
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
              <v-text-field
                v-model="nm_email"
                label="이메일"
                :messages="[error.email]"
              ></v-text-field>
              <v-text-field
                v-model="nm_password"
                label="비밀번호"
                :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show2 ? 'text' : 'password'"
                @click:append="show2 = !show2"
              ></v-text-field>
              <v-btn
                rounded
                color="rgb(233, 105, 30)"
                dark
                @click="nm_login()"
                :loading="loading"
                >로그인</v-btn
              >
              <v-btn rounded color="rgb(0,0,0)" dark @click="mvpage(true)"
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
              <v-text-field
                v-model="nm_email"
                :messages="[error.email]"
                label="이메일"
                ref="nm_email"
              ></v-text-field>
              <v-text-field v-model="nm_name" label="이름"></v-text-field>
              <v-text-field v-model="nm_nickname" label="닉네임"></v-text-field>
              <v-text-field
                v-model="nm_password"
                :messages="[error.pwd]"
                label="비밀번호"
                ref="nm_password"
                :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show3 ? 'text' : 'password'"
                @click:append="show3 = !show3"
              ></v-text-field>
              <v-text-field
                v-model="nm_password_confirm"
                :messages="[error.pwdconfirm]"
                label="비밀번호 확인"
                ref="nm_password_confirm"
                :append-icon="show4 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show4 ? 'text' : 'password'"
                @click:append="show4 = !show4"
              ></v-text-field>
              <v-text-field
                label="주소"
                @click="findAddress()"
                readonly="readonly"
                v-model="nm_address"
              ></v-text-field>
              <v-container fluid style="height:fit-content;">
                <v-layout style="height:fit-content;" row>
                  <v-radio-group v-model="nm_gender" row>
                    <v-flex xs4>
                      <label for="nm_gender">성별</label>
                    </v-flex>
                    <v-flex xs4>
                      <v-radio label="FEMALE" value="1"></v-radio>
                    </v-flex>
                    <v-flex xs4>
                      <v-radio label="MALE" value="0"></v-radio>
                    </v-flex>
                  </v-radio-group>
                </v-layout>
              </v-container>
              <v-text-field
                label="출생년도"
                type="number"
                v-model="nm_birthyear"
              ></v-text-field>
              <v-btn rounded color="rgb(0,0,0)" dark @click="checkHandler()"
                >회원가입</v-btn
              >
            </div>
          </div>
        </div>
        <div class="cont_center_right">
          <div v-if="biz_page === 0" class="start">
            <div>
              <h2>사업자회원</h2>
              <v-btn rounded color="rgb(0,0,0)" dark @click="mvpage(false)"
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
              <v-btn rounded color="rgb(0,0,0)" dark @click="mvpage(false)"
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
              <v-btn rounded color="rgb(0,0,0)" dark @click="biz_signup()"
                >회원가입</v-btn
              >
            </div>
          </div>
        </div>
      </div>
    </v-container>
  </v-main>
</template>

<script src="http://dmaps.daum.net/map_js_init/postcode.v2.js"></script>
<script src="//dapi.kakao.com/v2/maps/sdk.js?appkey=48cbffa8392e1a7acffc1975347ec0d3&libraries=services"></script>

<script>
import axios from "axios";
import * as firebase from "firebase";
const baseURL = "http://127.0.0.1:8000/";
export default {
  name: "LogIn",
  data() {
    return {
      show2: false,
      show3: false,
      show4: false,
      nm_page: 0,
      nm_email: "",
      nm_name: "",
      nm_nickname: "",
      nm_password: "",
      nm_password_confirm: "",
      nm_address: "",
      nm_gender: "",
      nm_birthyear: 0,

      biz_page: 0,
      biz_email: "",
      biz_name: "",
      biz_password: "",
      biz_password_confirm: "",
      biz_address: "",

      error: {
        email: "",
        pwd: "",
        pwdconfirm: "",
      },
      password: "password",

      rules: [
        {
          message: "이메일을 확인해주세요",
          regex: /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/,
        },
        {
          message: "사용불가능한 비밀번호입니다",
          regex: /(?=.*\d)(?=.*[a-z]).{8,}/,
        },
      ],
    };
  },
  watch: {
    nm_email: function() {
      if (this.nm_email.length > 0) {
        if (!this.rules[0].regex.test(this.nm_email)) {
          this.error.email = this.rules[0].message;
          return;
        }
        this.error.email = "";
      }
      this.nm_nickname = this.nm_email;
      axios
        .post(baseURL + "accounts/user_email/", {
          email: this.nm_email,
        })
        .then((res) => {
          console.log(res.data.message);
          if (res.data.message === "이미 존재하는 이메일입니다.") {
            this.error.email = "이미 존재하는 이메일입니다.";
          }
        });
    },
    nm_password: function() {
      var temp = ["qwert", "asdfg", "zxcvb"];
      var nm_password = this.nm_password;
      if (this.nm_password.length > 0) {
        for (var t in temp) {
          if (this.nm_password.includes(temp[t])) {
            this.error.pwd = this.rules[1].message;
            return;
          }
        }
        this.error.pwd = this.rules[1].message;
        if (!this.rules[1].regex.test(nm_password)) {
          this.error.pwd = this.rules[1].message;
          return;
        }
        this.error.pwd = "";
        return;
      }
    },
    nm_password_confirm: function() {
      if (this.nm_password_confirm.length > 0) {
        if (this.nm_password_confirm !== this.nm_password) {
          this.error.pwdconfirm = "비밀번호가 틀렸습니다";
          return;
        }
        this.error.pwdconfirm = "";
      }
    },
  },
  computed: {
    // comparePasswords () {
    //     return this.password !== this.confirmPassword ? 'Passwords do not match.' : true
    //   },
    user() {
      return this.$store.getters.user;
    },
    error() {
      return this.$store.getters.error;
    },
    loading() {
      return this.$store.getters.loading;
    },
  },
  methods: {
    checkHandler() {
      let err = true;
      let msg = "";
      !this.nm_email &&
        ((msg = "이메일을 입력해주세요!"),
        (err = false),
        this.$refs.nm_email.focus());
      err &&
        !this.nm_password &&
        ((msg = "비밀번호를 입력해주세요!"),
        (err = false),
        this.$refs.nm_password.focus());
      err &&
        !this.nm_password_confirm &&
        ((msg = "비밀번호 확인을 입력해주세요!"),
        (err = false),
        this.$refs.nm_password_confirm.focus());
      if (!err) {
        alert(msg);
      } else if (
        !this.error.email &&
        !this.error.password &&
        !this.error.passwordConfirm
      ) {
        this.nm_signup();
      }
    },
    findAddress() {
      new daum.Postcode({
        oncomplete: (data) => {
          var fullAddr = data.address;
          console.log(data.address);
          var extraAddr = "";

          if (data.addressType === "R") {
            if (data.bname !== "") {
              extraAddr += data.bname;
              console.log("bname : " + extraAddr);
            }
            if (data.buildingName !== "") {
              extraAddr +=
                extraAddr !== "" ? ", " + data.buildingName : data.buildingName;
              console.log("buildingName : " + extraAddr);
            }
            fullAddr += extraAddr !== "" ? " (" + extraAddr + ")" : "";
            this.nm_address = fullAddr;
            console.log("fullADDR : " + fullAddr);
          }
        },
      }).open();
    },

    setCookie(token) {
      this.$cookies.set("auth-token", token);
      this.isLoggedIn = true;
    },

    onSignin() {
      this.$store.dispatch("signUserIn", {
        email: this.nm_email,
        password: this.nm_password,
      });
    },

    onSignup() {
      this.$store.dispatch("signUserUp", {
        email: this.nm_email,
        password: this.nm_password,
        username: this.nm_nickname,
      });
    },

    nm_login() {
      // var nm_password = this.nm_password;
      // 로그인화면에서 아이디, 비밀번호 유효성 검사 해주세요
      axios
        .post(baseURL + "account/login/", {
          email: this.nm_email,
          password: this.nm_password,
        })
        .then((res) => {
          firebase
            .auth()
            .setPersistence(firebase.auth.Auth.Persistence.SESSION)
            .then(() => {
              firebase
                .auth()
                .signInWithEmailAndPassword(this.nm_email, this.nm_password);
              this.setCookie(res.data.key);
              this.$router.push("/");
            });
          this.onSignin();
        });
    },

    nm_signup() {
      axios
        .post(baseURL + "account/signup/", {
          username: this.nm_nickname,
          email: this.nm_email,
          password1: this.nm_password,
          password2: this.nm_password_confirm,
        })
        .then((res) => {
          console.log(res.data.key);
          axios
            .post(
              baseURL + "accounts/user_detail/",
              {
                username: this.nm_nickname,
                email: this.nm_email,
                usertype: 1,
                gender: this.nm_gender,
                address: this.nm_address,
                birth_year: this.nm_birthyear,
              },
              {
                headers: {
                  Authorization: `Token ${res.data.key}`,
                },
              }
            ) // post > post
            .then((res) => {
              this.onSignup();
              this.nm_page = 1;
            }); // post > post > then
        })
        .catch((res) => {
          console.log(res);
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
