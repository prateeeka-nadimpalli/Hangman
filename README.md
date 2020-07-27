This is a Python program of the game “Hangman”. The word to guess is represented by a row of dashes. If the player guess a letter which exists in the word, then all places in the answer where that letter appear will be revealed. If it is wrong you loose a life and the hangman begins to appear, piece by piece. The player has a chance of 6 wrong guesses.

                initial empty state

                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                   
                head
        
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
           head and torso
          
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                 
         head, torso, and one arm

                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   - 
          head, torso, and both arms
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -     
             head, torso, both arms, and one leg
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
            
              final hangman
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \                   -
         
          
           
         
          
