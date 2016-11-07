from setuptools import setup

setup(name='word_forms',
      version='1.0',
      description='Generate different forms of a word.',
      author='Dibya Chakravorty',
      packages=['word_forms'],
      package_data={'word_forms' : ['en-verbs.txt']},
      include_package_data=True,
      author_email='dibyachakravorty@gmail.com',
      )
