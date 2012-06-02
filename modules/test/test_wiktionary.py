# -*- coding: utf-8 -*-
"""
test_wiktionary.py - tests for the wiktionary module
author: mutantmonkey <mutantmonkey@mutantmonkey.in>
"""

import re
import unittest
from mock import MagicMock, Mock
from modules import wiktionary


class TestWiktionary(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()

    def test_wiktionary(self):
        w = wiktionary.wiktionary('test')

        assert len(w[0]) > 0
        assert len(w[1]) > 0

    def test_w(self):
        input = Mock(group=lambda x: 'test')
        wiktionary.w(self.phenny, input)

        out = self.phenny.say.call_args[0][0]
        m = re.match('^test — noun: .*$', out, flags=re.UNICODE)
        self.assertTrue(m)
