import pytest
from django.conf import settings

@pytest.fixture(scope='session', autouse=True)
def set_test_db():
    settings.DATABASES['default']['NAME'] = 'railway_test'