class TestMediaFeature:
    def test_get_image_height(self) -> int:
        """
        Height of the rendered landing page
        """
        raise NotImplementedError

    def test_get_image_width(self) -> int:
        """
        Width of the rendered landing page
        """
        raise NotImplementedError

    def test_get_number_of_images(self) -> int:
        """
        Number of images contained in the landing page
        """
        raise NotImplementedError

    def test_get_media(self) -> bool:
        """
        Is there a media (e.g., video) on the landing page?
        """
        raise NotImplementedError
