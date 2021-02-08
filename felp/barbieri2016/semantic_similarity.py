from typing import List

from bs4 import BeautifulSoup
from natto import MeCab


class SemanticSimilarity(object):
    def __init__(self, soup: BeautifulSoup) -> None:
        pass

    def get_nouns(self) -> List[str]:
        """
        Detected nouns in the landing page
        """
        raise NotImplementedError

    def get_number_of_concept_annotation(self) -> int:
        """
        Number of concepts detected in the landing page
        """
        raise NotImplementedError

    def get_similarity_noun(self) -> float:
        """
        Jaccard between the set of nouns in the title/abstract and the main text
        """
        raise NotImplementedError

    def get_similarity_wiki_ids(self) -> float:
        """
        Jaccard between the set of wiki entities in the title/abstract and the main text
        """
        raise NotImplementedError


class SemanticSimilarityJa(SemanticSimilarity):
    pass


class SemanticSimilarityEn(SemanticSimilarity):
    pass
