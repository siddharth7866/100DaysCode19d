#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
number_list=[20,25,30,35,40]
number=random.choice(number_list)
print("Lets Play Number guess game")
game_level=input(" easy or hard ")
if game_level=="easy":
    life=10
    print("Life = 10 ")
else:
    life=5
    print("Life = 5 ")


while life !=0:
    chose_number=int(input("enter the number"))
    if chose_number==number:
        print(f"You got the right answer {number} ")
        life=0
    elif chose_number<number:
        print(f"The chooses numbers is too small")
        life=life-1
    elif chose_number>number:
        print(f"The chooses numbers is too high")
        life=life-1
        
        
        
        


# In[ ]:




