AUTHOR = 'inazuel'
SITENAME = 'record of my life'
SITEURL = "https://inazuel.github.io"

PATH = "content"

TIMEZONE = 'Etc/GMT+9'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# 20250701 추가항목
# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "images",
    "extra/robots.txt",
]


import os

# pelicanconf.py 파일이 있는 디렉토리 (즉, C:\git_blog\blog\inazuel.github.io\)의 절대 경로
PATH = os.path.abspath(os.path.dirname(__file__))

# THEME 변수 설정:
# PATH (현재 디렉토리) 안에 'pelican-themes' 폴더가 있고,
# 그 안에 'pelican-bootstrap3' 폴더가 있다는 것을 명시합니다.
THEME = os.path.join(PATH, 'pelican-themes', 'pelican-bootstrap3')

# 플러그인 경로도 동일한 방식으로 설정 (만약 pelican-plugins도 inazuel.github.io 안에 있다면)
PLUGIN_PATHS = [os.path.join(PATH, 'pelican-plugins')]
PLUGINS = ['i18n_subsites'] # i18n_subsites 플러그인 활성화
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']} # Jinja2 i18n 확장 활성화

# 게시물 상단에 저자 정보를 표시할지 여부
SHOW_ARTICLE_AUTHOR = True

# 게시물 상단에 카테고리 정보를 표시할지 여부
SHOW_ARTICLE_CATEGORY = True

# 메인 페이지에 글 목록 대신 글의 전체 내용을 표시할지 여부
SHOW_FULL_ARTICLE = True