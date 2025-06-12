import mysql.connector
from config import db_config


def create_database(database_name):
    conn = mysql.connector.connection.MySQLConnection(host=db_config["host"], user=db_config["user"], password=db_config["password"])
    cursor = conn.cursor()
    cursor.execute(f'DROP DATABASE IF EXISTS {database_name}')
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
    conn.commit()
    conn.close()
    
   



def create_table_user():
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE USER(
                        CID              BIGINT UNSIGNED NOT NULL PRIMARY KEY,
                        NAME             VARCHAR(100) NOT NULL,
                        LAST_NAME        VARCHAR(100),
                        USERNAME         VARCHAR(100),
                        REGISTER_DATE    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        LAST_UPDATE      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)
                   """)
    conn.commit()
    conn.close()
   

def create_table_artist():
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE ARTIST(
                        ID                   INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        NAME                 VARCHAR(255) NOT NULL,
                        LAST_NAME            VARCHAR(100),
                        REGISTER_DATE        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        LAST_UPDATE          TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)
                   
                   """)
    conn.commit()
    conn.close()
    





def create_table_album():
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    cursor.execute(""" 
                   CREATE TABLE ALBUM(
	                    ID                INT UNSIGNED  NOT NULL AUTO_INCREMENT PRIMARY KEY, 
		                ALBUM_NAME        VARCHAR(100) NOT NULL, 
		                ARTIST_ID         INT UNSIGNED NOT NULL, 
		                GENRE             VARCHAR(50) NOT NULL, 
                        REGISTER_DATE     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        LAST_UPDATE       TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                        FOREIGN KEY (ARTIST_ID) REFERENCES ARTIST(ID))
  
                    """)
    conn.commit()
    conn.close()




def create_table_song():
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE SONG(
                        ID                  INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        SONG_NAME           VARCHAR(100) NOT NULL,
                        ARTIST_ID           INT UNSIGNED NOT NULL,
                        ALBUM_ID            INT UNSIGNED  NOT NULL,
                        LYRIC               TEXT,
                        GENRE               VARCHAR(100) NOT NULL,
                        MESSAGE_LINK        VARCHAR(255),
                        LANG                VARCHAR(50),
                        RELEASE_YEAR        VARCHAR(100),
                        REGISTER_DATE       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        LAST_UPDATE         TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                        FOREIGN KEY(ARTIST_ID) REFERENCES ARTIST(ID),
                        FOREIGN KEY(ALBUM_ID) REFERENCES ALBUM(ID))
                   
                """)
    conn.commit()
    conn.close()
   
   
    

def create_table_playlist():
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE PLAYLIST(
                   ID 		            INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
 		           PLAYLIST_NAME        VARCHAR(100) NOT NULL,
 		           USER_CID             BIGINT UNSIGNED NOT NULL, 
   		           REGISTER_DATE        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   LAST_UPDATE          TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
		           FOREIGN KEY(USER_CID) REFERENCES USER(CID),
                   UNIQUE (USER_CID, PLAYLIST_NAME))


                    """)
    conn.commit()
    conn.close()
 


def create_table_playlist_song():
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE PLAYLIST_SONG(
 		           PLAYLIST_ID          INT UNSIGNED NOT NULL,
 		           SONG_ID              INT UNSIGNED NOT NULL,
                   PRIMARY KEY (PLAYLIST_ID,SONG_ID),
 		           FOREIGN KEY (PLAYLIST_ID) REFERENCES PLAYLIST(ID), 
		           FOREIGN KEY(SONG_ID) REFERENCES SONG(ID))
                    
                   
                   """)
    conn.commit()
    conn.close()
    

def create_table_favorite():
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE FAVORITE(
		           ID                   INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	               USER_CID             BIGINT UNSIGNED NOT NULL,
		           SONG_ID              INT UNSIGNED NOT NULL,
		           REGISTER_DATE        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   LAST_UPDATE          TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
		           FOREIGN KEY (USER_CID) REFERENCES USER(CID),
		           FOREIGN KEY(SONG_ID) REFERENCES SONG(ID))
                   
                   
                   """)
    conn.commit()
    conn.close()
    

def create_table_follow():
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE FOLLOW(
                   ID                   INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	               USER_CID             BIGINT UNSIGNED NOT NULL,
 		           ARTIST_ID            INT UNSIGNED NOT NULL, 
                   REGISTER_DATE        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   LAST_UPDATE          TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
		           FOREIGN KEY(USER_CID) REFERENCES USER(CID),
                   FOREIGN KEY(ARTIST_ID) REFERENCES ARTIST(ID)
		           
)
""")
    conn.commit()
    conn.close()
    



def insert_into_artist_table():
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (1,'Chase Atlantic')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (2,'Billie Eilish')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (3,'Bad Omens')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (4,'The Neighburhood')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (5,'Lana Del Rey')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (6,'Halsey')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (7,'Conan Gray')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (8,'The Weekend')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (9,'Bruno Mars')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (10,'Stray Kids')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (11,'NF')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (12,'Zayn')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (13,'Harry Styles')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (14,'Taylor Swift')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (15,'Selena Gommez')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (16,'Ariana Grande')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (17,'5 Seconds Of Summer')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (18,'Mohsen Chavoshi')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (19,'Mehrad Hidden')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (20,'Shadmehr Aghili')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (21,'Julia Michaels')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (22,'G_Eazy')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (23,'Tom Odell')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (24,'Calum Scott')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (25,'Green Day')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (26,'Sogand')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (27,'Ehaam')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (28,'Sahar')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (29,'Baran')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (30,'25Band')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (31,'Haamim')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (32,'Kendrick Lamar')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (33,'Eminem')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (34,'K3NT4')""")
    cursor.execute("""INSERT INTO ARTIST(ID,NAME) VALUES (35,'MXZI')""")








    conn.commit()
    conn.close()

def insert_into_album_table():
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (1,'Hit me hard and soft',2,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (2,'Chase Atlantic',1,'rock')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (3,'The death of peace of mind',3,'rock')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (4,'The neibourhood',4,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (5,'Born to die',5,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (6,'Badlands',6,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (7,'Superache',7,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (8,'After hours',8,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (9,'24k magic',9,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (10,'5-Star',10,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (11,'Hope',11,'rap')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (12,'Mind of mine',12,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (13,'Harry styles',13,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (14,'Reputation',14,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (15,'Rare',15,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (16,'Dangerous woman',16,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (17,'Youngblood',17,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (18,'Abraham',18,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (19,'Tonel Vol 1',19,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (20,'Par-e-Parvaz',20,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (21,'Second Self',21,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (22,"When It's Dark Out",22,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (23,"A Wonderful life",23,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (24,"Avenoir",24,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (25,"The Saviors",25,'rock')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (26,"No Album",26,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (27,"No Album",27,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (28,"No Album",28,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (29,"No Album",29,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (30,"No Album",30,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (31,"No Album",31,'pop')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (32,"Damn",32,'rap')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (33,"No Album",33,'rap')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (34,"No Album",32,'rap')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (35,"No Album",34,'fonk')""")
    cursor.execute("""INSERT INTO ALBUM(ID,ALBUM_NAME,ARTIST_ID,GENRE) VALUES (36,"No Album",35,'fonk')""")


    conn.commit()
    conn.close()


def insert_into_song_table():
    conn = mysql.connector.connection.MySQLConnection(**db_config)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(1,'Cassie',1,2,'[Verse 1: Mitchel Cave]
The writing''s on the wall right now
And I''m way too involved somehow
Shit, I probably tore her heart right out
At least that''s how it feels right now (Yeah)

[Pre-Chorus: Mitchel Cave]
But we''re holdin'' on, we''re holdin'' on
We say some words, we land them wrong
Say what you need, then move along
She said, "It''s seven in the morning, what''d you take me for?"

[Chorus: Mitchel Cave]
Cassie''s been waiting too long
The drug in her veins is too strong
She fell in love with the medicine she''s on
Yeah, in a matter of minutes, her mind''s gone
Cassie''s been waiting too long
Cassie''s been waiting too long

[Verse 2: Christian Anthony]
It''s kinda hard to deal out there
There''s way too many feels out there
She said, "Not if you''re a millionaire"
And I swear I fell in love right there (Yeah)

[Pre-Chorus: Christian Anthony]
We take it off, we take it all
She''ll get me high, but at a cost
I see it in her eyes, that girl is lost
But Cassie, if you stay with me, I''ll never stop

[Chorus: Mitchel Cave]
Cassie''s been waiting too long
The drug in her veins is too strong
She fell in love with the medicine she''s on
Yeah, in a matter of minutes, her mind''s gone
Cassie''s been waiting too long
Cassie''s been waiting too long

[Outro: Mitchel Cave]
She built a world with her own two hands
Well, just give that a thought
And she don''t ever want to make no plans
Cause she don''t go outside no more
She left a dent in my heart as she drove with her car into my life, though
She tilts her head to the side, what a night, yeah
But Cassie, don''t you overdose','pop','CQACAgQAAxkBAAITq2hH4g4aZX0e7MQWaIoz8PmiHpj8AAKDCAACnKsRUvE6X_fYmtHRNgQ','en',2017)""")


    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(2,'The Walls',1,2,'[Verse 1: Mitchel Cave]
Sorry if I look a little lost
I just keep my head up in the clouds, yeah, yeah, yeah       
Give it to her however she wants
Told her that she gotta keep it down though, yeah, yeah      
I could do this shit like every night
Grab your friends and pull them to the side, yeah, yeah, yeah
Never been so busy in my life
Told me that she wanna do it twice now, yeah, yeah

[Pre-Chorus: Mitchel Cave]
Honestly, she needs a little lovin''
Fuck it now I''m gettin'' off the subject, yeah, yeah
I just think she needs a little something
Or someone to get into heavy drugs with, yeah, yeah
Yeah, yeah, yeah

[Chorus: Mitchel Cave]
Everybody''s leaning on the walls
I don''t think they''re ready for the fall (yeah, yeah, yeah)
Cut a little, now she wanting more
Told her that I gotta make some calls (yeah, yeah, yeah)
This just might be one hell of a night (yeah, yeah, yeah)
Come with me we gotta go outside (yeah, yeah, yeah)
Everybody''s hitting on the walls
Fuck it, I might take a little more now, yeah, yeah

[Verse 2: Mitchel Cave]
Life is getting busy everyday
Take a little more to stay awake now, yeah, yeah
She been busy digging out her grave
Telling me that I gotta behave now, yeah, yeah

[Pre-Chorus: Mitchel Cave]
Honestly she needs a little lovin''
Fuck it now I''m gettin'' off the subject, yeah, yeah
I just think she needs a little something
Or someone to get into heavy drugs with, yeah, yeah

[Chorus: Mitchel Cave]
Everybody''s leaning on the walls
I don''t think they''re ready for the fall (yeah, yeah, yeah)
Cut a little, now she wanting more
Told her that I gotta make some calls (yeah, yeah, yeah)
This just might be one hell of a night (yeah, yeah, yeah)
Come with me we gotta go outside (yeah, yeah, yeah)
Everybody''s leaning on the walls
Fuck it, I might take a little more now, yeah, yeah, yeah

Yeah, yeah, yeah, yeah
This just might be one hell of a night (yeah, yeah, yeah)
Come with me we gotta go outside (yeah, yeah, yeah)
Everybody''s hitting on the walls
Fuck it, I might take a little more now','pop','CQACAgQAAxkBAAIT-WhINSCMS8FYvnTSbbYSldaXtF3hAAKfCgACTaYpUlO6W0BJ6qSbNgQ','en',2017)""") 
    

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES (3,'Swim',1,2,'[Verse 1: Mitchel Cave]
Yeah
I bet you feel it now, baby
Especially since we''ve only known each other one day
But, I''ve gotta work shit out, baby
I''m exorcising demons, got ''em running ''round the block now

[Pre-Chorus: Mitchel Cave]
Location drop, now
Pedal to the floor like you running from the cops now
Oh, what a cop out
You picked a dance with the devil and you lucked out (Yeah)

[Chorus: Mitchel Cave]
The water''s getting colder, let me in your ocean, swim
Out in California, I''ve been forward stroking, swim
So hard to ignore ya'', ''specially when I''m smoking, swim
World is on my shoulders, keep your body open, swim
I''m swimming, I''m swimming, I''m swimming, yeah
I''m swimming, I''m swimming, I''m swimming, yeah
Out in California, I''ve been forward stroking, swim
So hard to ignore ya'', keep your body open, swim

[Verse 2: Mitchel Cave]
Pop a couple pills in the daytime, ah
Heard you got a friend, what her head like?, ah
Probably should''ve fucked on the first night, ah
Now I gotta wait for the green light, ah
I don''t wanna wait for no green light, ah
Narcolepsy got me feeling stage fright, ah
Luckily I fly at insane heights
Luckily, luckily, luckily, ya

[Pre-Chorus: Mitchel Cave]
Location drop, now
Pedal to the floor like you running from the cops now
Oh, what a cop out
You picked a dance with the devil and you lucked out (Yeah)

[Chorus: Mitchel Cave]
The water''s getting colder, let me in your ocean, swim
Out in California, I''ve been forward stroking, swim
So hard to ignore ya'', ''specially when I''m smoking, swim
World is on my shoulders, keep your body open, swim
I''m swimming, I''m swimming, I''m swimming, yeah
I''m swimming, I''m swimming, I''m swimming, yeah
Out in California, I''ve been forward stroking, swim
So hard to ignore ya'', keep your body open, swim

[Bridge: Mitchel Cave]
Swim, push the water to the edge and watch it drip
Check your footing, don''t get caught up in the rip, no
I know I said I''d call, I never did, no
Swim, swim now
I can take you even though I''ve never been there
The tide has currently been thrashing around me again and again, yeah
And I''ve been drowning for a minute, your body keeps pulling me in, girl

[Chorus: Mitchel Cave]
The water''s getting colder, let me in your ocean, swim
Out in California, I''ve been forward stroking, swim
So hard to ignore ya'', ''specially when I''m smoking, swim
World is on my shoulders, keep your body open, swim
I''m swimming, I''m swimming, I''m swimming, yeah
I''m swimming, I''m swimming, I''m swimming, yeah
Out in California, I''ve been forward stroking, swim
So hard to ignore ya'', keep your body open, swim','pop','CQACAgQAAxkBAAIUNGhIPc6eEFtBnrjYLg-74THStw_pAALJCAACvP4YUhFBm6IQPbZnNgQ','en',2017)""")
    

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES (4,'WILDFLOWER',2,1,"[Verse 1]
Things fall apart
And time breaks your heart
I wasn't there, but I know
She was your girl
You showed her the world
You fell out of love and you both let go

[Pre-Chorus]
She was cryin' on my shoulder
All I could do was hold her
Only made us closer until July
Now I know that you love me
You don't need to remind me
I should put it all behind me, shouldn't I?

[Chorus]
But I see her in the back of my mind all the time
Like a fever, like I'm burning alive, like a sign
Did I cross the line?
(Mm) Hmm

[Verse 2]
Well, good things don't last
And life moves so fast
I'd never ask who was better
'Cause she couldn't be
More different from me
Happy and free in leather

[Pre-Chorus]
And I know that you love me
You don't need to remind me
Wanna put it all behind me, but baby

[Chorus]
I see her in the back of my mind all the time
Feels like a fever, like I'm burning alive, like a sign
Did I cross the line?

[Verse 3]
You say no one knows you so well (Oh)
But every time you touch me, I just wonder how she felt
Valentine's Day, cryin' in the hotel
I know you didn't mean to hurt me, so I kept it to myself

[Bridge]
And I wonder
Do you see her in the back of your mind in my eyes?

[Outro]
You say no one knows you so well
But every time you touch me, I just wonder how she felt
Valentine's Day, cryin' in the hotel
I know you didn't mean to hurt me, so I kept it to myself",'pop','CQACAgQAAxkBAAIUSmhIQt6AJ8h9XfIX9bDzNehNV8eCAAKoFwACKJyhUYxTjwABtirrtDYE','en',2024)""")


    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(5,'Softcore',4,4,"[Verse 1]
[Verse 1]
You've been my muse for a long time
You get me through every dark night
I'm always gone, out on the go
I'm on the run and you're home alone
I'm too consumed with my own life

[Pre-Chorus]
Are we too young for this?
Feels like I can't move

[Chorus]
Sharing my heart
It's tearing me apart
But I know I'd miss you, baby, if I left right now
Doing what I can, tryna be a man
And every time I kiss you, baby
I can hear the sound of breaking down

[Verse 2]
I've been confused as of late (yeah)
Watching my youth slip away (yeah)
You're like the sun, you make me young
But you drain me out if I get too much
I might need you or I'll break

[Pre-Chorus]
Are we too young for this?
Feels like I can't move

[Chorus]
Sharing my heart
It's tearing me apart
But I know I'd miss you, baby, if I left right now
Doing what I can, tryna be a man
And every time I kiss you, baby
I can hear the sound of breaking down

[Bridge]
Breaking down, breaking down, breaking down
Breaking down, breaking down, breaking down
I don't want to play this part
But I do all for you
I don't want to make this hard
But now I will 'cause I'm still

[Chorus]
Sharing my heart
It's tearing me apart
But I know I'd miss you, baby, if I left right now (I know I would)
Doing what I can, tryna be a man (be your man)
And every time I kiss you, baby
I can hear the sound of breaking down

[Outro]
Sharing my bed, uh
Sharing my bread, yeah
Sharing my bread
Sharing my head
(I'm breaking down)
Sharing my heart
Sharing my, suddenly I'm
(Breaking down)
Sharing, I'm done
Sharing my life",'pop','CQACAgQAAxkBAAIUY2hIRV5_erxmoSnxWatWXU2-4othAAIGBQACDq8oUztnOEaYVmPlNgQ','en',2018)""")
    
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(6,'THE DEATH OF PEACE OF MIND',3,3,"I made another mistake, thought I could change
Thought I could make it out
Promises break, need to hear you say
You're gonna keep it now
I miss the way you say my name
The way you bend, the way you break
Your makeup running down your face
The way you touch, the way you taste
When the curtains call the time
Will we both go home alive?
It wasn't hard to realize
Love's the death of peace of mind
You're in the walls that I made with crosses and frames
Hanging upside down
For granted, in vain, I took everything
I ever cared about
I miss the way you say my name
The way you bend, the way you break
Your makeup running down your face
The way you fuck, the way you taste
When the curtains call the time
Will we both go home alive?
It wasn't hard to realize
Love's the death of peace of mind
When the curtains call the time
Will we both be satisfied?
It wasn't hard to realize
Love's the death of peace of mind
Love's the death of peace of mind
You come and go in waves
Leaving me in your wake
You come and go in waves
Swallowing everything
Are you satisfied?
Love's the death of peace of mind
Mind, mind
When the curtains call the time
Will we both go home alive?
It wasn't hard to realize
Love's the death of peace of mind
When the curtains call the time
Will we both be satisfied?
It wasn't hard to realize
Love's the death of peace of mind
Love's the death of peace of mind
Love's the death of peace of mind",'rock','CQACAgQAAxkBAAIUaWhIR0pYg9OQUyWNrBNaozkfxeUyAAL5GQACzE3xUxjB1oDSBzdQNgQ','en',2022)""")
    
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(7,'Born To Die',5,5,"[Intro]
Why?
Who, me?
Why?

[Verse 1]
Feet don’t fail me now
Take me to the finish line
Oh my heart, it breaks
every step that I take
But I’m hoping at the gates
They’ll tell me that you’re mine

Walking through the city streets
Is it by mistake or design?
I feel so alone on a Friday night
Can you make it feel like home
if I tell you you’re mine?
It's like I told you, honey

[Pre-Chorus]
Don’t make me sad
don’t make me cry
Sometimes love is not
enough and the
road gets tough
I don’t know why
Keep making me laugh
Let’s go get high
The road is long, we carry on
Try to have fun in the meantime

[Chorus]
Come and take a walk
on the wild side
Let me kiss you hard in
the pouring rain
You like your girls insane
Choose your last words
this is the last time
Cause you and I
we were born to die

[Verse 2]
Lost but now I am found
I can see but once I was blind
I was so confused as a little child
Tried to take what I could get
Scared that I couldn't find
All the answers, honey

[Pre-Chorus]
Don’t make me sad
don’t make me cry
Sometimes love is
not enough and the
road gets tough
I don’t know why
Keep making me laugh
Let’s go get high
The road is long, we carry on
Try to have fun in the meantime

[Chorus]
Come and take a
walk on the wild side
Let me kiss you hard
in the pouring rain
You like your girls insane
So, choose your last words
this is the last time
Cause you and I
we were born to die
We were born to die
We were born to die

[Bridge]
Come and take a walk
on the wild side
Let me kiss you hard
in the pouring rain
You like your girls
insane So

[Pre-Chorus]
Don’t make me sad
don’t make me cry
Sometimes love is not
enough and the
road gets tough
I don’t know why
Keep making me laugh
Let’s go get high
The road is long
we carry on
Try to have fun in
the meantime

[Chorus]
Come and take a
walk on the wild side
Let me kiss you hard
in the pouring rain
You like your girls insane
So, choose your last words
this is the last time
Cause you and I
we were born to die
We were born to die
We were born to die",'pop','CQACAgQAAxkBAAIUb2hISfbLwQGkJqMgcSVNxOAaMc9RAAKfFgACJl-BUd03ra7CtLVINgQ','en',2011)""")

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(8,'Drive',6,6,"[Verse 1]
My hands wrapped around a stick shift
Swerving on the 405, I can never keep my eyes off this
My neck, the feeling of your soft lips
Illuminated in the light, bouncing off the exit signs I missed

[Chorus]
All we do is drive
All we do is think about the feelings that we hide
All we do is sit in silence waiting for a sign
Sick and full of pride
All we do is drive

And California never felt like home to me
And California never felt like home
And California never felt like home to me
Until I had you on the open road and now we're singing

[Breakdown]
Ah, ah, ah-ah, ah ah ah ah
Ah, ah, ah-ah, ah ah ah
Ah, ah, ah-ah, ah ah ah ah
Ah, ah, ah-ah, ah ah ah

[Verse 2]
Your laugh echoes down the highway
Carves into my hollow chest, spreads over the emptiness
It's bliss
It's so simple but we can't stay
Over analyze again, would it really kill you if we kissed?

[Chorus]
All we do is drive
All we do is think about the feelings that we hide
All we do is sit in silence waiting for a sign
Sick and full of pride
All we do is drive

And California never felt like home to me
And California never felt like home
And California never felt like home to me
Until I had you on the open road and now we're singing

[Breakdown]
Ah, ah, ah-ah, ah ah ah ah
Ah, ah, ah-ah, ah ah
Ah, ah, ah-ah, ah ah ah ah
Ah, ah, ah-ah, ah ah ah",'pop','CQACAgQAAxkBAAIUd2hIS_vmskKJYgqHO7Zt8s4AAdzIWgACtRoAAkDJgVEShMtimVJcLzYE','en',2015)""")
    
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(9,'Family Line',7,7,"[Verse 1]
My father never talked a lot
He just took a walk around the block
'Til all his anger took a hold of him
And then he'd hit
My mother never cried a lot
She took the punches, but she never fought
'Til she said, ""I'm leaving and I'll take the kids""
So she did

[Pre-Chorus]
I say they're just the ones who gave me life
But I truly am my parents' child

[Chorus]
Scattered 'cross my family line
I'm so good at telling lies
That came from my mother's side
Told a million to survive
Scattered 'cross my family line
God, I have my father's eyes
But my sister's when I cry
I can run, but I can't hide
From my family line

[Verse 2]
It's hard to put it into words
How the holidays will always hurt
I watch the fathers with their little girls
And wonder what I did to deserve this
How could you hurt a little kid?
I can't forget, I can't forgive you
'Cause now I'm scared that everyone I love will leave me

[Chorus]
Scattered 'cross my family line
I'm so good at telling lies
That came from my mother's side
Told a million to survive
Scattered 'cross my family line
God, I have my father's eyes
But my sister's when I cry
I can run, but I can't hide
From my family line

[Post-Chorus]
From my family line

[Bridge]
Oh-oh
All that I did to try to undo it
All of my pain and all your excuses
I was a kid, but I wasn't clueless
(Someone who loves you wouldn't do this)
All of my past I tried to erase it
But now I see, would I even change it?
Might share a face and share a last name but
(We are not the same, same)

[Chorus]
Scattered 'cross my family line
I'm so good at telling lies
That came from my mother's side
Told a million to survive
Scattered 'cross my family line
God, I have my father's eyes
But my sister's when I cry
I can run, but I can't hide
From my family line

[Outro]
From my family line (Mmhm)",'pop','CQACAgQAAxkBAAIUfWhITZDga4yrRMGvJTkhMcy5_3KSAALyDQACrAmYUfh4PaIKd-XPNgQ','en',2022)""")
    
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(10,'After Hours',8,8,"Thought I almost died in my dream again (Baby, almost died)
Fightin\' for my life, I couldn\'t breathe again
I\'m fallin\' in too deep (Oh, oh)
Without you, I can\'t sleep (Fallin\' in)
\'Cause my heart belongs to you
I\'ll risk it all for you
I want you next to me
This time, I\'ll never leave
I wanna share babies
Protection, we won\'t need
Your body next to me
Is just a memory
I\'m fallin\' in too deep, oh
Without you, I can\'t sleep
Insomnia relieve, oh
Talk to me, without you, I can\'t breathe

[Verse 2]
My darkest hours
Girl, I felt so alone inside of this crowded room
Different girls on the floor, distractin\' my thoughts of you
I turned into the man I used to be, to be
Put myself to sleep
Just so I can get closer to you inside my dreams
Didn\'t wanna wake up \'less you were beside me
I just wanted to call you and say, and say

[Chorus]
Oh, baby
Where are you now when I need you most?
I\'d give it all just to hold you close
Sorry that I broke your heart, your heart

[Verse 3]
Never comin\' down, uh
I was running away from facin\' reality, uh
Wastin\' all of my time out living my fantasies
Spendin\' money to compensate, compensate
\'Cause I want you, baby, uh
I be livin\' in heaven when I\'m inside of you
It was simply a blessing wakin\' beside you
I\'ll never let you down again, again

[Chorus]
Oh, baby
Where are you now when I need you most?
I\'d give it all just to hold you close
Sorry that I broke your heart, your heart
I said, baby
I\'ll treat you better than I did before
I\'ll hold you down and not let you go
This time, I won\'t break your heart, your heart, yeah

[Bridge]
I know it\'s all my fault
Made you put down your guard
I know I made you fall
Then said you were wrong for me
I lied to you, I lied to you, I lied to you (To you)
Can\'t hide the truth, I\'d stay with her in spite of you
You did some things that you regret, still ride for you
\'Cause this house is not a home

[Chorus]
Without my baby
Where are you now when I need you most?
I gave it all just to hold you close
Sorry that I broke your heart, your heart
And I said, baby
I\'ll treat you better than I did before
I\'ll hold you down and not let you go
This time, I won\'t break your heart, your heart, no",'pop','CQACAgQAAxkBAAIUg2hITzPkgc-MCSCccoN0hxhhiBJUAALhGQACQqWBUQsX5g6oAu0iNgQ','en',2020)""")

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(11,'24K Magic',9,9,"[Intro]
Tonight
I just want to take you higher
Throw your hands up in the sky
Let's set this party off right

[Chorus]
Players, put yo' pinky rings up to the moon
Girls, what y'all trying to do?
24 karat magic in the air
Head to toe soul player
Uh, look out!
[Verse 1]
Pop pop, it's show time (Show time)
Show time (Show time)
Guess who's back again?
Oh they don't know? (Go on tell 'em)
Oh they don't know? (Go on tell 'em)
I bet they know soon as we walk in (Showin' up)
Wearing Cuban links (ya)
Designer minks (ya)
Inglewood's finest shoes (Whoop, whoop)
Don't look too hard
Might hurt ya'self
Known to give the color red the blues

[Pre-Chorus]
Ooh shit, I'm a dangerous man with some money in my pocket
(Keep up)
So many pretty girls around me and they waking up the rocket
(Keep up)
Why you mad? Fix ya face
Ain't my fault y'all be jocking
(Keep up)

[Chorus]
Players only, come on
Put your pinky rings up to the moon
Girls, what y'all trying to do?
24 karat magic in the air
Head to toe soul player
Uh, look out!

[Verse 2]
Second verse for the hustlas (hustlas)
Gangstas (gangstas)
Bad bitches and ya ugly ass friends (Haha)
Can I preach? (Uh oh) Can I preach? (Uh oh)
I gotta show 'em how a pimp get it in
First, take your sip (sip), do your dip (dip)
Spend your money like money ain't shit (Whoop, whoop)
We too fresh
Got to blame in on Jesus
Hashtag blessed
They ain't ready for me

[Pre-Chorus]
I'm a dangerous man with some money in my pocket
(Keep up)
So many pretty girls around me and they waking up the rocket
(Keep up)
Why you mad? Fix ya face
Ain't my fault y'all be jocking
(Keep up)

[Chorus]
Players only, come on
Put your pinky rings up to the moon
Hey girls
What y'all trying to do?
24 karat magic in the air
Head to toe soul player
Uh, look out!

[Bridge]
(Wooh)
Everywhere I go they be like
Ooh, soul player ooh
Everywhere I go they be like
Ooh, soul player ooh
Everywhere I go they be like
Ooh, soul player ooh
Now, now, now
Watch me break it down like (Uh)
24 karat, 24 karat magic
What's that sound?
24 karat, 24 karat magic
Come on now
24 karat, 24 karat magic
Don't fight the feeling
Invite the feeling

[Chorus]
Just put your pinky rings up to the moon
Girls, what y'all trying to do?
24 karat magic in the air
Head to toe soul player
Put your pinky rings up to the moon
Girls, what y'all trying to do? (Do)
24 karat magic in the air
Head to toe soul player
(24 karat)
Uh, look out

[Outro]
(24 karat magic, magic, magic)",'pop','CQACAgQAAxkBAAIUsWhIWGT9y-4lStZybSNNZUWqBRJNAALfAwAC4dyxUgId8ylyWOMqNgQ','en',2016)""")
    
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(12,'Youtiful',10,10,"Looking at yourself
A lot goes in your mind
'I don't know if I'm ready to show myself'
You worry day and night
Look at the stars fall
They leave the sky, goodbye
Must be an oracle, like a waterfall
They shower you with love tonight
'Cause you are
You're perfect in my eyes
You are
Don't ever doubt yourself
(You are) I know that feeling too, I've been inside the dark
I've never been so empty, hopeless
(You are) but no, it isn't true
'Cause know that all the stars are by your side
You know whenever there's a chance
I'll tell you that you're amazing as you are
'Cause when you give me a glance
I'm sure that I see the universe in your eyes
Don't you ever tell yourself that you're not enough
I am certain that you're truly fine
You are a miracle, miracle
You are youtiful
Let me tell a little story
About the star that couldn't shine or blink
Out of a million, billion
Felt like an alien, alien
Then that little star was surely
Going to become the biggest thing
Making a fantasy family
Beautiful galaxy, galaxy
'Cause you are
More than beautiful, one of a kind
You are
Just know I'm always by your side
You know whenever there's a chance
I'll tell you that you're amazing as you are
'Cause when you give me a glance
I'm sure that I see the universe in your eyes
Don't you ever tell yourself that you're not enough
I am certain that you're truly fine
You are a miracle, miracle
You are youtiful
Another day ahead, don't wanna leave the bed
You're looking at the mirror, see the tears covered in red
I know that you've been cold this whole time
But now I'm here to make it end
You know whenever there's a chance
I'll tell you that you're amazing as you are (amazing as you are)
'Cause when you give me a glance
I'm sure that I see the universe in your eyes (universe in your eyes)
Don't you ever tell yourself that you're not enough
I am certain that you're truly fine (certain that you're truly fine)
You are a miracle, miracle
You are youtiful",'pop','CQACAgQAAxkBAAIUt2hIWiB68H7YYLjM4p-cVSle_1k_AALpEQACk-pBUzaDN1rsEq6HNgQ','en',2023)""")
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(13,'HOPE',11,11,"
Hope
Yeah, I'm on my way, I'm coming
Don't, don't lose faith in me
I know you've been waitin'
I know you've been prayin' for my soul
Hope, hope
Thirty years you been draggin' your feet
Tellin' me I'm the reason we're stagnant
Thirty years you've been claiming you're honest
And promising progress, well, where's it at?
I don't want you to feel like a failure (failure)
I know this hurts
But I gave you your chance to deliver (deliver)
Now it's my turn
Don't get me wrong, Nate, you've had a great run
But it's time to give the people somethin' different
So without further ado, I'd
Like to introduce my
(My album, my album, my album, my album, my album, my album, my album)
Hope
What's my definition of success? (Of success)
Listening to what your heart says (your heart says)
Standing up for what you know is (is)
Right, while everybody else is (is)
Tucking their tail between their legs (okay)
What's my definition of success? (Of success)
Creating something no one else can (else can)
Being brave enough to dream big (big)
Grindin' when you're told to just quit (quit)
Giving more when you got nothin' left (left)
It's a person that'll take a chance on
Something they were told could never happen
It's a person that can see the bright side through the dark times when there ain't one
It's when someone who ain't never had nothin'
Ain't afraid to walk away from more profit
'Cause they'd rather do somethin' that they really love and take the pay cut
It's a person that would never waver
Or change who they are
Just to try and gain some credibility
So they could feel accepted by a stranger
It's a person that can take the failures in their life and turn them into motivation
It's believing in yourself when no one else does, it's amazing
What a little bit of faith can do if you don't even believe in you
Why would you think or expect anybody else that's around you to?
I done did things that I regret
I done said things I can't take back
Was a lost soul at a crossroad who had no hope but I changed that
I spent years of my life holdin' on to things I never should've kept, full of hatred
Years of my life carryin' a lot of baggage that I should've walked away from
Years of my life wishin' I was someone different, lookin' for some validation
Years of my life tryna fill the void, pretending I was in
They get it
Growing pain's a necessary evil
Difficult to go through, yes, but beneficial
Some would say having a mental breakdown is a negative thing
Which on one hand, I agree with
On the other hand, it was the push I needed
To get help and start the healing process, see
If I'd have never hit rock bottom
Would I be the person that I am today?
I don't believe so
I'm a prime example of what happens when you choose to not accept defeat and face your demons
Took me thirty years to realize that if you want to get the opportunity
To be the greatest version of yourself
Sometimes you got to be someone you're not to hear the voice of reason
Having kids will make you really take a step back and look in the mirror
At least for me that's what it did, I
Wake up every day and pick my son up, hold him in my arms
And let him know he's loved (loved)
Standing by the window questioning if dad is ever going to show up (up)
Isn't something he's gon' have to worry about
Don't get it twisted, that wasn't a shot
Mama, I forgive you
I just don't want him to grow up thinkin' that he'll never be enough
Thirty years of running, thirty years of searching
Thirty years of hurting, thirty years of pain
Thirty years of fearful, thirty years of anger
Thirty years of empty, thirty years of shame
Thirty years of broken, thirty years of anguish
Thirty years of hopeless, thirty years of (hey)
Thirty years of never, thirty years of maybe
Thirty years of later, thirty years of fake
Thirty years of hollow, thirty years of sorrow",'rap','CQACAgQAAxkBAAIUvWhIW_lNwePNXCfg4zoBJufyW-KWAAJCFwACCjKJUYLbJTS5YcfvNgQ','en',2023)""")
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(14,'Drunk',12,12,"[Intro]
We're so late nights
Red eyes, amnesia, on ice
Late nights, red eyes
Amnesia, I need ya

[Verse 1]
Right now, I can't see straight
Intoxicated, it's true, when I'm with you
I'm buzzing and I feel laced
I'm coming from a different phase when I'm with you

[Pre-Chorus]
Another way now, like we're supposed to do
Take you to the back now, I'd take a shot for you
Wasted every night, gone for every song
Faded every night, dancing all night long

[Chorus]
Drunk all summer, drunk all summer
We've been drunk all summer
Drinking and flowing and rolling
We're falling down

[Refrain]
We're so late nights
Red eyes, amnesia, I need ya

[Verse 2]
Right now, I'm emotional
I lose control when I'm with you
I hope I haven't said too much
Guess I always push my luck when I'm with you

[Pre-Chorus]
Another way now, like we're supposed to do
Take you to the back now, I'd take a shot for you
Wasted every night, gone for every song
Faded every night, dancing all night long

[Chorus]
Drunk all summer, drunk all summer
We've been drunk all summer
Drinking and flowing and rolling
We're falling down

[Refrain]
We're so late nights
Red eyes, amnesia, on ice
Late nights, red eyes
Amnesia, I need ya

[Outro]
Drunk, drunk, drunk, drunk
Drunk, drunk, drunk, drunk
(You put your drinks up)
Drunk, drunk, drunk, drunk
Drunk, drunk, drunk, drunk
Drunk all summer
Drunk all summer
It's goin' around yeah",'pop','CQACAgQAAxkBAAIUzGhIXpENyYcv0eA_AAHnGhYLAnBksQAC0wQAAk1nEFI25YBxtLWUgDYE','en',2016)""")
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(15,'Woman',13,13,"[Intro]
Should we just search romantic comedies on Netflix and see what we find?

[Verse 1]
I'm selfish, I know
But I don't ever want to see you with him
I'm selfish, I know
I told you, but I know you never listen

[Pre-Chorus]
I hope you can see, the shape that I'm in
While he's touching your skin
He's right where I should, where I should be
But you're making me bleed

[Chorus]
Woman
Woman (la la la la la)
W-Woman
Woman
Woman
Woman (la la la la la)
W-Woman
Woman

[Verse 2]
Tempted, you know
Apologies are never gonna fix this
I'm empty, I know
And promises are broken like a stitch is

[Pre-Chorus 2]
I hope you can see, the shape I've been in
While he's touching your skin
This thing upon me, howls like a beast
You flower, you feast

[Chorus]
Woman
Woman (la la la la la)
W-Woman
Woman
Woman
Woman (la la la la la)
W-Woman
Woman

[Ending]
Woman!",'pop','CQACAgQAAxkBAAIU12hIYER9hXnhTKsPpu_xVNdbsThbAAJRGwAC8QqIUSVk9UcWMqDlNgQ','en',2017)""")
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(16,'Delicate',14,14,"[Intro]
This ain't for the best
My reputation's never been worse, so
You must like me for me…
We can't make
Any promises now, can we, babe?
But you can make me a drink

[Verse 1]
Dive bar on the east side, where you at?
Phone lights up my nightstand in the black
Come here, you can meet me in the back
Dark jeans and your Nikes, look at you
Oh damn, never seen that color blue
Just think of the fun things we could do
'Cause I like you

[Pre-Chorus]
This ain't for the best
My reputation's never been worse, so
You must like me for me…
Yeah, I want you
We can't make
Any promises now, can we, babe?
But you can make me a drink
[Chorus]
Is it cool that I said all that?
Is it chill that you're in my head?
'Cause I know that it's delicate (delicate)
Is it cool that I said all that?
Is it too soon to do this yet?
'Cause I know that it's delicate
Isn't it? Isn't it? Isn't it? Isn't it?
Isn't it? Isn't it? Isn't it?
Isn't it delicate?

[Verse 2]
Third floor on the west side, me and you
Handsome, you're a mansion with a view
Do the girls back home touch you like I do?
Long night, with your hands up in my hair
Echoes of your footsteps on the stairs
Stay here, honey, I don't wanna share
'Cause I like you

[Pre-Chorus]
This ain't for the best
My reputation's never been worse, so
You must like me for me…
Yeah, I want you
We can't make
Any promises now, can we, babe?
But you can make me a drink
[Chorus]
Is it cool that I said all that?
Is it chill that you're in my head?
'Cause I know that it's delicate (delicate)
Is it cool that I said all that?
Is it too soon to do this yet?
'Cause I know that it's delicate
Isn't it? Isn't it? Isn't it? Isn't it?
Isn't it? Isn't it? Isn't it?
Isn't it delicate?

[Bridge]
Sometimes I wonder when you sleep
Are you ever dreaming of me?
Sometimes when I look into your eyes
I pretend you're mine, all the damn time
'Cause I like you

[Chorus]
Is it cool that I said all that?
Is it chill that you're in my head?
'Cause I know that it's delicate (delicate)
(Yeah, I want you)
Is it cool that I said all that?
Is it too soon to do this yet?
'Cause I know that it's delicate (delicate)
'Cause I like you
Is it cool that I said all that?
Isn't it? Isn't it? Isn't it? Isn't it?
Is it chill that you're in my head?
Isn't it? Isn't it? Isn't it? Isn't it?
'Cause I know that it's delicate
Isn't it? Isn't it? Isn't it? Isn't it?
(Yeah, I want you)
Is it cool that I said all that?
Isn't it? Isn't it? Isn't it? Isn't it?
Is it too soon to do this yet?
Isn't it? Isn't it? Isn't it?
'Cause I know that it's delicate
Isn't it delicate",'pop','CQACAgQAAxkBAAIU4mhIYSYqpXgUaxb1usm11ALLROiTAAIbBAACob-xUuNFz7KF_TIaNgQ','en',2017)""")
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(17,'Lose You to Love Me',15,15,"[Verse 1]
You promised the world and I fell for it
I put you first and you adored it
Set fires to my forest
And you let it burn
Sang off-key in my chorus
'Cause it wasn't yours
I saw the signs and I ignored it
Rose-colored glasses all distorted
Set fire to my purpose
And I let it burn
You got off on the hurtin'
When it wasn’t yours, yeah

[Pre-Chorus]
We'd always go into it blindly
I needed to lose you to find me
This dancing was killing me softly
I needed to hate you to love me, yeah

[Chorus]
To love love, yeah
To love love, yeah
To love, yeah
I needed to lose you to love me, yeah
To love love, yeah
To love love, yeah
To love, yeah
I needed to lose you to love me

[Verse 2]
I gave my all and they all know it
You turned me down and now it's showing
In two months, you replaced us
Like it was easy
Made me think I deserved it
In the thick of healing, yeah

[Pre-Chorus]
We'd always go into it blindly
I needed to lose you to find me
This dancing was killing me softly
I needed to hate you to love me, yeah

[Chorus]
To love love, yeah
To love love, yeah
To love, yeah
I needed to lose you to love me, yeah
To love love, yeah
To love love, yeah
To love, yeah
I needed to lose you to love me

[Verse 1]
You promised the world and I fell for it
I put you first and you adored it
Set fires to my forest
And you let it burn
Sang off-key in my chorus

[Chorus]
To love love, yeah
To love love, yeah
To love, yeah
I needed to hate you to love me, yeah
To love love, yeah
To love love, yeah
To love, yeah
I needed to lose you to love me
To love love, yeah
To love love, yeah
To love, yeah

[Post-Chorus]
And now the chapter is closed and done
To love love, yeah
To love love, yeah
To love, yeah
And now it's goodbye, it's goodbye for us",'pop','CQACAgQAAxkBAAIU6GhIYlFtk5v_sekdeat3UBO2owUOAAL7BgACeYu4UOPcXoJldttENgQ','en',2020)""")
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(18,'Dangerous Woman',16,16,"[Verse 1]
Don't need permission
Made my decision to test my limits
Cause it's my business, God as my witness
Start what I finished
Don't need no hold up
Taking control of this kind of moment
I'm locked and loaded
Completely focused, my mind is open

[Pre-Chorus]
All that you got, skin to skin, oh my God
Don't ya stop, boy

[Chorus]
Somethin' 'bout you makes me feel like a dangerous woman
Somethin' 'bout, somethin' 'bout, somethin' 'bout you
Makes me wanna do things that I shouldn't
Somethin' 'bout, somethin' 'bout, somethin' 'bout

[Verse 2]
Nothing to prove and I'm bulletproof and
Know what I'm doing
The way we're movin' like introducing
Us to a new thing
I wanna savor, save it for later
The taste of flavor, cause I'm a taker
Cause I'm a giver, it's only nature
I live for danger

[Pre-Chorus]
All that you got, skin to skin, oh my God
Don't ya stop, boy

[Chorus]
Somethin' 'bout you makes me feel like a dangerous woman
Somethin' 'bout, somethin' 'bout, somethin' 'bout you
Makes me wanna do things that I shouldn't
Somethin' 'bout, somethin' 'bout, somethin' 'bout you

[Refrain]
All girls wanna be like that
Bad girls underneath, like that
You know how I'm feeling inside
Somethin' 'bout, somethin' 'bout
All girls wanna be like that
Bad girls underneath, like that
You know how I'm feeling inside
Somethin' 'bout, somethin' 'bout

[Instrumental Bridge]

[Chorus]
Somethin' 'bout you makes me feel like a dangerous woman
Somethin' 'bout, somethin' 'bout, somethin' 'bout you
Makes me wanna do things that I shouldn't
Somethin' 'bout, somethin' 'bout, somethin' 'bout you

[Refrain]
All girls wanna be like that
Bad girls underneath like that
You know how I'm feeling inside
Somethin' 'bout, somethin' 'bout
All girls wanna be like that
Bad girls underneath like that
You know how I'm feeling inside
Somethin' 'bout, somethin' 'bout

[Outro]
Yeah, there's somethin' 'bout you boy
Yeah, there's somethin' 'bout you boy
Yeah, there's somethin' 'bout you boy
Yeah, there's somethin' 'bout you boy
(Somethin' 'bout, somethin' 'bout, somethin' 'bout you)
Yeah, there's somethin' 'bout you boy
Yeah, there's somethin' 'bout you boy
Yeah, there's somethin' 'bout you boy
Yeah, there's somethin' 'bout you boy
(Somethin' 'bout, somethin' 'bout, somethin' 'bout you)",'pop','CQACAgQAAxkBAAIU7mhIY7eXuoR0QuJRgPv8iP48FqvhAAJYBAACK2K4UldgcaTB6M_eNgQ','en',2016)""")
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(19,'Youngblood',17,17,"[Verse 1]
Remember the words you told me, ""Love me 'til the day I die""?
Surrender my everything 'cause you made me believe you’re mine
Yeah, you used to call me baby, now you're calling me by name
Takes one to know one, yeah, you beat me at my own damn game

[Bridge]
You’re pushing, you're pushing
I’m pulling away, pulling away from you
I give and I give and I give
And you take, give and you take

[Chorus]
Young blood
Say you want me, say you want me out of your life
And I’m just a dead man walking tonight
But you need it, yeah, you need it all of the time
Yeah, ooh, ooh, ooh
Young blood
Say you want me, say you want me back in your life
So I’m just a dead man crawling tonight
'Cause I need it, yeah, I need it all of the time
Yeah, ooh, ooh, ooh

[Verse 2]
Lately, our conversations end like it’s the last goodbye
Yeah, one of us gets too drunk and calls about a hundred times
So who you been calling, baby? Nobody could take my place
When you looking at those strangers, hope to God you see my face

[Chorus]
Young blood
Say you want me, say you want me out of your life
And I’m just a dead man walking tonight
But you need it, yeah, you need it all of the time
Yeah, ooh, ooh, ooh
Young blood
Say you want me, say you want me back in your life
So I’m just a dead man crawling tonight
'Cause I need it, yeah, I need it all of the time
Yeah, ooh, ooh, ooh

[Bridge]
You’re pushing, you're pushing
I’m pulling away, pulling away from you
I give and I give and I give
And you take, give and you take
You’re running around and I’m running away
Running away from you, from you

[Chorus]
Young blood
Say you want me, say you want me out of your life
And I’m just a dead man walking tonight
But you need it, yeah, you need it all of the time
Yeah, ooh, ooh, ooh
Young blood
Say you want me, say you want me back in your life
So I’m just a dead man crawling tonight
'Cause I need it, yeah, I need it all of the time
Yeah, ooh, ooh, ooh
[Bridge]
You’re pushing, you're pushing
I’m pulling away, pulling away from you
I give and I give and I give
And you take, give and you take

[Outro]
Young blood
Say you want me, say you want me out of your life
And I’m just a dead man walking tonight",'pop','CQACAgQAAxkBAAIWM2hIa3MqspFAPZdbyifyoe7zmesbAAIRBQACWzG5UtJ_Z8S_eSyONgQ','en',2018)""")
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(20,'To Dar Masafate Barani',18,18,"تو در مسافت بارانی
 و غم درشکه ای از اشک است
و  اشک شیهه ی کوتاهی

منو تو آخورمان مرگ است
از این درشکه بیا پایین
تو نیز شیهه بکش گاهی

بتاز گله ی اکسیژن
و راه مال رویی چیزی
به سمت پنجره پیدا کن
هوا حبس نفس گیرست

بتاخت قفل مرا وا کن
بتاز ای کی پر از راهی

منم که لک لک غمگینی
به روی دودکشت هستم

منم که ماهی دریای
بلند موی مشت هستم

منم که طعمه ی قلابم
مرا شکار کن ای ماهی

منم شکار شکارم کن
سپس ببوس و بچرخانم
سپس چکار چکارم کن
چکار هر چه تو میخواهیست
بخواه آنچه که میخواهی

آهای بینی سر بالا
از این درشکه بیا پایین
به من بچسب همین الان  
مرا ببوس همین حالا

که زندگی دو سه نخ کامست
و عمر سرفه ی کوتاهی",'pop','CQACAgQAAxkBAAIWOWhIbJetB6Jxyv5IIbUbszQhWNbCAAK5AwACTvW4UvaAxM-nvoaoNgQ','fa',2018)""")
    
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(21,'Try Your Luck',21,21,"[Pre-Chorus]
I could be into it too
Depending on you
Hey, hey, hey

[Chorus]
So if you wanna talk
If you're lovestruck
If you want the goal
Then you gotta shoot the puck
Oh, baby
You can come and try your luck
And if you wanna uhh
Don't let it build up
I'll untie your tongue
If your feelings get stuck
Oh, baby
You can come and try your luck

[Outro]
If you want to
Come try your luck
Come try your luck
Come try your luck
(Come try your luck, baby)
Come try your luck
Come try your luck
Come try your luck
(Come try your luck, baby)
If you want to
Come try your luck
Come try your luck
Come try your luck
(You can come and try your luck)
I want you to, yeah, I want you to
Yeah, I want you to
I want you to, yeah, I want you to
Yeah",'pop','CQACAgQAAxkBAAIZxmhKh_iwQsPcKKWSSdV8mzYJ-ho6AAJhHAACI_mZUUAoL8Ui_HCSNgQ','en',2025)""")

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(22,'After Dark',22,22,"[Intro]
Yeah
Haha
This story about a guy I know
Yeah

[Chorus]
After dark, wonder where you are
Are you lonely like me?
Are you on these backstreets?
After dark, wonder where you are
Are you thinking of me (You know)
When you're fading out?

[Verse 1]
Em said you could do anything you set your mind on
It's crazy that it happened, my first tour had my mind blown
Time to do your meet and greet, the line's like a mile long
Go shake your hand, ? off and go put your smile on
Feelin' like Santa Claus in the mall, guess they like me
They wait in line to take a picture, come and stand by me
Just to be ushered away, we say, Thank you kindly
Summer 2010, the first time I met *, yeah, uh
She said, I know I don't have much time
But I've waited so long for this moment in there's something I have to do
She lifted up her shirt and then she showed me her back tattoo
It's crazy when you see your own face starin' back at you
Understand you're a fan, but didn't know I meant that to you
I had that impact on you, ain't know how to react to you
You told me you loved me, so I repeated it back to you
Like what else could I say? I was so filled of gratitude
Speechless and floored, ain't know I was that adored
Fast forward two tours and twenty tattoos later, all about me
Now this means I'm forever attached to you
How the fuck did I become someone that these things would happen to?
Yeah

[Chorus]
After dark (After dark), wonder where you are (Where are you?)
Are you lonely like me? (Are you lonely too)
Are you on these backstreets? (Uh)
After dark (After dark), wonder where you are (Where are you?)
Are you thinking of me
When you're fading out? (Uh)",'pop','CQACAgQAAxkBAAIaGmhKkNXN6tfkrlFBSMsg3A9ViP3sAAKcGQACTCCZUe7ZJTZ3_0BMNgQ','en',2025)""")
    
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(23,"Dont't Cry Put Your Head On My Shoulder",23,23,"[Intro]
La-la, la-la
La-la, la-la
La-la

[chorus]
Don′t cry, put your head on my shoulder
Tell me what happened, my friend
God knows how long I have known you
It always works out in the end

[verse]
The door is locked, the kettle's screaming
And I can′t stop this sinking feeling
Watching you do this damage to yourself
Knowing I can't help

[chorus]
But don't cry, put your head on my shoulder
Take all the time that you need
God knows I′m gonna show ya
It′s never as bad as it seems

[verse]
It hurts right now, but it won't forever
We′re gonna get through it together
You're doing your best, and what more can you do?

[bridge]
You know, I think that you are gonna be alright
You′re gonna be alright
You're gonna be alright
I feel you′re gonna be just fine
When this whole world has walked away
Come and find me
You're gonna hear me say

[chorus]
''Don't cry, put your head on my shoulder''
We′ll figure out what to do
God knows, have I ever told you
''I′m sorry for what you've been through?''

[outro]
You′re doing your best, and what more can you do?
Yeah, yeah, it's true
I said, la-la, la-la
La-la, la-la
La-la-la, la-la
La-la, la-la
La-la-la",'pop','CQACAgQAAxkBAAIaIGhKkp8zZ8zgLoYYJmqQLpCTtVROAALDGQACDcqRUYGAATjfnRIQNgQ','en',2025)""")
    
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(24,'Die For You',24,24,"[Verse 1]
I wish that it was simple
I wish there was a way
To fix what I have broken
To change the way I'm made
'Cause words, they don't come easy
And everything I hate
Is listening to the silence

[Pre-Chorus]
When there's a million things to say to you
I wish you knew how hard it is for me to let you know
'Cause you don't know

[Chorus]
If the world was on fire, I'd fight it for you
I'd cry enough water and breathe all the fumes
All the burns and the scars I'd wear like tattoos
And if it meant dying, then I'd die for you

[Post-Chorus]
You, you, you
I'd die for you

[Verse 2]
'Cause I don't wanna know what
Living's like without you
I can't do this without you

[Pre-Chorus]
When there's a million things to say to you
I wish you knew how hard it is for me to let you know
'Cause you don't know

[Chorus]
If the world was on fire, I'd fight it for you
I'd cry enough water and breathe all the fumes
All the burns and the scars I'd wear like tattoos
And if it meant dying, then I'd die for you

[Post-Chorus]
You, you, you
I'd die for you
You, you, you
I'd die for you",'pop','CQACAgQAAxkBAAIaJWhKlIZcVvtnJ9mxrd5VK1DSRCoTAALVGAACVTmQUXlXT5rMwwABJTYE','en',2025)""")

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(25,'Stay Young',25,25,"Here we are, face to face
Now you're gone, I'm a mess
As it was like before
And there's nothing I can say

Can't look at you in your eyes (your eyes)
'Cause everything fades and dies

Stay young, stay young
Stay young, stay young
Stay young, stay young
Stay young, stay young
Stay young, you didn't have to be like like everyone
So stay young, stay

I regret what we are
Do you know what we were?
I imagine you're a star
Always there overhead

Now all I can do is pretend (pretend)
'Cause everything, it must end

Stay young, stay young
Stay young, stay young
Stay young, stay young
Stay young, stay young
So stay young, you didn't have to be like like everyone
So stay young, stay

So stay young, you can never be like everyone
So stay young, stay
Stay young, stay young
Stay young, stay young
Stay young, stay young
Stay young, stay young
Stay young, you didn't have to be like like everyone
So stay young, stay young",'rock','CQACAgQAAxkBAAIa3WhKnf6cB7uyH8uHuEeLPG54op83AAK3HwACA-KZUe2JmtM4fbC_NgQ','en',2025)""")


    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(26,'Deli',26,26,"همسفر تنها نرو بذار تا با هم بریم
  سرنوشتمون یکی هردومون مسافریم
    تازه از راه رسیدم هنوزم خسته رام
       همسفر تنها نرو بذار تا منم بیام

            جون به لبهام رسیده تا به کی در به دری
       درد غربت رو تنم که بازم باید بری
  بذار تا خستگی از این تن خسته بره
سخته دلبستگی از شهر دلبسته بره",'pop','CQACAgQAAxkBAAIbGWhK0c5LZ0iRifh8FrUNxhwEDl42AAJVGAACC79AUpyPaUSR_cXhNgQ','fa',2025)""")


    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(27,'Emshab',27,27,"ای داد از آتش چشمانت آن خنده ی مستانت
 برده همه شب قرار از من
ای داد از دست دلم فریاد مجنون ترم از فرهاد
 دیوانه نکن فرار از من

بگو از جان من ای جان تو چه میخواهی
 تا کی از حسرت عشقت بکشم آهی
سر بزن به آسمان دل من گاهی
 تو به چشمانم ماه تر از ماهی

امشب چشمت دلبر طناز شد
 امشب عشقت خانه برانداز شد
میرقصاند دست مرا موی تو
شاید امشب یک گره ای باز شد

در سر من زلزله همه جا هلهله
 دل من با دلت ای وای ای وای
مست و غزل خوان تو موی پریشان تو
 جان من و جان تو ای وای ای وای",'pop','CQACAgQAAxkBAAIbYGhK1RGD_URJKP7-gP4qCGwJQ_0xAAKpGAACIgsxUvDk0MqgtIpjNgQ','fa',2025)""")

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(28,'Ghalam Gozashti',28,28,"خوبتو خواستم اگه نخواستم من هیچی واسه خودم 
تورو میخاستم آره تورو میخاستم به روش خاص خودم
ای لعنت به من به تو که تا به هم میزدیم
سمتت میومدم بدو بدو به خواست خودم

رفتی منو قالم گذاشتی
زخمتو رو بالم گذاشتی
شرمندمون کردی
ببین عجب دردی
تو واسه امسالم گذاشتی

این روزا بی تو با خودم حرف میزنم
پرم از عشقت ولی کم حرف میزنم
دلم از دوریت آب شد
هرچی ساختم خراب شد
روزای تنهایی شبای دلتنگی
پای قلبم حساب شد",'pop','CQACAgQAAxkBAAIbb2hK1kkKVK5drKngZKWayv2nEqaPAAKgFwACj9lRUjz83SyYUWW0NgQ','fa',2025)""")

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(29,'Shabihe To',29,29,"چی داری آخه تو چشات خودش یه عالمه نگات
گم شده بودم تو خودم شدی فرشته نجات
همه لحظه های من کنار تو خاطره شد
میشه سایه بون دلت این عاشق دیوونه چون

شبیه تو فقط تویی عاشق بی توقعی
چه خوبه دیوونت شدم تو هم دیوونم شدی
هیشکی نیست مثال تو راز تو نگاه تو
دیگه یکی همیشه هست نمیشه بی خیال تو

سر کیف دلم با تو جات سیفه تو دل
اول و آخری تو نمیکنی دستمو ول
زمان حیف بره کنار تو هر چی بشه
من و تو واسه همیم دلامون خورده گره

شبیه تو فقط تویی عاشق بی توقعی
چه خوبه دیوونت شدم تو هم دیوونم شدی
هیشکی نیست مثال تو راز تو نگاه تو
دیگه یکی همیشه هست نمیشه بی خیال تو",'pop','CQACAgQAAxkBAAIboWhK16J5nZir5o6yz5FqX7eQC6fDAALXFwACRj0wUm1iqqTw7X4bNgQ','fa',2025)""")

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(30,'Cheshmo Abroot',30,30,"چشم و ابروت عزیزم واسه مو کل دنیا شده

توی دلم ببین چجور زلزله پر پا شده

عشق تو با مو مثه آدم و حوا شده

بعد یه عمری دلم دوباره سر پا شده

مو‌ برای داشتنت، کلی دست و پا زدم

کی گفته جا زدم مو هنوز دوست دارم

چقد شبا تا صبح، خدا رو صدا زدم، دست به دعا زدم، مو‌هنووز دوست دارم



تورو دارم غمم نی

هوایی تو سرم نی

مو ای دلو دریا زدم

به جز اسمت رو لبم نیست

آبادانه او لبا

مو اسیر او نگاه

عقیق تو چشا

ای دل خونه خو برات

ایها الناس ، ایها الناس

بدین عروسم‌رو‌برم که رفتم از حال



با تو بند ، یا تو ساحل

با تو زیر نور ماه کامل

آی امون از ، در غافل

مو‌ دیوونتم ، دلم نمیشه عاقل



مو‌ برای داشتنت، کلی دست و پا زدم

کی گفته جا زدم ؟ مو هنوز دوست دارم

چقد شبا تا صبح، خدا رو صدا زدم، دست به دعا زدم، مو‌هنووز دوست دارم",'pop','CQACAgQAAxkBAAIbp2hK2ZREBUhSuUFb5QgBM_B7e8n1AAKnHAACHq8wUp15qmPwvH7LNgQ','fa',2025)""")
    
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(31,'Hanoozam',31,31,"برای من هنوز شکل روز اولتی 
هنوز تازگیتو داری واسم
هنوزم به چشمات که زل می زنم
به هیچی جز نگات نیست حواسم

هنوزم به فکر تو شبا می ره خوابم
هنوز حرف تو که می شه من یه بی اراده‌م
که واسه دیدنت حاضرم تموم شهرو
بیام پیاده زیر پام بزارم

من تموم  زندگیمو دنبال یکی شبیه تو بودم
بعد پیدا کردنت تمومه شعرامو برا تو خوندم
تو تموم زندگیمی دیگه عشق آخریمی اره
هیشکی وقتی هستی جز‌تو واسه من اهمیت نداره

فکرشم نکن خسته شم ازت
فکرشم نکن دست بکشم ازت 
فکرشم نکن تورو نبینمت یه روز
من به عشق دیدنت نفس می کشم فقط

برای من هنوز قشنگه دیدنت
قشنگی مثل روز اولی که دیدمت
همیشه تو دلم ادامه می دمت 
ادامه می دمت ادامه می دمت
نه تکرار می شی نه تکراری
به تو حسی رو دارم که تو بهم داری
همه دنیا برن می مونم پیش تو
می‌دونم تو منو تنها نمیذاری",'pop','CQACAgQAAxkBAAIbrWhK2bh9_hwP50HnoP1he9zc_lCxAALJGgACLo_4UeKj0SLGZqdVNgQ','fa',2025)""")

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(32,'Humble',32,32,"[Video Intro]
Wicked or weakness
You gotta see this
Waaaaay (yeah, yeah!)

[Streaming Intro]
Nobody pray for me
It's been that day for me
Waaaaay (yeah, yeah!)

[Verse 1]
Ayy, I remember syrup sandwiches and crime allowances
Finesse a nigga with some counterfeits
But now I’m countin' this
Parmesan where my accountant lives
In fact, I'm downin’ this
D'USSÉ with my boo bae tastes like Kool-Aid for the analysts
Girl, I can buy yo' ass the world with my paystub
Ooh, that pussy good, won't you sit it on my taste bloods?
I get way too petty once you let me do the extras
Pull up on your block, then break it down: we playin' Tetris
A.M. to the P.M., P.M. to the A.M., funk
Piss out your per diem, you just gotta hate 'em, funk
If I quit your BM, I still ride Mercedes, funk
If I quit this season, I still be the greatest, funk
My left stroke just went viral
Right stroke put lil' baby in a spiral
Soprano C, we like to keep it on a high note
It's levels to it, you and I know, bitch, be humble

[Chorus]
(Hol’ up, bitch) sit down
(Hol’ up lil' bitch, hol’ up lil' bitch) be humble
(Hol' up, bitch) sit down
(Sit down, hol' up, lil’ bitch)
Be humble (bitch)
(Hol' up, hol' up, hol' up, hol' up) bitch, sit down
Lil' bitch (hol' up, lil' bitch) be humble
(Hol' up, bitch) sit down
(Hol' up, hol' up, hol' up, hol' up) be humble
(Hol' up, hol' up, hol' up, hol' up, lil' bitch) sit down
(Hol' up lil' bitch) be humble
(Hol' up, bitch) sit down
(Hol' up, sit down, lil' bitch)
(Sit down, lil' bitch, be humble)
(Hol' up, hol' up, hol' up, hol' up, lil' bitch) bitch, sit down
(Hol' up, bitch) be humble
(Hol' up, bitch) sit down
(Hol' up, hol' up, hol' up, hol' up)

[Verse 2]
Who dat nigga thinkin' that he frontin' on Man-Man?
(Man-Man)
Get the fuck off my stage, I'm the Sandman (Sandman)
Get the fuck off my dick, that ain't right
I make a play fuckin' up your whole life
I'm so fuckin' sick and tired of the Photoshop
Show me somethin' natural like afro on Richard Pryor
Show me somethin' natural like ass with some stretch marks
Still will take you down right on your mama's couch in Polo socks, ayy
This shit way too crazy, ayy, you do not amaze me, ayy
I blew cool from AC, ayy, Obama just paged me, ayy
I don't fabricate it, ayy, most of y'all be fakin', ayy
I stay modest 'bout it, ayy, she elaborate it, ayy
This that Grey Poupon, that Evian, that TED Talk, ayy
Watch my soul speak, you let the meds talk, ayy
If I kill a nigga, it won't be the alcohol, ayy
I'm the realest nigga after all, bitch, be humble

[Chorus]
(Hol' up, bitch) sit down
(Hol' up lil' bitch, hol' up lil' bitch) be humble
(Hol' up, bitch) sit down
(Sit down, hol' up, lil' bitch)
Be humble (bitch)
(Hol' up, hol' up, hol' up, hol' up) bitch, sit down
Lil' bitch (hol' up, lil' bitch) be humble
(Hol' up, bitch) sit down
(Hol' up, hol' up, hol' up, hol' up) be humble
(Hol' up, hol' up, hol' up, hol' up, lil' bitch) sit down
(Hol' up lil' bitch) be humble
(Hol' up, bitch) sit down
(Hol' up, sit down, lil' bitch)
(Sit down, lil' bitch) be humble
(Hol' up, hol' up, hol' up, hol' up, lil' bitch) bitch, sit down
(Hol' up, bitch) be humble
(Hol' up, bitch) sit down
(Hol' up, hol' up, hol' up, hol' up)",'rap','CQACAgQAAxkBAAIbymhK3UWUrOxHl8USSk8rfawUtJ71AAL-FwACigWhUV5tSsxFzHsdNgQ','en',2017)""")

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(33,'Venom',33,33,"[Intro]
I got a song filled with shit for the strong-willed
When the world gives you a raw deal
Set you off 'til you scream, ""Piss off! Screw you!""
When it talks to you like you don't belong
Or tells you you're in the wrong field
When's something's in your mitochondrial
'Cause it latched on to you, like—

[Verse 1]
Knock knock, let the devil in
Malevolent as I've ever been, head is spinnin'
This medicine's screamin', ""L-l-l-let us in!""
L-l-lick like a salad bowl, Edgar Allen Poe
Bedridden, shoulda been dead a long time ago
Liquid Tylenol, gelatins, think my skeleton's meltin'
Wicked, I get all high when I think I've smelled the scent
Of elephant manure—hell, I meant Kahlúa
Screw it, to hell with it, I went through hell with accelerants
And blew up my-my-myself again
Volkswagen, tailspin, bucket matches my pale skin
Medal win, went from Hellmann's and being rail thin
Filet-o-Fish, to Scribble Jam and Rap Olympics '97 Freaknik
How can I be down? Me and Bizarre in Florida
Proof's room slept on floor of the motel then
Dr. Dre said ""hell yeah!""
And I got his stamp like a postcard, word to Mel-Man
And I know they're gonna hate
But I don't care, I barely could wait
To hit them with the snare and the bass
Square in the face, this fuckin' world better prepare to get laced
Because they're gonna taste my—

[Chorus]
Venom, (I got that) adrenaline momentum
Venom, not knowin' when I'm
Ever gonna slow up in 'em
Ready to snap any moment-um
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(When they get bitten with the—)
Venom, (I got that) adrenaline momentum
Venom, not knowin' when I'm
Ever gonna slow up in 'em
Ready to snap any moment-um
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(When they get bit with the—)

[Verse 2]
I said knock knock, let the devil in
Shotgun p-p-pellets in the felt pen
Cocked, fuck around and catch a hot one
I-i-it's evident I'm not done
V-venomous, the thought spun
Like your web and you just caught in 'em
Held against your will like a hubcap or a mud flap
Be strangled or attacked
So this ain't gonna feel like a love tap
Eat painkiller pills, fuck a blood track
Like, what's her name's at the wheel? Danica Patrick
Throw the car into reverse at the Indy, end up crashin'
Into ya, the back of it—just mangled steel
My Mustang and your Jeep Wrangler grill
With the front smashed, much as my rear fender, assassin
Slim be a combination of an actual kamikaze and Gandhi
Translation, I will probably kill us both
When I end up back in India
You ain't gonna be able to tell what the fuck's happenin' to you
When you're bit with the—

[Chorus]
Venom, (I got that) adrenaline momentum
Venom, not knowin' when I'm
Ever gonna slow up in 'em
Ready to snap any moment-um
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(When they get bitten with the—)
Venom, (I got that) adrenaline momentum
Venom, not knowin' when I'm
Ever gonna slow up in 'em
Ready to snap any moment-um
Thinkin' it's time to go get 'em
They ain't gonna know what hit 'em
(When they get bit with the—)",'rap','CQACAgQAAxkBAAIb0GhK3ecdqeoFCPWgUvXu8FJrnVHBAAIGFgAC8Px5URfaNU27CxozNgQ','en',2018)""")
    

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(34,'Not Like Us',32,34,"Psst, I see dead people
(Mustard on the beat, ho)
Ayy, Mustard on the beat, ho
Deebo any rap nigga, he a free throw
Man down, call an amberlamps, tell him, ""Breathe, bro""
Nail a nigga to the cross, he walk around like Teezo
What's up with these jabroni-ass niggas tryna see Compton?
The industry can hate me, fuck 'em all and they mama
How many opps you really got? I mean, it's too many options
I'm finna pass on this body, I'm John Stockton
Beat your ass and hide the Bible if God watchin'
Sometimes you gotta pop out and show niggas
Certified boogeyman, I'm the one that up the score with 'em
Walk him down, whole time, I know he got some ho in him
Pole on him, extort shit, bully, Death Row on him
Say, Drake, I hear you like 'em young
You better not ever go to cell block one
To any bitch that talk to him and they in love
Just make sure you hide your lil' sister from him
They tell me Chubbs the only one that get your hand-me-downs
And Party at the party playin' with his nose now
And Baka got a weird case, why is he around?
Certified Lover Boy? Certified pedophiles
Wop, wop, wop, wop, wop, Dot, fuck 'em up
Wop, wop, wop, wop, wop, I'ma do my stuff
Why you trollin' like a bitch? Ain't you tired?
Tryna strike a chord and it's probably A minor
They not like us, they not like us, they not like us
They not like us, they not like us, they not like us
You think the Bay gon' let you disrespect Pac, nigga?
I think that Oakland show gon' be your last stop, nigga
Did Cole fouI, I don't know why you still pretendin'
What is the owl? Bird niggas and bird bitches, go
The audience not dumb
Shape the stories how you want, hey, Drake, they're not slow
Rabbit hole is still deep, I can go further, I promise
Ain't that somethin'? B-Rad stands for bitch and you Malibu most wanted
Ain't no law, boy, you ball boy, fetch Gatorade or somethin'
Since 2009, I had this bitch jumpin'
You niggas'll get a wedgie, be flipped over your boxers
What OVO for? The ""Other Vaginal Option""? Pussy
Nigga better straighten they posture, got famous all up in Compton
Might write this for the doctorate, tell the pop star, ""Quit hidin""
Fuck a caption, want action, no accident
And I'm hands-on, he fuck around, get polished
Fucked on Wayne girl while he was in jail, that's connivin'
Then get his face tatted like a bitch apologizin'
I'm glad DeRoz' came home, y'all didn't deserve him neither
From Alondra down to Central, nigga better not speak on Serena
And your homeboy need subpoena, that predator move in flocks
That name gotta be registered and placed on neighborhood watch
I lean on you niggas like another line of Wock'
Yeah, it's all eyes on me, and I'ma send it up to Pac, ayy
Put the wrong label on me, I'ma get 'em dropped, ayy
Sweet Chin Music and I won't pass the aux, ayy
How many stocks do I really have in stock? Ayy
One, two, three, four, five, plus five, ayy
Devil is a lie, he a 69 God, ayy
Freaky-ass niggas need to stay they ass inside, ayy
Roll they ass up like a fresh pack of 'za, ayy
City is back up, it's a must, we outside, ayy
They not like us, they not like us, they not like us
They not like us, they not like us, they not like us
Once upon a time, all of us was in chains
Homie still doubled down callin' us some slaves
Atlanta was the Mecca, buildin' railroads and trains
Bear with me for a second, let me put y'all on game
The settlers was usin' townfolk to make 'em richer
Fast-forward, 2024, you got the same agenda
You run to Atlanta when you need a check balance
Let me break it down for you, this the real nigga challenge
You called Future when you didn't see the club (Ayy, what?)
Lil Baby helped you get your lingo up (What?)
21 gave you false street cred
Thug made you feel like you a slime in your head (Ayy, what?)
Quavo said you can be from Northside (What?)
2 Chainz say you good, but he lied
You run to Atlanta when you need a few dollars
No, you not a colleague, you a fuckin' colonizer
The family matter and the truth of the matter
It was",'rap','CQACAgQAAxkBAAIb1mhK4GEbfcZN7ty47-wQJvSe8VTjAAJnFgAC8MMgUFwu6vysZ8TnNgQ','fa',2024)""")
    
    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(35,"I Can't Do This Slowed",34,35,"(I knew it..)
I've been through it
Its all ruined
I can’t do this
(I knew it..)
It’s all ruined
(I knew it..)
It’s all ruined
Ah-ah-ah-ahh Ah-ah-ah-ahh
Tell me to end it all
Tell me to end it all
I don't wanna give it out
I don't wanna give it out",'fonk','CQACAgQAAxkBAAIcLmhK5HJzeLHbwMp3GVUaVcg6VAw8AALUEgACPYDxUBx3WWOLnZnTNgQ','en',2025)""")

    cursor.execute("""INSERT INTO SONG(ID,SONG_NAME,ARTIST_ID,ALBUM_ID,LYRIC,GENRE,MESSAGE_LINK,LANG,RELEASE_YEAR) VALUES(36,"MONTAGEM TOMADA(Slowed)",35,36,"[Intro: Bsharry]
La—, la—, la vida es un carrusel
Carrus—, ca—, ca—, ca—, ca—, ca—, ca—, ca—
Carrus—, carrusel, —el, carrus—, carrus—

[Drop 1: Bsharry]
La vida, la vida es un carrusel
(Oah) Carrusel
Carrusel
Carrusel
La vida, la vida es un carrusel
(Oah) Carrusel
Carrusel
Carrusel
La vida, la vida es un—
[Chorus: Bsharry]
Carrus—, carrusel
(Oah) Carrus—, carrusel
Carrus—, carrusel
Carrus—, carrus—

[Drop 2: Bsharry]
La vida, la vida es un carrusel
(Oah) Carrusel
Carrusel (Esse é o MXZI)
(É o brabo da putaria) Carrusel

[Refrain: Bsharry]
La vida, la vida es un carrusel
Vamos a disfrutarla
Vamos a disfrutarla

[Buildup: Bsharry]
Carrus—, carrusel
(Oah) Carrus—, carrusel
Carrus—, carrusel
Carrus—, carrus—

[Drop 3: Bsharry]
La vida, la vida es un carrusel
(Oah) Carrusel
Carrusel
Carrusel
La vida, la vida es un carrusel
(Oah) Carrusel
Carrusel
Carrusel",'fonk','CQACAgIAAxkBAAIcNGhK5IMxQ2XbV61h6sSxECigaEYcAAL6YwACdRXpSjr3AlDpDl2FNgQ','en',2025)""")




    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database(db_config["database"])
    create_table_user()
    create_table_artist()
    create_table_album()
    create_table_song()
    create_table_playlist()
    create_table_playlist_song()
    create_table_follow()
    create_table_favorite()

    insert_into_artist_table()
    insert_into_album_table()
    insert_into_song_table()
