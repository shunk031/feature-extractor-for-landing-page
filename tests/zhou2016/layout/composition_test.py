class TestCompositionFeatures(object):
    def test_get_presence_of_objects(self) -> int:
        """
        Amount of saliency in 9 image quadrants
        """
        raise NotImplementedError

    def test_get_uniqueness(self) -> int:
        """
        Difference between the image spectral signal and the average spectrum of natural images
        """
        raise NotImplementedError

    def test_get_symmetry(self) -> int:
        """
        Difference between the HOG feature vectors of the image left-half and right-half
        """
        raise NotImplementedError

    def test_get_depth_of_field(self) -> int:
        """
        Low DOF indicators based on haar wavelets
        """
        raise NotImplementedError

    def test_get_image_text_detector(self) -> int:
        """
        Likelihood of image text detector
        """
        raise NotImplementedError
