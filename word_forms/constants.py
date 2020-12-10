from collections import defaultdict
from pathlib import Path
import json

class Verb(object):
    def __init__(self, verbs=None):
        self.verbs = verbs if verbs else set()

    def __repr__(self):
        return "Verbs" + str(self.verbs)

    def update(self, verbs):
        self.verbs.update(verbs)


verbs_fh = open(str(Path(__file__).parent.absolute() / "en-verbs.txt"))
lines = verbs_fh.readlines()
verbs_fh.close()

CONJUGATED_VERB_DICT = defaultdict(Verb)
for line in lines:
    if line[0] != ";":
        verbs = {string for string in line.strip().split(",") if string != ""}
        for verb in verbs:
            CONJUGATED_VERB_DICT[verb].update(verbs)

adj_fh = open(str(Path(__file__).parent.absolute() / "adj_to_adv.txt"))
ADJECTIVE_TO_ADVERB = json.load(adj_fh)
adj_fh.close()
