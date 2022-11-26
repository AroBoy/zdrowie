#
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # from seleniumlogin import force_login
#
# from zdrowie.users.tests.factories import UserFactory
#
#
# class TestForLoggedInUser(LiveServerTestCase):
#     def test_main_page(self):
#         driver = webdriver.Firefox()
#
#         user = UserFactory()
#         force_login(user, driver, self.live_server_url)
#         driver.get(self.live_server_url)
#         element = driver.find_element(By.CSS_SELECTOR, 'ul li.nav-item:last-child a')
#
#         assert "Wyloguj" in element.text
#         driver.quit()
