# Corona-Virus-Website

## Prerequisites:

- Install python
- Install pip

### Installing python

Optionally, if you have a mac, you can install python with Homebrew, which can be done by following [this guide](https://docs.python-guide.org/starting/install3/osx/).

Homebrew is a useful package manager, and will simplify the install process by automatically installing pip (python's package manager) as well, however macOS should already come with a version of python installed so this is not absolutely necessary.

If you're lazy, this should do it:

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
```

### Installing pip

If you do not install python using Homebrew, you will need to manually install pip.

This can be accomplished by following [this guide](https://ahmadawais.com/install-pip-macos-os-x-python/), but note that easyinstall has been depreciated, so you should follow the updated section up the top of the guide instead.

If you're lazy, this should do it:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

## How to use:

See below for detailed steps

1. Set up a virtual environment
2. run main.py
3. Navigate to the URL given in the terminal

### Setting up a virtual environment:

If it is your first time setting up the virtual environment, run the following to create and activate a virtual environment and install the necessary packages:

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

After the first time - run the following to activate the virtual environment:

```
. venv/bin/activate
```

### Running main.py:

Run main.py:

```
python3 main.py
```

### Navigating to the URL:

Once you have run main.py, it should output the URL into the terminal. It should be http://0.0.0.0:5000/ by default.

## Random stuff that used to be comments in setup.py

【sss】
https://packaging.python.org/discussions/install-requires-vs-requirements/
https://stackoverflow.com/questions/46877667/how-to-push-a-new-initial-project-to-github-using-vs-code
https://github.com/avinassh/rockstar/blob/master/setup.py#L11,#L19

should i use this? https://pipenv.readthedocs.io/en/latest/
https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe
https://medium.com/@krishnaregmi/pipenv-vs-virtualenv-vs-conda-environment-3dde3f6869ed
https://docs.python-guide.org/dev/virtualenvs/
https://packaging.python.org/guides/tool-recommendations/
https://docs.python.org/3/tutorial/venv.html
I will just use venv for the moment.

https://www.reddit.com/r/learnpython/comments/9lrcee/should_i_use_pipenv_or_virtualenv/
follow those commands to set up venv

doesn't seem to want to install with:
pip install .
use:
pip install -r requirements.txt
for the time being

!/usr/bin/env python

source venv/bin/activate
is the same as
. venv/bin/activate

For the first time running, run:
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

https://guides.github.com/features/mastering-markdown/
https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
