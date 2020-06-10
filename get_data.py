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
import urllib.request
from bs4 import BeautifulSoup


################################################################################
# Main
if __name__ == "__main__":
    with urllib.request.urlopen("https://thefootballcrestindex.com/blogs/premier-league-clubs") as response:
        page = response.read()

    soup = BeautifulSoup(page, "html.parser")
    print(soup)
