Title: pelican blog 폰트 변경하기
Date: 2025-07-04 20:00
Modified: 2025-07-04 20:00
Category: Pelican
Tags: python, pelican
Slug: 20250704_02_Adjust line-height for blog post content
Authors: inazuel
Summary: Pelican Posts

&nbsp;&nbsp;이번에는 줄 간격을 변경해주었다. 글의 줄이 너무 가까워서 가시성이 좋지 않다고 판단했기 때문이다 <br>

&nbsp;&nbsp;content/static/css/custom.css 에 아래의 코드를 입력했다. 참고로 이것은 실패했다.

```
/* 블로그 글 본문의 줄 간격 설정 */
.article-content p,
.article-content li {
    line-height: 2.0 !important; /* 폰트 크기의 200% (2배) */
}
```

&nbsp;&nbsp;그래서 다음으로 나온 해결방법은 아래의 코드와 같다.
```
/* 웹페이지 전체의 기본 줄 간격 설정 */
body {
    line-height: 2.0 !important; /* 폰트 크기의 200% (2배) */
}

```
&nbsp;&nbsp;빌드 및 배포
```
git add content/static/css/custom.css
git commit -m "Adjust line-height in theme style.css"
git push origin master
```
&nbsp;&nbsp;이 방법은 분명 본문의 줄간격을 변경해준다. 그러나 문제가 있는데, 본문을 포함한 블로그 전체의 줄간격도 200%로 바뀐다는 것이다.<br>
&nbsp;&nbsp;여러모로 아쉽지만 이 방법을 사용하기로 했다.


