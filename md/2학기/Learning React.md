## Learning React

---

#### 디폴트 파라미터

```javascript
const log = (name="오성원", activity="테니스") => {
    console.log(`${name}은 ${activity}를 좋아합니다.`)
}
log() // 오성원은 테니스를 좋아합니
```

- 아무 인자도 지정하지 않아도 디폴트 값을 사용해 실행 가능

```javascript
const defaultPerson = {
    name: {
        first: "성원",
        last: "오"
    },
    favActivity: "테니스"
};

const log = (p=defaultPerson) => {
    console.log(`${p.name.first}은(는) ${p.favActivity}를 좋아합니다.`)
}
log() // 성원은(는) 
```

---

#### 객체 리터럴 개선

- 구조 분해의 반대

- 구조를 다시 만들어내는 과정 또는 내용을 한데 묶는 과정

---

#### 스프레드 연산자

- 스프레드 연산자는 3개의 점(...)으로 이뤄진 연산자

- 내용을 조합

```javascript
const peaks = ["대청봉", "중청봉", "소청봉"];
const canyons = ["천불동계곡", '가야동계곡'];
const seoraksan = [...peaks, ...canyons];

console.log(seoraksan.join(', '))
// 대청봉, 중청봉, 소청봉, 천불동계곡, 가야동계곡
```

---

#### 프로미스 만들기

- **getPerple** 함수는 새로운 프로미스를 반환한다. 프로미스는 API에 요청을 보낸다. 프로미스가 성공하면 데이터를 읽어온다. 프로미스가 성공하지 않으면 오류를 발생시킨다.

```javascript
const getPeople = count => 
new Promise((resolves, rejects) => {
  const api = `https://api.randomuser.me/?nat=US&results=${count}`;
  const request = new XMLHttpRequest();
  request.open("GET", api);
  request.onload = () =>
    request.status === 200
      ? resolves(JSON.parse(request.response).results)
      : PromiseRejectionEvent(Error(request.statusText));
  request.onerror = err => rejects(err);
  request.send();
});

getPeople(5)
  .then(members => console.log(members))
  .catch(error => console.log(`getPeople failed: ${error.message}`));
