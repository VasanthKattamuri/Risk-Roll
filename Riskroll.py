# print("Hello")


#rolling a dice using the function
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

# value = roll()
# print(value)   


#we will write in while true to handle the code in the exceptional case
while True:
    players = input("Enter the number of Players: ")
    #if the entered number is digit go to if condition
    if players.isdigit():
        players = int(players)
        if 2<=players<=4:
            print("The number of players: ",players)
            break
        else:
            print("The number must be from 2 to 4")
    else:
        print("Invalid, please try again")

max_score = 50
total_scores = [0 for _ in range(players)] #assigning the scores as zero for all the players what ever the number of players
# print(total_scores)
#prints an array like [0,0,0] if there are 3 players

#in the line above instead of giving the underscore we can use a variable like i but we dont have any use of the variable there so just keep _

while max(total_scores)<max_score:
    
    for player_idx in range(players):
#in the practice first write the code for 1 player first when he rolles then add a for loop so that same applies to all the players
        print("\nPlayer", player_idx+1, "turn has started") #we have added +1 because we say player 1 not player 0
        print("Your Total score is: ",total_scores[player_idx])
        current_score = 0
        #first we will ask them if they want to roll then start rolling 
        while True:
            asking_roll = input("Do u want to roll (y):")
            if(asking_roll.lower()!= "y"):
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Your turn is done!")
                current_score = 0
                break
            else:
                current_score+=value
                print("You rolled a number: ",value)

            print("Your score is: ",current_score)

        total_scores[player_idx] += current_score
        print("Your Total score is: ",total_scores[player_idx])

#now who ever reaches 50 we must display a msg saying that you won but after only when all the players completed the same number of turns

max_score = max(total_scores)
winning_idx  = total_scores.index(max_score)
print("Player number",winning_idx+1,"won with a score of: ",max_score)


            
        




    