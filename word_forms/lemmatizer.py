from word_forms.word_forms import get_word_forms


def lemmatize(word):
    """
    Out of all the related word forms of ``word``, return the smallest form that appears first in the dictionary
    """
    forms = get_word_forms(word).values()
    if not any(forms):
        raise ValueError("{} is not a real word".format(word))
    return min([word for pos_form in forms for word in pos_form], key=len)