```

---

#### 클래스

- ES2015 이전에는 공식적으로 자바스크립트 명세에 클래스 문법이 없었음

- 리액트는 점차 클래스를 멀리하기 시작함

- 리액트는 함수를 사용해 컴포넌트를 구성

- 클래스를 만들 때는 보통 첫 글자를 대문자로 표시

---

#### ES6 모듈

- 자바스크립트 모듈은 다른 자바스크립트 파일에서 이름 충돌이 없이 쉽게 불러서 활용할 수 있는 재사용 가능한 코드 조각을 말한다.

- JS는 모듈을 한 모듈당 하나씩 별도의 파일로 저장

---

#### 함수형이란 무엇인가?

- 정수나 문자열 같은 일반적인 값과 마친가지로 함수를 취급할 수 있다

- 함수가 애플리케이션의 데이터를 표현할 수 있음

- 문자열이나 수, 또는 다른 모든 값과 마찬가지로 var 키워드를 사용해서 함수를 정의할 수 있다.

```javascript
var log - function(message) {
    console.log(message);
}
log("자바스크립트에서는 함수를 변수에 넣을 수 있습니다.)

// 화살표 함수
const log = msg => {
    console.log(msg)
}
```

- 함수를 변수에 넣을 수 있는 것과 마찬가지로, 함수를 객체에도 넣을 수 있다

```javascript
const obj = {
    msg: "함수를 다른 값과 마찬가지로 객체에 추가할 수 있습니다.",
    log(msg) {
        console.log(msg);
    }
}

obj.log(obj.msg);
```

- 인자로도 넘길 수 있음

```javascript
const insideFn = logger => {
    logger("함수를 다른 함수에 인자로 넘길수도 있다.");
}

insideFn(msg => console.log(msg));
```

---

#### 명령형 프로그래밍과 선언적 프로그래밍 비교

- 함수형 프로그램이은 선언적 프로그래밍이라는 더 넓은 프로그래밍 패러다임의 한 가지

- 선언적 프로그래밍
  
  - 과정을 하나하나 기술하는 것보다 필요한 것이 어떤 것인지를 기술하는 것에 더 중점을 두고 구조를 세워나가는것

- 명령형 프로그래밍
  
  - 코드로 원하는 결과를 달성해 나가는 과정에만 관심을 두는것

---

#### 불변성

- push

```javascript
let list = [
  { title: "과격한 빨강"},
  { title: "잔디"},
  { title: "파티 핑크"}
];

const addColor = function(title, colors) {
  colors.push({ title: title });
  return colors;
}

console.log(list.length); // 3
console.log(addColor("화려한 녹색", list).length); // 4
console.log(list.length); // 4
```

- push는 불변성 함수가 아님

- 불변성을 지키기 위해서는 concat을 사용

```javascript
let list = [
  { title: "과격한 빨강"},
  { title: "잔디"},
  { title: "파티 핑크"}
];

const addColor = (title, array) => array.concat({ title });

console.log(list.length); // 3
console.log(addColor("화려한 녹색", list).length); // 4
console.log(list.length); // 3
```

---

#### 순수 함수

- 파라미터에 의해서만 반환값이 결정되는 함수를 뜻함

- 순수 함수는 최소한 하나 이상의 인수를 받고, 인자가 같으면 항상 같은 값이나 함수를 반환한다

- 순수하지 않은 함수

```javascript
const frederick = {
  name: "Frederick Douglass",
  canRead: false,
  canWrite: false
};

const selfEducate = () => {
  frederick.canRead = true;
  frederick.canWrite = true;
  return frederick;
}

selfEducate();
console.log(frederick);
// { name: 'Frederick Douglass', canRead: true, canWrite: true }
```

- 이 함수는 인자를 취하지 않으며, 값을 반환하거나 함수를 반환하지도 않는다

- 파라미터를 받아보자

```javascript
const frederick = {
  name: "Frederick Douglass",
  canRead: false,
  canWrite: false
};

const selfEducate = (person) => {
  person.canRead = true;
  person.canWrite = true;
  return person;
}

console.log(frederick);
console.log(selfEducate(frederick));
console.log(frederick);
//{ name: 'Frederick Douglass', canRead: false, canWrite: false }       
// { name: 'Frederick Douglass', canRead: true, canWrite: true }
// { name: 'Frederick Douglass', canRead: true, canWrite: true }
```

- 파라미터를 받기는 하지만 이 함수도 순수하지 않다(부수 효과가 있기 때문)

- 순수 함수

```javascript
const frederick = {
  name: "Frederick Douglass",
  canRead: false,
  canWrite: false
};

const selfEducate = (person) => ({
  ...person,
  canRead: true,
  canWrite: true
});

console.log(frederick);
console.log(selfEducate(frederick));
console.log(frederick);
// { name: 'Frederick Douglass', canRead: false, canWrite: false }       
// { name: 'Frederick Douglass', canRead: true, canWrite: true }
// { name: 'Frederick Douglass', canRead: false, canWrite: false }  
```

- **순수 함수는 파라미터를 최소 하나 이상 받아야 한다**
- **순수 함수는 값이나 다른 함수를 반환해야 한다**
- **순수 함수는 인자나 함수 밖에 있는 다른 변수를 변경하거나, 입출력을 수행해서는 안된다**

---

#### 데이터 변환

- Array.join은 배열의 모든 원소를 인자로 받은 구분자로 연결한 문자열을 반환

```javascript
const schools = ["동신", "서울", "고려", "동덕"]

console.log(schools.join(", "));
// 동신, 서울, 고려, 동덕);
```

- Array.filter는 '동'으로 시작하는 단어를 추출

```javascript
const schools = ["동신", "서울", "고려", "동덕"]

const wSchools = schools.filter(school => school[0] === "동");
console.log(wSchools)
// [ '동신', '동덕' ]
```

- Array.map은 배열의 모든 원소에 적용해서 반환받은 값으로 이뤄진 새 배열을 반환

```javascript
const schools = ["동신", "서울", "고려", "동덕"]

const cxz = schools.map(school => `${school} 대학교`);
console.log(cxz.join(", "));
// 동신 대학교, 서울 대학교, 고려 대학교, 동덕 대학교
```
