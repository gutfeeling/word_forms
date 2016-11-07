from setuptools import setup

setup(name="word_forms",
      version="1.0",
      description="Generate all possible forms of an English word.",
      author="Dibya Chakravorty",
      author_email="dibyachakravorty@gmail.com",
      packages=["word_forms"],
      package_data={"word_forms" : ["en-verbs.txt"]},
      include_package_data=True,
      install_requires = ["Unipath==1.1", "inflect==0.2.5", "nltk==3.2.1"]
      )
