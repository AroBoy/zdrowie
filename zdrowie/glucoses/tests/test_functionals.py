# from django.urls import reverse
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
#
# class By(object): """
#    Set of supported locator strategies.
#    """
#    ID = "id"
#    XPATH = "xpath"
#    LINK_TEXT = "link text"
#    PARTIAL_LINK_TEXT = "partial link text"
#    NAME = "name"
#    TAG_NAME = "tag name"
#    CLASS_NAME = "class name"
#    CSS_SELECTOR = "css selector"
#
#
# class TestForNotLoggedInUser(LiveServerTestCase):
#     def test_main_page(self):
#         driver = webdriver.Chrome()
#         driver.get(self.live_server_url)
#
#         element = driver.find_element(By.ID, 'log-in-link')
#         assert "Zaloguj" in element.text
#         driver.close()
#
#    def test_glucoses_list_page(self):
#        driver = webdriver.Chrome()
#        driver.get(self.live_server_url + reverse('glucoses:list'))
#        expected_url = self.live_server_url + '/accounts/login/?next=/glucoses/'
#
#        assert driver.current_url == expected_url
#        driver.quit
