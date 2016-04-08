import unittest
from src.util.string_util import StringUtil 

class StrUtilTest(unittest.TestCase):

    def test_emoji_regex_compile(self):
        assert StringUtil.char_count("123") == 3