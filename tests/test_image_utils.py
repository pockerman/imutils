import unittest
from pathlib import Path
from imutils.imutils.image_utils import get_img_files
from imutils.imutils.image_enums import ImageFileEnumType


class TestImageUtils(unittest.TestCase):

    def test_get_img_files(self):
        files = get_img_files(img_dir=Path('/home/alex/qi3/vision_utils/imutils/test_data'),
                              img_formats=(ImageFileEnumType.PNG,
                                           ImageFileEnumType.JPG))

        self.assertEqual(2, len(files))

if __name__ == '__main__':
    unittest.main()