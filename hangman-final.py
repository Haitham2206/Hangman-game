
bold_blue_color = "\033[1;34;m"
bold_black_color = "\033[1;30;m"
bold_red_color = "\033[1;31;m"
bold_green_color = "\033[1;32;m"
HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""

MAX_TRIES = 7
HANGMAN_PHOTOS = {1: " x-------x", 2: """    
 x-------x
 |
 |
 |
 |
 |
""", 3: """
 x-------x
 |       |
 |       0
 |
 |
 |""", 4: """
  x-------x
  |       |
  |       0
  |       |
  |
  |""", 5: """
 x-------x
 |       |
 |       0
 |      /|\\
 |
 |""", 6: """
 x-------x
 |       |
 |       0
 |      /|\\
 |      /
 |""", 7: """
 x-------x
 |       |
 |       0
 |      /|\\
 |      / \\
 |"""}


def choose_word(file_path, index):
    """This method gets a word from the file according to the input of the user
    :param file_path: The path of the text file that containing the words
    :param index: The index of the word chosen by the user
    :return: The secret word."""
    with open(file_path, 'r') as content:
        data = content.read().split(' ')
    while index > len(data):
        index = index - len(data)
    return data[index - 1]


def show_hidden_word(secret_word, old_letter_guessed):
    """This method takes a word and list of letters, and returns corresponding letters from the list in a word.
    :param secret_word: the word to guess.
    :param old_letter_guessed: The list with old guessed letters.
    :return : corresponding letters in there position in the secret word."""

    underscore_list = ['_']*len(secret_word)

    for i in old_letter_guessed:
        if i in secret_word:
            n = 0
            while n < len(secret_word):
                if i == secret_word[n]:
                    underscore_list[n] = i
                n += 1
    return ' '.join(underscore_list)


def check_win(secret_word, old_letter_guessed):
    """This method checks if the user succeeds to guess all the letters of the secret word.
    :param secret_word: the word to guess.
    :param old_letter_guessed: The list with old guessed letters.
    :return: True if succeeded or false otherwise."""

    if '_' in show_hidden_word(secret_word, old_letter_guessed):
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letter_guessed):
    """This method checks if the input is valid, and if it is already guessed.
    :param letter_guessed: input from the user.
    :param old_letter_guessed: list of already guessed letters.
    :return: true if its is a new valid guess, false otherwise."""
    if not check_valid_input(letter_guessed, old_letter_guessed):
        print("X")
        return False
    else:
        old_letter_guessed.append(letter_guessed)
        return True


def check_valid_input(letter_guessed, old_letter_guessed):
    """This method checks if the input is valid, and if it is already guessed.
    :param letter_guessed: input from the user.
    :param old_letter_guessed: list of already guessed letters.
    :return: true if its is a new valid guess, false otherwise."""
    if len(letter_guessed) > 1 \
       or not (chr(65) <= letter_guessed <= chr(90)
       or chr(97) <= letter_guessed <= chr(122)) \
            or letter_guessed.lower() in old_letter_guessed\
            or letter_guessed.upper() in old_letter_guessed:
        return False
    else:
        return True


def colored_hangman_photos(number_of_tries):
    """This method prints colored HANGMAN PHOTOS
    :param number_of_tries: number of tries to guess a correct letter"""
    if 1 <= number_of_tries <= 2:
        print(bold_green_color)
        return HANGMAN_PHOTOS[number_of_tries]
    elif 3 <= number_of_tries <= 4:
        print(bold_blue_color)
        return HANGMAN_PHOTOS[number_of_tries]
    else:
        print(bold_red_color)
        return HANGMAN_PHOTOS[number_of_tries]


def main():
    # Variables
    old_letters_guessed = []
    num_of_tries = 1
    print(bold_blue_color)  # Bold blue color
    print(HANGMAN_ASCII_ART)
    print("Maximum tries: %d" % (MAX_TRIES - 1))
    print(bold_black_color)  # Bold black color
    file_path = input("Enter a path to the words file: \n")

    while True:
        # Check valid input
        print(bold_black_color)  # Bold black color
        number = input("Enter a random number: \n")
        try:
            val = int(number)
            break
        except ValueError:
            print(bold_red_color)  # Bold red color
            print("That is not a number. Try again!")
    secret_word = choose_word(file_path, int(number))
    print("Let's start! \n\n")
    print(bold_green_color)  # Bold green color
    print("\t %s\n" % HANGMAN_PHOTOS[1])

    while True:
        print(bold_black_color)  # Bold black color
        print(show_hidden_word(secret_word, old_letters_guessed))
        letter = input("Guess a letter: ")
        is_correct = try_update_letter_guessed(letter, old_letters_guessed)
        if letter not in secret_word and is_correct:
            num_of_tries += 1
            print(":(")
            print('->'.join(old_letters_guessed))
            print("\t %s\n" % colored_hangman_photos(num_of_tries))
        elif not is_correct:
            print('->'.join(old_letters_guessed))
            print(bold_red_color)  # Bold red color
            print("Not valid input or already guessed letter. Try again!")
        if num_of_tries == MAX_TRIES:
            print("Game over.")
            print("The secret word is: '%s'" % secret_word)
            break

        win = check_win(secret_word,old_letters_guessed)
        if win:
            print("\n" + ' '.join(secret_word), end="")
            print(bold_green_color)
            print("Congratulation!! you won!")
            break


if __name__ == "__main__":
    main()