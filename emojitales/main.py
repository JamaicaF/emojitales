import string
import time

import text_constants
from util import (
    clear_terminal,
    exit,
    list_text_files,
    lookup_emoji,
    map_color,
    open_file,
    singularize,
    wrap_text,
)


def init():
    clear_terminal()
    render_intro()
    render_story_options()


def render_intro():
    icon = lookup_emoji("FAIRY") or ("")
    title = f"\n\n{icon}   EMOJI TALES   {icon}\n\n"

    print(title)
    for line in text_constants.APP_INTRODUCTION.split("\n"):
        time.sleep(1.2)
        print(wrap_text(line))


def render_story_options():
    stories = create_story_list()
    time.sleep(2)

    if len(stories):
        print("\nTable of Contents:")
        for index, (title, _) in enumerate(stories):
            print(f"\n   {index + 1} - {title}")
            time.sleep(0.5)
    else:
        print("\nNo stories found.")

    select_story(stories)


def create_story_list():
    files = list_text_files(text_constants.SOURCE_TEXT_FILE_PATH)

    stories = []
    for file in files:
        title = file.replace("_", " ").replace(".txt", "").title()
        stories.append((title, file))

    return stories


def select_story(stories):
    selection = handle_select_input(stories)
    time.sleep(1)

    if not selection:
        print("\nInvalid input. Enter a number to choose a story.")
        time.sleep(1)
        select_story(stories)

    display_story(selection)


def handle_select_input(stories):
    if len(stories):
        print("\n\nChoose a story.")
    print(
        wrap_text(
            "To translate your own story, add it as a `.txt` file to the `source_texts` directory. Then enter 'R' to refresh the story list."
        )
    )
    selection = input("Or enter 'X' to exit: ").strip()

    if selection.upper() == "X":
        exit()
    elif selection.upper() == "R":
        render_story_options()

    else:
        try:
            title_index = int(selection) - 1
            if 0 <= title_index < len(stories):
                title = stories[title_index][0]
                filename = stories[title_index][1]

                return {"title": title, "filename": filename}
            else:
                return None
        except ValueError:
            return None


def display_story(selection):
    display_text = input(
        f"\n{wrap_text('This is less fun, but display the original text, too? (y/N): ')}"
    ).upper()

    clear_terminal()
    print(f"\n\n{wrap_text(f"{selection['title']} {parse_text(selection['title'])}")}")
    time.sleep(1)

    file = open_file(f"{text_constants.SOURCE_TEXT_FILE_PATH}{selection['filename']}")
    if not file:
        print("\nStory not found.")
        render_story_options()

    # files do not have line_count property, so first get total file length to know where file ends
    line_count = 0
    for line in file:
        line_count += 1

    file.seek(0)  # start again from beginning of file
    for line_number, line in enumerate(file):
        if display_text == "Y":  # only show original text if user explicitly requested
            print(f"\n{wrap_text(line)}")
        emojis = parse_text(line)

        if len(emojis):
            print(f"\n\n{emojis}\n\n")

            if line_number < line_count - 1:
                input("Press Enter to continue...")

    file.close()
    print(f"\n\nThe End\n\n")
    time.sleep(1)
    handle_end_of_story()


def handle_end_of_story():
    selection = input("Press Enter to continue or enter 'X' to exit: ").strip()

    if selection.upper() == "X":
        exit()
    else:
        render_story_options()


def parse_text(text):
    word_list = []
    word = ""
    for i, char in enumerate(text):
        if char.isalpha():
            word += char.upper()
            if i == len(text) - 1:
                word_list.append(word)
        elif len(word) > 0 and (char == " " or char in string.punctuation):
            word_list.append(word)
            word = ""
        else:  # TODO: handle other char types
            continue

    emojis = convert_text_to_emojis(word_list)

    return emojis


def convert_text_to_emojis(word_list):
    emojis = ""
    for word in word_list:
        variations = create_emoji_lookup_list(word)

        for var in variations:
            emoji = lookup_emoji(var)

            if emoji and emoji.isprintable():  # catch any non-printable unicode
                emojis += f"{emoji}  "
                break

    return emojis


# generate list of word forms to improve emoji lookup matching
def create_emoji_lookup_list(word):
    variations = [word]

    singular = singularize(word)
    if word != singular:
        variations.append(singular)

    # many animals and emotions use 'face' in descriptor name
    variations.append(singular + " FACE")

    # represent colors when possible
    color = map_color(word)
    if color:
        variations.append(color)

    return variations


init()
