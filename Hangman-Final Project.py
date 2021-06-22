"""
Self.py course - Final Project - HANGMAN!
Made by: Almog Braunstein
"""

# -----------------------------------------------------game functions---------------------------------------------------
from string import ascii_lowercase
from termcolor import colored


def opening_screen():
    """prints the game logo with a welcoming sentence."""
    hangman_logo = colored("""
         _    _                                         
        | |  | |                                        
        | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
        |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | |  | | (_| | | | | (_| | | | | | | (_| | | | |
        |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                             __/ |                      
                            |___/

       """, 'blue')
    print(hangman_logo)
    print(f"Welcome to Hangman game!!\n"
          f"{player_one} you have", MAX_TRIES,
          "attempts to try and guess all the letters of the secret word. "
          "good luck!")


def update_screen(num_of_tries):
    """
    prints the current status of the game
    :param num_of_tries: the number of incorrect tries
    :type num_of_tries: int
    :return: current status of the game according to number of tries
    :rtype: str
    """
    picture_1 = colored("""    x-------x




    """, 'red')
    picture_2 = colored("""    x-------x
    |
    |
    |
    |
    |""", 'red')
    picture_3 = colored("""    x-------x
    |       |
    |       0
    |
    |
    |
""", 'red')
    picture_4 = colored("""
    x-------x
    |       |
    |       0
    |       |
    |
    |""", 'red')
    picture_5 = colored("""
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 'red')
    picture_6 = colored("""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / 
    |
""", 'red')
    picture_7 = colored("""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""", 'red')
    hangman_photos = {1: picture_1, 2: picture_2, 3: picture_3, 4: picture_4, 5: picture_5, 6: picture_6, 7: picture_7}
    if num_of_tries == 6:
        print("Sorry", colored(player_one, 'green'), "you loose :( ")
        print(colored(player_two, 'red'), "is the winner !")
        return hangman_photos[7]
    else:
        return hangman_photos[num_of_tries + 1]


def choose_word(file_path, index):
    """
    Selects a secret word placed by the index parameter in the "file path" file
    :param file_path: the direction to the file
    :param index: the index of the word in the file
    :type file_path: str
    :type index: int
    :return: The secret word.
    :rtype: str
    """
    with open(file_path, "r") as file:
        global secret_word
        non_duplicate_list_of_words = []
        list_of_words = file.read().split()
        for word in list_of_words:
            if word not in non_duplicate_list_of_words:
                non_duplicate_list_of_words.append(word)
            else:
                continue
        index_from_list = index - 1
        if index_from_list < len(list_of_words):
            secret_word = list_of_words[index_from_list]
        else:
            secret_word = list_of_words[(index % len(list_of_words)) - 1]

        return secret_word


def show_hidden_word(secret_word, old_letters_guessed):
    """The function returns a string made of bottom lines and letters that have been guessed in their accurate position.
    :param secret_word: The word to guess
    :param old_letters_guessed: A list of letters that was guessed earlier
    :type secret_word: str
    :type old_letters_guessed: list
    :return: hidden word made of correct letters and bottom lines
    :rtype: str
    """
    hidden_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter
        else:
            hidden_word += "_ "
    return hidden_word


def check_win(secret_word, old_letters_guessed):
    """Checks if the player succeeded to guess correctly all the letters of the secret word
    :param secret_word: The word to guess
    :param old_letters_guessed: A list of letters that were guessed already
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if all the letters of the secret word were guessed and otherwise returns False
    :rtype: bool
    """
    for letter in secret_word:
        if letter in old_letters_guessed:
            continue
        else:
            return False
    return True


def make_a_guess():
    """Asking a player to guess a letter"""
    global letter_guessed
    letter_guessed = input("Please enter your guess: ")
    return letter_guessed


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks if the guessed letter is valid and if it was guessed earlier in the game.
    :param letter_guessed: a letter that the player guessed
    :param old_letters_guessed: list of guessed letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True only if the letter is valid and wasn't guessed already.
    :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) != 1:
        print("You have to choose only 1 letter!")
        return False
    elif not letter_guessed.isalpha():
        print("You have to choose an alphabetic letter!")
        return False
    elif letter_guessed in old_letters_guessed:
        print("You have already guessed this letter, please try and guess a new one.")
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks if its valid to add the guessed letter to the list of old letters guessed
    :param letter_guessed: a letter that the player guessed
    :param old_letters_guessed: list of guessed letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True only if the letter is valid and wasn't guessed already.
             False if the letter is invalid or exist in the list already.
    :rtype: bool and str
    """
    global remaining_letters
    remaining_letters = list(ascii_lowercase)
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letters_guessed) is True:
        old_letters_guessed.append(letter_guessed)
        remaining_letters.remove(letter_guessed)
        print('Letters you have guessed:', ', '.join(old_letters_guessed))
        print('Remaining letters:', ' '.join(remaining_letters))
        print('\n')
        return True
    else:
        print('X')
        new_list = sorted(old_letters_guessed)
        new_list = "-->".join(new_list)
        print("old letters: ", new_list)
        print('Remaining letters:', ' '.join(remaining_letters))
        print('\n')
        return False


def game_mode():
    """
    I have decided to make 2 options for playing the game:
    The first one is against the computer, and then we'll use the words file.
    The second one is vs. another player and then the second player get to choose the secret word.
    """

    global player_two
    global secret_word
    mode = input('Please enter 1 for single player mode or 2 for two players mode: ')
    if mode.strip() == '1':
        player_two = 'The computer'
        file_path = input("Please enter the path to your words' file:\n")
        index_for_word = int(input("Please choose the index(an integer) of the word you'll like to use from the "
                                   "file: "))
        choose_word(file_path, index_for_word)
    elif mode.strip() == '2':
        player_two = input('Please enter the name of the rival player that will provide the secret word: ')
        word = (input('Please enter your word: ')).lower()
        secret_word = word
        print('\n' * 40)
    else:
        game_mode()


# -----------------------------------------------------game play--------------------------------------------------------
def hangman():
    """
    This function gathers the game functions and all of the actions and the inputs needed for the game to run.
    """
    global MAX_TRIES
    global num_of_tries
    global player_one
    global old_letters_guessed

    num_of_tries = 0
    MAX_TRIES = 6
    old_letters_guessed = []

    player_one = input("Welcome Player, please enter your name:\n")
    game_mode()
    opening_screen()
    print(update_screen(num_of_tries))
    print(show_hidden_word(secret_word, old_letters_guessed))

    # As long as the player didn't use all of his incorrect attempt the game will keep running.
    while num_of_tries < 6:
        make_a_guess()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed) is True and letter_guessed not in secret_word:
            num_of_tries += 1
        show_hidden_word(secret_word, old_letters_guessed)
        print(f'you have {MAX_TRIES - num_of_tries} attempts left.')
        print(update_screen(num_of_tries))
        print(show_hidden_word(secret_word, old_letters_guessed))
        print('\n' * 2)
        if check_win(secret_word, old_letters_guessed):
            print("Congratulations!! the secret word was: ", (colored(secret_word, 'yellow')))
            print(colored(player_one, 'green'), "is the winner")
            break


def main():
    hangman()


if __name__ == '__main__':
    main()
