+++
title = 'github hugo에서 date와 lastmod 자동 입력'
date = 2026-02-10T23:42:33+09:00
draft = false
categories = ["블로그 관리"]
tags = ['hugo', 'blog', 'frontmatter', 'git']
+++

# 1. 개요

hugo로 포스트를 작성하다 보면 매번 front matter에 date 값을 입력해야 한다. 이런 불편함을 최소화하기 위해 여기에서는 date와 lastmod를 자동으로 입력되게 하는 방법이 있다.

# 2. hugo.toml 편집

[https://gohugo.io/methods/page/gitinfo/](https://gohugo.io/methods/page/gitinfo/) 를 참고하여 아래의 내용을 ```inazuel.github.io/config/_default/hugo.toml```에 추가한다.


```python
enableGitInfo = true
timeZone = "Asia/Seoul"
[frontmatter]
date = ["date", "publishDate", "lastmod", ":git"]
lastmod = ["lastmod", "date", "publishDate", ":git"]
```

 포스트의 front matter 필드에 date와 lastmod를 입력하지 않아도 이젠 자동으로 처리가 될 것이다.

 그리고 기존의 포스트에서 date와 lastmod를 삭제해도 되지만 굳이 이미 입력한 내용을 제거할 필요는 없다. front matter 필드에 작성된 내용이 우선순위가 높은 것으로 보인다. 그러나 문제가 발생했다.

 # 3. 문제점

아쉽게도 커밋을 할 때의 기록이 적용되는 것을 이용한 것이 오류를 일으켰다. 포스트를 수정하면 lastmod가 갱신되어야 하는데 date가 갱신되는 현상이 발생한 것이다. 해결 방법은 찾지 못했다. 깃과 구글 드라이브를 연동해서 사용하고 있는 상황에서는 다른 방법을 찾기 전까지는 프론트 메타를 직접 입력하는 선택지 밖에 없어 보인다.