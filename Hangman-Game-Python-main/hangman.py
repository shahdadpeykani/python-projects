import random
import hangman_art
import hangman_words
print(hangman_art.logo)
print()
chosen_word = random.choice(hangman_words.word_list)
lives = 6

display = []
for i in range(len(chosen_word)):
    display.append("_")
print(display)

while "_" in display:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
    if guess not in chosen_word:
        lives -= 1
        print("You guessed "+guess+", that is not in the word. you lose a life")
        print(hangman_art.stages[lives])
        if lives == 0:
            print("You lose.")
            print("Correct answer is: "+chosen_word)
            break
    print(display)
