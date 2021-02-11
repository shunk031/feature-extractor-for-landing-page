class TestContentFeature(object):
    def test_get_yct(self) -> int:
        """
        Likelihood of the most top level YCT (Yahoo Category Taxonomy, e.g., sports)
        the text to be classified from CAP
        """
        raise NotImplementedError

    def test_get_adult_text(self) -> int:
        """
        Likelihood of text to contain adult contents from CAP
        """
        raise NotImplementedError

    def test_get_adult_image(self) -> int:
        """
        Likelihood of image to contain adult related images (e.g., too much skin)
        """
        raise NotImplementedError

    def test_get_image_cnn_classifier(self) -> int:
        """
        Likelihood of image to contain deep learning based object
        based on the second last layer of the Convolutional Neural Networks (CNNs)
        """
        raise NotImplementedError
