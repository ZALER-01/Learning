import random
wolrd_list = ['python', 'java', 'kotlin', 'javascript']
choosen_word = random.choice(wolrd_list)
print(choosen_word)


placeholder = '-'
word_length = len(choosen_word)

for position in range(word_length):
    placeholder += '-'
    print("word to guess: " + placeholder)

game_over = False
corrct_ansawer = []
while not game_over:
    user_guess = input("Guess a letter: ")
    if user_guess in choosen_word:
        corrct_ansawer.append(user_guess)
        print("Good guess: " + user_guess)
    else:
        print("Wrong guess: " + user_guess)


