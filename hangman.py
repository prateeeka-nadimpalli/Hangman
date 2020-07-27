import random


def get_word():
    word_list = ['wares','soup','mount','extend','brown','expert','tired','humidity','backpack','crust','dent','market','knock','smite','windy','coin',
    'throw','silence','bluff','downfall','climb','lying','weaver','snob','kickoff','match','quaker','foreman','excite','thinking','mend','allergen','pruning','coat','emerald',
    'coherent','manic','multiple','square','funded','funnel','sailing','dream','mutation','strict','mystic','film','guide','strain','bishop','settle','plateau','emigrate',
    'marching','optimal','medley','endanger','wick','condone','schema','rage','figure','plague','aloof','there','reusable','refinery','suffer','affirm','captive',
    'flipping','prolong']
    word = random.choice(word_list)
    return word


def play(word):
    complete_word = "_" * len(word)
    guessed = False
    gue_let = []
    gue_wds = []
    t = 6
    print("Start Hangman!")
    print(display_hangman(t))
    print(complete_word)
    print("\n")
    while guessed==False and t > 0:
        g = input("guess a letter or word: ")
        if len(g) == 1 and g.isalpha():
            if g in gue_let:
                print("You already guessed the letter")
            elif g not in word:
                print("gussed letter is not in the word.")
                t=t-1
                gue_let.append(g)
            else:
                print("Good job, letter is in the word!")
                gue_let.append(g)
                complete_word_list = list(complete_word)
                ind = []
                for i,let in enumerate(word):
                    if let == g:
                        ind.append(i)
                for index in ind:
                    complete_word_list[index] = g
                complete_word = "".join(complete_word_list)
                if "_" in complete_word:
                    guessed = False
                else:
                    guessed = True

        else:
            print("Not a valid guess.")
        print(display_hangman(t))
        print(complete_word)
        print("\n")
    if guessed:
        print("Congrats,You win!")
    else:
        print("Sorry, The word was " + word)


def display_hangman(t):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[t]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (y/n) ") == "y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
