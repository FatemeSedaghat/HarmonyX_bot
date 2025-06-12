import mysql.connector
from config import db_config
from DML import insert_artist_data,insert_album_data


def get_known_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT CID FROM USER"
    cursor.execute(SQL_Query)
    result = cursor.fetchall()
    conn.close()
    return [i['CID'] for i in result]

def get_user_data(CID):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM USER WHERE CID=%s"
    cursor.execute(SQL_Query, (CID,))
    result = cursor.fetchall()
    conn.close()
    return result[0]





def get_artist_id(artist_name):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ID FROM ARTIST WHERE NAME=%s"
    cursor.execute(SQL_Query, (artist_name,))
    result = cursor.fetchall()
    conn.close()
    if result:
        return result[0]['ID']
    else:
        return insert_artist_data(artist_name) 
    

def get_album_id(album_name,artist_id,album_genre):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ID FROM ALBUM WHERE ALBUM_NAME=%s AND ARTIST_ID=%s"
    cursor.execute(SQL_Query, (album_name,artist_id))
    result = cursor.fetchall()
    conn.close()
    if result:
        return result[0]['ID']
    else:
        return insert_album_data(album_name,artist_id,album_genre) 


def newest(lang,page):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    start = (page-1)*5
    SQL_Query = "SELECT *FROM SONG WHERE RELEASE_YEAR=2025 AND LANG=%s LIMIT 5 OFFSET %s"
    cursor.execute(SQL_Query,(lang,start))
    songs = cursor.fetchall()
    conn.close()
    return songs

def get_jenre(jenre,page):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    start = (page-1)*5
    SQL_Query = "SELECT *FROM SONG WHERE GENRE=%s LIMIT 5 OFFSET %s"
    cursor.execute(SQL_Query,(jenre,start))
    songs = cursor.fetchall()
    conn.close()
    return songs


def get_following(USER_CID,ARTIST_ID):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ID FROM FOLLOW WHERE USER_CID=%s AND ARTIST_ID=%s"
    cursor.execute(SQL_Query, (USER_CID,ARTIST_ID))
    result = cursor.fetchall()
    conn.close()
    if result:
        return True
    else:
        return False


def get_favourite(USER_CID,SONG_ID):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ID FROM favorite WHERE USER_CID=%s AND SONG_ID=%s"
    cursor.execute(SQL_Query, (USER_CID,SONG_ID))
    result = cursor.fetchall()
    conn.close()
    if result:
        return True
    else:
        return False






