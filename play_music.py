import os
import pathlib
import random
import colors
import notify2

notify2.init('Terminal-Assistant')

go_home = "cd ~"

def clear_screen():
    os.system('clear')

def create_and_move_text_file():
    here = pathlib.Path().absolute()
    if os.path.exists('music.txt'):
        return True
    else:
        search_music = f'{go_home} && find . -iname "*.mp3" -print 2>/dev/null>music.txt'
        move_file = f"{go_home} && mv music.txt {here}"
        os.system(search_music)
        os.system(move_file)


def choose_random_music():
    file = open('music.txt', 'r')
    musics = file.readlines()
    file.close()
    music = musics[random.randrange(0, len(musics)+1)]
    return music


def become_playable(music_path):
    music = music_path.split('/')
    music_name = music.pop()
    music_path = '/'.join(music)

    music_name = music_name.split('\n')
    music_name = f'/"{music_name[0]}"'
    music_path += music_name

    return music_path


def play_music(music_path):
    try:
        music_path = become_playable(music_path)
        play = f'{go_home} && xdg-open {music_path}'
        os.system(play)
        name = music_path.split('/')
        name = name[-1]
        n = notify2.Notification('Play Music', f'{name} played')
        n.show()
    except:
        print(colors.error+"we can't play that music.")


def validate_selected_method(number):
    if number.isdigit() and number in ['1', '2']:
        return True
    else:
        clear_screen()
        print(colors.error+'Please Enter correct number.')
        return False


def select_method_for_play():
    while True:
        text_for_show = colors.starter+"""
        [1] Play random music
        [2] Play choose song
        """
        print(text_for_show)
        user_method_choice = input("Select your method : ")
        validate = validate_selected_method(user_method_choice)
        if validate == True:
            return int(user_method_choice)


def find_song(musics, user_choice):
    for music in musics:
        music_name = music.split('/')
        music_name = music_name[-1]
        if music_name == user_choice:
            return music
        if user_choice in music_name:
            return music


def choose_song():
    user_choice = input(colors.starter+"Enter music : ")
    try:
        file = open('music.txt', 'r')
        musics = file.readlines()
        return find_song(musics, user_choice)
    except:
        print(colors.error+"Some error happend.")
    finally:
        file.close()


def music():
    method = select_method_for_play()
    create_and_move_text_file()
    if method == 1:
        music_path = choose_random_music()
    if method == 2:
        music_path = choose_song()

    play_music(music_path)


def run():
    music()