import sqlite3
from peewee import *
from datetime import datetime
import csv
from athlete_db import DataStream
from athlete_db import WBBTesting
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
        athlete = row[0]
        query = Athlete.get(Athlete.name == athlete)
        date = row[1]
        tt = row[2]
        hand = int(row[3])
        ohsq = int(row[4])
        hsr = int(row[5])
        hsl = int(row[6])
        illr = row[7]
        illl = row[8]
        smr = row[9]
        sml = row[10]
        impr = int(row[11])
        impl = row[12]
        aslrr = row[13]
        aslrl = row[14]
        tspu = row[15]
        pressup = row[16]
        rsr = row[17]
        rsl = row[18]
        rockback = row[19]
        fmscomp = row[20]
        dflexr = row[21]
        dflxl = row[22]
        ll = row[23]
        antr = row[24]
        antl = row[25]
        pmr = row[26]
        pml = row[27]
        plr = row[28]
        pll = row[29]
        lqrcomp = row[30]
        lqlcomp = row[31]
        antllr = row[32]
        antlll = row[33]
        pmllr = row[34]
        pmlll = row[35]
        plllr = row[36]
        pllll = row[37]
        al = row[38]
        medr = row[39]
        medl = row[40]
        ilr = row[41]
        ill = row[42]
        slr = row[43]
        sll = row[44]
        uqrcomp = row[45]
        uqlcomp = row[46]
        medalr = row[47]
        medall = row[48]
        ilalr = row[49]
        ilall = row[50]
        slalr = row[51]
        slall = row[52]
        less = row[53]
        entry = RQuestionaire.create(athlete=query, date=date, tt=tt, hand=hand, \
        ohsq=ohsq, hsr=hsr, hsl=hsl, illr=illr, illl=illl, smr=smr, sml=sml, \
        impr=impr, impl=impl, aslrr=aslrr, aslrl=aslrl, tspu=tspu, pressup=pressup \
        rsr=rsr, rsl=rsl, rockback=rockback, fmscomp=fmscomp, dflexr=dflexr, \
        dflxl=dflxl, ll=ll, antr=antr, antl=antl, pmllr=pmllr, pmlll=pmlll, \
        plllr=plllr, pllll=pllll, al=al, medr=medr, medl=medl, ilr=ilr, ill=ill, \
        slr=slr, sll=sll, uqrcomp=uqrcomp, uqlcomp=uqlcomp, medalr=medalr, \
        medall=medall, ilalr=ilalr, ilall=ilall, slalr=slalr, slall=slall, less=less)
        entry.save()

db.close
