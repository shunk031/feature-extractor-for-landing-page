class LanguageStyleFeature(object):
    def __init__(self) -> None:
        pass

    def get_formality(self) -> int:
        """
        Formality f-score based on the frequencies of different word classes (part-of-speech)
        and machine learning based formality classifier trained on various features
        """
        raise NotImplementedError

    def get_punctuation(self) -> int:
        """
        Number of different punctuation marks, including exclaim point '!', question mark '?' and quotes
        """
        raise NotImplementedError

    def get_start_with_number(self) -> int:
        """
        Whether text starts with number
        """
        raise NotImplementedError

    def get_contain_non_starting_number(self) -> int:
        """
        Where text contains number that does not start with the text
        """
        raise NotImplementedError

    def get_start_with_5w1h(self) -> int:
        """
        Whether text starts with 'what', 'where', 'when', 'why', 'who' and 'how'
        """
        raise NotImplementedError

    def get_contain_superlative(self) -> int:
        """
        Whether text contains a superlative adverb or djective
        """
        raise NotImplementedError
