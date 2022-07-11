import pytest
import requests
from configuration import SERVICE_URL

# scope='function' означает, что когда данная фикстура выполняется, код в ней запускается каждый раз с самого начала;
# scope='session' - код выполняется один раз и дальше результат кэшируется;
# autouse=True - фикстура выполняется самостоятельно для каждого нашего теста, даже когда не передаём её как параметр;
# conftest может лежать как в корне папки tests, так и в каждой папке, которая содержит в себе тесты каких-то
# определённых модулей, может быть свой conftest.py;

@pytest.fixture
def get_users():
    return requests.get(url=SERVICE_URL)