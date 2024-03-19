Link to this repo: https://github.com/AshokSivathayalan/COMP3005-Assignment3/blob/master/README.txt

VIDEO DEMONSTRATION: https://youtu.be/idkk9qW0DSo

SETTING UP DATABASE:

Needs Postgresql & pgAdmin4. 

Create database named students (if giving other name, will need to change line 4 of python program to correct database name)
Run db.sql script to automatically create the database and populate it with default values

RUNNING PYTHON PROGRAM:
Needs psycopg python module installed with pip.
If not, run pip install "psycopg[binary]"

Ensure that username and password in line 4 are correct - these are "postgres" and "postgres" by default.

Open command line in folder where python program is stored, and run 
py assignment3.py
