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
    # Test values must be in the form [(text_input, expected_output), (text_input, expected_output), ...]
    test_values = [
        (
            "president",
            {
                "n": {
                    "president",
                    "presidentship",
                    "presidencies",
                    "presidency",
                    "presidentships",
                    "presidents",
                },
                "r": {"presidentially"},
                "a": {"presidential"},
                "v": {"presiding", "presides", "preside", "presided"},
            },
        ),
        (
            "elect",
            {
                "n": {
                    "elector",
                    "elects",
                    "electors",
                    "elective",
                    "electorates",
                    "elect",
                    "electives",
                    "elections",
                    "electorate",
                    "eligibility",
                    "election",
                    "eligibilities",
                },
                "r": set(),
                "a": {"elect", "electoral", "elective", "eligible"},
                "v": {"elect", "elects", "electing", "elected"},
            },
        ),
        (
            "running",
            {
                "n": {
                    "runninesses",
                    "runnings",
                    "runs",
                    "running",
                    "runniness",
                    "runners",
                    "runner",
                    "run",
                },
                "a": {"running", "runny"},
                "v": {"running", "ran", "runs", "run"},
                "r": set(),
            },
        ),
        (
            "run",
            {
                "n": {
                    "runninesses",
                    "runnings",
                    "runs",
                    "running",
                    "runniness",
                    "runners",
                    "runner",
                    "run",
                },
                "a": {"running", "runny"},
                "v": {"running", "ran", "runs", "run"},
                "r": set(),
            },
        ),
        (
            "operations",
            {
                "n": {
                    "operators",
                    "operations",
                    "operation",
                    "operative",
                    "operator",
                    "operatives",
                },
                "a": {"operant", "operative"},
                "v": {"operated", "operating", "operate", "operates"},
                "r": {"operatively"},
            },
        ),
        (
            "operate",
            {
                "n": {
                    "operators",
                    "operations",
                    "operation",
                    "operative",
                    "operator",
                    "operatives",
                },
                "a": {"operant", "operative"},
                "v": {"operated", "operating", "operate", "operates"},
                "r": {"operatively"},
            },
        ),
        (
            "invest",
            {
                "n": {
                    "investitures",
                    "investors",
                    "investiture",
                    "investor",
                    "investments",
                    "investings",
                    "investment",
                    "investing",
                },
                "a": set(),
                "v": {"invested", "invests", "invest", "investing"},
                "r": set(),
            },
        ),
        (
            "investments",
            {
                "n": {
                    "investitures",
                    "investors",
                    "investiture",
                    "investor",
                    "investments",
                    "investings",
                    "investment",
                    "investing",
                },
                "a": set(),
                "v": {"invested", "invests", "invest", "investing"},
                "r": set(),
            },
        ),
        (
            "conjugation",
            {
                "n": {"conjugate", "conjugation", "conjugates", "conjugations"},
                "a": {"conjugate"},
                "v": {"conjugating", "conjugated", "conjugate", "conjugates"},
                "r": set(),
            },
        ),
        (
            "do",
            {
                "n": {"does", "doer", "doers", "do"},
                "a": set(),
                "v": {
                    "doing",
                    "don't",
                    "does",
                    "didn't",
                    "do",
                    "doesn't",
                    "done",
                    "did",
                },
                "r": set(),
            },
        ),
        (
            "word",
            {
                "n": {"words", "word", "wordings", "wording"},
                "a": set(),
                "v": {"words", "word", "worded", "wording"},
                "r": set(),
            },
        ),
        (
            "love",
            {
                "a": {"lovable", "loveable"},
                "n": {"love", "lover", "lovers", "loves"},
                "r": set(),
                "v": {"love", "loved", "loves", "loving"},
            },
        ),
        (
            "word",
            {
                "n": {"words", "word", "wordings", "wording"},
                "a": set(),
                "v": {"words", "word", "worded", "wording"},
                "r": set(),
            },
        ),
        (
            "verb",
            {
                "n": {"verbs", "verb"},
                "a": {"verbal"},
                "v": {"verbifying", "verbified", "verbify", "verbifies"},
                "r": {"verbally"},
            },
        ),
        (
            "genetic",
            {
                "n": {"geneticist", "genetics", "geneticists", "genes", "gene"},
                "a": {"genic", "genetic", "genetical"},
                "v": set(),
                "r": {"genetically"},
            },
        ),
        (
            "politician",
            {
                "r": {"politically"},
                "a": {"political"},
                "n": {"politician", "politicians", "politics"},
                "v": set(),
            },
        ),
        (
            "death",
            {
                "n": {"death", "dying", "deaths", "die", "dyings", "dice"},
                "a": {"dying", "deathly"},
                "v": {"died", "die", "dying", "dies"},
                "r": {"deathly"},
            },
        ),
        (
            "attitude",
            {
                "n": {"attitudes", "attitude"},
                "a": set(),
                "v": {
                    "attitudinise",
                    "attitudinized",
                    "attitudinize",
                    "attitudinizes",
                    "attitudinizing",
                },
                "r": set(),
            },
        ),
        (
            "cheek",
            {
                "n": {"cheek", "cheekinesses", "cheeks", "cheekiness"},
                "a": {"cheeky"},
                "v": {"cheek", "cheeks", "cheeked", "cheeking"},
                "r": {"cheekily"},
            },
        ),
        (
            "world",
            {
                "n": {"worldliness", "world", "worldlinesses", "worlds"},
                "a": {"worldly", "world"},
                "v": set(),
                "r": set(),
            },
        ),
        ("lake", {"n": {"lake", "lakes"}, "a": set(), "v": set(), "r": set()}),
        (
            "guitar",
            {
                "n": {"guitarist", "guitarists", "guitar", "guitars"},
                "a": set(),
                "v": set(),
                "r": set(),
            },
        ),
        (
            "presence",
            {
                "n": {
                    "presenter",
                    "present",
                    "presents",
                    "presentness",
                    "presenters",
                    "presentnesses",
                    "presentments",
                    "presentations",
                    "presences",
                    "presence",
                    "presentment",
                    "presentation",
                },
                "a": {"present"},
                "v": {"present", "presents", "presenting", "presented"},
                "r": {"presently"},
            },
        ),
        (
            "enthusiasm",
            {
                "n": {"enthusiasm", "enthusiasms"},
                "a": {"enthusiastic"},
                "v": set(),
                "r": {"enthusiastically"},
            },
        ),
        (
            "organization",
            {
                "n": {"organizers", "organization", "organizations", "organizer"},
                "a": set(),
                "v": {"organize", "organized", "organizing", "organizes"},
                "r": set(),
            },
        ),
        (
            "player",
            {
                "n": {
                    "plays",
                    "playlet",
                    "playings",
                    "players",
                    "playing",
                    "playlets",
                    "play",
                    "player",
                },
                "a": set(),
                "v": {"plays", "play", "playing", "played"},
                "r": set(),
            },
        ),
    ]
    suite = unittest.TestSuite()
    suite.addTests(
        TestWordForms(inp, out, f"get_word_forms({repr(inp)})")
        for inp, out in test_values
    )
    unittest.TextTestRunner().run(suite)
