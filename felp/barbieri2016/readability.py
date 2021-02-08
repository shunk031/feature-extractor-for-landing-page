from bs4 import BeautifulSoup
from felp.barbieri2016.document_object import DocumentObjectFeature


class ReadabilityFeature(object):
    def __init__(self, lp_url: str, soup: BeautifulSoup) -> None:
        self._soup = soup
        self._doc_feat_extractor = DocumentObjectFeature(lp_url, soup)

    def get_main_total_text_size_ratio(self) -> float:
        """
        Main text (without boilerplate text) per total links ratio
        """
        main_text_size = len(self._doc_feat_extractor.get_main_text())

        internal_links = self._doc_feat_extractor.get_internal_links()
        internal_link_text_size = sum([len(link.text) for link in internal_links])

        external_links = self._doc_feat_extractor.get_external_links()
        external_link_text_size = sum([len(link.text) for link in external_links])

        return (internal_link_text_size + external_link_text_size) / main_text_size

    def get_total_text_size(self) -> float:
        """
        Text size
        """
        return len(self._soup.get_text(strip=True))

    def get_main_text_size(self) -> float:
        """
        Main text size
        """
        return len(self._doc_feat_extractor.get_main_text())

    def get_flash_kincaid_title_readability(self) -> float:
        """
        Readability of the title
        """
        title = self._soup.find("title")
        raise NotImplementedError

    def get_flash_kincaid_abstract_readability(self) -> float:
        """
        Readability of the abstract
        """
        raise NotImplementedError

    def get_token_count(self) -> float:
        """
        Number of tokens
        """
        breakpoint()
        raise NotImplementedError

    def get_summarizability_score(self) -> float:
        """
        Summarizability of the text
        """
        raise NotImplementedError

    def get_flash_kincaid_main_text_readability(self) -> float:
        """
        Readability of the main text
        """
        raise NotImplementedError
