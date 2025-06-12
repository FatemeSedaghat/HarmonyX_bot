import telebot
from config import admin_id,channel_cid,TOKEN
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton
from telebot.util import antiflood
import logging
logging.basicConfig(filename='project.log',format='%(asctime)s, %(filename)s, %(levelname)s, %(message)s')
from texts import text
from DQL import get_artist_id, get_known_users, get_album_id,newest,get_artist_name,get_jenre,get_song_link,get_song_lyric,get_following,show_following_list,remove_from_follow,check_in_follow_list,get_song_id,get_favourite,show_favourite_list,get_song_name,get_artist_id_from_song,remove_from_favourite,show_user_playlist,get_playlist_id,get_playlist_songs,check_existing_playlist,get_songs_ids_from_playlist_song,remove_playlist_song,remove_from_playlist
from DML import insert_user_data,insert_song_data,insert_follow_data,insert_favorite_data,insert_playlist_data,insert_playlist_song_data



hideboard = ReplyKeyboardRemove()


knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts
adminstep ={}
song_info=[]
song_lyric=[]
commands = {  # command bioription used in the "help" command
    'start'       : 'شروع بات',
    'help'        : 'این منو دستورات موجود را در اختیارتان میگذارد',
}

admins_commands = {
    'add_music'           :       'اضافه کردن موزیک به بات',
    
}

message_ids = {
    'start'       :   2,
    'help_message':   8,
    'add_music_1' :   16,
    'add_music_2' :   17,
    'add_music_3' :   18,
    'new_playlist_resp' : 19,
}

message_id=[1058]

user_state={}

PAGE_SIZE = 5
user_pages ={}
removelist = {}
playlist_id_for_delete=[]
playlist_info=[]

def check_user(cid):
    global KnownUsers
    if cid in KnownUsers:
        return True
    info = bot.get_chat(cid)
    first_name = info.first_name
    last_name = info.last_name
    username = info.username
    if insert_user_data(cid, first_name, last_name, username):
        KnownUsers.append(cid)
        return True
    return False



def send_message(*args, **kwargs):
    try:
        return antiflood(bot.send_message, *args, **kwargs)
    except telebot.apihelper.ApiTelegramException:
        logging.error('error in sending message')
    except Exception as e:
        logging.error(f'another eeror happend in sending message, {repr(e)}')

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        logging.warning("New user detected, who hasn't used \"/start\" yet")
        return 0
    


def listener(messages):
    for m in messages:
        logging.info(m)
        if m.content_type == 'text':
            logging.info(f'{m.chat.first_name} [{m.chat.id}] : {m.text}')


def send_new_song_list(cid,lang,page=1):
    songs = newest(lang,page)
    if not songs:
        send_message(cid,text['new_eror'])
        return
    user_pages[cid]={'lang':lang,'page':page}
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('⬅️')
    for song in songs:
        artist_name = get_artist_name(song['ARTIST_ID'])
        markup.add(f'🎵{song['SONG_NAME']}-{artist_name}')
    if page>1 :
        markup.add(text['prev'])
    if len(songs) == PAGE_SIZE:
        markup.add(text['next'])
    send_message(cid,text['othersongs'],reply_markup = markup)
    

def send_jenre_song_list(cid,jenre,page=1):
    songs = get_jenre(jenre,page)
    if not songs:
        send_message(cid,text['new_eror'])
        return
    user_pages[cid]={'jenre':jenre,'page':page}
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('⬅️')
    for song in songs:
        artist_name = get_artist_name(song['ARTIST_ID'])
        markup.add(f'🎵{song['SONG_NAME']}-{artist_name}')
    if page>1 :
        markup.add(text['prev'])
    if len(songs) == PAGE_SIZE:
        markup.add(text['next'])
    send_message(cid,text['othersongs'],reply_markup = markup)
    

def send_following_list(cid,page=1):
    songs = get_jenre(page)
    if not songs:
        send_message(cid,text['new_eror'])
        return
    user_pages[cid]={'page':page}
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('⬅️')
    for song in songs:
        artist_name = get_artist_name(song['ARTIST_ID'])
        markup.add(f'🎵{song['SONG_NAME']}-{artist_name}')
    if page>1 :
        markup.add(text['prev'])
    if len(songs) == PAGE_SIZE:
        markup.add(text['next'])
    send_message(cid,text['othersongs'],reply_markup = markup)
    
