AUTHOR = 'inazuel'
SITENAME = 'record of my life'
SITEURL = ""

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

# 펠리칸-부트스트랩3 테마 추가
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# 테마경로
import os

# Pelicanconf.py 파일이 있는 디렉토리 (즉, /github/workspace)
PATH = os.path.abspath(os.path.dirname(__file__))

# THEME: 블로그 프로젝트 폴더 안의 'pelican-themes' 폴더를 가리키도록 수정
THEME = os.path.join(PATH, 'pelican-themes', 'pelican-bootstrap3')

# PLUGIN_PATHS: 블로그 프로젝트 폴더 안의 'pelican-plugins' 폴더를 가리키도록 수정
PLUGIN_PATHS = [os.path.join(PATH, 'pelican-plugins')]