<template>
  <div class="cotn_principal">
    <img src="../assets/image/loginbackground.jpg" alt="" />
    <div class="cont_centrar">
      
      <div class="cont_login">

        <div class="cont_info_log_sign_up">
          <div class="col_md_login">
            <div class="cont_ba_opcitiy">
              <h2>일반 회원</h2>
              <button class="btn_login" @click="cambiar_login()">
                시작하기
              </button>
            </div>
          </div>
          <div class="col_md_sign_up">
            <div class="cont_ba_opcitiy">
              <h2>사업자 회원</h2>
              <button class="btn_start_biz" @click="cambiar_login_biz()">
                시작하기
              </button>
            </div>
          </div>
        </div>

        <!-- <div class="cont_back_info"></div> -->
        
        <!-- 일반회원 -->
        <div class="cont_forms">
          <div class="cont_img_back_">
            <img
              src="https://images.unsplash.com/42/U7Fc1sy5SCUDIu4tlJY3_NY_by_PhilippHenzler_philmotion.de.jpg?ixlib=rb-0.3.5&q=50&fm=jpg&crop=entropy&s=7686972873678f32efaf2cd79671673d"
              alt=""
            />
          </div>
          <div class="cont_form_login">
            <a href="#" @click="ocultar_login_sign_up()"
              ><i class="material-icons">&#xE5C4;</i></a
            >
            <h2>LOGIN</h2>
            <input type="text" v-model="email" placeholder="Email" />
            <input type="password" v-model="password" placeholder="Password" />
            <button class="btn_login" @click="cambiar_login_form()">로그인</button>
            <button class="btn_to_sign_up" @click="cambiar_sign_up()">
              회원가입
            </button>
          </div>

          <div class="cont_form_sign_up">
            <a href="#" @click="ocultar_login_sign_up()"
              ><i class="material-icons">&#xE5C4;</i></a
            >
            <h2>SIGN UP</h2>
            <input type="text" v-model="email" placeholder="이메일" />
            <input type="text" v-model="name" placeholder="사용자이름" />
            <input type="text" v-model="nickname" placeholder="닉네임" />
            <input type="password" v-model="password" ref="confrimpw" placeholder="비밀번호" />
            <input type="text" v-model="confirmpw" ref="confirmpw" placeholder="비밀번호 확인" />
            <button class="btn_sign_up" @click="cambiar_sign_up_form()">
              SIGN UP
            </button>
          </div>
        </div>

        <!-- 사업자 부분 -->
        <div class="cont_forms_biz">
          <div class="cont_img_back_">
            <img
              src="https://images.unsplash.com/42/U7Fc1sy5SCUDIu4tlJY3_NY_by_PhilippHenzler_philmotion.de.jpg?ixlib=rb-0.3.5&q=50&fm=jpg&crop=entropy&s=7686972873678f32efaf2cd79671673d"
              alt=""
            />
          </div>
          <div class="cont_form_login_biz">
            <a href="#" @click="ocultar_login_sign_up_biz()"
              ><i class="material-icons">&#xE5C4;</i></a
            >
            <h2>LOGIN</h2>
            <input type="text" placeholder="사업자 번호" />
            <input type="password" placeholder="Password" />
            <button class="btn_login" @click="cambiar_login()">로그인</button>
            <button class="btn_to_sign_up" @click="cambiar_sign_up_biz()">
              사업자 등록
            </button>
          </div>

          <div class="cont_form_sign_up_biz">
            <a href="#" @click="ocultar_login_sign_up_biz()"
              ><i class="material-icons">&#xE5C4;</i></a
            >
            <h2>SIGN UP</h2>
            <input type="text" placeholder="사업자 번호" />
            <input type="text" placeholder="업주명" />
            <input type="password" placeholder="Password" />
            <input type="password" placeholder="Confirm Password" />
            <button class="btn_sign_up" @click="cambiar_sign_up()">
              SIGN UP
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data:()=>{
    return {
      email: '',
      name: '',
      nickname: '',
      password: '',
      confirmpw: ''
    }
  },
  watch:{
    confirmpw: function () {
      this.checkForm();
    }
  },
  methods: {
    checkForm(){
      if (this.confirmpw.length >= 0 && this.password != this.confirmpw) {
        console.log(this.confirmpw)
        console.log(this.password)
        alert('비밀번호를 확인해주세요')
      }
    },
    cambiar_login() {
      document.querySelector(".cont_forms").className =
        "cont_forms cont_forms_active_login";
      document.querySelector(".cont_form_login").style.display = "block";
      document.querySelector(".cont_form_sign_up").style.opacity = "0";

      setTimeout(function() {
        document.querySelector(".cont_form_login").style.opacity = "1";
      }, 400);

      setTimeout(function() {
        document.querySelector(".cont_form_sign_up").style.display = "none";
      }, 200);
    },

    cambiar_login_form(){ // 여기에 axios
      console.log(this.email)
      console.log(this.password)
    },

    // 사업자 로그인 부분
    ///////////////////////////////////////////////////////////////////
    cambiar_login_biz() {
      document.querySelector(".cont_forms_biz").className =
        "cont_forms_biz cont_forms_active_login_biz";
      document.querySelector(".cont_form_login_biz").style.display = "block";
      document.querySelector(".cont_form_sign_up_biz").style.opacity = "0";

      setTimeout(function() {
        document.querySelector(".cont_form_login_biz").style.opacity = "1";
      }, 400);

      setTimeout(function() {
        document.querySelector(".cont_form_sign_up_biz").style.display = "none";
      }, 200);
    },
    ///////////////////////////////////////////////////////////////////

    cambiar_sign_up() {
      document.querySelector(".cont_forms").className =
        "cont_forms cont_forms_active_sign_up";
      document.querySelector(".cont_form_sign_up").style.display = "block";
      document.querySelector(".cont_form_login").style.opacity = "0";

      setTimeout(function() {
        document.querySelector(".cont_form_sign_up").style.opacity = "1";
      }, 100);

      setTimeout(function() {
        document.querySelector(".cont_form_login").style.display = "none";
      }, 400);
    },

    cambiar_sign_up_biz() {
      document.querySelector(".cont_forms_biz").className =
        "cont_forms_biz cont_forms_active_sign_up_biz";
      document.querySelector(".cont_form_sign_up_biz").style.display = "block";
      document.querySelector(".cont_form_login_biz").style.opacity = "0";

      setTimeout(function() {
        document.querySelector(".cont_form_sign_up_biz").style.opacity = "1";
      }, 100);

      setTimeout(function() {
        document.querySelector(".cont_form_login_biz").style.display = "none";
      }, 400);
    },

    ocultar_login_sign_up() {
      document.querySelector(".cont_forms").className = "cont_forms";
      document.querySelector(".cont_form_sign_up").style.opacity = "0";
      document.querySelector(".cont_form_login").style.opacity = "0";

      setTimeout(function() {
        document.querySelector(".cont_form_sign_up").style.display = "none";
        document.querySelector(".cont_form_login").style.display = "none";
      }, 500);
    },

    ocultar_login_sign_up_biz() {
      document.querySelector(".cont_forms_biz").className = "cont_forms_biz";
      document.querySelector(".cont_form_sign_up_biz").style.opacity = "0";
      document.querySelector(".cont_form_login_biz").style.opacity = "0";

      setTimeout(function() {
        document.querySelector(".cont_form_sign_up_biz").style.display = "none";
        document.querySelector(".cont_form_login_biz").style.display = "none";
      }, 500);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "../assets/css/login.css";
</style>
