from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

class scraper():

    def __init__(self,channel):
        self.channel = channel

    option = Options()
    option.headless = False
    driver = webdriver.Firefox(options=option)
    driver.implicitly_wait(7)


    def scrape(self):
        main_url = "https://www.youtube.com/"
        #self.channel = "@krishnaik06"
        link = '/videos'
        url = main_url + self.channel + link

        self.driver.get(url)
        time.sleep(3)

        self.scroll()

        allvideo_list = list(self.driver.find_elements(By.CSS_SELECTOR,'#thumbnail.yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail'))
        
        links = list(dict.fromkeys(map(lambda a: a.get_attribute('href'),allvideo_list)))
        
        _url = links[1]
        
        self.driver.get(_url)
        time.sleep(3)

        video_url = _url
        title = self.driver.find_element(By.CSS_SELECTOR,"#title.style-scope.ytd-watch-metadata h1.style-scope.ytd-watch-metadata yt-formatted-string.style-scope.ytd-watch-metadata").text
        desc = self.driver.find_element(By.ID,"plain-snippet-text").text
        likes = self.driver.find_element(By.CSS_SELECTOR,"#segmented-like-button.style-scope.ytd-segmented-like-dislike-button-renderer ytd-toggle-button-renderer.style-scope.ytd-segmented-like-dislike-button-renderer yt-button-shape button.yt-spec-button-shape-next.yt-spec-button-shape-next--tonal.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--icon-leading.yt-spec-button-shape-next--segmented-start div.cbox.yt-spec-button-shape-next--button-text-content span.yt-core-attributed-string.yt-core-attributed-string--white-space-no-wrap").text
        f = open("video_details.csv",'w+')
        f.write("video_Title,video_description,likes,video_url\n")
        f.close()

        f = open("laptop_data.csv",'a')

        f.write(f"{title},{desc},{likes},{video_url}\n")

        f.close()

        #print(title)
        #print(desc)
        #print(likes)

    def scroll(self):
        x = 0
        y = 1200
        for i in range(0,2):
            location = f"window.scrollTo({x}, {y})"
            self.driver.execute_script(location) 
            x = y
            y = x + 1500
            time.sleep(2)