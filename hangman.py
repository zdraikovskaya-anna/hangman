import random

print("H A N G M A N")
words = ['javascript'] #['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
show_word = "-" * len(word)
input_letters = []
mode = 'play'
i = 0

while mode != 'exit':
    mode = input('Type "play" to play the game, "exit" to quit:')
    if mode == 'play':
        while i < 8:
            print()
            print(show_word)
            if show_word == word:
                break
            letter = input("Input a letter:")
            if len(letter) != 1:
                print("You should input a single letter")
            else:
                if ord(letter) not in range(97, 123):
                    print("Please enter a lowercase English letter")
                else:
                    if letter in input_letters:
                        print("You've already guessed this letter")
                    else:
                        input_letters.append(letter)
                        if letter in word:
                            for j in range(len(word)):
                                if word[j] == letter:
                                    show_word = show_word[:j] + letter + show_word[j+1:]
                        else:
                            i += 1
                            print("That letter doesn't appear in the word")

        if show_word == word:
            print("You guessed the word!")
            print("You survived!")
        else:
            print("You lost!\n")