import random
print("welcome to the hangman game")
instructions=input("do you know to see the instructions [yes or no] \n").lower()
if instructions == "yes":
     print(''' you will guess a letter depended on the space that appears to you
     2. if your guess is wrong , a part of the peaniata appears
     3.when tha all peaniata appears you lose 🤔
     4. else if your guess is right , you win 😎
           ''')
else:
     print("are you ready let's go 😉")
# مراحل هانج مان بالسكي عشان احطها في قائمة واطلع الاندكس بتاعها يسهولة
hangman_stage=[
    '''+---+
  |   |
      |
      |
      |
      |
=========''', 

''' +---+
  |   |
  O   |
      |
      |
      |
=========''', 

'''+---+
  |   |
  O   |
  |   |
      |
      |
=========''', 

''' +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 

'''+---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 

''' +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 

'''+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
] 

words=["mody", "yassien", "samy"]
random_word=random.choice(words)
display=["_"]*len(random_word)
print(" ".join(display))
lives=6
guessed_letters=[]
print(hangman_stage[0])
while "_" in display and lives>0:
    guessed=input("please guess a letter :\n").lower()
    if guessed in guessed_letters:
        print("you already guessed that . please try again")
        print(f"you have[{lives}]more tries")
        continue
    guessed_letters.append(guessed)
    if guessed not in random_word:
        lives-=1
        print(hangman_stage[6-lives])
    else:
        for position in range(len(random_word)):
            if random_word[position]==guessed:
                display[position]=guessed
    print(" ".join(display))   
    print(f"you have[{lives}] more tries")
if  lives ==0:
        print('''
        you lose!
        ''')
        print(hangman_stage[-1])  
else:
     print("***** YOU WIN *****")  
   








