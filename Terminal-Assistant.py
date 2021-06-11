import os
os.system('sudo apt install mpg321')
os.system('pip install -r requirment.txt')
import time
import colors
import voice
import open_close_app as app
import play_music as music

def clear_screen():
    os.system('clear')



clear_screen()

def say_hi():
    file = open('text.txt', 'r')
    name = file.readline()
    file.close()
    voice.say_hi(name)


def creat_owner():
    name = input("Enter Your Name : ")
    file = open('text.txt', 'a+')
    file.writelines(name)
    file.close()
    voice.say_hi(name)


def cheak_name_exist():
    if(os.path.exists('text.txt')):
        say_hi()
        clear_screen()
    else:
        creat_owner()
        clear_screen()


def say_bye():
    file = open('text.txt', 'r')
    name = file.readline()
    file.close()
    voice.say_bye(name)


def say_job():
    while True:
        try:
            job = input(colors.starter+"what can i do for you (q = exit app) ? ")
            if job == 'q':
                return True
            job = job.split()
            if job[0] == 'open':
                if app.open_app(app.app_commends[job[1]], job[1]) == False:
                    time.sleep(4)
                    clear_screen()
            if job[0] == 'close':
                if app.close_app(app.app_commends[job[1]], job[1]) == False:
                    time.sleep(4)
                    clear_screen()
            if job[0] == 'play':
                music.run()
            clear_screen()
        except:
            clear_screen()
            print(colors.error+"some error happend")


def run():
    cheak_name_exist()
    say_job()
    say_bye()


run()