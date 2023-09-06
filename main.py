from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time


class YoutubeHomework(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.youtube.com/")

    def test_test1(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "style-scope ytd-searchbox")
        search_field.click()
        search_field.send_keys("Python unittest testcase")
        time.sleep(5)
        search_field.send_keys(Keys.ENTER)
        time.sleep(5)

        self.assertEqual(f"{'Python unittest testcase' + ' - YouTube'}", self.driver.title)

        first_video = self.driver.find_element(By.CLASS_NAME, "style-scope ytd-video-renderer")
        first_video.click()
        time.sleep(5)

        pause_video = self.driver.find_element(By.CSS_SELECTOR, "[data-title-no-tooltip='Pause']")
        pause_video.click()
        time.sleep(3)

        first_video_right_part = self.driver.find_element(By.TAG_NAME, "ytd-compact-video-renderer")
        first_video_right_part.click()
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.close()




