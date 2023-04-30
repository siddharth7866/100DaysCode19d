#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
word_list=["mango","cherry","baboon","litchi"]
word=random.choice(word_list)

life=len(word)
Blank_list=[]
for i in range(len(word)):
        Blank_list.append("_")
# print(Blank_list)
print(word)
while life!=0:
    guess=input(" guess word ")
    print(life)
    if guess in word:
        
        print("yes")
        print(life)
        for i in range(len(word)):
            if word[i]==guess:
                Blank_list[i]=guess
                print(Blank_list)
                if "_" in Blank_list:
                    continue
                else:
                    life=0
                    print(f"Great Job the word is {Blank_list} ")



    else:
        print("no")
        life=life-1
        print(Blank_list)





# In[ ]:




        


# In[ ]:




