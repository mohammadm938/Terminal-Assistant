import voice
import os
import colors
import notify2

notify2.init('Terminal-Assistant')

app_commends = {
    # you can add app name and commend that app opend with that commend
    'telegram': 'telegram-desktop',
    'vscode': 'code',
    'firefox' : 'firefox',
}


def clear_screen():
    os.system('clear')


def close_open_app(commend, name, method):
    try:
        if method == 'close':
            commend = f'killall {commend}'
        os.system(f'gnome-terminal -- bash -c "{commend}; exec bash"')
        voice.job_compleated(name, method)
        clear_screen()
        print(colors.success+f'{name} successfully {method}')
        return True
    except:
        clear_screen()
        print(colors.error+'we cant do that')
        return False


def open_app(commend, name):
    close_open_app(commend, name, 'open')
    n = notify2.Notification('Open App', f'{name} opened')
    n.show()


def close_app(commend, name):
    close_open_app(commend, name, 'close')
    n = notify2.Notification('Open App', f'{name} closed')
    n.show()
