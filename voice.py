from gtts import gTTS
import os

language = 'en'


def voice(my_text):
    my_text = my_text.split()
    my_text = '-'.join(my_text)
    if(os.path.exists(my_text)):
        os.system(f"mpg321 Voices/{my_text}.mp3")
    else:
        myobj = gTTS(text=my_text, lang=language, slow=False)
        myobj.save(f"Voices/{my_text}.mp3")
        os.system(f"mpg321 Voices/{my_text}.mp3")


def say_hi(name):
    my_text = f'hi {name}'
    voice(my_text)


def say_bye(name):
    my_text = f'goodbye {name} I hope you enjoyed the program'
    voice(my_text)


def job_compleated(app, job):
    my_text = f'the {app} successfully {job}'
    voice(my_text)