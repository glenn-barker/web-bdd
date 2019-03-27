# web-bdd
BDD framework for web-based test automation with Python.

## Pre-requisites

1. Python 3.7
2. `pip` for managing and installing Python packages.
3. `pip install virtualenv` to configure a virtual environment. (*Recommended, not required.*)
4. Currently, the web drivers required by Selenium (e.g. `chromedriver.exe`) are not packaged or included,
   so you will need to provide these yourself and ensure they are in a location that is accessible. (I.E.
   they are visible in your `$PATH`.)

## Install

Clone or fork this repo, create & activate a new Python virtual environment (*recommended, not required.*), and
install the required modules.

### Windows:
```
$ git clone https://github.com/glenn-barker/web-bdd.git
$ cd web-bdd
$ virtualenv .env && .env\scripts\activate
$ pip install -r requirements.txt
```

### *Nix:
```
$ git clone https://github.com/glenn-barker/web-bdd.git
$ cd web-bdd
$ virtualenv .env && source .env/bin/activate
$ pip install -r requirements.txt
```

## Running

Kick off the sample web automation provided once installation is complete. You should see several web browsers open
and run a set of simple scripts that navigate around Wikipedia: 

`$ behave`
