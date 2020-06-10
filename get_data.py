"""
Michael Patel
June 2020

Project description:
    CNN for EPL logos

File description:
    To scrape image data from website: https://thefootballcrestindex.com/blogs/premier-league-clubs
"""
################################################################################
# Import
import os
import re
import urllib.request
from bs4 import BeautifulSoup


################################################################################
# Main
if __name__ == "__main__":
    # use selenium to load dynamic data

    with urllib.request.urlopen("https://thefootballcrestindex.com/blogs/premier-league-clubs") as response:
        page = response.read()

    #page = re.sub('<!--|-->', "", str(page))

    soup = BeautifulSoup(page, "html5lib")

    #image_urls = soup.findAll("div", {"class": "grid--uniform grid--blog article-matrix"})
    image_urls = soup.findAll("img")
    for i in image_urls:
        print(i)
