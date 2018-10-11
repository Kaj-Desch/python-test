import sys

turns = 10
secret_word = "hedgehog"
guesses = [" "]

while turns > 0:
    print("")
    print(guesses)
    guess_is_valid = False
    while (not guess_is_valid):
        guess = input("Guess an letter ")
        if len(guess) != 1:
            print("Whoa! Slow down! One letter at a time")
            continue
        if guess in guesses:
            print("Your memory clearly sucks, cuase you already guessed that!")
            continue
        guess_is_valid = True
    guesses.append(guess)
    if (guess in secret_word):
        turns -= 0
    else:
        turns -= 1
    win = True
    for letter in secret_word:
        if (letter in guesses):
            sys.stdout.write(" " + letter + " ")
            turns -= 0
        else:
            win = False
            sys.stdout.write(" _ ")
    print("")
    print("")
    print("You have " + str(turns) + " turns left")
    if (win):
        print("")
        print("You win")
        exit()
print("")
print("you lose")
print("the word was " + secret_word)
