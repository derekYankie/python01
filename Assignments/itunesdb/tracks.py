''' Exit
Welcome Joe Carrano from Using Databases with Python

To get credit for this assignment, perform the instructions below and upload your SQLite3 database here: 
Choose File
(Must have a .sqlite suffix)
Submit
You do not need to export or convert the database - simply upload the .sqlite file that your program creates. See the example code for the use of the connect() statement.

Musical Track Database
This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.pythonlearn.com/code/tracks.zip. The ZIP file contains the Library.xml file to be used for this assignment. You can export your own tracks from iTunes and create a database, but for the database that you turn in for this assignment, only use the Library.xml data that is provided.

To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
The expected result of this query on your database is:
Track	Artist	Album	Genre
Chase the Ace	AC/DC	Who Made Who	Rock
D.T.	AC/DC	Who Made Who	Rock
For Those About To Rock (We Salute You)	AC/DC	Who Made Who	Rock
'''


import xml.etree.ElementTree as ET 

import sqlite3

conn = sqlite3.connect('trackdb.sqlite')#open db connection 

cur = conn.cursor()#send commands to DB

#db setup

cur.execute('''
	CREATE TABLE IF NOT EXISTS Artist (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT UNIQUE
		)''')

cur.execute('''
	CREATE TABLE IF NOT	EXISTS Album (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		artist_id INTEGER,
		title TEXT UNIQUE
		)''')

cur.execute('''
	CREATE TABLE IF NOT EXISTS Track(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT UNIQUE,
	album_id INTEGER,
	genre_id INTEGER,
	len INTEGER,
	rating INTEGER,
	count INTEGER
	)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Genre(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT UNIQUE
	)''')


#end db setup 

fname = raw_input('Enter File Name: ')
if(len(fname)<1):fname = 'Library.xml'

def lookup(d, key):
	found = False
	for child in d:
		if found: return child.text 
		if child.tag == 'key' and child.text == key:
			found =  True 
	return None


stuff = ET.parse(fname)

all = stuff.findall('dict/dict/dict') #finding 3rd level dictionaries (where the info we are looking to import lives at)
print 'Dict Count', len(all)
for entry in all:
	if( lookup(entry, 'Track ID') is None ): continue 

	name = lookup(entry, 'Name')
	artist = lookup(entry, 'Artist')
	album = lookup(entry, 'Album')
	genre = lookup(entry, 'Genre')
	count = lookup(entry, 'Play Count')
	rating = lookup(entry, 'Rating')
	length = lookup(entry, 'Total Time')

	if name is None	or artist is None or album is None or genre is None:
		continue

	print name, artist, album, genre, count, rating, length

	cur.execute('''INSERT OR IGNORE INTO Artist(name)
		/*Artist Table is a tuple, Primary key and artisit name*/
		VALUES (?)''', (artist,)
		)
	cur.execute('SELECT id FROM Artist WHERE name = ?',(artist, ))
	artist_id = cur.fetchone()[0] 

	cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
		VALUES(?,?)''', (album, artist_id))

	cur.execute('SELECT id FROM Album WHERE title=?', (album,))
	album_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Genre (name)
		VALUES(?)''', (genre,)
		)
	cur.execute('SELECT id FROM Genre WHERE name=?', (genre,))
	genre_id = cur.fetchone()[0]

	cur.execute(''' INSERT OR REPLACE INTO Track
		(title, album_id, genre_id, len, rating, count)
		VALUES(?,?,?,?,?,?)''',
		(name, album_id, genre_id, length, rating, count))

	conn.commit() 







