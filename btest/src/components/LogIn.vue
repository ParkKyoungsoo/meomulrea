<template>
    <div class="cont">
        <div class="cont_center_left">
            <div v-if="nm_page===0" class="start">
                <div>
                <h2>일반회원</h2>
                <v-btn rounded color="primary" dark @click="nm_page=1">시작하기</v-btn>
                </div>
            </div>
            <div v-if="nm_page===1" class="start">
                <div>
                    <div><button @click="nm_page=0"><i class="material-icons">&#xE5C4;</i></button><h2>일반회원</h2></div>
                    <v-text-field v-model="nm_email" label="이메일"></v-text-field>
                    <v-text-field v-model="nm_password" label="비밀번호"></v-text-field>
                    <v-btn rounded color="rgb(233, 105, 30)" dark @click="nm_login()">로그인</v-btn>
                    <v-btn rounded color="primary" dark @click="nm_page=2">회원등록</v-btn>
                </div>
            </div>
            <div v-if="nm_page===2" class="start">
                <div>
                    <div><button @click="nm_page=1"><i class="material-icons">&#xE5C4;</i></button><h2>일반회원</h2></div>
                    <v-text-field v-model="nm_email" label="이메일"></v-text-field>
                    <v-text-field v-model="nm_name" label="이름"></v-text-field>
                    <v-text-field v-model="nm_nickname" label="닉네임" placeholder="nm_email"></v-text-field>
                    <v-text-field v-model="nm_password" label="비밀번호"></v-text-field>
                    <v-text-field v-model="nm_password_confirm" label="비밀번호"></v-text-field>
                    <v-text-field v-model="nm_address" label="주소" readonly="readonly" @click="findAddress()"></v-text-field>
                    <v-container fluid >
                        <v-radio-group v-model="nm_gender" row>
                            <v-radio label="Option 1" value="radio-1"></v-radio>
                            <v-radio label="Option 2" value="radio-2"></v-radio>
                        </v-radio-group>
                    </v-container>
                    <v-btn rounded color="primary" dark @click="nm_signup()">회원가입</v-btn>
                </div>
            </div>
        </div>
        <div class="cont_center_right">
            <div v-if="biz_page===0" class="start">
                <div >
                <h2>사업자회원</h2>
                <v-btn rounded color="primary" dark @click="biz_page=1">시작하기</v-btn>
                </div>
            </div>
            <div v-if="biz_page===1" class="start">
                <div>
                    <div><button @click="biz_page=0"><i class="material-icons">&#xE5C4;</i></button><h2>사업자회원</h2></div>
                    <v-text-field v-model="biz_email" label="사업자번호"></v-text-field>
                    <v-text-field v-model="biz_password" label="비밀번호"></v-text-field>
                    <v-btn rounded color="rgb(233, 105, 30)" dark @click="biz_login()">로그인</v-btn>
                    <v-btn rounded color="primary" dark @click="biz_page=2">사업자등록</v-btn>
                </div>
            </div>
            <div v-if="biz_page===2" class="start">
                <div>
                    <div><button @click="biz_page=1"><i class="material-icons">&#xE5C4;</i></button><h2>사업자회원</h2></div>
                    <v-text-field v-model="biz_email" label="사업자번호"></v-text-field>
                    <v-file-input accept="image/*" label="사진"></v-file-input>
                    <v-text-field v-model="biz_name" label="업주명"></v-text-field>
                    <v-text-field v-model="biz_password" label="비밀번호"></v-text-field>
                    <v-text-field v-model="biz_password_confirm" label="비밀번호"></v-text-field>
                    <v-text-field v-model="nm_address" label="사업장주소" readonly="readonly" @click="findAddress()"></v-text-field>
                    <v-btn rounded color="primary" dark @click="biz_signup()">회원가입</v-btn>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
const baseURL = 'http://127.0.0.1:8000/';
export default {
  name: "LogIn",
  data(){
      return{
          nm_page:0,
          nm_email:'',
          nm_name:'',
          nm_nickname:'',
          nm_password:'',
          nm_password_confirm:'',
          nm_address:'',
          nm_gender:'',

          biz_page:0,
          biz_email:'',
          biz_name:'',
          biz_password:'',
          biz_password_confirm:'',
          biz_address:'',

      }
  },
  methods: {
      findAddress(){
          console.log("findADDRESS")
      },
      nm_login(){
          console.log('login axios')
      },
      nm_signup(){
          axios.post(baseURL + 'account/signup/', {
              username: this.nm_name,
              email: this.nm_email,
              password1: this.nm_password,
              password2: this.nm_password_confirm
          })
          .then(()=>{
              console.log('then')
          })
          .catch(()=>{
              console.log('catch')
          })
      },
}
};
</script>
<style scoped>
@import "../assets/login.css";
</style>