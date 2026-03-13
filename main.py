import random
import hangman_words
import hangman_art


print (hangman_art.logo)


lives = 6     #<--- Total number of lives in the game

chosen_word = random.choice(hangman_words.word_list)    #<--- The code randomly chooses a word


placeholder = ""                                #
word_length = len(chosen_word)                  #
for position in range(word_length):             #   <---- This part of the code makes " _ " for the word that is chosen
    placeholder += "_"                          #
print("Word to guess: " + placeholder)          #


game_over = False
correct_letters = []   #<---- A list created to store the letter, if the letter is predicted correctly


while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}!")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"***********************It was {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
