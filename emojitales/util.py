import os
import sys
import unicodedata


def clear_terminal():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def exit():
    print("\nGoodbye!\n")
    sys.exit(0)


def list_text_files(directory):
    all_files = os.listdir(directory)
    files_list = [file for file in all_files if os.path.isfile(os.path.join(directory, file)) and file.endswith('.txt')]
    
    return files_list


def lookup_emoji(name):
    try:
        return unicodedata.lookup(name)
    except KeyError:
        return None
    

def open_file(file_path):
    try:
        return open(file_path, 'r')
    except FileNotFoundError:
        return None

def singularize(word):
    if word.endswith('IES'):
        return word[:-3] + 'Y'
    elif word.endswith('ES') and word[-3] in ['X', 'Z'] or word[-4:-2] in ['CH', 'SH', 'SS']:
        return word[:-2]
    elif word.endswith('S') and not word.endswith('SS'):
        return word[:-1]
    else:
        return word


def map_color(word):
    colors = {
        'RED': 'LARGE RED CIRCLE',
        'ORANGE': 'LARGE ORANGE CIRCLE',
        'YELLOW': 'LARGE YELLOW CIRCLE',
        'GREEN': 'LARGE GREEN CIRCLE',
        'BLUE': 'LARGE BLUE CIRCLE',
        'PURPLE': 'LARGE PURPLE CIRCLE',
        'BROWN': 'LARGE BROWN CIRCLE',
        'BLACK': 'MEDIUM BLACK CIRCLE',
        'WHITE': 'MEDIUM WHITE CIRCLE',
    }

    return colors.get(word)
