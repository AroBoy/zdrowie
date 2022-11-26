from django.forms import DateTimeInput
from django.test import client
from zdrowie.zdrowie.users.tests.factories import UserFactory
from django.urls import reverse
from zdrowie.zdrowie.bloodpressures.views import BloodpressureCreateView
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.utils import timezone
from django.test import RequestFactory
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
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
#
#     def test_main_page(self):
#         driver = webdriver.chrome()
#         driver.get(self.live_server_url)
#         element = driver.find_element(By.ID, 'log-in-link')
#         assert "Zaloguj" in element.text
#         driver.close()
# #
# #
#     def test_form_valid(self, user, request_factory):
#         data = {'systolic': 140, 'diastolic': 105, 'pulse': 70, 'record_datetime': timezone.now()}
#         request = request_factory.post(reverse("bloodpressures:add"), data=data)
#         request.user = user
#         session_middleware = SessionMiddleware()
#         session_middleware.process_request(request)
#         msg_middleware = MessageMiddleware()
#         msg_middleware.process_request(request)
#         response = BloodpressureCreateView.as_view()(request)
#         user.refresh_from_db()
#
#         assert response.status_code == 302
#         bp = user.bloodpressure_set.last()
#         assert bp.systolic == data.get('systolic')
#         assert bp.diastolic == data.get('diastolic')
#         assert bp.pulse == data.get('pulse')
#         assert bp.record_datetime == data.get('record_datetime')
#
#
#
# class TestBloodPressureListView:
#
#     def test_user_without_measurements(self, user):
#         c = client.Client()
#         c.force_login(user)
#         response = c.get(reverse('bloodpressures:list'))
#         assert 'object_list' in response.context
#         assert response.context.get('object_list').count() == 0
#
#
#     def test_user_with_measurements(self, bloodpressure):
#         c = client.Client() c.force_login(bloodpressure.user)
#         response = c.get(reverse('bloodpressures:list'))
#         assert 'object_list' in response.context
#         assert response.context.get('object_list').count() == 1
#
#
#     def test_user_checks_other_user_measurements(self, bloodpressure, user):
#         assert bloodpressure.user is not user
#         c = client.Client()
#         c.force_login(user)
#         response = c.get(reverse('bloodpressures:list'))
#         assert 'object_list' in response.context
#         assert response.context.get('object_list').count() == 0
#
#
# class TestBloodPressureCreateView:
#
#     def test_get_form(self, request_factory: RequestFactory):
#         view = BloodpressureCreateView()
#         request = request_factory.get(reverse("bloodpressures:add"))
#         view.setup(request)
#         form = view.get_form()
#         assert isinstance(form.fields['record_datetime'].widget, DateTimeInput)
