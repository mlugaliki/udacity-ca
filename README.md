##### Data modelling project

##### Introduction
Sparkify is a startup that runs a music streaming app. The Sparkify analytics team wants to analyse stream data on their app in order to understand what their listeners are listening to.<br/>
This project aims to process the stream data currently in CSV files and store it in a non relational database(Cassandra) that will allow the analytics team to run queries that will enable them to understand how the app is being used.<br/>
In this project, we will extract all the data and model it in such a way that we will avoid duplication of data across different tables and make it easy to understand.<br/>

##### Environment requirements
- Install python3
- Install cassandra
- Install project dependencies by running the command below from the project dir
```python3
    pip install -r requirements.txt
```

##### How to run the project
- Create cassandra database and tables
```python
    python create_tables.py
```
- Process streaming data from csv files and save in cassandra database
```python
    python main.py
```

##### Verify data
verify.py will run specific queries that will query cassandra database to answer the following
```python
    python verify.py
```
- Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4
```sql
    ------------------------------
    Query - SELECT artist,song,length FROM artists WHERE sessionId=338 and itemInSession=4
    ------------------------------
    Row(artist='Faithless', song='Music Matters (Mark Knight Dub)', length=495.30731201171875)
```

- Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
```
    ------------------------------
    SELECT artist,itemInSession,song,firstName,lastname FROM artist_playlist WHERE userId=10 and sessionId=182
    ------------------------------
    Row(artist='Down To The Bone', iteminsession=0, song="Keep On Keepin' On", firstname='Sylvie', lastname='Cruz')
    Row(artist='Three Drives', iteminsession=1, song='Greece 2000', firstname='Sylvie', lastname='Cruz')
    Row(artist='Sebastien Tellier', iteminsession=2, song='Kilometer', firstname='Sylvie', lastname='Cruz')
    Row(artist='Lonnie Gordon', iteminsession=3, song='Catch You Baby (Steve Pitron & Max Sanna Radio Edit)', firstname='Sylvie', lastname='Cruz')
```

- Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'
```sql
    ------------------------------
    SELECT firstName,lastName FROM popular_music WHERE song='All Hands Against His Own'
    ------------------------------
    Row(firstname='Jacqueline', lastname='Lynch')
    Row(firstname='Sara', lastname='Johnson')
    Row(firstname='Tegan', lastname='Levine')
```