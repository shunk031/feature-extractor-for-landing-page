class LanguageUsageFeature(object):
    def test_get_spam(self) -> float:
        """
        Likelihood oftext to be classified as spam from CAP (trained on HTML web documents)
        """
        raise NotImplementedError

    def test_get_hate_speech(self) -> float:
        """
        Likelihood of text to contain abusive speech targeting specific group characteristics,
        such as ethnicity, religion, or gender, from CAP
        """
        raise NotImplementedError

    def test_get_click_bait(self) -> int:
        """
        Likelihood of text to be classified as clickbait, exploiting a learned prediction model
        based on a set of low-level, sentiment and bag-of-words features
        """
        raise NotImplementedError

    def test_get_number_of_slang_words(self) -> int:
        """
        Number of slang words used (defined in a word list)
        """
        raise NotImplementedError

    def test_get_number_of_profane_words(self) -> int:
        """
        Number of profane words used (define in a word list)
        """
        raise NotImplementedError
