import re

try:
    from nltk.corpus import wordnet as wn
    raise_lookuperror_if_wordnet_data_absent = wn.synsets("python")
except LookupError:
    import nltk
    nltk.download("wordnet")
from nltk.stem import WordNetLemmatizer
import inflect
from Levenshtein import ratio

from .constants import CONJUGATED_VERB_DICT, ADJECTIVE_TO_ADVERB


def belongs(lemma, lemma_list):
    """
    args:
        - lemma : a Wordnet lemma e.g. Lemma('administration.n.02.governance')
        - lemma_list : a list of lemmas

    returns True if lemma is in lemma_list and False otherwise.

    The NLTK Wordnet implementation of Lemma is such that two lemmas are
    considered equal only if their names are the same.
    i.e Lemma('regulate.v.02.govern') == Lemma('govern.v.02.govern')
    Therefore the python statement "lemma in lemma_list" yields
    unexpected results. This function implements the expected
    behavior for the statement "lemma in list_list".
    """
    return any(
        element.name() == lemma.name() and element.synset() == lemma.synset()
        for element in lemma_list
    )


def get_related_lemmas(word):
    """
    args
        - word : a word e.g. "lovely"

    returns a list of related lemmas e.g [Lemma('cover_girl.n.01.lovely'),
        Lemma('lovely.s.01.lovely'), Lemma('adorable.s.01.lovely'),
        Lemma('comeliness.n.01.loveliness')]
    returns [] if Wordnet doesn't recognize the word
    """
    return get_related_lemmas_rec(word, [])


def get_related_lemmas_rec(word, known_lemmas, similarity_threshold):
    # Turn string word into list of Lemma objects
    all_lemmas_for_this_word = [
        lemma
        for ss in wn.synsets(word)
        for lemma in ss.lemmas()
        if lemma.name() == word
    ]
    # Add new lemmas to known lemmas
    known_lemmas += [
        lemma for lemma in all_lemmas_for_this_word if not belongs(lemma, known_lemmas)
    ]
    # Loop over new lemmas, and recurse using new related lemmas, but only if the new related lemma is similar to the original one
    for lemma in all_lemmas_for_this_word:
        for new_lemma in lemma.derivationally_related_forms() + lemma.pertainyms():
            if (
                not belongs(new_lemma, known_lemmas)
                and ratio(word, new_lemma.name()) > similarity_threshold
            ):
                get_related_lemmas_rec(new_lemma.name(), known_lemmas, similarity_threshold)
    # Return the known lemmas
    return known_lemmas


def get_word_forms(word, similarity_threshold=0.4):
    """
    args
        word : a word e.g "love"
        similarity_threshold: minimum levenshtein ratio e.g 0.5 (default: 0.4)

    returns the related word forms corresponding to the input word. the output
    is a dictionary with four keys "n" (noun), "a" (adjective), "v" (verb)
    and "r" (adverb). The value for each key is a python Set containing
    related word forms with that part of speech.

    e.g. {'a': {'lovable', 'loveable'},
          'n': {'love', 'lover', 'lovers', 'loves'},
          'r': set(),
          'v': {'love', 'loved', 'loves', 'loving'}}
    """
    words = {
        WordNetLemmatizer().lemmatize(word, pos)
        for pos in [wn.NOUN, wn.ADJ, wn.VERB, wn.ADV]
    }
    related_lemmas = []
    for lemmatized_word in words:
        get_related_lemmas_rec(lemmatized_word, related_lemmas, similarity_threshold)
    related_words_dict = {"n": set(), "a": set(), "v": set(), "r": set()}
    for lemma in related_lemmas:
        pos = lemma.synset().pos()
        if pos == "s":
            pos = "a"
        related_words_dict[pos].add(lemma.name().lower())

    for noun in related_words_dict["n"].copy():
        plural = inflect.engine().plural_noun(noun)
        # inflect's pluralisation of nouns often fails by adding an additional "s" when pluralising
        # uninflectable nouns ending in -cs, such as "politics" or "genetics". We drop these cases.
        # In particular, if the new plural ends with a consonant + ss, while the noun itself did not
        # then we do *not* add the plural
        if not re.search("[b-df-hj-np-tv-z]ss$", plural) or re.search(
            "[b-df-hj-np-tv-z]ss$", noun
        ):
            related_words_dict["n"].add(plural)

    for verb in related_words_dict["v"].copy():
        if verb in CONJUGATED_VERB_DICT:
            related_words_dict["v"] |= CONJUGATED_VERB_DICT[verb].verbs

    for adjective in related_words_dict["a"].copy():
        if adjective in ADJECTIVE_TO_ADVERB:
            related_words_dict["r"].add(ADJECTIVE_TO_ADVERB[adjective])

    return related_words_dict
