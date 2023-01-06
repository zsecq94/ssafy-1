## 221109 - Vue Router

---

#### Sketch, Figma(프로토타입 툴)

---

- vue create cue-router-app : 프로젝트생성

- cd vue-router-app : 디렉토리 이동

- vue add router : vue cli를 통해 router plugin 적용

---

- $router.push : url 이동

- [Math.floor(Math.random() * this.list.length)]; : 랜덤번호생성

---

- 전역 가드

- 다른 url주소로 이동할 때 항상 실행

```js
router.beforeEach((to, from, next) => {
  // 로그인 여부
  const isLoggedIn = false

  // 로그인이 필요한 페이지
  const authPages = ['hello']

  // 앞으로 이동할 페이지(to)가 로그인이 필요한 사이트인지 확인
  const isAuthRequired = authPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    console.log('로그인으로 이동!')
    next({ name: 'login' })
  } else {
    console.log('to로 이동!')
    next()
  }
})
```

---

- 라우터 가드(라우트 안에 작성)

- 특정 route에 대해서만 가드를 설정하고 싶을 때

```js
const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    // 여기부터
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인이 되어있음')
        next({ name: 'home' })
      } else {
        next()
      }
    }
  }
]
```

---

- 컴포넌트 가드

- 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행

```js
// 컴포넌트에 작성
export default {
  beforeRouteUpdate(to, from, next) {
  this.userName = to.params.userName
  next()
  }
}
```

---

- 404

- 작성한 목록이 아닌 다른 모든 요청이 있을시

- 라우트 목록의 가장 마지막에 작성해야 함

```js
  {
    path: '*',
    redirect: { name: 'NotFound404' }
  }
```

---
