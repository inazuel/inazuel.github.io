+++
title = 'colab notebook에서 nbconvert를 사용하여 ipynb를 md로 변환 및 git commit'
categories = ["블로그 관리"]
tags = ['hugo', 'blog', 'colab', 'ipynb', 'md']
+++

&nbsp;&nbsp; 구글 코랩 노트북(colab notebook)에서 hugo blog의 포스팅을 하기 위해서 글을 쓰는 방법이 있다. hugo blog를 비롯한 md로 포스팅을 하는 블로그 서비스(hexo, pelican, jekyll ...) 코랩에서는 기본적으로 nbconvert가 설치되어있어서 명령어로 ipynb 파일을 md로 변경할 수 있다. 또한 온라인 서비스이기 때문에 외부에서 접속해서 글을 작성할 수 있다는 점이 있다. 이것은 인터넷 연결만 되어있다면, 공용 컴퓨터 혹은 모바일 환경에서도 포스팅이 가능해진다는 것을 의미한다.

&nbsp;&nbsp;다만, 모바일 구글 드라이브 앱에서는 코랩 노트북을 생성할 수 없다. 코랩 노트북을 생성하기 위해서는 <a href="https://colab.google/" target="_blank">https://colab.google/</a>에 접속해서 ```New Notebook```을 클릭하는 별도의 과정을 거치면 된다. 나의 경우, 구글 드라이브의 Colab Notebooks 폴더 내부에 새로운 colab notebook이 생성된 것을 확인할 수 있었다.

&nbsp;&nbsp;nbconvert가 설치되어 있는 것은 <a href="https://colab.research.google.com/notebooks/relnotes.ipynb" target="_blank">https://colab.research.google.com/notebooks/relnotes.ipynb</a>에서 확인할 수 있다. 2023-03-10 일자로 nbconvert 5.6.1 -> 6.5.4로 업데이트되어 있다. 오늘(2025.12.16)기준으로 nbconvert 7.16.6이 최신 버전이고, 코랩에서는 구버전만 지원하지만 마크다운으로 변한하는데 문제가 발생하지 않는다. nbconver가 지원하는 출력 포멧은 HTML, LaTeX, PDF, WebPDF, Reveal.js HTML slideshow, Markdown, Ascii, reStructuredText, executable script, notebook이 있다고 한다.

&nbsp;&nbsp;코랩 노트북에서 nbconver를 사용하기 위한 명령어는 아래와 같다.


```python
from google.colab import drive
drive.mount('/content/drive')
```


```python
!jupyter nbconvert --to markdown "/content/drive/MyDrive/Colab Notebooks/hugo_blog_post/test-blog-post.ipynb"
```

&nbsp;&nbsp; <a href="https://nbconvert.readthedocs.io/en/latest/usage.html" target="_blank">https://nbconvert.readthedocs.io/en/latest/usage.html</a>을 참조하면, 두 번째 명령어의 구조가 ```!jupyter nbconvert --to [변환 포맷] "/content/drive/MyDrive/디렉토리/파일명.ipynb"```인 것을 알 수 있을 것이다. 구글 드라이브를 사용하기 때문에 명령어가 길지만, 일반적인 환경에서는 명령어는 더 짧을 것이다. 문제없이 실행되었다면 ```hugo_blog_post``` 폴더 내부에 ```test-blog-post.md```라는 파일이 생성되었을 것이다.

&nbsp;&nbsp;구글 드라이브와 깃허브가 연동되어 있다면, 앞에서 생성된 md 파일을 적절한 위치(```\inazuel.github.io\content\blog```)로 이동시킨 다음, 아래의 명령어를 참고하여 commit, push를 한다.


```python
commit_name = input('커밋 메시지를 입력하시오 :')
print(commit_name)
```


```python
!git add .
!git commit -m "New post: [{commit_name}]"
print("Changes committed locally.")
!git push "{PUSH_URL}" "{BRANCH_NAME}"
print("Changes pushed to remote.")
```
