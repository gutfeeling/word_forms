from difflib import get_close_matches
from pathlib import Path

try:
    from nltk.corpus import wordnet as wn
    raise_lookuperror_if_wordnet_data_absent = wn.synsets("python")
except LookupError:
    import nltk
    nltk.download("wordnet")
try:
    from nltk.corpus import words
except LookupError:
    nltk.download("words")

ALL_WORDNET_WORDS = set(words.words())


class Verb(object):
    def __init__(self, verbs):
        self.verbs = verbs

    def __repr__(self):
        return "Verbs" + str(self.verbs)


verbs_fh = open(str(Path(__file__).parent.absolute() / "en-verbs.txt"))
lines = verbs_fh.readlines()
verbs_fh.close()
CONJUGATED_VERB_DICT = {}
for line in lines:
    if line[0] != ";":
        verb_obj = Verb({string for string in line.strip().split(",") if string != ""})
        for verb in verb_obj.verbs:
            CONJUGATED_VERB_DICT[verb] = verb_obj

ADJECTIVE_TO_ADVERB = {"good" : "well", "fast" : "fast", "hard" : "hard",
                       "late" : "late", "early" : "early", "daily" : "daily",
                       "straight" : "straight"}
for ss in wn.all_synsets(pos="r"):
    for lemma in ss.lemmas():
        word = lemma.name()
        this_word_lemmas = [
            lemma
            for ss in wn.synsets(word, pos=wn.ADV)
            for lemma in ss.lemmas()
            if lemma.name() == word
        ]
        pertainyms = {
            pertainym.name()
            for this_word_lemma in this_word_lemmas
            for pertainym in this_word_lemma.pertainyms()
        }
        matches = get_close_matches(word, pertainyms)
        for match in matches:
            ADJECTIVE_TO_ADVERB[match] = word
