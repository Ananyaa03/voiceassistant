from selenium import webdriver

class infow():
    def __init__(self):
       self.driver = webdriver.Chrome(executable_path='C:/Users/chromedriver.exe')
       
    def get_info(self,query):
       self.query=query
       self.driver.get(url='https://www.wikipedia.org')
       search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
       search.click()
       search.send_keys(query)       
       #trigger variable
       enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
       enter.click()
# assist = infow()
# assist.get_info('neutron stars')


class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/chromedriver.exe')

    def play(self,query):
        self.query=query
        self.driver.get(url='https://www.youtube.com/results?search_query='+query)
        video=self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        video.click()

# assist=music()
# assist.play('dynamite')