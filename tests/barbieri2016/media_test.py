import pytest
from bs4 import BeautifulSoup
from felp.barbieri2016.media import MediaFeature
from felp.common.testing import FelpTestCase


class TestMediaFeature(FelpTestCase):
    @pytest.mark.parametrize(
        "soup, expected", (("lp01", 14), ("lp02", 90), ("lp03", 88)), indirect=["soup"]
    )
    def test_get_image_height(self, soup: BeautifulSoup, expected: int):
        """
        Height of the rendered landing page
        """
        extractor = MediaFeature(soup)
        height = extractor.get_image_height()
        assert height == expected

    @pytest.mark.parametrize(
        "soup, expected", (("lp01", 14), ("lp02", 90), ("lp03", 88)), indirect=["soup"]
    )
    def test_get_image_width(self, soup: BeautifulSoup, expected: int):
        """
        Width of the rendered landing page
        """
        extractor = MediaFeature(soup)
        width = extractor.get_image_width()
        assert width == expected

    @pytest.mark.parametrize(
        "soup, expected", (("lp01", 4), ("lp02", 4), ("lp03", 3)), indirect=["soup"]
    )
    def test_get_number_of_images(self, soup: BeautifulSoup, expected: int):
        """
        Number of images contained in the landing page
        """
        extractor = MediaFeature(soup)
        num_of_images = extractor.get_number_of_images()
        assert num_of_images == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (("lp01", True), ("lp02", True), ("lp03", True)),
        indirect=["soup"],
    )
    def test_get_media(self, soup: BeautifulSoup, expected: bool):
        """
        Is there a media (e.g., video) on the landing page?
        """
        extractor = MediaFeature(soup)
        is_media = extractor.get_media()
        assert is_media == expected
