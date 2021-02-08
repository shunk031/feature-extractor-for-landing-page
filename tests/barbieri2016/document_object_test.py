import pytest
from felp.barbieri2016.document_object import DocumentObjectFeature
from felp.common.testing import FelpTestCase


class TestDocumentObjectFeature(FelpTestCase):
    @pytest.mark.skip()
    @pytest.mark.parametrize(
        "soup, expected", (("lp01", 14), ("lp02", 90), ("lp03", 88)), indirect=["soup"]
    )
    def test_get_internal_links(self, soup, expected):
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        internal_links = extractor.get_internal_links()
        raise NotImplementedError

    @pytest.mark.skip()
    @pytest.mark.parametrize(
        "soup, expected", (("lp01", 14), ("lp02", 90), ("lp03", 88)), indirect=["soup"]
    )
    def test_get_external_links(self, soup, expected):
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        external_links = extractor.get_external_links()
        raise NotImplementedError

    @pytest.mark.parametrize(
        "soup, expected", (("lp01", 17), ("lp02", 72), ("lp03", 65)), indirect=["soup"]
    )
    def test_get_num_of_internal_links(self, soup, expected):
        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        num_of_internal_links = extractor.get_num_of_internal_links()
        assert num_of_internal_links == expected

    @pytest.mark.parametrize(
        "soup, expected", (("lp01", 9), ("lp02", 35), ("lp03", 31)), indirect=["soup"]
    )
    def test_get_num_of_external_links(self, soup, expected):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        num_of_external_links = extractor.get_num_of_external_links()
        assert num_of_external_links == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (
            ("lp01", 26),
            ("lp02", 107),
            ("lp03", 96),
        ),
        indirect=["soup"],
    )
    def test_num_of_links(self, soup, expected):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        num_of_links = extractor.get_num_of_links()
        assert num_of_links == expected

    @pytest.mark.parametrize(
        "soup, expected_internal, expected_external",
        (
            ("lp01", 17, 9),
            ("lp02", 72, 35),
            ("lp03", 65, 31),
        ),
        indirect=["soup"],
    )
    def test_get_links(self, soup, expected_internal, expected_external):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        links = extractor.get_links()

        assert len(links.internal) == expected_internal
        assert len(links.external) == expected_external

    @pytest.mark.parametrize(
        "soup, expected_main_text_num",
        (
            ("lp01", "lp01"),
            ("lp02", "lp02"),
            ("lp03", "lp03"),
        ),
        indirect=["soup"],
    )
    def test_get_main_text(self, soup, expected_main_text_num):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        main_text = extractor.get_main_text()

        expected_path = self.FIXTURES_ROOT / expected_main_text_num / "main_text.txt"
        with expected_path.open("r") as rf:
            expected_text = rf.read()

        assert main_text == expected_text

    @pytest.mark.parametrize(
        "soup, expected",
        (
            ("lp01", 0.53),
            ("lp02", 0.49),
            ("lp03", 0.48),
        ),
        indirect=["soup"],
    )
    def test_get_number_of_external_internal_link_ratio(self, soup, expected):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        number_of_external_internal_link_ratio = (
            extractor.get_number_of_external_internal_link_ratio()
        )
        assert round(number_of_external_internal_link_ratio, 2) == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (
            ("lp01", 0.65),
            ("lp02", 0.67),
            ("lp03", 0.68),
        ),
        indirect=["soup"],
    )
    def test_get_number_of_internal_total_links_ratio(self, soup, expected):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        number_of_internal_total_links_ratio = (
            extractor.get_number_of_internal_total_links_ratio()
        )
        assert round(number_of_internal_total_links_ratio, 2) == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (
            ("lp01", 0.35),
            ("lp02", 0.33),
            ("lp03", 0.32),
        ),
        indirect=["soup"],
    )
    def test_number_of_external_total_links_ratio(self, soup, expected):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        number_of_external_total_links_ratio = (
            extractor.get_number_of_external_total_links_ratio()
        )
        assert round(number_of_external_total_links_ratio, 2) == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (
            ("lp01", 0.38),
            ("lp02", 0.3),
            ("lp03", 0.29),
        ),
        indirect=["soup"],
    )
    def test_get_text_size_internal_links_ratio(self, soup, expected):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        text_size_internal_links_ratio = extractor.get_text_size_internal_links_ratio()
        assert round(text_size_internal_links_ratio, 2) == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (
            ("lp01", 0.08),
            ("lp02", 0.1),
            ("lp03", 0.09),
        ),
        indirect=["soup"],
    )
    def test_get_text_size_external_links_ratio(self, soup, expected):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        text_size_external_links_ratio = extractor.get_text_size_external_links_ratio()
        assert round(text_size_external_links_ratio, 2) == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (
            ("lp01", 0.46),
            ("lp02", 0.41),
            ("lp03", 0.38),
        ),
        indirect=["soup"],
    )
    def test_get_text_size_links_ratio(self, soup, expected):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )
        text_size_links_ratio = extractor.get_text_size_links_ratio()

        assert round(text_size_links_ratio, 2) == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (
            ("lp01", 0.36),
            ("lp02", 0.29),
            ("lp03", 0.28),
        ),
        indirect=["soup"],
    )
    def test_get_main_text_size_internal_links_ratio(self, soup, expected):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        main_text_size_internal_links = (
            extractor.get_main_text_size_internal_links_ratio()
        )
        assert round(main_text_size_internal_links, 2) == expected

    @pytest.mark.parametrize(
        "soup, expected",
        (
            ("lp01", 0.36),
            ("lp02", 0.29),
            ("lp03", 0.28),
        ),
        indirect=["soup"],
    )
    def test_get_main_text_size_external_links_ratio(self, soup, expected):

        extractor = DocumentObjectFeature(
            lp_url="https://felp_dummy_internal.com", soup=soup
        )

        main_text_size_external_links = (
            extractor.get_main_text_size_internal_links_ratio()
        )
        assert round(main_text_size_external_links, 2) == expected
