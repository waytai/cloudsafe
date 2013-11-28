from setuptools import setup, find_packages

setup(
    name = 'cloudsafe',
    version = '0.0.1',
    keywords = ('cloudsafe', 'golismero'),
    description = 'cloudsafe',
    license = 'MIT License',
    install_requires = ['Django>=1.4'],

    author = 'wengcc',
    author_email = 'wengcc@ihep.ac.cn',

    packages = find_packages(),
    platforms = 'any',
    )

