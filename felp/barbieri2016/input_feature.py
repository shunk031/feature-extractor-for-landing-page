from bs4 import BeautifulSoup


class InputFeature(object):
    def __init__(self, soup: BeautifulSoup) -> None:
        self._soup = soup

    def get_number_of_clickable(self) -> int:
        """
        Number of clickable objects in the landing page
        """
        raise NotImplementedError

    def get_number_of_dropdown(self) -> int:
        """
        Number of dropdown elements
        """
        return len(self._soup.find_all("select"))

    def get_number_of_check_box(self) -> int:
        """
        Number of checkbox
        """
        return len(self._soup.find_all("input", {"type": "checkbox"}))

    def get_number_of_input_strings(self) -> int:
        """
        Number of Input Strings
        """
        return len(self._soup.find_all("input", {"type": "text"}))

    def get_number_of_radio_buttons(self) -> int:
        """
        Number of radio buttons
        """
        return len(self._soup.find_all("input", {"type": "radio"}))
