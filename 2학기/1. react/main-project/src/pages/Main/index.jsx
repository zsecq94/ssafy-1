import "./main.scss";
import * as React from 'react';

const Main = () => {

  return (
    <div className="main-wrapper">
      <div className="main-title">
        <span>I GoAT</span>
      </div>
      <div className="main-contents">
        이 프로젝트는 Duckgugong의 서비스를 모티브로 작성했습니다.
      </div>
      <div className="about-project">
        싸피 개발자가 직접 제작한 퍼스널컬러 진단 사이트! <br />
        머신러닝 학습 모델을 통해 퍼스널컬러를 진단해드립니다!<br />
      </div>
      <div className="my-website">
        <div className="my-website-title">Our Projects</div>
        <a href="https://lab.ssafy.com/s08-webmobile3-sub2/S08P12C201">
          🏴GitLab
        </a>
        <br /><br />
      </div>
      화장품 추천, 패션 추천 등 자세한 정보를 알고싶다면 회원가입을 진행해주세요! <br />
      <a href="/register"><span>회원가입</span></a>
    </div>
  )
}
export default Main;