def send_song_of_followings(artist_id,song_name):
    user_list = get_known_users()
    for user in user_list:
        if check_in_follow_list(user,artist_id):
            song_link = get_song_link(artist_id,song_name)
            send_message(user,text['text_for_followings_song_update'])
            bot.send_audio(user,song_link)
        else:
            return



bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener) 

@bot.message_handler(commands=['start'])
def send_message_welcome(message):
    cid = message.chat.id
    check_user(cid)
    bot.copy_message(cid,channel_cid,message_ids['start'])
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['newest'])
    markup.add(text['following'],text['playlist'], text['jenre'])
    markup.add(text['contactus'],text['help'],text['myfavourite'])
    send_message(cid,text['menu_reps'],reply_markup=markup)
    
@bot.message_handler(func=lambda message: message.text==text['main menu'])
def return_main_menu(message):
    cid = message.chat.id
    check_user(cid)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['newest'])
    markup.add(text['following'],text['playlist'], text['jenre'])
    markup.add(text['contactus'],text['help'],text['myfavourite'])
    send_message(cid,text['menu_reps'],reply_markup=markup)


@bot.message_handler(commands=['help'])
def command_help(message):
    cid = message.chat.id
    check_user(cid)
    text = 'منوی راهنما برای شما:\n\n'
    for command, desc in commands.items():
        text += f'/{command}  -      {desc}\n'
    if cid in admin_id:
        text += 'دسترسی های ادمین:\n\n'
        for command, desc in admins_commands.items():
            text += f'/{command}  -   {desc}\n'
    send_message(cid, text, reply_to_message_id=message.message_id)

@bot.message_handler(commands=['add_music'])
def command_add_music(message):
    cid = message.chat.id
    check_user(cid)
    if cid in admin_id:
        bot.copy_message(cid,channel_cid,message_ids['add_music_1'])
        adminstep[cid] = 'AS'
    else:
        command_default(message)



@bot.message_handler(func=lambda message: message.text==text['newest'])
def show_newest(message):
    cid = message.chat.id
    check_user(cid)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['main menu'])
    markup.add(text['irani'],text['foreign'])
    send_message(cid,text['new_resp'],reply_markup=markup)

@bot.message_handler(func=lambda message: message.text==text['foreign'])
def show_foreign_newest(message):
    cid = message.chat.id
    check_user(cid)
    send_new_song_list(cid,'en',1)


@bot.message_handler(func=lambda message: message.text==text['irani'])
def show_irani_newest(message):
    cid = message.chat.id
    check_user(cid)
    send_new_song_list(cid,'fa',1)


@bot.message_handler(func=lambda message: message.text==text['following'])
def show_following_to_user(message):
    cid = message.chat.id
    check_user(cid)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['main menu'])
    for ids in show_following_list([cid]):
        name= get_artist_name(ids['ARTIST_ID'])
        markup.add(f'❌{name}')
    send_message(cid,text['follow'], reply_markup=markup)


@bot.message_handler(func=lambda message: message.text==text['playlist'])
def show_playlist(message):
    cid = message.chat.id
    check_user(cid)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['main menu'])
    markup.add(text['newplaylist'],text['myplaylist'])
    send_message(cid,text['playlist_resp'],reply_markup=markup)  


@bot.message_handler(func=lambda message: message.text==text['myplaylist'])
def my_playlist(message):
    cid = message.chat.id
    check_user(cid)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('🔙')
    for name in show_user_playlist([cid]):
        playlist_name = name['PLAYLIST_NAME']
        markup.add(f'💿{playlist_name}')
    send_message(cid,text['your_playlists'],reply_markup=markup) 
    send_message(cid,reply_markup=markup)
    





@bot.message_handler(func=lambda message: message.text==text['newplaylist'])
def show_newplaylist(message):
    cid = message.chat.id
    check_user(cid)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('🔙','➕')
    bot.copy_message(cid,channel_cid,message_ids['new_playlist_resp'],reply_markup=markup)



@bot.message_handler(func=lambda message: message.text=='🔙')
def return_to_show_playlist(message):
    cid = message.chat.id
    check_user(cid)
    message == '🔙'
    user_state[cid] = None

    show_playlist(message)


@bot.message_handler(func=lambda message: message.text=='➕')
def create_new_playlist(message):
    cid = message.chat.id
    check_user(cid)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['return in new playlist_menu'])
    user_state[cid] = 'playlist_name'
    send_message(cid,text['name_for_playlist'],reply_markup=markup)



@bot.message_handler(func=lambda message: message.text==text['return in new playlist_menu'])
def return_to_add_playlist(message):
    cid = message.chat.id
    check_user(cid)
    user_state[cid]=None
    show_newplaylist(message)

