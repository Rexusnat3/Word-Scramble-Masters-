import json
import random


def word_to_scramble(data, max_length=6):
    """pull a word from my dictionary file by filtering
    out all words that are between 3 and the max length of characters
    :param data: merriam_webster dictionary
    :param max_length: maximum length of the word bank """
    filtered_words = []
    for w in data:
        if 3 <= len(w) <= max_length:  # here is where the filtering is made
            filtered_words.append(w)  # here I add the filtered words to the list
    if filtered_words:
        return random.choice(filtered_words)  # returns a random word from the list


def dictionary_data(filename):
    """Read a file and returns a file
    :param filename: name of the file to read
    :return: data from dictionary"""
    with open(filename) as file:
        data = json.load(file)  # here I load the JSON file
    return data


def scramble_word(word_):
    """Function to scramble the letters of the word
    :param word_: word taken from list to scramble
    :return: the word scrambled"""
    char_list = list(word_)  # convert the characters into a list
    random.shuffle(char_list)  # shuffle the list
    scrambled_word = ''.join(char_list)  # then join the characters back
    while scrambled_word == word_:  # make sure the word is
        random.shuffle(char_list)   # different from the original
        scrambled_word = ''.join(char_list)  # join the scrambled characters again
    return scrambled_word


def get_hint(word, word_data):
    """ Get the meaning from the dictionary data file to give as a hint
    :param word: the word to use
    :param word_data: """
    return word_data[word]


def word_scramble_masters():
    """ here is the game itself """
    filename = 'webster_dictionary.json'
    word_data = dictionary_data(filename)  # Load the data from the webster_dictionary file

    print("Welcome to the Word Scramble Masters!")
    score = 0  # Starting score of the game

    while True:
        word = word_to_scramble(word_data, 6)  # Get a random word from the data then set the max length to 6 characters

        scrambled_word = scramble_word(word)  # scramble the word like eggs

        print(f"\nScrambled word: {scrambled_word}")  # Serve up breakfast of scrambled word

        hint = input("Want a hint? (Type 'h' for a hint, press enter to skip): ").strip().lower()  # give hint if wanted

        if hint == 'h':
            word_meaning = get_hint(word, word_data)  # Get the definition as a hint
            print(f"\nHint: {word_meaning}")

        guess = input("Your guess: ").strip().lower()

        # Check if the guess is correct
        if guess == word.lower():
            print("Correct!")
            score = score + 10  # add to the score function written on line 42
        else:
            print(f"Wrong! The correct word was: {word}")
            score = score - 5  # since the function is false, take away points

        # Display current score
        print(f"Current Score: {score}")

        # Ask if the player wants to play again
        play_again = input("\nKeep playing? (y/n): ").strip().lower()
        if play_again != 'y':
            break  # Loop exit for when player wants to stop playing

    print("\nThank you for playing!")
    print(f"Final Score: {score}")  # Final score display


if __name__ == "__main__":
    word_scramble_masters()  # Run the Word_Scramble_Masters function if the entire code was read correctly
