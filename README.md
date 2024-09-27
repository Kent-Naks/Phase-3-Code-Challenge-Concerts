# Phase-3-Code-Challenge-Concerts

1. concerts_project tree sample 1, might change along the way/

── migrations/
   ── versions/
   ── env.py
── app.py                  # Entry point to run the app
── config.py               # Configuration file for database
── models.py               # Contains SQLAlchemy models for Band, Venue, Concert
── seed.py                 # Script to seed the database with initial data
── README.md               # Project documentation
── Pipfile                 # Pipenv file for managing dependencies

So step 1 completed, now off to installation of needed files.

2. Installing Pipenv.(pip install pipenv)

3. Installing the dependancies. (pipenv install)

4. Set up the Database. (pipenv run alembic upgrade head)
   -- error occcired due to a lack of an alembic.ini file. Now going to create the file. 
