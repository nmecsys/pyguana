from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pyguana',
      version='0.1',
      description='The pyguana provides a python wrapper to the Iguana API.',
      url='http://github.com/nmecsys/pyguana',
      author='Fernando Teixeira',
      author_email='fernando.teixeira@fgv.br',
      license='MIT',
      packages=['pyguana'],
	  install_requires=[
          'requests',
      ],
      zip_safe=False)