#_*_coding:utf_8 _*_

import unittest

from country_codes import get_country_code

class CodeTestCase(unittest.TestCase):
    """测试获取国别码"""
    def test_country_code(self):
        code = get_country_code('United States')
        self.assertEqual(code,'us')

unittest.main()