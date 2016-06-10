To get started, create a new project in a directory called tbay, and cd into the directory. Then initialize and activate a virtual environment:

sudo apt-get update
sudo apt-get install python3.4-venv
python3 -m venv env
source env/bin/activate
Next, install SQLAlchemy and psycopg2 using pip install sqlalchemy psycopg2. Then create a new Postgres database for the project by running: createdb tbay.