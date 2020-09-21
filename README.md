# SSAFY big data project



## 팀구성

|                            이미지                            |     이름     |   업무   |
| :----------------------------------------------------------: | :----------: | :------: |
| <img src="https://user-images.githubusercontent.com/59987117/93558687-efc22c00-f9b8-11ea-86da-26070f0070e8.png" width="80"> | 박경수(팀장) | frontend |
| <img src="https://user-images.githubusercontent.com/59987117/93560402-0bc7cc80-f9bd-11ea-9782-71c130edff8c.png" width="50"> |    정현희    | frontend |
| <img src="https://user-images.githubusercontent.com/59987117/93560455-2e59e580-f9bd-11ea-8d49-1a65fa274daf.png" width="50"> |    최규식    | backend  |
| <img src="https://user-images.githubusercontent.com/59987117/93560485-46316980-f9bd-11ea-9e5a-4ad085d72cb6.png" width="50"> |    고소영    | backend  |
| <img src="https://user-images.githubusercontent.com/59987117/93560546-606b4780-f9bd-11ea-8694-752476a80c7c.png" width="50"> |    유혜린    | backend  |



## 기술스택

![image](https://user-images.githubusercontent.com/59987117/93558491-84785a00-f9b8-11ea-891d-251f5a4f0ce4.png)

## 실행방법

### Sub1

```sh
cd sub1
pip install -r requirements.txt
python parse.py
python analyse.py
python visualize.py
```



### Sub 2

**Backend**

```sh
cd sub2/backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py initialize
python manage.py runserver
```

**Frontend**

```sh
cd sub2/frontend
npm install
npm run serve		OR		yarn serve --port 3000
```

