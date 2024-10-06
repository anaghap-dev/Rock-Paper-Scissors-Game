import random


print("\n-------------------------------------------------------")
print("                 Rock Paper Scissors")
print("-------------------------------------------------------")

print('Rules for this game!')
print("-------------------------------------------------------")
print("Rock vs Paper -> Paper wins \n"
      "Rock vs Scissors -> Rock wins \n"
      "Paper vs Scissors -> Scissors wins \n")

user = comp = 0
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors")
    ch = int(input("Enter your choice: "))

    while ch > 3 or ch < 1:
        ch = int(input('Enter a valid choice please : '))

    if ch == 1:
        choice_name = 'Rock'
    elif ch == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print('\nUser choice is:', choice_name)

    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if ch == comp_choice:
        result = "DRAW"
    elif (ch == 1 and comp_choice == 2) or (comp_choice == 1 and ch == 2):
        result = 'Paper'
    elif (ch == 1 and comp_choice == 3) or (comp_choice == 1 and ch == 3):
        result = 'Rock'
    elif (ch == 2 and comp_choice == 3) or (comp_choice == 2 and ch == 3):
        result = 'Scissors'

    print("-------------------------------------------------------")
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choice_name:
        print("<== User wins! ==>")
        user += 1
    else:
        print("<== Computer wins! ==>")
        comp += 1

    print('User: ', user, 'Computer: ', comp)
    print("-------------------------------------------------------")

    ans = input("Do you want to play again? (Y/N): ").lower()
    if ans == 'n':
        break

print("\n-------------------------------------------------------")
print("                     Final Score")
print("-------------------------------------------------------")
print('User: ', user, 'Computer: ', comp)
print("-------------------------------------------------------\n")
