import sqlite3
from peewee import *
from datetime import datetime
import csv
from athlete_db import DataStream
from athlete_db import TQuestionaire
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
        athlete = row[1]
        query = Athlete.get(Athlete.name == athlete)
        date = datetime.strptime(row[0], '%m/%d/%Y %H:%M').strftime('%m/%d/%Y %H:%M')
        sessiontype = row[2]
        sessionduration = int(row[3])
        breathlessness = int(row[4])
        lowerbodyload = int(row[5])
        upperbodyload = int(row[6])
        overallexertion = int(row[7])
        entry = TQuestionaire.create(athlete=query, date=date, \
        sessiontype=sessiontype, sessionduration=sessionduration, \
        breathlessness=breathlessness, lowerbodyload=lowerbodyload, \
        upperbodyload=upperbodyload, overallexertion=overallexertion)
        entry.save()

db.close
