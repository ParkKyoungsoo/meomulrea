# API

## SIGNUP

http://127.0.0.1:8000/account/signup/

- BODY
  - username
  - email
  - password1
  - password2



## USER_DETAIL

http://127.0.0.1:8000/accounts/user_detail/

- HEADERS
  - {"Authorization" :  "Token abcde12345"}
- BODY
  - username
  - email
  - usertype
    - 사업자일 경우
      - 0
    - 일반 사용자일 경우
      - 1
  - gender
    - 남성
      - 0
    - 여성
      - 1
  - address
  - birth_year
    - 길이 4 최대 설정
      - ex> 2002
  - (아래는 사업자일 경우만 - 이미지는 추가할 예정)
  - biznumber
  - bizname
  - bizaddress



## LOGIN

http://127.0.0.1:8000/account/login/

- BODY
  - email
  - password



## LOGOUT

http://127.0.0.1:8000/account/logout/

- HEADERS
  - {"Authorization" :  "Token abcde12345"}