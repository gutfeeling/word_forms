from setuptools import setup

setup(name="word_forms",
      version="1.0",
      description="Generate all possible forms of an English word.",
      author="Dibya Chakravorty",
      author_email="dibyachakravorty@gmail.com",
      packages=["word_forms"],
      package_data={"word_forms" : ["en-verbs.txt"]},
      include_package_data=True,
      install_requires=["inflect==4.1.0", "nltk==3.5", "python-Levenshtein==0.12.0"]
      )
