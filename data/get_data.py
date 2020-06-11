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
from time import sleep
import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


################################################################################
# Main
if __name__ == "__main__":
    # use selenium to load dynamic data
    chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        chromedriver_path,
        options=chrome_options
    )
    url = "https://thefootballcrestindex.com/blogs/premier-league-clubs"
    driver.get(url)

    # parse html
    names = []
    image_urls = []

    for i in range(10):  # guessing 10 pages
        # get club name
        hrefs = driver.find_elements_by_tag_name("a")
        for h in hrefs:
            name = str(h.get_attribute("href"))
            if "premier-league-clubs/" in name:
                _, name = name.rsplit("/", 1)
                if name not in names:
                    names.append(name)

        # get club image url
        imgs = driver.find_elements_by_tag_name("img")
        for img in imgs:
            s = str(img.get_attribute("src"))
            if "articles" in s:
                if s not in image_urls:
                    image_urls.append(s)

        # load more clubs, "View More" button
        buttons = driver.find_elements_by_xpath("//*[contains(text(), 'View More')]")
        for b in buttons:
            b.click()

    #
    print(f'Number of clubs: {len(names)}')
    print(f'Number of images: {len(image_urls)}')

    driver.close()
    quit()

    """
    with open(image_file_name, "wb") as f:
        response = requests.get(i, stream=True)
        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            f.write(block)
    """

