from bs4 import BeautifulSoup


class MediaFeature(object):
    def __init__(self, soup: BeautifulSoup) -> None:
        pass

    def get_image_height(self) -> int:
        """
        Height of the rendered landing page
        """
        raise NotImplementedError

    def get_image_width(self) -> int:
        """
        Width of the rendered landing page
        """
        raise NotImplementedError

    def get_number_of_images(self) -> int:
        """
        Number of images contained in the landing page
        """
        raise NotImplementedError

    def get_media(self) -> bool:
        """
        Is there a media (e.g., video) on the landing page?
        """
        raise NotImplementedError
