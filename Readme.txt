To Do:
1. setup sqllite / noSQL for storing the data rather than csv.
2. set up the logger
3. Any other features i can still use from spotify?
4. add a last run check to only get most recent data. so only new information is added to the database.

# setup
pythom -m venv .venv

# activate venv
.venv\Scripts\activate

#install dependencies
pip install -r requirements.txt

# run
python main.py

# folder structure
WorkSpace.
├───config
│	└───config.json
├───data
├───logs
│	└───my_logs.log
├───src
│    └───__init__.py
│    └───my_libraries.py
├───main.py
├───Readme.txt
└───requirements.txt