import unittest

from pathlib import Path

from imutils.imutils.image_statistics import compute_image_channels_means
from imutils.imutils.image_statistics import compute_image_channels_variance
from imutils.imutils.image_utils import load_img
from imutils.imutils.image_enums import ImageLoadersEnumType


class TestImageStatistics(unittest.TestCase):

    def test_compute_image_channels_means(self):

        image = load_img(path=Path('/home/alex/qi3/vision_utils/imutils/test_data/corrosion_4.png'),
                         loader=ImageLoadersEnumType.PIL)
        means = compute_image_channels_means(image=image)
        self.assertEqual(len(means), 4)

    def test_compute_image_channels_variance(self):

        image = load_img(path=Path('/home/alex/qi3/vision_utils/imutils/test_data/corrosion_4.png'),
                         loader=ImageLoadersEnumType.PIL)
        means = compute_image_channels_variance(image=image)
        self.assertEqual(len(means), 4)


if __name__ == '__main__':
    unittest.main()