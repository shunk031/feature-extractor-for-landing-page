import pytest
from bs4 import BeautifulSoup
from felp.common.testing import FelpTestCase


@pytest.fixture
def soup(request) -> BeautifulSoup:
    lp_num = request.param
    html_path = FelpTestCase.FIXTURES_ROOT / lp_num / "page.html"
    with html_path.open("r") as rf:
        soup = BeautifulSoup(rf, "lxml")
    return soup
