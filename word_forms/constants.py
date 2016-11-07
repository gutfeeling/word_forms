from difflib import get_close_matches

try:
    from nltk.corpus import wordnet as wn
    raise_lookuperror_if_wordnet_data_absent = wn.synsets("python")
except LookupError:
    import nltk
    nltk.download("wordnet")
from unipath import Path
import inflect

ALL_WORDNET_WORDS = set()
for synset in list(wn.all_synsets()):
    for lemma in synset.lemmas():
        ALL_WORDNET_WORDS.add(lemma.name())

verbs_fh =  open(Path(__file__).ancestor(1).child("en-verbs.txt"))
lines = verbs_fh.readlines()
verbs_fh.close()
CONJUGATED_VERB_LIST = []
for line in lines:
    if line[0] != ";":
        CONJUGATED_VERB_LIST.append(
            [string for string in line.strip().split(",") if string != ""])

ADJECTIVE_TO_ADVERB = {"good" : "well", "fast" : "fast", "hard" : "hard",
                       "late" : "late", "early" : "early", "daily" : "daily",
                       "straight" : "straight"}
for ss in wn.all_synsets(pos = "r"):
    for lemma in ss.lemmas():
        word = lemma.name()
        this_word_lemmas = [lemma for ss in wn.synsets(word, pos = wn.ADV)
                            for lemma in ss.lemmas() if lemma.name() == word]
        pertainyms = [pertainym.name() for this_word_lemma in this_word_lemmas
                      for pertainym in this_word_lemma.pertainyms() ]
        matches = get_close_matches(word, pertainyms)
        if len(matches) > 0:
            ADJECTIVE_TO_ADVERB[matches[0]] = word
