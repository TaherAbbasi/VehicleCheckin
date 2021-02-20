# VehicleCheckin

Features
--------


Installation
------------

This process assumes a basic knowledge of the Python ecosystem. If you are unfamilliar with [Pip], [Virtualenv] and it's counterpart Virtualenvwrapper, and the like, you may want to do some initial research into those topics.

0. Create a virtual environment `mkvirtualenv venv` or `python -m venv venv`
1. Clone this repository `git clone git@github.com:TaherAbbasi/VehicleCheckin.git`
2. From within the repository root, install project dependencies `pip install -r requirements.txt`

Usage
-----

Once you have cloned this repository.

0. Activate the virtual Environmnet.
2. In the project root: `cd backend`
3. makemigrations `python manage.py makemigrations`
3. apply the migrations to the database `python manage.py migrate`
3. `python manage.py runserver`