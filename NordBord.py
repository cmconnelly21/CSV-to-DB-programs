import sqlite3
from peewee import *
from datetime import datetime
import csv
from athlete_db import DataStream
from athlete_db import NordBord
from athlete_db import Athlete
import itertools
import argparse


db = SqliteDatabase('athletes.db')

db.connect('athletes.db')

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
args = parser.parse_args()

for i in args.file:
    for row in itertools.islice(csv.reader(i, delimiter=','), 3, None):
        #header
        athlete = row[0]
        query = Athlete.get(Athlete.name == athlete)
        date = row[1]
        testtype = row[2]
        leftreps = row[3]
        rightreps = row[4]
        maxforceleft = row[5]
        maxforceright = row[6]
        maximbal = row[7]
        maxtorqueleft = row[8]
        maxtorqueright = row[9]
        avgforceleft = row[10]
        avgforceright = row[11]
        avgimbal = row[12]
        avgtorqueleft = row[13]
        avgtorqueright = row[14]
        entry = NordBord.create(athlete=query, date=date, testtype=testtype, \
        leftreps=leftreps, rightreps=rightreps, maxforceleft=maxforceleft, \
        maxforceright=maxforceright, maximbal=maximbal, maxtorqueleft=maxtorqueleft, \
        maxtorqueright=maxtorqueright, avgforceleft=avgforceleft, \
        avgforceright=avgforceright, avgimbal=avgimbal, avgtorqueleft=avgtorqueleft, \
        avgtorqueright=avgtorqueright)
        entry.save()

db.close
