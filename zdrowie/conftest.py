import pytest
from django.test import RequestFactory

from .glucoses.models import Glucose
from .bloodpressures.models import BloodPressure
from .glucoses.tests.factories import GlucoseFactory
from .bloodpressures.tests.factories import BloodpressureFactory
from .users.models import User
from .users.tests.factories import UserFactory


@pytest.fixture
def bloodpressure() -> BloodPressure:
    return BloodpressureFactory

@pytest.fixture
def glucose() -> Glucose:
    return GlucoseFactory


# @pytest.fixture(autouse=True)
# def media_storage(settings, tmpdir):
# settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User: return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory: return RequestFactory()
