class ReadabilityFeature(object):
    def __init__(self) -> None:
        pass

    def get_fleschs_reading_ease_test(self) -> int:
        """
        Combination of number of words per sentence and syllables per words
        """
        raise NotImplementedError

    def get_flesch_kincaid_grade_level(self) -> int:
        """
        Combination of number of words per sentence and syllables per words
        """
        raise NotImplementedError

    def get_gunning_fog_index(self) -> int:
        """
        Combination of number of words per sentence and percentager of complex words
        """
        raise NotImplementedError

    def get_coleman_liau_index(self) -> int:
        """
        Combination of number of letters per words and average number of sentences per words
        """
        raise NotImplementedError

    def get_rix_index(self) -> int:
        """
        Number of long words (words over six characters) per sentences
        """
        raise NotImplementedError

    def get_number_of_capitalized_words(self) -> int:
        """
        Number of capitalized words, and whether text contains at least one capitalized words
        """
        raise NotImplementedError

    def get_number_of_acronyms(self) -> int:
        """
        Number of acronyms, and where text contains at least one acronyms
        """
        raise NotImplementedError

    def get_words_per_sentence(self) -> int:
        """
        Number of words per sentence
        """
        raise NotImplementedError

    def get_percentage_of_complex_words(self) -> float:
        """
        Complex words contain three or more syllables
        """
        raise NotImplementedError

    def get_syllables_per_words(self) -> int:
        """
        Number of syllables per words
        """
        raise NotImplementedError
