## 221011 - Static/Media

---

#### Static files

- 정적 파일
  
  - 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
  
  - 파일 자체가 고정되어 있고, 서비스 중에도 추가되거나 변경되지 않고 고정 되어있음

---

#### Media file

- 사용자가 웹에서 업로드하는 정적 파일

---

#### Django에서 정적 파일을 구성하고 사용하기 위한 단계

- INSTALLED_APPS에 'django.contrib.staticfiles'가 등록돼있는지 확인

- STATIC_URL = '/static/' 추가하기

- 앱의 static 폴더에 정적 파일을 위치하기
  
  - 예시) my_app/static/sample_img.jpg

- 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기

---


