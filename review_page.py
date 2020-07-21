import requests
from requests_html import HTMLSession
import pandas as pd
import time

s = HTMLSession()
r = s.get('https://www.beerwulf.com/en-gb/p/beers/birra-moretti-lautentica-2l-keg')
r.html.render(sleep=1) # sleep=1 is important - sleeps for x seconds after the render

review = r.html.find( '.label-stars', first = True).text

print(review)
