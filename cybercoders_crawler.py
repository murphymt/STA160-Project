import requests_cache
import lxml.html as lx
from urllib.request import urlopen
from bs4 import BeautifulSoup
requests_cache.install_cache("cache")


