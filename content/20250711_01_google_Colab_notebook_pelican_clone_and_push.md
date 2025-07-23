Title: pelican blog 05. 구글 코랩 노트북 pelican clone과 push 하기
Date: 2025-07-11 0:50
Modified: 2025-07-11 0:50
Category: Pelican
Tags: python, pelican, colab
Slug: 20250711_01_google_Colab_notebook_pelican_clone_and_push
Authors: inazuel
Summary: Pelican Posts

&nbsp;&nbsp;지난번에는 <a href="https://inazuel.github.io/20250709_01_google_Colab_notebook_post.html" target="_blank">구글 코랩 노트북을 md로 변환하는 방법</a>을 알아봤었다. 이것의 목적은 온라인에서 글을 쓰기 위함이었다. 이번에는 이와 관련하여 구글 드라이브에 pelican을 구글 드라이브로 clone하고 push하는 것을 하겠다. 이것이 성공하면 모든 것을 컴퓨터만 있으면, 그리고 git을 컴퓨터에 설치하지 않고도 깃허브 블로그 포스팅은 물론이고, 인터넷에 접속할 수 있는 환경만 된다면 때와 장소를 가리지 않고 블로그 포스팅 및 push를 할 수 있게 될 것이다(물론 네이버 블로그나 티스토리같은 블로그를 사용하는 것이 가장 속이 편하긴 하지만).

## 1. clone 하기

&nbsp;&nbsp;사전에 PC에서 push 했던 리포지토리의 내용을 clone 해줘야 한다. 그 전에 아래의 명령어를 실행시킨다. 그리고 나오는 내용을 동의한다.


```python
from google.colab import drive
drive.mount('/gdrive')
```

    Mounted at /gdrive


&nbsp;&nbsp;다음에 입력하는 cd 명령어는 때에 따라서는 생략하고 바로 clone 명령어를 실행해도 된다. 이 경우에는 명령어를 실행하는 코랩 노트북이 있는 위치에 inazuel.github.io 폴더가 자동으로 생성된다. 즉, /Colab Notebooks/clone-and-push.ipynb 에서 clone 명령어를 실행하면 자동으로 /Colab Notebooks/xxxxxx.github.io/ 폴더가 생성된다. 그러니 미리 내가 원하는 위치에 코랩 노트북을 만들고 명령어를 실행하면 생략해도 괜찮다.


```python
# 명령어를 실행하는 코랩 노트북이 해당 위치에 있으면 실행하지 않아도 된다.
%cd '/gdrive/MyDrive/Colab Notebooks'
!git clone https://github.com/inazuel/inazuel.github.io.git
```

    /gdrive/MyDrive/Colab Notebooks


##2. pelican 설치 (선택사항)

&nbsp;&nbsp; 필요하다면 pelican 을 설치한다. 그러나 이러한 것은 일반적인 환경(노트북, 데스크탑 등)에서 하는 것이 좋다. 이번에 설치되었다고 하더라도 런타임을 재설정하거나 코랩 노트북을 닫았다 열면 다시 실행하여 설치해야 하므로 push를 할 때마다 반복적으로 설치를 해야 한다. 그리고** 사실상 yml 파일을 설정했기때문에 불필요한 부분**이다.


```python
!pip install pelican
```

&nbsp;&nbsp;또한 아래와 같은 오류가 발생한다고 해서 pelican 명령어를 사용하지 못하는 것은 아니다.
```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
ipython 7.34.0 requires jedi>=0.16, which is not installed.
```
&nbsp;&nbsp;pelican과 마찬가지로 필요에 따라서 설치 유무를 선택한다.


```python
!pip install jedi
```

## 3. 변수 설정

&nbsp;&nbsp;편의를 위해서 아래의 변수를 설정한다. 변수로 설정 하면 나중에 수정할 때 편하고 실수가 줄어들 수 있을것이다. 각자의 상황에 맞게 변경하고 실행한다.


```python
GIT_USERNAME = "inazuel" # 깃허브 유저네임
GIT_EMAIL = "inazuel@gmail.com" # 깃허브 이메일
GITHUB_PAT = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # 깃허브에서 생성한 PAT
DRIVE_REPO_PATH = "/gdrive/MyDrive/Colab Notebooks/inazuel.github.io" # !git clone 한 리포지토리의 root 경로
GITHUB_REPO_URL = "https://github.com/inazuel/inazuel.github.io.git"  # !git clone 한 리포지토리의 URL
PUSH_URL =  GITHUB_REPO_URL.replace("https://", f"https://{GIT_USERNAME}:{GITHUB_PAT}@")  # !git push 리포지토리의 URL
BRANCH_NAME = "master" # 설정에 따라 main 또는 master
```


```python
# git 사용자 정보
!git config --global user.name "{GIT_USERNAME}"
!git config --global user.email "{GIT_EMAIL}"
```


```python
# 클론된 저장소 디랙토리로 이동
%cd "{DRIVE_REPO_PATH}"
```


```python
# commit & push
# !pelican content -s pelicanconf.py #필요한 경우에만 사용
!git add content
!git commit -m "Update blog content & add new post: [여기에 실제 포스트 제목을 입력하세요]"
!git push "{PUSH_URL}" "{BRANCH_NAME}"
```

&nbsp;&nbsp;이것으로 컴퓨터(또는 모바일기기) 그리고 인터넷 연결만 된다면 포스팅부터 push까지 모두 가능하게 되었다. 이젠 무거운 노트북을 들고 다니지 않아도 된다. 편의를 위해서 무선 키보드와 마우스 정도가 필요하다고 할 수 있다.
