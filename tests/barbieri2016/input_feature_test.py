import pytest
from bs4 import BeautifulSoup
from felp.barbieri2016.input_feature import InputFeature
from felp.common.testing import FelpTestCase


class TestInputFeature(FelpTestCase):
    @pytest.mark.parametrize(
        "soup, expected",
        (("lp01", 46), ("lp02", 228), ("lp03", 182)),
        indirect=["soup"],
    )
    def test_get_number_of_clickable(self, soup: BeautifulSoup, expected: int):
        """
        Number of clickable objects in the landing page
        """
        extractor = InputFeature(soup)
        num_of_clickable = extractor.get_number_of_clickable()

        assert num_of_clickable == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (("lp01", 8), ("lp02", 33), ("lp03", 24)),
        indirect=["soup"],
    )
    def test_get_number_of_dropdown(self, soup: BeautifulSoup, expected: int):
        """
        Number of dropdown elements
        """
        extractor = InputFeature(soup)

        num_of_dropdown = extractor.get_number_of_dropdown()
        assert num_of_dropdown == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (("lp01", 18), ("lp02", 78), ("lp03", 57)),
        indirect=["soup"],
    )
    def test_get_number_of_check_box(self, soup: BeautifulSoup, expected: int):
        """
        Number of checkbox
        """
        extractor = InputFeature(soup)

        num_of_check_box = extractor.get_number_of_check_box()
        assert num_of_check_box == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (("lp01", 2), ("lp02", 27), ("lp03", 23)),
        indirect=["soup"],
    )
    def test_get_number_of_input_strings(self, soup: BeautifulSoup, expected: int):
        """
        Number of Input Strings
        """
        extractor = InputFeature(soup)

        num_of_input_strings = extractor.get_number_of_input_strings()
        assert num_of_input_strings == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (("lp01", 18), ("lp02", 90), ("lp03", 78)),
        indirect=["soup"],
    )
    def test_get_number_of_radio_buttons(self, soup: BeautifulSoup, expected: int):
        """
        Number of radio buttons
        """
        extractor = InputFeature(soup)

        num_of_radio_buttons = extractor.get_number_of_radio_buttons()
        assert num_of_radio_buttons == expected
