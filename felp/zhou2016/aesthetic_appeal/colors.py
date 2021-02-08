class ColorsFeature(object):
    def __init__(self) -> None:
        pass

    def get_contrast(self) -> int:
        """
        Ratio between the sum of max and min luminance values and the average luminance
        """
        raise NotImplementedError

    def get_hsv(self) -> int:
        """
        Average Hue, Saturation, Brightness computed on the whole image
        """
        raise NotImplementedError

    def get_hsv_central_quadrant(self) -> int:
        """
        Average Hue, Saturation, Brightness computed on the central quadrant
        """
        raise NotImplementedError

    def get_hsv_color_histograms(self) -> int:
        """
        Hisrograms of H, S and V values quantized over 12, 3, and 5 bins
        """
        raise NotImplementedError

    def get_hsv_contrasts(self) -> int:
        """
        Standard deviation of the HSV Color Histograms distributions
        """
        raise NotImplementedError

    def get_pleasure_arousal_dominance(self) -> int:
        """
        Based on average HSV combinations
        """
        raise NotImplementedError