@bot.message_handler(func=lambda message: message.text==text['return_to_my_playlist'])
def return_to_my_playlist(message):
    cid = message.chat.id
    check_user(cid)
    my_playlist(message)


@bot.message_handler(func=lambda message: message.text==text['remove_specific_playlist'])
def confirmation_for_removing_from_playlist(message):
    cid = message.chat.id
    check_user(cid)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['yes_for_delete'],text['return_to_my_playlist'])
    send_message(cid,text['delete_playlist_confirmation'],reply_markup=markup)

    
@bot.message_handler(func=lambda message: message.text==text['yes_for_delete'])
def remove_from_playlist(message):
    cid = message.chat.id
    check_user(cid)
    remove_playlist_song([playlist_id_for_delete[0]])
    remove_from_playlist(cid,playlist_id_for_delete[1])
    playlist_id_for_delete.clear()
    send_message(cid,text['done'])
    my_playlist(message)

        




@bot.message_handler(func=lambda message: message.text==text['jenre'])
def show_jenre(message):
    cid = message.chat.id
    check_user(cid)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['main menu'])
    markup.add(text['pop'],text['rock'],text['rap'],text['fonk'])
    send_message(cid,text['jenre_resp'],reply_markup=markup)  

@bot.message_handler(func=lambda message: message.text==text['pop'])
def show_pop_jenre(message):
    cid = message.chat.id
    check_user(cid)
    send_jenre_song_list(cid,'pop',1)


@bot.message_handler(func=lambda message: message.text==text['rock'])
def show_rock_jenre(message):
    cid = message.chat.id
    check_user(cid)
    send_jenre_song_list(cid,'rock',1)



@bot.message_handler(func=lambda message: message.text==text['rap'])
def show_rap_jenre(message):
    cid = message.chat.id
    check_user(cid)
    send_jenre_song_list(cid,'rap',1)


@bot.message_handler(func=lambda message: message.text==text['fonk'])
def show_fonk_jenre(message):
    cid = message.chat.id
    check_user(cid)
    send_jenre_song_list(cid,'fonk',1)




@bot.message_handler(func=lambda message: message.text==text['contactus'])
def show_contact_us(message):
    cid = message.chat.id
    check_user(cid)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('⬅️')
    user_state[cid] = 'feedback'
    send_message(cid,text['contact_resp'],reply_markup=markup)
    

@bot.message_handler(func=lambda message: message.text==text['myfavourite'])
def my_downloads(message):
    cid = message.chat.id
    check_user(cid)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['main menu'])
    for ids in show_favourite_list([cid]):
        song_name= get_song_name(ids['SONG_ID']) 
        artist_id = get_artist_id_from_song(ids['SONG_ID'])
        artist_name = get_artist_name(artist_id)
        markup.add(f'❤️{song_name}-{artist_name}')

    send_message(cid,text['myfave_resp'], reply_markup=markup)

@bot.message_handler(func=lambda message: message.text==text['help'])
def help_message(message):
    cid = message.chat.id
    check_user(cid)
    bot.copy_message(cid,channel_cid,message_ids['help_message'])


@bot.message_handler(func=lambda message:user_state.get(message.chat.id) == 'feedback')
def handle_feedback(message):
    if message.text == '⬅️':
        cid = message.chat.id
        return_main_menu(message)
        user_state[cid]=None

    
    
    else:
        cid = message.chat.id
        check_user(cid)
        user_message = message.text
        user_name = message.from_user.first_name
        send_message(admin_id[0],f' پیام جدید از {user_name}:\n{user_message}')
        send_message(cid,text['feedback_resp'])
        return_main_menu(message)
        user_state[cid] = None
    

@bot.message_handler(func=lambda message:user_state.get(message.chat.id) == 'playlist_name')
def handle_feedback(message):
    cid = message.chat.id
    check_user(cid)
    user_message = message.text
    if user_message!=text['main menu']:
        if insert_playlist_data(cid,user_message):
            send_message(cid,text['playlist_created'].format(user_message))
            show_newplaylist(message)
            user_state['playlist_name']=None

        else:
            send_message(cid,text['invalid_playlist_name'])
            show_newplaylist(message)
            user_state['playlist_name']=None
    else:
         user_state['playlist_name']=None
         return_main_menu(message)

    

    




@bot.message_handler(func=lambda message: message.text=='⬅️')
def return_premenu(message):
    user_state['playlist_name']=None
    return_main_menu(message)