def get_artist_name(artist_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT NAME FROM ARTIST WHERE ID=%s"
    cursor.execute(SQL_Query,(artist_id,))
    artist_name = cursor.fetchall()
    conn.close()
    return artist_name[0]['NAME']

    
def get_song_link(artist_id,song_name):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT MESSAGE_LINK FROM SONG WHERE ARTIST_ID=%s AND SONG_NAME=%s"
    cursor.execute(SQL_Query,(artist_id,song_name))
    message_link = cursor.fetchall()
    conn.close()
    return message_link[0]['MESSAGE_LINK']

def get_song_lyric(artist_id,song_name):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT LYRIC FROM SONG WHERE ARTIST_ID=%s AND SONG_NAME=%s"
    cursor.execute(SQL_Query,(artist_id,song_name))
    lyric = cursor.fetchall()
    conn.close()
    return lyric[0]['LYRIC']

def get_song_id(artist_id,song_name):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ID FROM SONG WHERE ARTIST_ID=%s AND SONG_NAME=%s"
    cursor.execute(SQL_Query,(artist_id,song_name))
    song_id = cursor.fetchall()
    conn.close()
    return song_id[0]['ID']
 
def get_artist_id_from_song(song_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ARTIST_ID FROM SONG WHERE ID=%s"
    cursor.execute(SQL_Query,(song_id,))
    artist_id = cursor.fetchall()
    conn.close()
    return artist_id[0]['ARTIST_ID']
 







def show_following_list(USER_CID):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ARTIST_ID FROM FOLLOW WHERE USER_CID=%s"
    cursor.execute(SQL_Query,(USER_CID))
    artist_id = cursor.fetchall()
    conn.close()
    return artist_id

def remove_from_follow(USER_CID,artist_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = 'DELETE FROM FOLLOW WHERE USER_CID=%s AND ARTIST_ID=%s'
    cursor.execute(SQL_Query,(USER_CID,artist_id))
    conn.commit()
    conn.close()


def check_in_follow_list(USER_CID,artist_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = 'SELECT *FROM FOLLOW WHERE USER_CID=%s AND ARTIST_ID=%s'
    cursor.execute(SQL_Query,(USER_CID,artist_id))
    result = cursor.fetchall()
    conn.close()
    if result:
        return True 
    else:
        return False

    
def show_favourite_list(USER_CID):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT SONG_ID FROM FAVORITE WHERE USER_CID=%s"
    cursor.execute(SQL_Query,(USER_CID))
    song_id = cursor.fetchall()
    conn.close()
    return song_id

def get_song_name(song_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT SONG_NAME FROM SONG WHERE ID=%s"
    cursor.execute(SQL_Query,(song_id,))
    song_name = cursor.fetchall()
    conn.close()
    return song_name[0]['SONG_NAME']


def remove_from_favourite(USER_CID,song_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = 'DELETE FROM FAVORITE WHERE USER_CID=%s AND SONG_ID=%s'
    cursor.execute(SQL_Query,(USER_CID,song_id))
    conn.commit()
    conn.close()

def show_user_playlist(USER_CID):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT PLAYLIST_NAME FROM PLAYLIST WHERE USER_CID=%s"
    cursor.execute(SQL_Query,(USER_CID))
    playlist_name = cursor.fetchall()
    conn.close()
    return playlist_name

def check_existing_playlist(playlist_name,cid):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ID FROM PLAYLIST WHERE PLAYLIST_NAME=%s AND USER_CID=%s"
    cursor.execute(SQL_Query,(playlist_name,cid))
    result = cursor.fetchall()
    conn.close()
    if result:
        return result[0]['ID']
    else:
        return False


def get_songs_ids_from_playlist_song(playlist_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT SONG_ID FROM PLAYLIST_SONG WHERE PLAYLIST_ID=%s"
    cursor.execute(SQL_Query,(playlist_id))
    song_id = cursor.fetchall()
    conn.close()
    return song_id







def get_playlist_id(USER_CID,PLAYLIST_NAME):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ID FROM PLAYLIST WHERE USER_CID=%s AND PLAYLIST_NAME=%s"
    cursor.execute(SQL_Query,(USER_CID,PLAYLIST_NAME))
    playlist_id = cursor.fetchall()
    conn.close()
    return playlist_id[0]['ID']



def get_playlist_songs(PLAYLIST_ID):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = 'SELECT SONG_ID FROM PLAYLIST_SONG WHERE PLAYLIST_ID=%s' 
    cursor.execute(SQL_Query,(PLAYLIST_ID,))
    song_ids = [row[0] for row in cursor.fetchall()]
    if not song_ids:
        return[]
    placeholders= ','.join(['%s']*len(song_ids))
    query = f'SELECT SONG_NAME,MESSAGE_LINK FROM SONG WHERE ID IN ({placeholders})'
    cursor.execute(query,tuple(song_ids))
    results = cursor.fetchall()
    return results






def remove_playlist_song(PLAYLIST_ID):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = 'DELETE FROM PLAYLIST_SONG WHERE PLAYLIST_ID=%s'
    cursor.execute(SQL_Query,(PLAYLIST_ID))
    conn.commit()
    conn.close()

def remove_from_playlist(USER_CID,PLAYLIST_NAME):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    SQL_Query = 'DELETE FROM PLAYLIST WHERE USER_CID=%s AND PLAYLIST_NAME=%s'
    cursor.execute(SQL_Query,(USER_CID,PLAYLIST_NAME))
    conn.commit()
    conn.close()


