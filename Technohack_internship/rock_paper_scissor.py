import random
rock = "0"
paper ="1"
scissors ="2"
game_choices = [rock, paper, scissors]

print("welcome to rock paper scissors game")
choice=int(input("what do you choose? type 0 for rock, type 1 for paper, type 2 for scissors\n"))
print(game_choices[choice])
           
display_choice=random.randint(0, 2)
print("computer choose:")
print(game_choices[display_choice])


if choice>=3 or display_choice<0:
    print("the number you typed is invalid, you lose")
elif choice==0 and display_choice==2:
    print ("you win")
elif display_choice==0 and choice==2:
    print("you lose")
elif display_choice>choice:
    print("you lose")
elif choice>display_choice:
    print("you win")
elif display_choice==choice:
    print("it is a draw")
    
    
    
    