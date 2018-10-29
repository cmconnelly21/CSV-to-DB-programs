import sqlite3
from peewee import *
from datetime import datetime
import csv
from athlete_db import DataStream
from athlete_db import FitFor90
from athlete_db import Athlete
import argparse


db = SqliteDatabase('athletes.db')

db.connect('athletes.db')

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
args = parser.parse_args()

for i in args.file:
    next(i)
    reader = csv.reader(i, delimiter=',')
    for row in reader:
        athlete = row[3]+" "+row[2]
        query = Athlete.get(Athlete.name == athlete)
        date = datetime.strptime(row[0]+" "+row[1], '%Y-%m-%d %H:%M %p %Z').strftime('%m/%d/%Y %H:%M')
        rpe = int(row[4])
        duration = int(row[5])
        load = int(row[6])
        category = row[7]
        type = row[8]
        entry = FitFor90.create(athlete=query, date=date, rpe=rpe,
        duration=duration, load=load, category=category, type=type)
        entry.save()

db.close
