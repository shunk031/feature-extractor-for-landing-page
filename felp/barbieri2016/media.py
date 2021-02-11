from bs4 import BeautifulSoup


class MediaFeature(object):
    def __init__(self, soup: BeautifulSoup) -> None:
        self._soup = soup

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
        return len(self._soup.find_all("img"))

    def get_media(self) -> bool:
        """
        Is there a media (e.g., video) on the landing page?
        """
        is_image = len(self._soup.find_all("img")) > 0
        is_video = len(self._soup.find_all("video")) > 0
        return is_image or is_video
