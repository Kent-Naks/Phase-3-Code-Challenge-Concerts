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
    -- Succeful.

5. Seeding the database. (pipenv run python seed.py)

6. After adding the necessary information on the seed.py file, I then pipenv shell so as to activate the Pipenv shell then pipenv install sqlalchemy. Lastly its to run the pipenv run python seed.py again to see if the module not found error is still there.

7. Needed to first add intial setup of SQLAlchemy, config data base connection and sessions and define model relationships.

8. Completed with the 

9. Created the cli.py file. This commit implements a basic CLI for managing bands, venues, and concerts. It introduces functions to list all bands and venues by querying the database and displaying relevant details such as band ID, name, hometown, venue ID, title, and city. A create_concert function is added, which validates band and venue IDs before creating a new concert and saving it to the database. The main function serves as the entry point for the CLI, offering users options to list bands, list venues, create a concert, or exit. It handles user input, provides feedback for invalid options, and ensures the program runs smoothly with error handling for invalid band or venue IDs.

created a config.py. Included config.py to set up the database connection using SQLAlchemy.

FAILED: Directory migrations already
  exists and is not empty, solution was to create a new migration. 
  SOLUTION:

  1. "alembic revision --autogenerate -m "Initial migration"
"
  2. IndentationError: unexpected indent, fixing indention error on env.py. Error was on line 41.
  3.Running the migration using "alembic upgrade head". Migration was a success.
  4. Verifying database changes