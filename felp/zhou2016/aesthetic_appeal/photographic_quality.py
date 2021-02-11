class PhotographicQualityFeature(object):
    def __init__(self) -> None:
        pass

    def get_contrast_balance(self) -> int:
        """
        Distance between original and contrast-normalized images
        """
        raise NotImplementedError

    def get_exposure_balance(self) -> int:
        """
        Absolute value of the luminance histogram skewness
        """
        raise NotImplementedError

    def get_jpeg_quality(self) -> int:
        """
        No-reference quality estimation algorithm in Wang et al.

        Wang, Zhou, Hamid R. Sheikh, and Alan C. Bovik.
        \"No-reference perceptual quality assessment of JPEG compressed images.\"
        Proceedings. International Conference on Image Processing. Vol. 1. IEEE, 2002.

        https://ieeexplore.ieee.org/document/1038064
        """
        raise NotImplementedError

    def get_jpeg_blockiness(self) -> int:
        """
        JPEG artifacts detection based on image re-compression
        """
        raise NotImplementedError

    def get_sharpness(self) -> int:
        """
        Sum of the image pixels after applying horizontal/vertical Sobel masks
        """
        raise NotImplementedError

    def get_foreground_sharpness(self) -> int:
        """
        Sum of the image pixel after applying horizontal/vertical Sobel masks on the salient image zones
        """
        raise NotImplementedError
