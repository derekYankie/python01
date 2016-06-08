#MusicalTrack
import sqlite3

conn = sqlite3.connect('musical_track.sqlite')

cur = conn.cursor()
print "Opened database successfully";

#Create tables
cur.execute('''CREATE TABLE Artist (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name    TEXT UNIQUE
)
	''')

cur.execute('''CREATE TABLE Genre (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name    TEXT UNIQUE
)''')

cur.execute('''CREATE TABLE Album (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id  INTEGER,
	title   TEXT UNIQUE
);''')

#Set primary key for the Table Track
cur.execute('''
	CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
    PRIMARY KEY (album_id,genre_id)
)''')


#end of database setup

#Accept xml file from user
fname = raw_input('Enter File Name: ')
if(len(fname)<1):fname = 'Library.xml'

def lookup(d, key):
	found = False
	for child in d:
		if found: return child.text 
		if child.tag == 'key' and child.text == key:
			found =  True 
	return None
---------------------------------
# Save/commit the changes
conn.commit()

