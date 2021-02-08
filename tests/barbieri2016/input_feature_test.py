import pytest
from bs4 import BeautifulSoup
from felp.barbieri2016.input_feature import InputFeature
from felp.common.testing import FelpTestCase


class TestInputFeature(FelpTestCase):
    @pytest.mark.parametrize(
        "html_file, expected",
        (("lp01.html", 5), ("lp02.html", 30), ("lp03.html", 32)),
    )
    def test_get_number_of_clickable(self, html_file, expected):
        """
        Number of clickable objects in the landing page
        """
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")

        extractor = InputFeature(soup)
        num_of_clickable = extractor.get_number_of_clickable()

        assert num_of_clickable == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (("lp01.html", 5), ("lp02.html", 30), ("lp03.html", 32)),
    )
    def test_get_number_of_dropdown(self, html_file, expected):
        """
        Number of dropdown elements
        """
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")

        extractor = InputFeature(soup)

        num_of_dropdown = extractor.get_number_of_dropdown()
        assert num_of_dropdown == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (("lp01.html", 9), ("lp02.html", 96), ("lp03.html", 69)),
    )
    def test_get_number_of_check_box(self, html_file, expected):
        """
        Number of checkbox
        """
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")

        extractor = InputFeature(soup)

        num_of_check_box = extractor.get_number_of_check_box()
        assert num_of_check_box == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (("lp01.html", 1), ("lp02.html", 26), ("lp03.html", 19)),
    )
    def test_get_number_of_input_strings(self, html_file, expected):
        """
        Number of Input Strings
        """
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")

        extractor = InputFeature(soup)

        num_of_input_strings = extractor.get_number_of_input_strings()
        assert num_of_input_strings == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (("lp01.html", 21), ("lp02.html", 105), ("lp03.html", 51)),
    )
    def test_get_number_of_radio_buttons(self, html_file, expected):
        """
        Number of radio buttons
        """
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")

        extractor = InputFeature(soup)

        num_of_radio_buttons = extractor.get_number_of_radio_buttons()
        assert num_of_radio_buttons == expected
