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
    # webdriver.Chrome(path to chromedriver)
    chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        chromedriver_path,
        options=chrome_options
    )
    # .get(url)
    url = "https://thefootballcrestindex.com/blogs/premier-league-clubs"
    driver.get(url)

    # click "View More" buttons
    images = []
    for i in range(10):
        x = driver.find_elements_by_tag_name("img")
        for j in x:
            s = j.get_attribute("src")
            if "articles" in s:
                if s not in images:
                    images.append(s)

        buttons = driver.find_elements_by_xpath("//*[contains(text(), 'View More')]")
        for b in buttons:
            b.click()

        #sleep(1)

    print(f'Number of images: {len(images)}')
    for i in images:
        print(i)
    quit()

    """
    z = driver.find_elements_by_tag_name("img")
    for i in z:
        print(i.get_attribute("src"))
    """

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.close()

    x = soup.findAll("img")
    for i in x:
        print(i)

    #print(soup.prettify())

    quit()

    # soup = BeautifulSoup(driver.page_source, 'html.parser')

    with urllib.request.urlopen() as response:
        page = response.read()

    #page = re.sub('<!--|-->', "", str(page))

    soup = BeautifulSoup(page, "html5lib")

    #image_urls = soup.findAll("div", {"class": "grid--uniform grid--blog article-matrix"})
    image_urls = soup.findAll("img")
    for i in image_urls:
        print(i)
