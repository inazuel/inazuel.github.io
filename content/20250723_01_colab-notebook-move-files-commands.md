Title: pelican blog 06.코랩 노트북에서 명령어로 파일이동 하는 방법
Date: 2025-07-23 19:45
Modified: 2025-07-23 19:45
Category: Pelican
Tags: python, pelican, google, colab
Slug: 20250722_01_colab-notebook-move-files-commands
Authors: inazuel
Summary: Pelican Posts

&nbsp;&nbsp; 지난 포스트 <a href="https://inazuel.github.io/20250711_01_google_Colab_notebook_pelican_clone_and_push.html" target="_blank">pelican blog 05. 구글 코랩 노트북 pelican clone과 push 하기</a>와 <a href="https://inazuel.github.io/20250709_01_google_Colab_notebook_post.html" target="_blank">pelican blog 04. 구글 코랩 노트북에서 블로그 글 쓰기</a>를 하나로 합쳐서 코랩 노트북으로 깃허브 블로그를 좀 더 편하게 이용하는 것을 기록해 둔다.

## 1. 구글드라이브 마운트


```python
from google.colab import drive
drive.mount('/gdrive')
```

## 2. 파일명 변수 지정

&nbsp;&nbsp; 편의를 위해서 파일명을 변수로 지정해 줬다.


```python
# 파일명 입력
a = input('파일명을 입력하시오 :')
```

## 3. 백업을 위해 파일 이동

&nbsp;&nbsp; 백업을 위해 이러한 방식을 선택했다. 하지만 다른 방식이 편하다면 생략 가능하다. (나의 경우는 /content/drive/MyDrive/Colab Notebooks/ 내부에 포스트 할 파일을 먼저 만들고 1차로 한번 읽어본 다음 /github_blog_post/ 로 {a}.ipynb 를 이동시켜서 백업을 해놓기 때문에 이런 방식이 되는데 개인의 취향에 따라서 이 과정은 제외할 수도 있다.)


```python
# 파일 이동하기
import shutil
# --- 이동할 파일/폴더의 원본 경로 ---
source_path = f'/content/drive/MyDrive/Colab Notebooks/{a}.ipynb'

# --- 이동될 대상 경로 (폴더 또는 새로운 이름) ---
destination_path = '/content/drive/MyDrive/Colab Notebooks/github_blog_post'
shutil.move(source_path, destination_path)
```

## 4. nbconvert 로 ipynb에서 md 파일로 변환

&nbsp;&nbsp; 자세히 알고 싶다면 <a href="https://inazuel.github.io/20250709_01_google_Colab_notebook_post.html" target="_blank">pelican blog 04. 구글 코랩 노트북에서 블로그 글 쓰기</a> 또는 <a href="https://nbconvert.readthedocs.io/en/latest/usage.html" target="_blank">https://nbconvert.readthedocs.io/en/latest/usage.html</a>를 참고하면 된다. 또한 구글 코랩에서는 2025년 7월 22일 기준으로 6.5.4 버전이 설치되어있다.


```python
# ipynb 를 md로 변환
!jupyter nbconvert --to markdown "/content/drive/MyDrive/Colab Notebooks/github_blog_post/{a}.ipynb"
```

## 5. 특정 경로로 md 파일 복사

&nbsp;&nbsp;구글 드라이브의 GUI 환경에서 직접 해당 파일을 이동시키는 게 더 편하다면 생략 가능하다.


```python
# github_blog_post/{a}.md 파일을 inazuel.github.io/content 로 복사
# import shutil
source_file = f'/content/drive/MyDrive/Colab Notebooks/github_blog_post/{a}.md'
destination_folder ='/content/drive/MyDrive/Colab Notebooks/xxxxxxx.github.io/content'
shutil.copy(source_file, destination_folder)
```

&nbsp;&nbsp;마지막으로 아래의 변수설정 및 명령어를 참고하여 커밋을 한다.


```python
GIT_USERNAME = "xxxxxxx"  # 깃허브 유저네임
IDGIT_EMAIL = "xxxxxxx@xxxxxxx.com" # 깃허브 이메일
GITHUB_PAT = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # 깃허브에서 생성한 PAT
DRIVE_REPO_PATH = "/content/drive/MyDrive/Colab Notebooks/xxxxxxx.github.io" # !git clone 한 리포지토리의 root 경로
GITHUB_REPO_URL = "https://github.com/xxxxxxx/xxxxxxx.github.io.git"  # !git clone 한 리포지토리의 URL
PUSH_URL =  GITHUB_REPO_URL.replace("https://", f"https://{GIT_USERNAME}:{GITHUB_PAT}@")  # !git push 리포지토리의 URL
BRANCH_NAME = "master" # 설정에 따라 main 또는 master
```


```python
!git config --global user.name "{GIT_USERNAME}"
!git config --global user.email "{GIT_EMAIL}"
```


```python
# 클론된 저장소 디랙토리로 이동
%cd "{DRIVE_REPO_PATH}"
```


```python
commit_name = input('커밋 메시지를 입력하시오 :')
```


```python
!git add content
!git commit -m "New post: [{commit_name}]"
!git push "{PUSH_URL}" "{BRANCH_NAME}"
```
