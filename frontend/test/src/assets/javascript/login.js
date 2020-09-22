export default {
  name: "Loginjs",
  methods: {
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
