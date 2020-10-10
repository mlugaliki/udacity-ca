# DROP Keyspace

sparkify_keyspace_drop = "DROP KEYSPACE IF EXISTS sparkify;"

# CREATE Keyspace
sparkify_keyspace_create = ("""
CREATE KEYSPACE IF NOT EXISTS sparkify WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
""")

# CREATE TABLES
artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(artist varchar, firstName varchar, gender varchar, itemInSession int,
lastName varchar,length float,level varchar, location varchar,sessionId int,song varchar, userId int, 
PRIMARY KEY(sessionId,itemInSession));
""")

play_list_create = ("""
CREATE TABLE IF NOT EXISTS artist_playlist(artist varchar, firstName varchar, gender varchar, itemInSession int,
lastName varchar,length float,level varchar, location varchar,sessionId int,song varchar, userId int,
PRIMARY KEY((userId,sessionId), itemInSession)) WITH CLUSTERING ORDER BY (itemInSession ASC);
""")

popular_music_create = ("""
CREATE TABLE IF NOT EXISTS popular_music(artist varchar, firstName varchar, gender varchar, itemInSession int,
lastName varchar,length float,level varchar, location varchar,sessionId int,song varchar, userId int,
PRIMARY KEY((song), firstName,lastName));
""")

# INSERT RECORDS

insert_popular_music = ("""
INSERT INTO popular_music(artist,firstName,gender,itemInSession,lastName,length,level,location,sessionId,song,userId)
 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
""")
insert_artist_playlist = ("""
INSERT INTO artist_playlist(artist,firstName,gender,itemInSession,lastName,length,level,location,sessionId,song,userId)
 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
""")
insert_artists = ("""
INSERT INTO artists(artist,firstName,gender,itemInSession,lastName,length,level,location,sessionId,song,userId)
 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
""")

# QUERY LISTS
query1 = "SELECT artist,song,length FROM artists WHERE sessionId=338 and itemInSession=4"
query2 = "SELECT artist,itemInSession,song,firstName,lastname FROM artist_playlist WHERE userId=10 and sessionId=182"
query3 = "SELECT firstName,lastName FROM popular_music WHERE song='All Hands Against His Own'"

select_queries = [query1, query2, query3]
insert_queries = [insert_popular_music, insert_artist_playlist, insert_artists]
create_table_queries = [artist_table_create, play_list_create, popular_music_create]
