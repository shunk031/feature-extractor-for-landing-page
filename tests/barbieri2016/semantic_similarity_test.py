class TestSemanticSimilarity:
    def test_get_nouns(self):
        """
        Detected nouns in the landing page
        """
        raise NotImplementedError

    def test_get_number_of_concept_annotation(self):
        """
        Number of concepts detected in the landing page
        """
        raise NotImplementedError

    def test_get_similarity_noun(self):
        """
        Jaccard between the set of nouns in the title/abstract and the main text
        """
        raise NotImplementedError

    def test_get_similarity_wiki_ids(self):
        """
        Jaccard between the set of wiki entities in the title/abstract and the main text
        """
        raise NotImplementedError
