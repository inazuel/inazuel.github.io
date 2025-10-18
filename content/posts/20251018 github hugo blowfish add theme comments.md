+++
title = 'github hugo blowfish theme 댓글 추가하기'
draft = false
showComments = true
+++

# 개요

github blog를 만들었다. 이전에는 pelican blog를 사용하기 위해 시도해 봤으나 여러 어려움 때문에 포기하고 hugo로 넘어왔다. 향후 기회가 된다면 pelican blog와 hugo의 설치 과정도 기록할 생각이다.

이 포스트에서는 댓글 기능 추가하는 과정을 기록했다. 사용하는 테마는 blowfish이다. 댓글 기능 서비스 대상으로는 Disqus, Utterances, giscus 가 있었다. Hugo에서는 기본적으로 Disqus를 지원한다고 하지만 [https://en.wikipedia.org/wiki/Disqus](https://en.wikipedia.org/wiki/Disqus) 에 의하면 광고와 개인정보 관련 이슈가 있기 때문에 처음부터 고려 사항은 아니었다. giscus를 사용해 보려고 여러모로 시도를 해봤는데 blowfish에서 gisicus를 적용할 수 있는 자료를 찾지 못했다. 그렇기에 utterances를 사용하게 되었다.

## utterances 사용

utterances를 사용하기로 한 이유는  [Hugo 블로그에 utterances를 이용한 댓글기능 추가하기
오니부기 개발로그:티스토리](https://trialdeveloper.tistory.com/117) 에서 해당 정보를 접할 수 있었기 때문이다. 이 내용을 기반으로 blowfish theme v2.89.1 버전을 토대로 하여 작성했다. 현재(2025-10-18) v2.91.0까지 나와 있다.

## 1. repo 생성

github에서 블로그용 repositories를 만들어서 사용 중일 것이다. 이것과는 별개의 댓글용 repositories를 만들어서 운영하는 것이 관리 측면에서 편하다고 한다. 그러니 용도에 맞는 이름의 repositories를 만들어준다. (예를 들면 ```blog-comments```, ```comments``` 등처럼 직관적인 것이 가장 좋습니다.)

## 2. utterances 설치

[https://github.com/apps/utterances](https://github.com/apps/utterances) 에 접속해서 install을 선택하고,
Only select repositories에서 댓글용으로 만든 repositories를 선택한다.

## 3. utterances 설정

[https://utteranc.es/](https://utteranc.es/) 에서 설정을 해준다. configuration의 Repository의 repo: 부분은 inazuel/blog-comments 를 입력한다. 나머지는 기본값에서 변경해 줄 사항은 없으나 필요에 따라서 theme 부분을 본인이 원하는 것으로 바꿔준다. (제 경우는 icy Dark로 했습니다) 여기까지 진행했다면, Enable Utterances 부분에 그렇다면 아래와 같은 형식으로 코드가 생성된 것을 볼 수 있다.

```
<script src="https://utteranc.es/client.js"
        repo="[ENTER REPO HERE]"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
```

어디까지나 샘플이며, 이후 필요하다면, 일부 설정을 바꿀 수도 있다. theme의 기본 옵션으로는 ```github-light```, ```github-dark```, ```preferred-color-scheme```, ```github-dark-orange```, ```icy-dark```, ```dark-blue```, ```photon-dark```, ```boxy-light```, ```gruvbox-dark``` 가 있다.

# blog theme 파일 수정 및 추가

[https://blowfish.page/docs/partials](https://blowfish.page/docs/partials) 을 참고하여 파일을 만들거나 수정하면 된다.(테마 버전에 따라 달라질 수 있습니다) 이때 폴더 및 파일이 blowfish theme에 파일이 존재할 수도 있지만 경우에 따라서는 폴더 및 파일이 없을 수도 있다. 없다면 만들어주면 된다. 또한, 아래 경로에 있는 'inazuel.github.io'는 프로젝트명으로, 나의 경우는 repo명과 블로그 주소와 프로젝트명이 동일하다. 보통 이러한 방식으로 만든다고 한다.

## 4. comments.html 파일 추가

'3. utterances' 설정에서 최종적으로 생성된 코드를 ```inazuel.github.io/layouts/partials/comments.html```에 입력한다.

## 5. params.toml 내용 추가

```inazuel.github.io/config/_default/params.toml```의 ```[article]``` 하단부에 ```showComments = true```를 추가한다.

## 6. single.html 파일 복사

```inazuel.github.io/themes/blowfish/layouts/_default```의 ```single.html``` 파일을  ```inazuel.github.io/layouts/_default/```에 그대로 복사한다. 이때 내용에 별도의 수정 및 변경을 할 필요가 없다.

이것으로 utterances 설치는 되었다. 이후 commit과 push를 하여 github blog에 잘 적용되었는지 확인해 보면 된다.
