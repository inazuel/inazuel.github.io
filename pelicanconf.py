import os

# --- 기본 설정 ---
AUTHOR = 'inazuel'
SITENAME = 'record of my life'
SITEURL = "https://inazuel.github.io"
PATH = "content"
TIMEZONE = 'Etc/GMT+9'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 5 # 한 페이지당 게시물 수

# --- 피드 설정 (개발 시 보통 비활성화) ---
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- 링크 및 소셜 위젯 ---
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

# --- 경로 설정 ---
# pelicanconf.py 파일이 있는 디렉토리의 절대 경로
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 테마 경로 (pelicanconf.py 기준 themes/pelican-bootstrap3)
THEME = os.path.join(BASE_DIR, 'pelican-themes', 'pelican-bootstrap3') # 'pelican-themes' 폴더가 BASE_DIR 안에 있을 때

# 플러그인 경로 (pelicanconf.py 기준 pelican-plugins)
PLUGIN_PATHS = [os.path.join(BASE_DIR, 'pelican-plugins')]
PLUGINS = ['i18n_subsites', 'sitemap']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# --- 정적 파일 및 메타데이터 설정 ---
# images, extra 폴더, static 폴더의 내용을 output으로 복사
STATIC_PATHS = ['images', 'extra', 'static']

# 특정 파일에 대한 경로 메타데이터 (robots.txt 및 폰트 파일)
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    'static/fonts/D2Coding-Ver1.3.2-20180524-all.ttf': {'path': 'static/fonts/D2Coding-Ver1.3.2-20180524-all.ttf'},
    'extra/googlee0d7505564fd3417.html': {'path': 'googlee0d7505564fd3417.html'},
}

# 사용자 정의 CSS 파일 경로
CUSTOM_CSS = 'static/css/custom.css'

# --- 테마 관련 표시 설정 ---
SHOW_ARTICLE_AUTHOR = True     # 게시물 상단에 저자 정보 표시
SHOW_ARTICLE_CATEGORY = True   # 게시물 상단에 카테고리 정보 표시
SHOW_FULL_ARTICLE = True       # 메인 페이지에 글의 전체 내용 표시 (아니면 요약)

# --- READERS 설정 (이 부분을 새로 추가) ---
# .html 파일을 콘텐츠로 해석하지 않도록 명시적으로 설정
READERS = {
    'html': None,
}

# RELATIVE_URLS = True # 개발 시 문서 상대 URL 사용 (필요시 주석 해제)

# 사이트맵 생성----------------------------------
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
# ---------------------------------------------------