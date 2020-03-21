# 【sss】
# https://packaging.python.org/discussions/install-requires-vs-requirements/
# https://stackoverflow.com/questions/46877667/how-to-push-a-new-initial-project-to-github-using-vs-code
# https://github.com/avinassh/rockstar/blob/master/setup.py#L11,#L19

# should i use this? https://pipenv.readthedocs.io/en/latest/
# https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe
# https://medium.com/@krishnaregmi/pipenv-vs-virtualenv-vs-conda-environment-3dde3f6869ed
# https://docs.python-guide.org/dev/virtualenvs/
# https://packaging.python.org/guides/tool-recommendations/
# https://docs.python.org/3/tutorial/venv.html
# I will just use venv for the moment.

# https://www.reddit.com/r/learnpython/comments/9lrcee/should_i_use_pipenv_or_virtualenv/
# follow those commands to set up venv

# doesn't seem to want to install with:
# pip install .
# use:
# pip install -r requirements.txt
# for the time being

#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '0.1'

setup(
    name='Corona-Virus-Website',
    version=version,
    #install_requires=[
    #    'flask',
    #    'sqlite3'
    #],
    install_requires=requirements,
    author='Nicholas Langford',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/scorpiontornado/Corona-Virus-Website',
    description='A website for looking at corona virus data',
    long_description=long_description,
)
