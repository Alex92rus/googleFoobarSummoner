from selenium import webdriver
from selenium.webdriver.common.by import By
from configparser import ConfigParser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


class SearchHarness:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.stackOverflowDictionary = {}

    def execute(self):
        self.driver.get("https://www.google.com")

    def login(self):
        url = "https://www.google.com/accounts/Login"
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 6)

        username, password = self._get_login_details()

        self.driver.find_element_by_id("identifierId").send_keys(username)
        wait.until(EC.element_to_be_clickable((By.ID, "identifierNext")))
        self.driver.find_element_by_id("identifierNext").click()
        wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        password_element = self.driver.find_element_by_name("password")
        password_element.send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='passwordNext']/span")))
        next_element = self.driver.find_element_by_xpath("//*[@id='passwordNext']/span")
        next_element.click()

    def _get_login_details(self):
        config = ConfigParser()
        config.read('config.properties')
        username = config.get('Account', "username")
        password = config.get('Account', "password")
        return username, password

    def search_questions_from_stack_overflow(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get("https://google.com")
        for questionPair in self.stackOverflowDictionary.values():
            for question in questionPair:
                self.driver.find_element_by_xpath("//div/div/input").clear()
                search_element = self.driver.find_element_by_xpath("//div/div/input")
                search_element.clear()
                search_element.send_keys(question)
                search_element.send_keys(Keys.RETURN)
                sleep(20)
                wait.until(EC.visibility_of_element_located((By.ID, "resultStats")))

    def get_stack_overflow_tags(self):
        wait = WebDriverWait(self.driver, 6)

        self.driver.get("https://stackoverflow.com/tags")
        wait.until(EC.visibility_of_element_located((By.ID, "tags-browser")))
        tags_browser_element = self.driver.find_element_by_id("tags-browser")
        link_elements = tags_browser_element.find_elements_by_xpath("//a[@class='post-tag']")
        for tag in link_elements[:2]:
            tag_text = tag.text
            actions = ActionChains(self.driver)
            actions.move_to_element(tag)
            actions.key_down(Keys.CONTROL)
            actions.key_down(Keys.TAB)
            actions.click(tag)
            actions.key_up(Keys.CONTROL)
            actions.key_up(Keys.TAB)
            actions.perform()
            sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            wait.until(EC.visibility_of_element_located((By.ID, "questions")))
            questions_element = self.driver.find_element_by_id("questions")
            title_elements = questions_element.find_elements_by_xpath("//h3/a[@class='question-hyperlink']")
            for title in title_elements:
                if tag_text not in self.stackOverflowDictionary:
                    self.stackOverflowDictionary[tag_text] = []
                self.stackOverflowDictionary[tag_text].append(title.text)
                print(tag_text + "," + title.text)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    def run(self):
        self.login()
        self.get_stack_overflow_tags()
        self.search_questions_from_stack_overflow()


if __name__ == '__main__':
    searchHarness = SearchHarness()
    searchHarness.run()
