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

1. Clone or fork this repo:

   `$ git clone https://github.com/glenn-barker/web-bdd.git`

2. Create and activate a new Python virtual environment: (*Recommended, not required.*)

   * Windows:
   
      ```
      $ cd web-bdd
      $ virtualenv .env && .env\scripts\activate
      ```
      
   * *nix:
    
      ```
      $ cd web-bdd
      $ virtualenv .env && source .env/bin/activate
      ```

3. Install the required modules:

   ```
   $ pip install -r requirements.txt
   ```

4. Run the `behave` scenarios to kick off the sample web automation:

   `$ behave`