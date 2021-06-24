import json
from pathlib import Path
from collections import defaultdict


ABSOLUTE_PATH = Path(__file__).parent.absolute()
ADJECTIVE_TO_ADVERB = json.loads((ABSOLUTE_PATH / "adj_to_adv.txt").read_text())


class Verb(object):
    def __init__(self, verbs=None):
        self.verbs = verbs if verbs else set()

    def __repr__(self):
        return "Verbs" + str(self.verbs)

    def update(self, verbs):
        self.verbs.update(verbs)


CONJUGATED_VERB_DICT = defaultdict(Verb)
with open(ABSOLUTE_PATH / "en-verbs.txt") as lines:
    for line in lines:
        if line.startswith(";"):
            continue
        verbs = {string for string in line.strip().split(",") if string != ""}
        for verb in verbs:
            CONJUGATED_VERB_DICT[verb].update(verbs)
