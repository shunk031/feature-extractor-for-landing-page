from typing import Tuple

from bs4 import BeautifulSoup


class MobileOptimizedFeature(object):
    def __init__(self, soup: BeautifulSoup) -> None:
        pass

    def get_click_to_call(self) -> bool:
        """
        Is there a click to call button?
        """
        raise NotImplementedError

    def get_iphone_bottun(self) -> bool:
        """
        Is there an iPhone button?
        """
        raise NotImplementedError

    def get_view_port(self) -> bool:
        """
        Is view port available?
        """
        raise NotImplementedError

    def get_window_size(self) -> Tuple[int, int]:
        """
        Size of the window
        """
        raise NotImplementedError
