import mysql.connector
import logging
logging.basicConfig(filename='DML.log',format='%(asctime)s, %(filename)s, %(levelname)s, %(message)s')
from config import db_config

def insert_user_data(CID, NAME,LAST_NAME='',USERNAME=''):
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    SQL_Query = """INSERT IGNORE INTO USER (CID, NAME,LAST_NAME,USERNAME)
                VALUES (%s,%s,%s,%s)"""
    cursor.execute(SQL_Query, (CID, NAME,LAST_NAME,USERNAME))
    conn.commit()
    conn.close()
    logging.info(f'user data inserted with cid : {CID} succesfully')
    return True





def insert_artist_data(NAME,LAST_NAME=''):
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    SQL_Query = """INSERT IGNORE INTO ARTIST(NAME,LAST_NAME)
                   VALUES (%s,%s)"""
    cursor.execute(SQL_Query,(NAME,LAST_NAME))
    artist_id = cursor.lastrowid
    conn.commit()
    conn.close()
    logging.info(f'artist data inserted with id: {artist_id} succesfully')
    return artist_id


def insert_album_data(ALBUM_NAME,ARTIST_ID,GENRE=''):
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    SQL_Query = ("""INSERT IGNORE INTO ALBUM(ALBUM_NAME,ARTIST_ID,GENRE)
                    VALUES (%s,%s,%s)""")
    cursor.execute(SQL_Query,(ALBUM_NAME,ARTIST_ID,GENRE))
    album_id = cursor.lastrowid
    conn.commit()
    conn.close()
    logging.info(f'album data inserted with id: {album_id} succesfully')
    return album_id


def insert_song_data(SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC='',GENRE='',MESSAGE_LINK='',LANG='',RELEASE_YEAR=''):
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    SQL_Query = """INSERT IGNORE INTO SONG(SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(SQL_Query,(SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR))
    song_id = cursor.lastrowid
    conn.commit()
    conn.close()
    logging.info(f'song data inserted with id: {song_id} succesfully')
    return song_id


def insert_follow_data(USER_CID,ARTIST_ID):
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    SQL_Query = """INSERT IGNORE INTO FOLLOW(USER_CID,ARTIST_ID) VALUES (%s,%s)"""
    cursor.execute(SQL_Query,(USER_CID,ARTIST_ID))
    follow_id = cursor.lastrowid
    conn.commit()
    conn.close()
    logging.info(f'follow table data inserted with id: {follow_id} for user:{USER_CID} succesfully')
    return follow_id




def insert_favorite_data(USER_CID,SONG_ID):
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    SQL_Query = ("""INSERT IGNORE INTO FAVORITE(USER_CID,SONG_ID)
                    VALUES(%s,%s)""")
    cursor.execute(SQL_Query,(USER_CID,SONG_ID))
    favourite_id = cursor.lastrowid
    conn.commit()
    conn.close()
    logging.info(f'favorite table data inserted with id: {favourite_id} for user:{USER_CID} succesfully')
    return favourite_id



def insert_playlist_data(USER_CID,PLAYLIST_NAME):
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    SQL_Query = ("""INSERT IGNORE INTO PLAYLIST(USER_CID,PLAYLIST_NAME)
                    VALUES(%s,%s)""")
    cursor.execute(SQL_Query,(USER_CID,PLAYLIST_NAME))
    playlist_id = cursor.lastrowid
    conn.commit()
    conn.close()
    logging.info(f'playlist table data inserted with id: {playlist_id} for user:{USER_CID} succesfully')
    return playlist_id





def insert_playlist_song_data(PLAYLIST_ID,SONG_ID,USER_CID):
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    SQL_Query = ("""INSERT IGNORE INTO PLAYLIST_SONG(PLAYLIST_ID,SONG_ID)
                    VALUES(%s,%s)""")
    cursor.execute(SQL_Query,(PLAYLIST_ID,SONG_ID))
#    playlist_song_id = cursor.lastrowid
    conn.commit()
    conn.close()
    logging.info(f'playlist_song table data inserted with id:  for user:{USER_CID} succesfully')
    return True







