class ReadabilityFeature(object):
    def __init__(self) -> None:
        pass

    def get_number_of_sentences(self) -> int:
        """
        Number of sentences
        """
        raise NotImplementedError

    def get_number_of_words(self) -> int:
        """
        Number of words
        """
        raise NotImplementedError
