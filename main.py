
import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_choice_card=[]
computer_choice_card=[]

def user_card():
  user_choice_card.append(random.choice(cards))
  user_choice_card.append(random.choice(cards))
  print(f"Your cards: {user_choice_card}")
  total= sum(user_choice_card)
  return(total)

def computer_card():
  computer_choice_card.append(random.choice(cards))
  computer_choice_card.append(random.choice(cards))
  return(computer_choice_card[0])

def user_ace_card():
  for i in range(0,len(user_choice_card)):
    if(user_choice_card[i] == 11):
      user_choice_card[i]=1


def computer_ace_card():
  for i in range(0,len(computer_choice_card)):
    if(computer_choice_card[i] == 11):
      computer_choice_card[i]=1
  
  
  
user_input= input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if (user_input == 'y'):
  print(art.logo)
  card_value = user_card()
  computer_first_card= computer_card()
  computer_total = sum(computer_choice_card)
  print(f"Current score: {card_value}")
  print(f"Computer's first card: {computer_first_card}")
  
  user_input= input("Type y for another card and n for pass: ")
  
  if(user_input == "y"):
    while(user_input == 'y'):
          computer_total= sum(computer_choice_card)
          user_choice_card.append(random.choice(cards))
          card_value = sum(user_choice_card)
      
          if(card_value>21):
            user_ace_card()
            card_value = sum(user_choice_card)
          
          print(f"Your cards again: {user_choice_card}")  
          print(f"Current score: {card_value}")
        
          if(card_value>21):
            print(f"computer second card: {computer_choice_card}")
            print("You loss")
            break

          if(computer_total>21):
            print("You win")
            print(f"computer cards: {computer_choice_card}")
            break
        
          user_input= input("Type y for another card and n for pass: ")

  if(user_input == 'n'):
    
    while (computer_total<21):
          computer_choice_card.append(random.choice(cards))
          computer_total= sum(computer_choice_card)
          if(computer_total>21):
            computer_ace_card()
            computer_total = sum(computer_choice_card)

    if(computer_total>21):
            print("You win")
            print(f"computer cards: {computer_choice_card}")
            
    elif(computer_total > card_value):
      print("You loss")
      print(f"computer cards: {computer_choice_card}")
    elif(card_value > computer_total):
      print("You win")
      print(f"computer cards: {computer_choice_card}")
    else:
      print("Draw")
      print(f"computer cards: {computer_choice_card}")
      
elif(user_input == 'n'):
        print("Game end!")



