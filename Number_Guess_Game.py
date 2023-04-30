#!/usr/bin/env python
# coding: utf-8

# In[37]:


import random
word_list=["mango","chiku","grapes"]
word_number=random.randint(0,2)
word=word_list[word_number]
Blank_list=[]
for i in range(len(word)):
    Blank_list.append("_")
print(Blank_list)
def guess_word():
    word=input("enter guess word ").lower()
    return word
print(f"word:{word}")
life=len(word)
chance=len(word)-1
print(chance)
while chance!=0:
    print(chance)
    alphabet=guess_word()
    if alphabet in word:
         index=word.index(alphabet)
         Blank_list[index]=alphabet
         print(Blank_list)
         if "_" in Blank_list:
             pass
         else:
            chance=0
            print(f" good job ! The final word is {word}")
            
               
            
            
    else:
        chance=chance-1
            
    
   
        
       
        
        
        
    
        
       


# In[ ]:


import random
word_list=["mango","apple","cherry"]
word_number=random.randint(0,2)
word=word_list[word_number]
Blank_list=[]
for i in range(len(word)):
    Blank_list.append("_")
print(Blank_list)
def guess_word():
    word=input("enter b
               guess word ").lower()
    return word
print(f"word:{word}")
alphabet=guess_word()
index=word.index(alphabet)
Blank_list[index]=alphabet
print(Blank_list)


# In[ ]:


word="mango"
alp=input("enter the word")
if alp in word:
    print("good")
else:
    print("explore more")




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


word="mango"
a=word[1]
b=word.index('g')
print(a)
print(b)


# In[ ]:


a=['c', 'h', 'i', 'k', 'u']

if "_" in a:
    print("sucess")
else:
    print("then also sucess")


# In[28]:


def play_game():
    import random
    global chance
    word_list=["mango","chiku","grapes"]
    word_number=random.randint(0,2)
    word=word_list[word_number]
    Blank_list=[]
    for i in range(len(word)):
        Blank_list.append("_")
    print(Blank_list)
   
    print(f"word:{word}")
    life=len(word)
    chance=len(word)-1
    print(chance)

    


# In[31]:


play_game()
def guess_word():
    word=input("enter guess word ").lower()
    return word
        


# In[32]:


def play_again():
    a=input("Do u want to play again yes or no ")
    if a=="yes":
        play_game()
        game_start()
        guess_word()
    elif a=="no":
        print("Thanks for visiting XYZ play area")
    
  


# In[33]:


play_again()


# In[27]:


def game_start():
    global chance
    while chance!=0:
        print(chance)
        alphabet=guess_word()
        if alphabet in word:
             index=word.index(alphabet)
             Blank_list[index]=alphabet
             print(Blank_list)
             if "_" in Blank_list:
                 pass
             else:
                chance=0




        else:
            chance=chance-1


# In[ ]:





# In[ ]:




