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
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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

    # make directories named after clubs for Training and Test
    # as club names = labels
    data_dir = ["Training", "Test"]
    for dataset in data_dir:
        for i in range(len(names)):
            # create directory in Training/Test
            dir_name = dataset + "\\" + names[i]
            dir_path = os.path.join(os.getcwd(), dir_name)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            # save image in directory
            image_filename = names[i] + ".jpg"
            image_path = os.path.join(dir_path, image_filename)

            with open(image_path, "wb") as f:
                response = requests.get(image_urls[i], stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    f.write(block)
