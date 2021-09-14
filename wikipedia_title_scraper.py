'''
Slow, janky script to get title word count for random N Wikipedia articles

Writes data to a file

Adapted from https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/
'''

import requests
import os
import re
from bs4 import BeautifulSoup

NUM_ROWS = 312
OUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mydata.txt")

f = open(OUT_FILE, "a")
# f.write(f"Title length (in words) of {NUM_ROWS} random Wikipedia articles")

# https://stackoverflow.com/a/12982689
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    # cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', str(raw_html))
    return cleantext

titles = set()
while len(titles) < NUM_ROWS:
    response = requests.get(
        url="https://en.wikipedia.org/wiki/Special:Random",
    )
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find(id="firstHeading")
    if title.contents[0]:
        # https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string#comment82317372_12982689
        # clean_text = BeautifulSoup(title.contents[0], "html.parser").text
        clean_text = cleanhtml(title.contents[0])
        num_words = len([s for s in re.split("\W+", clean_text) if s])
        if clean_text not in titles:
            titles.add(clean_text)
            f.write("\n{0} (* {1} *)".format(num_words, clean_text))
