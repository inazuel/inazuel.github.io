Title: pelican blog 04. 구글 코랩 노트북에서 블로그 글 쓰기
Date: 2025-09-09 18:50
Modified: 2025-09-09 18:50
Category: Pelican
Tags: python, pelican
Slug: 20250709_01_google_Colab_notebook_post
Authors: inazuel
Summary: Pelican Posts

&nbsp;&nbsp; 이번에는 md 대신 구글 코랩의 주피터 노트북을 사용하여 포스트를 작성하기로 했다. 그 이유로는 두 가지가 있다. 첫 번째 이유는 외부에서 접속해서 글을 작성할 필요성이 있었다. 매번 깃이 설치된 노트북을 들고 다니며 글을 작성하고 커밋을 하기에는 불편한 점이 있기 때문이다. 즉, PC 이외의 도구를 사용해서도 블로그 포스팅이 가능해진다. 두 번째로는 md 편집기의 도움 없이도 포스트를 작성할 수 있다. (사실상 코랩 노트북이 md 편집기이다) 무엇보다 모바일 환경에서 사용할 만한 적절한 편집기도 없을뿐더러 쓸만한 대부분의 윈도우용 프로그램은 유료이다. 물론 코랩 노트북이 그런 유료 프로그램들만큼 편하다는 것은 아니지만, 그래도 쓸 만하다.


&nbsp;&nbsp;그렇다고 하여 장점만 있는 것은 아니다. 일단 태블릿에서는 코랩 파일을 작성하는 데 불편함이 존재한다. 웹에서 구글 드라이브에 접속하면 무조건 앱이 실행된다. 그러나 앱에서는 새 주피터 노트북을 만들고 수정할 수 없다. 그리고 만들어져 있는 파일을 열더라도 웹브라우저로 연결되어 열린다. 즉, 모바일 환경에서는 불편함이 존재한다.

&nbsp;&nbsp;글을 작성하는 도구와 그 도구에 따라서는 공간상의 제약이 사라지는 점, 그리고 글을 작성하기에 비교적 편하다는 장점 때문에 코랩의 주피터 노트북을 선택하였다. 이것을 사용하는 방법은 간단하다. 코랩에는 nnbconver가 설치되어 있는 것을 https://colab.research.google.com/notebooks/relnotes.ipynb 에서 확인할 수 있었다. 2023-03-10 일자로 nbconvert 5.6.1 -> 6.5.4로 업데이트되었다고 나와 있다. 이것을 사용하는 방법 https://nbconvert.readthedocs.io/en/latest/usage.html#convert-notebook에서 확인할 수 있다.

&nbsp;&nbsp;나의 경우는 https://colab.google 에서 New Notebook을 클릭했더니 구글 드라이브 내에 Calab Noteboos 라는 폴더가 자동으로 생성되었다. 그 내부에 github_blog_post라는 폴더를 생성했다. 앞으로 주피터 노트북으로 작성되는 내용은 github_blog_post 내부에 저장될 것이다. 그다음 필요한 것은 아래의 명령어를 사용해서 구글 드라이브를 마운트 해주면 된다.


```python
from google.colab import drive
drive.mount('/content/drive')
```

    Mounted at /content/drive


&nbsp;&nbsp;이것으로 마운트 되면 https://nbconvert.readthedocs.io/en/latest/usage.html을 참조해서 아래의 명령어를 사용하여 마크다운으로 변경해 주면 된다. md이외에도 html이나 그 외의 여러 종류의 변환을 제공하고 있음을 알 수 있다.


```python
!jupyter nbconvert --to markdown "/content/drive/MyDrive/Colab Notebooks/github_blog_post/test-blog-post.ipynb"
#[------------필수 구간----------------------------------]/[파일 위치에 따라 달라질 수 있음]/[--파일명 맟 확장자명---]
```

    [NbConvertApp] Converting notebook /content/drive/MyDrive/Colab Notebooks/blog_post/test-blog-post.ipynb to markdown
    [NbConvertApp] Writing 20 bytes to /content/drive/MyDrive/Colab Notebooks/blog_post/test-blog-post.md


&nbsp;&nbsp;  !jupyter nbconvert --to [원하는 변환 포맷] "/content/drive/MyDrive/디렉토리/파일명.ipynb" 의 구조인 것을 알 수 있을 것이다. 이렇게 복잡한 구조인 것은 구글 드라이브를 사용하기 때문이지 개인 PC에서 한다면 경로를 저렇게까지 할 필요는 없을 것이다. 문제없이 실행되었다면 blog_post 폴더 내부에 test-blog-post.md라는 파일이 생성되었을 것이다.

&nbsp;&nbsp;지금으로써는 구글 드라이브와 깃허브가 연동되어 있지 않아서 만들어진 것을 내려받아 PC에서 직접 커밋을 해줘야 한다는 불편함이 존재한다. 그리고 주의할 점이었다. 앞에서 sitemap.xml을 추가했기 때문에 커밋을 할 때의 명령어는 아래와 같이 입력해야 한다.
```
pelican content -s pelicanconf.py
git add .
git commit -m "New post: [포스트 제목]"
git push origin master
```

&nbsp;&nbsp;이것으로, 코랩으로 포스트 작성 및 md파일로 변환하기는 완료되었다. 이제는 외부에서 미리 블로그 글을 작성해 둘 수 있게 되었고, 작성 방식도 조금은 편해졌으며 필요에 따라서는 파이썬 코딩 및 실행 결과물도 출력할 수 있게 되었다.


```python
from google.colab import drive
drive.mount('/content/drive')
```

    Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).



```python
notebook_filename = "20250709_01_google_Colab_notebook_post.ipynb"
```


```python
!jupyter nbconvert --to markdown "/content/drive/MyDrive/Colab Notebooks/github_blog_post/{notebook_filename}"
```

    [NbConvertApp] Converting notebook /content/drive/MyDrive/Colab Notebooks/github_blog_post/20250709_01_google_Colab_notebook_post.ipynb to markdown
    [NbConvertApp] Writing 3240 bytes to /content/drive/MyDrive/Colab Notebooks/github_blog_post/20250709_01_google_Colab_notebook_post.md

