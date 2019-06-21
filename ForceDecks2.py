import sqlite3
from peewee import *
from datetime import datetime
import csv
from athlete_db import DataStream
from athlete_db import ForceDecks2
from athlete_db import Athlete
import itertools
import argparse


db = SqliteDatabase('athletes.db')

db.connect('athletes.db')

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
args = parser.parse_args()

for i in args.file:
    for row in itertools.islice(csv.reader(i, delimiter=','), 9, None):
        #header
        athlete = row[0]
        query = Athlete.get(Athlete.name == athlete)
        testtype = row[1]
        date = row[2]
        for i in range(4,7):
            if row[i] is not '':
                #trials
                trialnum = i-3
                rsi = row[i] #1
                si = row[i+6] #2
                jumpheight = row[i+12] #3
                activestiff = row[i+18] #4
                activestiffindex = row[i+24] #5
                conimpulse= row[i+30] #6
                conmeanforce = row[i+36] #7
                conmeanpowerbw = row[i+42] #8
                conmeanpower = row[i+48] #9
                conpeakvel = row[i+54] #10
                contacttime = row[i+60] #11
                cmdepth = row[i+66] #12
                dropheight = row[i+72] #13
                droplanding = row[i+78] #14
                eccconforceratio = row[i+84] #15
                eccimp = row[i+90] #16
                eccmeanforce = row[i+96] #17
                efectivedrop = row[i+102] #18
                flighttime = row[i+108] #19
                forcezerovel = row[i+114] #20
                starttopeakpwr = row[i+144] #25
                peakdriveforce = row[i+150] #26
                peaklandforce = row[i+156] #27
                peakpowerbw = row[162] #28
                peakpower = row[i+168] #29
                positiveimp = row[i+174] #30
                startconphase = row[i+180] #31
                velattakeoff = row[i+192] #33
                contacttrough = row[i+198] #34
                jhtolandrfd = row[i+204] #35
                jhtopeaklandforce = row[i+210] #36
                landnetpeak = row[i+216] #37
                landingrfd = row[i+222] #38
                meanlandaccel = row[i+228] #39
                meanlandpwr = row[i+234] #40
                meanlandvel = row[i+240] #41
                passivestiff = row[i+246] #42
                passivestiffindex = row[i+252] #43
                peakimpactforce = row[i+258] #44
                peaklandaccel = row[i+264] #45
                peaktakeoffaccel = row[i+288] #49
                entry = ForceDecks.create(athlete=query, date=date, \
                testtype=testtype, trialnum=trialnum, rsi=rsi, si=si,  \
                jumpheight=jumpheight, activestiff=activestiff, \
                activestiffindex=activestiffindex, conimpulse=conimpulse, \
                conmeanforce=conmeanforce, conmeanpowerbw=conmeanpowerbw, \
                conmeanpower=conmeanpower, conpeakvel=conpeakvel, \
                contacttime=contacttime, cmdepth=cmdepth, dropheight=dropheight, \
                droplanding=droplanding, eccconforceratio=eccconforceratio, \
                eccimp=eccimp, eccmeanforce=eccmeanforce, \
                efectivedrop=efectivedrop, flighttime=flighttime, \
                forcezerovel=forcezerovel, starttopeakpwr=starttopeakpwr, \
                peakdriveforce=peakdriveforce, peaklandforce=peaklandforce, \
                peakpowerbw=peakpowerbw, peakpower=peakpower, \
                positiveimp=positiveimp, startconphase=startconphase, \
                velattakeoff=velattakeoff, contacttrough=contacttrough, \
                jhtolandrfd=jhtolandrfd, jhtopeaklandforce=jhtopeaklandforce, \
                landnetpeak=landnetpeak, landingrfd=landingrfd, \
                meanlandaccel=meanlandaccel, meanlandpwr=meanlandpwr, \
                meanlandvel=meanlandvel, passivestiff=passivestiff, \
                passivestiffindex=passivestiffindex, peakimpactforce=peakimpactforce, \
                peaklandaccel=peaklandaccel, peaktakeoffaccel=peaktakeoffaccel)
                entry.save()

db.close
