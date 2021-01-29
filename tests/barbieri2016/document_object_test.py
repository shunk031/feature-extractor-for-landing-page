import pytest
from bs4 import BeautifulSoup
from felp.barbieri2016.document_object import DocumentObjectFeature
from felp.common.testing import FelpTestCase


class TestDocumentObjectFeature(FelpTestCase):
    @pytest.mark.parametrize(
        "html_file, expected",
        (("lp01.html", 14), ("lp02.html", 90), ("lp03.html", 88)),
    )
    def test_get_num_of_internal_links(self, html_file, expected):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        num_of_internal_links = extractor.get_num_of_internal_links()
        assert num_of_internal_links == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (("lp01.html", 13), ("lp02.html", 45), ("lp03.html", 46)),
    )
    def test_get_num_of_external_links(self, html_file, expected):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        num_of_external_links = extractor.get_num_of_external_links()
        assert num_of_external_links == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (
            ("lp01.html", 27),
            ("lp02.html", 135),
            ("lp03.html", 134),
        ),
    )
    def test_num_of_links(self, html_file, expected):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        num_of_links = extractor.get_num_of_links()
        assert num_of_links == expected

    @pytest.mark.parametrize(
        "html_file, expected_internal, expected_external",
        (
            ("lp01.html", 14, 13),
            ("lp02.html", 90, 45),
            ("lp03.html", 88, 46),
        ),
    )
    def test_get_links(self, html_file, expected_internal, expected_external):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        links = extractor.get_links()

        assert len(links.internal) == expected_internal
        assert len(links.external) == expected_external

    @pytest.mark.parametrize(
        "html_file, expected_file",
        (
            ("lp01.html", "lp01_main_text.txt"),
            ("lp02.html", "lp02_main_text.txt"),
            ("lp03.html", "lp03_main_text.txt"),
        ),
    )
    def test_get_main_text(self, html_file, expected_file):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        main_text = extractor.get_main_text()

        expected_path = self.FIXTURES_ROOT / expected_file
        with expected_path.open("r") as rf:
            expected_text = rf.read()

        assert main_text == expected_text

    @pytest.mark.parametrize(
        "html_file, expected",
        (
            ("lp01.html", 0.93),
            ("lp02.html", 0.50),
            ("lp03.html", 0.52),
        ),
    )
    def test_get_number_of_external_internal_link_ratio(self, html_file, expected):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        number_of_external_internal_link_ratio = (
            extractor.get_number_of_external_internal_link_ratio()
        )
        assert round(number_of_external_internal_link_ratio, 2) == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (
            ("lp01.html", 0.52),
            ("lp02.html", 0.67),
            ("lp03.html", 0.66),
        ),
    )
    def test_get_number_of_internal_total_links_ratio(self, html_file, expected):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        number_of_internal_total_links_ratio = (
            extractor.get_number_of_internal_total_links_ratio()
        )
        assert round(number_of_internal_total_links_ratio, 2) == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (
            ("lp01.html", 0.48),
            ("lp02.html", 0.33),
            ("lp03.html", 0.34),
        ),
    )
    def test_number_of_external_total_links_ratio(self, html_file, expected):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        number_of_external_total_links_ratio = (
            extractor.get_number_of_external_total_links_ratio()
        )
        assert round(number_of_external_total_links_ratio, 2) == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (
            ("lp01.html", 0.13),
            ("lp02.html", 0.27),
            ("lp03.html", 0.28),
        ),
    )
    def test_get_text_size_internal_links_ratio(self, html_file, expected):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        text_size_internal_links_ratio = extractor.get_text_size_internal_links_ratio()
        assert round(text_size_internal_links_ratio, 2) == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (
            ("lp01.html", 0.09),
            ("lp02.html", 0.08),
            ("lp03.html", 0.08),
        ),
    )
    def test_get_text_size_external_links_ratio(self, html_file, expected):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        text_size_external_links_ratio = extractor.get_text_size_external_links_ratio()
        assert round(text_size_external_links_ratio, 2) == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (
            ("lp01.html", 0.22),
            ("lp02.html", 0.35),
            ("lp03.html", 0.36),
        ),
    )
    def test_get_text_size_links_ratio(self, html_file, expected):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        text_size_links_ratio = extractor.get_text_size_links_ratio()

        assert round(text_size_links_ratio, 2) == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (
            ("lp01.html", 0.12),
            ("lp02.html", 0.26),
            ("lp03.html", 0.27),
        ),
    )
    def test_get_main_text_size_internal_links_ratio(self, html_file, expected):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        main_text_size_internal_links = (
            extractor.get_main_text_size_internal_links_ratio()
        )
        assert round(main_text_size_internal_links, 2) == expected

    @pytest.mark.parametrize(
        "html_file, expected",
        (
            ("lp01.html", 0.12),
            ("lp02.html", 0.26),
            ("lp03.html", 0.27),
        ),
    )
    def test_get_main_text_size_external_links_ratio(self, html_file, expected):
        html_path = self.FIXTURES_ROOT / html_file
        with html_path.open("r") as rf:
            soup = BeautifulSoup(rf, "lxml")
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        main_text_size_external_links = (
            extractor.get_main_text_size_internal_links_ratio()
        )
        assert round(main_text_size_external_links, 2) == expected
