<img src="https://github.com/gutfeeling/word_forms/blob/master/logo.png" alt="word forms logo" width="500">
## Accurately generate all possible forms of an English word

Word forms can accurately generate all possible forms of an English word. It can conjugate verbs. It can connect different
parts of speeches e.g noun to adjective, adjective to adverb, noun to verb etc. It can pluralize singular nouns. It does this all in one function. Enjoy!

## Examples

Some very timely examples :-P

```python
>>> from word_forms.word_forms import get_word_forms
>>> get_word_forms("president")
>>> {'n': {'president', 'Presidents', 'President', 'presidentship', 'presidencies', 'presidency', 'presidentships', 'presidents'}, 
     'r': {'presidentially'}, 
     'a': {'presidential'}, 
     'v': {'presiding', 'presides', 'preside', 'presided'}}
>>> get_word_forms("elect")
>>> {'n': {'elector', 'elects', 'electors', 'elective', 'electorates', 'elect', 'electives', 'elections', 'electorate', 'eligibility', 'election', 'eligibilities'}, 
     'r': set(), 
     'a': {'elect', 'electoral', 'elective', 'eligible'}, 
     'v': {'elect', 'elects', 'electing', 'elected'}}
>>> get_word_forms("politician")
>>> {'r': {'politically'}, 
     'a': {'political'}, 
     'n': {'politicss', 'politician', 'politicians', 'politics'}, 
     'v': set()}
>>> get_word_forms("trump")
>>> {'n': {'trump', 'trumps', 'trumping', 'trumpings'}, 
     'r': set(), 
     'a': set(), 
     'v': {'trumped', 'trump', 'trumps', 'trumping'}}
```
As you can see, the output is a dictionary with four keys. "r" stands for adverb, "a" for adjective, "n" for noun
and "v" for verb. Don't ask me why "r" stands for adverb. This is what WordNet uses, so this is why I use it too :-)

Help can be obtained at any time by typing the following:

```python
>>> help(get_word_forms)
```

## Why?
In Natural Language Processing and Search, one often needs to treat words like "run" and "ran", "love" and "lovable" 
or "politician" and "politics" as the same word. This is usually done by algorithmically reducing each word into a 
base word and then comparing the base words. The process is called Stemming. 
For example, the [Porter Stemmer](http://text-processing.com/demo/stem/) reduces both "love" and "lovely" 
into the base word "love".

Stemmers have several shortcomings. Firstly, the base word produced by the Stemmer is not always a valid English word. 
For example, the Porter Stemmer reduces the word "operation" to "oper". Secondly, the Stemmers have a high false negative rate. 
For example, "run" is reduced to "run" and "ran" is reduced to "ran". This happens because the Stemmers use a set of 
rational rules for finding the base words, and as we all know, the English language does not always behave very rationally. 

Lemmatizers are more accurate than Stemmers because they produce a base form that is present in the dictionary (also called the Lemma). So the reduced word is always a valid English word. However, Lemmatizers also have false negatives because they are not very good at connecting words across different parts of speeches. The [WordNet Lemmatizer](http://textanalysisonline.com/nltk-wordnet-lemmatizer) included with NLTK fails at almost all such examples. "operations" is reduced to "operation"  and "operate" is reduced to "operate".

Word Forms tries to solve this problem by finding all possible forms of a given English word. It can perform verb conjugations, connect noun forms to verb forms, adjective forms, adverb forms, plularize singular forms etc. 

## Compatibility

Works on both Python 2 and Python 3

## Installation

### 1. Clone the repository.
```
git clone https://github.com/gutfeeling/word_forms.git
```
### 2. Install it using pip or setup.py install
```
pip install -e word_forms
```
OR
```
cd word_forms
python setup.py install
```

### Alternatively, add this to your pip requirements file:
```
git+git://github.com/gutfeeling/word_forms.git#egg=word_forms
```

## Acknowledgement

1. [The XTAG project](http://www.cis.upenn.edu/~xtag/) for information on [verb conjugations](word_forms/en-verbs.txt).
2. [WordNet](http://wordnet.princeton.edu/)

## Maintainer

Hi, I am Dibya and I maintain this repository. I would love to hear from you. Feel free to get in touch with me 
at dibyachakravorty@gmail.com.

## Contributions

Word Forms is not perfect. In particular, a couple of aspects can be improved.

1. It sometimes generates non dictionary words like "politicss" because the pluralization/singularization algorithm is
not perfect. At the moment, I am using [inflect](https://pypi.python.org/pypi/inflect) for it. 

2. A function `has_same_base_form` for comparing two words can be added. At the moment, the information that "run" and 
"ran" are connected can only be figured out by querying `get_word_forms("run")` and not `get_word_forms("ran")`. This 
could be solved by creating a database of equivalence classes using this package (if word forms is an equivalence relation).

If you like this package, feel free to contribute. Your pull requests are most welcome.
