Title: pelican blog 03. google search console 등록하기
Date: 2025-07-08 0:55
Modified: 2025-07-08 1:05
Category: Pelican
Tags: pelican
Slug: 20250708_01_google_search_console
Authors: inazuel
Summary: Pelican Posts

&nbsp;&nbsp;이번에는 구글 search console에 내 블로그를 등록했다. 다만 문제가 있다면, 내가 사용하는 것은 pelican이고 지킬(Jekyll) 에 비하면 그 정보가 너무 적었다. 정확히는 적다고 느꼈다. 그 원인은 나는 웹이나 프로그래밍에 대해서 아는 바가 없기때문다. 공식 문서를 읽더라도 이해하기에 어려움이 있었기에 ai (google gemini)를 사용해서 구글 search console 에 내 블로그를 등록했다. 지금은 심사기간이고, 만약 여러분이 이 글을 읽고 있다면 이 방법은 성공한 것이라고 할 수 있다.<br>

**플러그인을 설치하는 방법도 있다고 합니다. 제가 한 방법이 더 어려울 수도 있으니 플러그인을 사용하는 방법을 찾아보시는 것도 좋으리라 생각합니다.**<br>

[Github-Blog-검색창-노출시키기](https://velog.io/@eona1301/Github-Blog-%EA%B2%80%EC%83%89%EC%B0%BD-%EB%85%B8%EC%B6%9C%EC%8B%9C%ED%82%A4%EA%B8%B0)를 참고하였다. 이 글에서 알 수 있는 것은 아래와 같다.<br>

1. [https://search.google.com/search-console/about](https://search.google.com/search-console/about) 에 접속하여 'URL 접두어' 방식으로 블로그를 등록한다.
2. 'HTML 파일'방식으로 등록후 /root 에 이동시킨다. (이 방법이 pelican에서는 많이 다르다.)
3. 'sitemap.xml'를 설정해야 한다.
4. 'robots.txt'를 만들어줘야 한다.

&nbsp;&nbsp;1. 구글 search console에서 우측의 'URL 접두어'를 선택한다. 다음, 'HTML 파일'을 선택한다. 'googlexxxxxxxxxxxxxxxxx.html' 형식의 파일을 다운로드 할 수 있을 것이다. 이것을 xxxxx.github.io\content\extra 폴더 내부로 이동시킨다. <br>
&nbsp;&nbsp;2. 동일한 xxxxxl.github.io\content\extra 폴더 내부에 'robots.txt' 파일을 만들어주고 아래의 내용을 입력해준다. 만약 해당 폴더가 없다면 만들어주면 된다.
```
User-agent: *
Allow: /

<!--아래를 본인의 블로그 주소에 맞게 적절히 수정하면 됩니다.-->
Sitemap: https://xxxxx.github.io/sitemap.xml 
```

&nbsp;&nbsp;3. root에 위치해있는 pelicanconf.py 를 편집해줘야 한다. pelicanconf.py를 열고 아래와 같은 내용들이 포함되어야 한다.

&nbsp;&nbsp;3.1.  STATIC_PATHS를 찾아 아래와 같이 되어있는지 확인한다. 만약 STATIC_PATHS이 없다면 아래와 같이 추가해주는 것이 좋다. 구글 search console 등록을 하기때문에 다른 것은 없더라도 extra 는 반드시 포함되어있어야 한다.
```
STATIC_PATHS = ['images', 'extra', 'static']
```
<br>

&nbsp;&nbsp;3.2. EXTRA_PATH_METADATA를 찾아 아래의 내용을 추가해야 한다.

```
EXTRA_PATH_METADATA = {
 "extra/robots.txt": {"path": "robots.txt"},
 'static/fonts/D2Coding-Ver1.3.2-20180524-all.ttf': {'path': 'static/fonts/D2Coding-Ver1.3.2-20180524-all.ttf'},
 'extra/googlexxxxxxxxxxxxxxxxx.html': {'path': 'googlexxxxxxxxxxxxxxxxx.html'},
}
```

&nbsp;&nbsp;이 부분은 추가적인 설명이 필요한데, D2Coding-Ver1.3.2-20180524-all.ttf 라는 폰트를 별도로 추가했기 때문에 이와같은 구조가 된 것이기때문에 일반적인 상황이라면, font 부분은 제거해주는 것이 좋을 것이다. robots.txt 부분과  'extra/google***************.html': {'path': 'google***************.html' 부분이 중요하다. 이 부분을 앞에서 다운받은 html 파일의 이름과 동일하게 바꾸고 추가해주면 된다.<br>

&nbsp;&nbsp;3.3. 그 후 pelicanconf.py에 아래의 내용을 추가해준다. 이 내용의 위치는 크게 상관 없는 거 같다. 나는 pelicanconf.py 내 하단 부분에 추가했다.

```
# --- READERS 설정 (이 부분을 새로 추가) ---
# .html 파일을 콘텐츠로 해석하지 않도록 명시적으로 설정
READERS = {
    'html': None,
}
```
<br>
&nbsp;&nbsp;이 부분이 추가가 되지 않으면 아래와 같은 오류가 발생한다. 아래의 오류의 원인은 gemini에 의하면, '이 에러는 여전히 Pelican이 해당 HTML 파일을 정적 파일이 아닌 블로그 콘텐츠(글이나 페이지)로 오해하고 처리하려 할 때 발생'한다고 한다.

```
[22:19:02] ERROR    Skipping                                                                            contents.py:176
 C:\git_blog\blog\inazuel.github.io\content\extra\googlexxxxxxxxxxxxxxxxx.html: could
 not find information about 'title'
Done: Processed 3 articles, 0 drafts, 0 hidden articles, 0 pages, 0 hidden pages and 0 draft pages in 0.77 seconds.
```
<br>

&nbsp;&nbsp;3.4. pelicanconf.py 하단부에 아래의 내용을 입력하여 sitemap을 생성한다.
```
# 사이트맵 생성----------------------------------
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'pages': 0.5,
        'indexes': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'pages': 'monthly',
        'indexes': 'daily',
    }
}
# ---------------------------------------------------
```
<br>

&nbsp;&nbsp;4. 이제 남은것은 cmd에서 아래의 명령어를 실행해준다. 그 다음은 구글 search console에서 내용을 이어서 해주면 된다. 이 부분은 개인의 상황, 설정 등에 따라 달라질 수 있으니 각자 적절하게 바꿔주면 된다. 
```
rmdir /s /q output
git add .
git commit -m "Successful Pelican build with GSC, sitemap, robots.txt configs"
git push origin master
```
<br>
&nbsp;&nbsp;커밋까지 완료되었다면, 아래의 주소를 적절히 수정해서 접속해보고 결과가 잘 나오는지 확인해보면 된다. 이 부분도 잘 되었다면, 다시 구글 search console로 돌아가서 나머지 절차를 진행하면 된다.

```
https://xxxxx.github.io/googlexxxxxxxxxxxxxxxxx.html
https://xxxxx.github.io/sitemap.xml
https://xxxxx.github.io/robots.txt
```

<br>
&nbsp;&nbsp;잘 되었다면, 구글 search console의 메인화면이 나타날 것이다. 마지막으로 좌측 메뉴의 sitemap에 들어가면, 새 사이트맵 추가라는 항목이 있을 것이다. 그곳에 내 블로그의 주소가 있고, 내 블로그 주소와 함께 별도의 입력칸이 있을 것이다. 그곳에 아래의 내용을 붙여넣어주기만 하면 된다.

``` 
sitemap.xml
```
<br>
&nbsp;&nbsp;이것으로 구글 search console 추가는 완료되었고, 구글 search console 블로그가 등록되기를 기다리기만 하면 된다. 가능하신 분들은 플러그인을 사용해보는 것도 좋을 것이다.