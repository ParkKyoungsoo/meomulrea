<template>
    <div class="container">
        <!-- <img src="../assets/image/background.jpg" alt="background"> -->
        <div class="start">
            <div class="normal_start">
                <div class="normal" v-show="nm_page===0">
                    <h2>NORMAL</h2>
                    <button id="mvlogin" @click="move_to_login()">START</button>
                </div>
                <div class="normal_login" v-if="nm_page===1">
                    <button @click="move_to_nm_start()">
                        <i class="material-icons" style="font-size:10px">arrow_back</i>
                    </button>
                    <h2>NORMAL_LOGIN</h2>
                    <label for="nm_login_email">이메일</label>
                    <input type="text" id="nm_login_email" ref="nm_login_email" v-model="nm_login_email" placeholder="aaa@abc.com">
                    <label for="nm_login_password">비밀번호</label>
                    <input type="password" id="nm_login_password" ref="nm_login_password" v-model="nm_login_password" placeholder="PASSWORD">
                    <button @click="nm_login()">로그인</button>
                    <button @click="move_to_nm_signup()">회원 가입</button>
                </div>
                <div v-show="nm_page=='2'" class="normal_signup">
                    <button @click="move_to_nm_login()">
                        <i class="material-icons" style="font-size:10px">arrow_back</i>
                    </button>
                    <h2>NORMAL_SIGNUP</h2>
                    <label for="nm_email">이메일</label>
                    <input type="text" ref="nm_email" v-model="nm_email" placeholder="aaa@abc.com">
                    <label for="nm_name">이름</label>
                    <input type="text" ref="nm_name" v-model="nm_name" placeholder="김싸피">
                    <label for="nm_nick">닉네임</label>
                    <input type="text" v-model="nm_nick">
                    <label for="nm_password">비밀번호</label>
                    <input type="password"  ref="nm_password" v-model="nm_password" placeholder="PASSWORD">
                    <label for="passwordConfirm">비밀번호확인</label>
                    <input type="password" ref="nm_passwordConfirm" v-model="nm_passwordConfirm" placeholder="PASSWORDCONFIRM">
                    <button @click="nm_signup()">회원 가입</button>
                </div>
            </div>

        </div>


    </div>
</template>
<script>
export default {
    name: "LogIn",
    data: ()=>{
        return {
            nm_page: 0,
            biz_page:'0',
            nm_login_email:'',
            nm_login_password:'',
            nm_email:'',
            nm_name:'',
            nm_nick: this.nm_email,
            nm_password:'',
            nm_passwordConfirm:''
        }
    },
    methods: {
        move_to_login(){
           this.nm_page+=1;
           return;
        },
        move_to_bizlogin(){
            this.biz_page='1';
        },
        move_to_nm_start(){
            this.nm_page-=1;
        },
        move_to_nm_login(){
            this.nm_page='1';
        },
        move_to_biz_start(){
            this.biz_page='0';
        },
        nm_login(){
            if(this.nm_login_email=='')
                // this.$refs.nm_login_email.focus();
                console.log('email')
            else if(this.nm_login_password=='')
                // this.$refs.nm_login_password.focus();
                console.log('password')
            else {
                console.log('axios 호출')
            }
        },
        move_to_nm_signup(){
            this.nm_page='2';
        },
        nm_signup(){
            if(this.nm_email=='')
                this.$refs.nm_email.focus();
            else if(this.nm_name=='')
                this.$refs.nm_name.focus();
            else if(this.nm_password=='')
                this.$refs.nm_password.focus();
            else if(this.nm_passwordConfirm=='')
                this.$refs.nm_passwordConfirm.focus();
            else if(this.nm_passwordConfirm!=this.nm_password)
                alert('비밀번호를 재확인해주세요')
            else
                console.log('axios signup 호출')
        }
    }
}
</script>
<style scoped>
    @import "../assets/css/login.css";
</style>