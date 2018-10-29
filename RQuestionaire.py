import sqlite3
from peewee import *
from datetime import datetime
import csv
from athlete_db import DataStream
from athlete_db import RQuestionaire
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
        athlete = row[2]
        query = Athlete.get(Athlete.name == athlete)
        date = datetime.strptime(row[1], '%m/%d/%y %H:%M').strftime('%m/%d/%Y %H:%M')
        fatigue = int(row[3])
        musclesoreness = int(row[4])
        sleepquality = int(row[5])
        stress = int(row[6])
        wellnesssum = int(row[10])
        entry = RQuestionaire.create(athlete=query, date=date, fatigue=fatigue, \
        musclesoreness=musclesoreness, sleepquality=sleepquality, stress=stress, \
        wellnesssum=wellnesssum)
        entry.save()

db.close
