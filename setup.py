from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '0.1'

setup(
    name='Corona-Virus-Website',
    version=version,
    # install_requires=[
    #    'flask',
    #    'sqlite3'
    # ],
    install_requires=requirements,
    author='Nicholas Langford',
    packages=find_packages(),
    include_package_data=True,
    scripts=["main.py"],
    url='https://github.com/scorpiontornado/Corona-Virus-Website',
    description='A website for looking at corona virus data',
    long_description=long_description,
)
