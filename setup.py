from setuptools import setup

setup(name='word_forms',
      version='1.0',
      description='Generate different forms of a word.',
      author='Dibya Chakravorty',
      author_email='dibyachakravorty@gmail.com',
      packages=['word_forms'],
      package_data={'word_forms' : ['en-verbs.txt']},
      include_package_data=True,
      install_requires = ["Unipath==1.1", "inflect==0.2.5", "nltk==3.2.1"]
      )
