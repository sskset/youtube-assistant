import unittest

from utilities.video import Video


class TestVideo(unittest.TestCase):

    def setUp(self):

        from settings import abs_dir_path, init_container
        init_container()


        self.video = Video(
            'https://v.youku.com/v_show/id_XMzcxNTk3MDc0MA==.html?spm=a2hfs.20010010.m_226528.5~5!2~5~5!3~5~A')

    def test_get_info(self):
        info = self.video.get_info()
        # pprint(info)
        self.assertIsNotNone(info)
        # print(info.get('title'))
        self.assertEqual(info.get('title'), '方大同《The Secret of The Golden Bricks》歌词版MV')

    def test_find_highest_resolution_format(self):
        format = self.video.find_highest_resolution_format()

        self.assertIsNotNone(format)
        print(format)

    def test_download(self):
        self.video.download()

    def test_download_highest_resolution(self):
        self.video.download_highest_resolution()


if __name__ == '__main__':
    unittest.main()
