from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name="word_forms",
      version="2.1.0",
      description="Generate all possible forms of an English word.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="Dibya Chakravorty",
      author_email="dibyachakravorty@gmail.com",
      url="https://github.com/gutfeeling/word_forms",
      packages=["word_forms"],
      package_data={"word_forms" : ["en-verbs.txt", "adj_to_adv.txt"]},
      include_package_data=True,
      install_requires=["inflect==4.1.0", "nltk>=3.3"],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      )
