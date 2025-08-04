import random
dict = { "s":1 , "g":0, "w":-1 }
reversedict = {1:"snake",0:"gun",-1:"water"}

user_score = 0
computer_score = 0
rounds = 5 

print("Welcome to Snake-Water-Gun game!")
print("Rules : snake>water , water>gun , gun>snake\n")

for round_no in range(1, rounds+1):
    print(f"\n Round {round_no}")
    computer = random.choice([-1,0,1])
    userstr = (input("Enter your choice here (s is for snake ,g is for gun or w is for water): "))
    
    if userstr not in dict:
        print("Invanlid input ! Round skipped. ")
        continue

    user = dict[userstr]
    print(f" You chose {reversedict[user]}\ncomputer chose {reversedict[computer]}")
    









    
    
                    
    if(computer == user):
        print("Its a draw")
        print(f"Current Score :: You : {user_score} | Computer:{computer_score}")
        

    else:
        if(computer ==-1 and user == 1): 
            print("You Win!")
            user_score +=1
            print(f"Current Score :: You : {user_score} | Computer:{computer_score}")

        elif(computer ==-1 and user == 0):
            print("You Lose!")
            computer_score +=1
            print(f"Current Score :: You : {user_score} | Computer:{computer_score}")

        elif(computer == 1 and user == -1):
            print("You Lose!")
            computer_score +=1
            print(f"Current Score :: You : {user_score} | Computer:{computer_score}")

        elif(computer ==1 and user == 0):
            print("You Win!")
            user_score +=1
            print(f"Current Score :: You : {user_score} | Computer:{computer_score}")

        elif(computer ==0 and user == -1):
            print("You Win!")
            user_score +=1
            print(f"Current Score :: You : {user_score} | Computer:{computer_score}")

        elif(computer == 0 and user == 1):
            print("You Lose!")
            computer_score +=1
            print(f"Current Score :: You : {user_score} | Computer:{computer_score}")

        

        else:
            print("Something went wrong!")




print("\n Game Over!")
print(f"Your score : {user_score}")
print(f"Computer's score : {computer_score}")


if user_score>computer_score:
    print("Congratulations ! You are the winner of this game . ")
elif computer_score>user_score:
    print("Computer wins this game")
else:
    print("It's a tie!")