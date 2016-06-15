#MusicalTrack

import xml.etree.ElementTree as ET 

import sqlite3

conn = sqlite3.connect('musical_track.sqlite')

cur = conn.cursor()

#Empty tables befor each run
cur.execute('''
DROP TABLE IF EXISTS Artist''')

cur.execute('''
DROP TABLE IF EXISTS Genre''')

cur.execute('''
DROP TABLE IF EXISTS Album''')

cur.execute('''
DROP TABLE IF EXISTS Track''')

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
#Parse the file into  xml
	stuff = ET.parse(fname)

all = stuff.findall('dict/dict/dict') #finding 3rd level dictionaries (where the info we are looking to import lives at)
print 'Dict Count', len(all)
for entry in all:
	if( lookup(entry, 'Track ID') is None ): continue 

	name = lookup(entry, 'Name')
	artist = lookup(entry, 'Artist')
	album = lookup(entry, 'Album')
	genre = lookup(entry, 'Genre')

	cur.execute('SELECT id FROM Artist WHERE name = ?',(artist, ))
	artist_id = cur.fetchone()[0] 

	cur.execute('''INSERT OR IGNORE INTO Genre (name)
		VALUES(?)''', (genre,)
		)
	cur.execute('SELECT id FROM Genre WHERE name=?', (genre,))
	genre_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
		VALUES(?,?)''', (album, artist_id))

	cur.execute('SELECT id FROM Album WHERE title=?', (album,))
	album_id = cur.fetchone()[0]

	cur.execute(''' INSERT OR REPLACE INTO Track
		(title, album_id, genre_id)
		VALUES(?,?,?)''',
		(name, album_id, genre_id))

	cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')


	
#---------------------------------
# Save/commit the changes
conn.commit()

