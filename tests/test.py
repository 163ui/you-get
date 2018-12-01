#!/usr/bin/env python

import unittest

from you_get.extractors import (
    imgur,
    magisto,
    youtube,
    bilibili,
    qq,
)


class YouGetTests(unittest.TestCase):

    def test_egame.qq(self):
        qq.download(
            'https://egame.qq.com/58815',
            info_only=True
        )

if __name__ == '__main__':
    unittest.main()
