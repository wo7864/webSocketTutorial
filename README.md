# 웹소켓 예제
React + TypeScript, Django 사이에서 웹소켓을 이용한 통신의 매우 작은 예제입니다.


# 준비

## Client
```
cd client
npm install
npm run dev
```

## django_server
django, restframework를 포함하는 가상환경
```
pip install channel
python manage.py runserver
```

# 실행
버튼을 누르면 서버에서 0에서 10까지 보냄에 따라 Clietn에 숫자가 반영되어 올라갑니다.

