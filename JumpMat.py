import sqlite3
from peewee import *
from datetime import date
import csv
from athlete_db import DataStream
from athlete_db import JumpMat
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
        date = row[1]
        jumpheight = int(row[3])
        contacttime = int(row[4])
        entry = JumpMat.create(athlete=query, date=date, jumpheight=jumpheight, \
        contacttime=contacttime)
        entry.save()

db.close
