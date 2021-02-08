class BrandQualityFeature(object):
    def __init__(self) -> None:
        pass

    def get_advertiser_domain_pagerrank(self) -> int:
        """
        the WCC pagerank score of the top level domain of the ad landing page
        """
        raise NotImplementedError

    def get_advertiser_search_volume(self) -> int:
        """
        the number of Yahoo search query volume given the advertiser name or the sponsored by label
        """
        raise NotImplementedError
