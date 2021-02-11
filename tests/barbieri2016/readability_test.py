import pytest
from bs4 import BeautifulSoup
from felp.barbieri2016.readability import ReadabilityFeature
from felp.common.testing import FelpTestCase


class TestReadabilityFeature(FelpTestCase):
    @pytest.mark.parametrize(
        "html_file, expected",
        (("lp01.html", 14), ("lp02.html", 90), ("lp03.html", 88)),
    )
    def test_get_main_total_text_size_ratio(self, html_file, expected) -> float:
        """
        Main text (without boilerplate text) per total links ratio
        """
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = ReadabilityFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        ratio = extractor.get_main_total_text_size_ratio()
        assert ratio == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (("lp01.html", 14), ("lp02.html", 90), ("lp03.html", 88)),
    )
    def test_get_total_text_size(self, html_file, expected) -> float:
        """
        Text size
        """
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = ReadabilityFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        total_text_size = extractor.get_total_text_size()
        assert total_text_size == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (("lp01.html", 14), ("lp02.html", 90), ("lp03.html", 88)),
    )
    def test_get_main_text_size(self, html_file, expected) -> float:
        """
        Main text size
        """
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = ReadabilityFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        main_text_size = extractor.get_main_text_size()
        assert main_text_size == expected

    def test_get_flash_kincaid_title_readability(self) -> float:
        """
        Readability of the title
        """
        raise NotImplementedError

    def test_get_flash_kincaid_abstract_readability(self) -> float:
        """
        Readability of the abstract
        """
        raise NotImplementedError

    @pytest.mark.parametrize(
        "html_file, expected",
        (("lp01.html", 14), ("lp02.html", 90), ("lp03.html", 88)),
    )
    def test_get_token_count(self, html_file, expected) -> float:
        """
        Number of tokens
        """
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = ReadabilityFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        token_count = extractor.get_token_count()
        assert token_count == expected

    def test_get_summarizability_score(self) -> float:
        """
        Summarizability of the text
        """
        raise NotImplementedError

    def test_get_flash_kincaid_main_text_readability(self) -> float:
        """
        Readability of the main text
        """
        raise NotImplementedError
