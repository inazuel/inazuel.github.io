+++
title = 'github hugo에서 date와 lastmod 자동 입력'
draft = false
author = 'admin'
+++

# 개요

hugo로 포스트를 작성하다 보면 매번 front matter에 date 값을 입력해야 한다. 이런 불편함을 최소화하기 위해 여기에서는 date와 lastmod를 자동으로 입력되게 하는 방법을 Gemini로 찾았다.

## hugo.toml 편집

[https://gohugo.io/methods/page/gitinfo/](https://gohugo.io/methods/page/gitinfo/) 를 참고하여 아래의 내용을 ```inazuel.github.io/config/_default/hugo.toml```에 추가한다.


```python
enableGitInfo = true
[frontmatter]
date = ["date", "publishDate", "lastmod", ":git"]
lastmod = ["lastmod", "date", "publishDate", ":git"]
```

## front matter 필드 변경



 앞으로 작성하는 포스트의 front matter 필드에 date와 lastmod를 입력하지 않아도 이젠 자동으로 처리가 된다.

 그리고 기존의 포스트에서 date와 lastmod를 삭제해도 되지만 굳이 이미 입력한 내용을 제거할 필요는 없다. front matter 필드에 작성된 내용이 우선순위가 높은 것으로 보인다.
