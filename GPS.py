import sqlite3
from peewee import *
from datetime import datetime
import csv
from athlete_db import DataStream
from athlete_db import GPS
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
        date = datetime.strptime(row[1], '%d/%m/%Y').strftime('%m/%d/%Y')
        playerload = int(row[3])
        avghr = int(row[4])
        hrabove85 = int(row[5])
        impacts = int(row[6])
        distancepermin = int(row[10])
        highspeedrun = int(row[])
        entry = GPS.create(athlete=query, date=date, playerload=playerload, \
        avghr=avghr, hrabove85=hrabove85, impacts=impacts, distancepermin=distancepermin, \
        highspeedrun=highspeedrun)
        entry.save()

db.close
