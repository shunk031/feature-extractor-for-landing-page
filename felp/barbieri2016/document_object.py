import copy
from dataclasses import dataclass
from typing import Dict, List
from urllib.parse import urlparse

from bs4 import BeautifulSoup


@dataclass
class Link(object):
    url: str
    text: str


@dataclass
class HtmlLinks(object):
    internal: List[Link]
    external: List[Link]


class DocumentObjectFeature(object):
    def __init__(self, lp_url: str, soup: BeautifulSoup) -> None:
        self._soup = soup
        self._lp_url = lp_url

        self._internal_external_links: HtmlLinks = self.get_links()

    def get_external_links(self) -> List[Link]:
        return self._internal_external_links.external

    def get_internal_links(self) -> List[Link]:
        return self._internal_external_links.internal

    def get_num_of_internal_links(self) -> int:
        """
        No. of links pointing to the same domain as the landing page
        """
        return len(self.get_internal_links())

    def get_num_of_external_links(self) -> int:
        """
        No. of links pointing to external domains
        """
        return len(self.get_external_links())

    def get_num_of_links(self) -> int:
        """
        Sum of the previous two features
        """
        num_links = self.get_num_of_internal_links() + self.get_num_of_external_links()
        assert num_links == len(self._soup.find_all("a"))

        return num_links

    def get_links(self) -> HtmlLinks:
        parsed_lp_url = urlparse(self._lp_url)

        links: Dict[str, List[Link]] = {"internal": [], "external": []}
        for a_tag in self._soup.find_all("a"):
            url = a_tag.get("href")
            parsed_url = urlparse(url)

            link = Link(url=url, text=a_tag.get_text().replace("\n", ""))

            if (parsed_url.netloc == parsed_lp_url.netloc) or (parsed_url.netloc == ""):
                links["internal"].append(link)
            else:
                links["external"].append(link)

        assert len(links["internal"]) > 0 and len(links["external"]) > 0

        return HtmlLinks(**links)

    def get_main_text(self) -> str:
        soup = copy.copy(self._soup)
        soup.find("head").decompose()

        header_tags = soup.find_all("header")
        for header_tag in header_tags:
            header_tag.decompose()

        footer_tags = soup.find_all("footer")
        for footer_tag in footer_tags:
            footer_tag.decompose()

        return soup.get_text()

    def get_number_of_external_internal_link_ratio(self) -> float:
        """
        Ratio of External vs. Internal links
        """
        return self.get_num_of_external_links() / self.get_num_of_internal_links()

    def get_number_of_internal_total_links_ratio(self) -> float:
        """
        Precentage of internal links
        """
        return self.get_num_of_internal_links() / self.get_num_of_links()

    def get_number_of_external_total_links_ratio(self) -> float:
        """
        Precentage of external links
        """
        return self.get_num_of_external_links() / self.get_num_of_links()

    def get_text_size_internal_links_ratio(self) -> float:
        """
        Text per internal links ratio
        """

        body_text = self._soup.get_text(strip=True)
        # TODO (shunk031): clean up the body text

        link_text = "".join(link.text for link in self.get_internal_links())
        return len(link_text) / len(body_text)

    def get_text_size_external_links_ratio(self) -> float:
        """
        Text per external links ratio
        """
        body_text = self._soup.get_text(strip=True)
        # TODO (shunk031): clean up the body text

        link_text = "".join(link.text for link in self.get_external_links())
        return len(link_text) / len(body_text)

    def get_text_size_links_ratio(self) -> float:
        """
        Text per total number of links ratio
        """
        body_text_size = len(self._soup.get_text(strip=True))
        # TODO (shunk031): clean up the body text

        internal_links = self.get_internal_links()
        internal_link_text_size = sum([len(link.text) for link in internal_links])

        external_links = self.get_external_links()
        external_link_text_size = sum([len(link.text) for link in external_links])

        links_size = internal_link_text_size + external_link_text_size
        return links_size / body_text_size

    def get_main_text_size_internal_links_ratio(self) -> float:
        """
        Main text (without boilerplate text) per Internal links ratio
        """
        internal_links = self.get_internal_links()
        internal_link_text_size = sum([len(link.text) for link in internal_links])
        main_text_size = len(self.get_main_text())

        return internal_link_text_size / main_text_size

    def get_main_text_size_external_links_ratio(self) -> float:
        """
        Main text (without boilerplate text) per External links ratio
        """
        external_links = self.get_external_links()
        external_link_text_size = sum([len(link.text) for link in external_links])

        main_text_size = len(self.get_main_text())

        return external_link_text_size / main_text_size
