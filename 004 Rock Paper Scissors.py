import random

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors")


comp_choice = random.randint(0, 2)

comp_img = ""
user_img = ""

if comp_choice == 0:
    comp_img = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

elif comp_choice == 1:
    comp_img = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

else:
    comp_img = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


if int(user_choice) == 0:
    user_img = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

elif int(user_choice) == 1:
    user_img = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

else:
    user_img = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print(user_img)
print(comp_img)

if int(user_choice) > comp_choice:
    if int(user_choice) == 2 and comp_choice == 0:
        print("You Loose")
    else:
        print("You win")

elif int(user_choice) == comp_choice:
    print("Its a tie")
else:
    print("You loose")