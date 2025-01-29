import random

def display_rules():
    print("Welcome to the Game of Pig!")
    print("Roll the die as many times as you want or hold")
    print("If you roll one, you lose the score from the current turn")
    print("The first player to score 100 or more wins!")

def congratulate(winner): 
    print(f"Congratulations, {winner}")


def player1_turn(player_total): 
    score_turn = 0 
    hold = False

    while not hold:  
        
        eyes = random.randint(1,6) 
        print(f"You rolled a {eyes}.")
        if eyes == 1: 
          print("Total this turn: 0")
          return 0
        score_turn += eyes
        
        # check if the player already has more than 100 total points
        # if so, don't ask again for another roll
        if player_total + score_turn >= 100: 
          return score_turn 
 
        print(f"Points for turn: {score_turn}")    
        ans = input("Do you want to hold (y/n):") 
        hold = ans == 'y'
    return score_turn
             
            
def player2_turn(player_total): 
    score_turn = 0 
    hold = False

    while not hold:  
        
        eyes = random.randint(1,6) 
        print(f"You rolled a {eyes}.")
        if eyes == 1: 
          print("Total this turn: 0")
          return 0
        score_turn += eyes
        
        # check if the player already has more than 100 total points
        # if so, don't ask again for another roll
        if player_total + score_turn >= 100: 
          return score_turn 
 
        print(f"Points for turn: {score_turn}")    
        hold = score_turn > 20
        if hold:
          print("Hold.")
        else: 
          print("Roll.")
          
    return score_turn
             
      
 

def play_game():

    player1_total = 0
    player2_total = 0 

    while player1_total < 100 and player2_total < 100: 

      print(f"Your turn. Current total: {player1_total}")
      p1_score_turn = player1_turn(player1_total) # get score for this turn only
      player1_total += p1_score_turn

      if player1_total < 100: 
        print(f"Computer turn. Current total: {player2_total}")
        p2_score_turn = player2_turn(player2_total) # get score for this turn only
        player2_total += p2_score_turn

    if player1_total > player2_total: 
      return "Player"
    else: 
      return "Computer"
 

def pig():
  
  display_rules()  

  winner = play_game()

  congratulate(winner)


if __name__ == "__main__":
  pig()
