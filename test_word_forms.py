#!/usr/bin/env python
# encoding: utf-8

from word_forms.word_forms import get_word_forms
import unittest


class TestWordForms(unittest.TestCase):
    """
    Simple TestCase for a specific input to output, one instance generated per test case for use in a TestSuite
    """

    def __init__(self, text_input: str, expected_output: dict, description: str = ""):
        super().__init__()
        self.text_input = text_input
        self.expected_output = expected_output
        self.description = description

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def runTest(self):
        self.assertEqual(
            get_word_forms(self.text_input), self.expected_output, self.description
        )


if __name__ == "__main__":
    from test_values import test_values
    suite = unittest.TestSuite()
    suite.addTests(
        TestWordForms(inp, out, f"get_word_forms({repr(inp)})")
        for inp, out in test_values
    )
    unittest.TextTestRunner().run(suite)