@bot.message_handler(func=lambda message: message.text in [text['prev'],text['next']])
def analys(message):
    cid = message.chat.id
    if cid not in user_pages:
        return
    current_page = user_pages[cid]['page']
    lang = user_pages[cid].get('lang')
    jenre = user_pages[cid].get('jenre')
    if jenre:
        if message.text==text['prev'] and current_page>1:
            send_jenre_song_list(cid,jenre,current_page-1)
        elif message.text==text['next']:
            send_jenre_song_list(cid,jenre,current_page+1)

    if lang:
        if message.text==text['prev'] and current_page>1:
            send_new_song_list(cid,lang,current_page-1)
        elif message.text==text['next']:
            send_new_song_list(cid,lang,current_page+1)

@bot.message_handler(content_types=['audio'])
def command_audio_handler(message):
    cid = message.chat.id
    check_user(cid)
    if adminstep.get(cid) == 'AS':
        if cid in admin_id:
            try:
                artist_name = message.audio.performer
                artist_id=get_artist_id(artist_name)
                info = message.caption.split('\n')
                album_name = info[-1].split(':', 1)[-1].strip()
                album_genre = info[-2].split(':', 1)[-1].strip()
                lang = info[-3].split(':', 1)[-1].strip()
                release_year = info[-4].split(':', 1)[-1].strip()
                song_name = message.audio.title
                file_id= message.audio.file_id
                album_id = get_album_id(album_name,artist_id,album_genre)
                #song_name = message.audio.title
                bot.copy_message(cid,channel_cid,message_ids['add_music_2'])
                adminstep[cid] = 'lyrics'
                print(file_id)
                song_info.append(song_name)
                song_info.append(artist_id)
                song_info.append(album_id)
                song_info.append(album_genre)
                song_info.append(file_id)
                song_info.append(lang)
                song_info.append(release_year)
                

            except Exception as e:
                send_message(cid, f'Something went wrong, {repr(e)}')
            return
    else:
        command_default(message)

@bot.message_handler(func=lambda  message: adminstep.get(message.chat.id) == 'lyrics')
def command_lyric_handler(message):
    cid = message.chat.id
    check_user(cid)
    try:
        info = message.text
        lyric = ''.join(info)
        print(lyric)
        song_id = insert_song_data(song_info[0],song_info[1],song_info[2],lyric,song_info[3],song_info[4],song_info[5],song_info[6])
        bot.copy_message(cid,channel_cid,message_ids['add_music_3'])
        adminstep[cid]= 'none'
        send_song_of_followings(song_info[1],song_info[0])
    
        song_info.clear()
    except Exception as e:
        send_message(cid,repr(e))
 

@bot.message_handler(func=lambda message: message.text.startswith('🎵'))
def download_song_options(message):
    cid = message.chat.id
    check_user(cid)
    song_information = message.text.split('-')
    song_name = song_information[0].strip('🎵')
    artist_name = song_information[1]
    artist_id = get_artist_id(artist_name)
    song_link = get_song_link(artist_id,song_name)
    song_lyric.append(artist_id)
    song_lyric.append(song_name)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text['lyric'], callback_data=f'lyric:{artist_id},{song_name}'), InlineKeyboardButton(text['follow_artist'],callback_data=f'follow:{artist_id}'))
    markup.add(InlineKeyboardButton('❤️', callback_data=f'favourite:{artist_id},{song_name}'),InlineKeyboardButton('➕', callback_data=f'playlist:{artist_id},{song_name}'))
    bot.send_audio(cid,song_link,reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.startswith('❌'))
def remove_from_following_confirmation(message):
    cid = message.chat.id
    check_user(cid)
    removelist[cid] = message.text.strip('❌')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['main menu'])
    markup.add(text['yes'],text['no'])
    send_message(cid,text['removing_follow_conf'].format(message.text.strip('❌')),reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in [text['yes'],text['no']])
def removing_from_following(message):
    cid = message.chat.id
    check_user(cid)
    if message.text == text['yes']:
        artist_id = get_artist_id(removelist[cid])
        remove_from_follow(cid,artist_id)
        send_message(cid,text['reply_for_removing'].format(removelist[cid]))
        removelist[cid] = None
    else:
        show_following_to_user(message)

@bot.message_handler(func=lambda message: message.text.startswith('❤️'))
def send_fave_music(message):
    cid = message.chat.id
    check_user(cid)
    song_information = message.text.split('-')
    song_name = song_information[0].strip('❤️')
    artist_name = song_information[1]
    artist_id = get_artist_id(artist_name)
    song_link = get_song_link(artist_id,song_name)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text['lyric'],callback_data=f'lyric:{artist_id},{song_name}'),InlineKeyboardButton(text['remove_from_fave'],callback_data=f'remove:{artist_id},{song_name}'))
    bot.send_audio(cid,song_link,reply_markup=markup)

    
    


