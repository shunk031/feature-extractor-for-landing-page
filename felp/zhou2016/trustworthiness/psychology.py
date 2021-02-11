class PsychologyFeature(object):
    def __init__(self) -> None:
        pass

    def get_positive_polarity(self) -> int:
        """
        Sentistrength positive polarity classification
        based on 298 positive terms in the sentiment word strength list
        """
        raise NotImplementedError

    def get_negative_polarity(self) -> int:
        """
        Sentistrength negative polarity classification
        based on 465 negative terms in the sentiment word strength list
        """
        raise NotImplementedError

    def get_aggregated_polarity(self) -> int:
        """
        Sum of sentistrength positive and negative polarity for the overall polarity
        """
        raise NotImplementedError

    def get_psychological_incentives(self) -> int:
        """
        Frequency of words relating to social, affective, cognitive, perceptual,
        biological, relativity, personal concerns in the LIWC dictionary
        """
        raise NotImplementedError