@bot.callback_query_handler(func=lambda call: call.data.startswith('lyric:'))
def send_song_lyric(call):
    cid = call.message.chat.id
    check_user(cid)
    artist_id = call.data.split(',')[0].strip('lyric:')
    song_name = call.data.split(',')[1]
    lyric = get_song_lyric(artist_id,song_name)
    result = ''.join(song_name.split())
    send_message(cid,f'📝#{result}\n{lyric}')

@bot.callback_query_handler(func=lambda call: call.data.startswith('follow:'))
def follow_artist(call):
    cid = call.message.chat.id
    check_user(cid)
    artist_id = call.data.split('follow:')[1]
    if get_following(cid,artist_id):
        send_message(cid,text['follow_resp2'])
    else:
        insert_follow_data(cid,artist_id)
        send_message(cid,text['follow_resp'])

@bot.callback_query_handler(func=lambda call: call.data.startswith('favourite:'))
def add_to_favourite_songs(call):
    cid = call.message.chat.id
    check_user(cid)
    artist_id = call.data.split(',')[0].strip('favourite:')
    song_name = call.data.split(',')[1]
    song_id = get_song_id(artist_id,song_name)
    if get_favourite(cid,song_id):
        send_message(cid,text['already_added_to_fave'])
    else:
        insert_favorite_data(cid,song_id)
        send_message(cid,text['add_to_fave'])

@bot.callback_query_handler(func=lambda call: call.data.startswith('remove:'))
def add_to_favourite_songs(call):
    cid = call.message.chat.id
    check_user(cid)
    artist_id = call.data.split(',')[0].strip('remove:')
    song_name = call.data.split(',')[1]
    song_id = get_song_id(artist_id,song_name)
    remove_from_favourite(cid,song_id)
    send_message(cid,text['fave_song_removed'])






@bot.callback_query_handler(func=lambda call: call.data.startswith('playlist:'))
def add_to_playlist(call):
    cid = call.message.chat.id
    check_user(cid)
    artist_id = call.data.split(',')[0].strip('playlist:')
    song_name = call.data.split(',')[1]
    song_id = get_song_id(artist_id,song_name)

    playlist_info.append(song_id)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['main menu'])
    playlist_names=show_user_playlist([cid])
    if not playlist_names:
        send_message(cid,text['no existing playlist'],reply_markup=markup)
        return
    for name in playlist_names:
        playlist_name = name['PLAYLIST_NAME']
        markup.add(f'📀{playlist_name}')
    send_message(cid,text['selecting playlist'],reply_markup=markup)



@bot.message_handler(func=lambda message: message.text.startswith('📀'))
def playlist_soongs(message):
    cid = message.chat.id
    check_user(cid)
    playlist_name = message.text.strip('📀')
    playlist_id = get_playlist_id(cid,playlist_name)
    if insert_playlist_song_data(playlist_id,playlist_info[0],cid):
        send_message(cid,text['song_added_to_playlist_succesfully'].format(f'"{playlist_name}"'))
        return_main_menu(message)
        playlist_info.clear()
    else:
        send_message(cid,'error')
        playlist_info.clear()


@bot.message_handler(func=lambda message: message.text.startswith('💿'))
def show_playlist_contents(message):
    cid = message.chat.id
    check_user(cid)
    playlist_name = message.text.strip('💿')
    playlist_id = check_existing_playlist(playlist_name,cid)
    playlist_id_for_delete.append(playlist_id)
    playlist_id_for_delete.append(playlist_name)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text['return_to_my_playlist'],text['remove_specific_playlist'])
    if playlist_id:
        song_id_playlist = get_songs_ids_from_playlist_song([playlist_id])

        for song in song_id_playlist:
            song_id = song['SONG_ID']
            artist_id = get_artist_id_from_song(song_id)
            artist_name = get_artist_name(artist_id)
            song_name = get_song_name(song_id)
            markup.add(f'🎵{song_name}-{artist_name}')
    
        send_message(cid,text['showing_specific_playlist'].format(f'"{playlist_name}"'),reply_markup = markup)
    else:
        command_default(message)

   
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(message):
    send_message(message.chat.id, text['message_handler'].format(message.text)+'/help')

if __name__ == "__main__":
    KnownUsers = get_known_users()
    bot.infinity_polling()
