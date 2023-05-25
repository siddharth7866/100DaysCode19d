#!/usr/bin/env python
# coding: utf-8

# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[10]:


word=input("please enter the word/number which you want to check for pallindrome ")
len_word=len(word)
reverse=[]
pallindrome=""
j=1
for i in range(len_word):
    
#     print(word[i])
    if word[i]==word[len_word-j]:
        j=j+1
        reverse.append(word[i])
        
    else:
        pass
        
        
new_word=pallindrome.join(reverse)

# print(new_word)
if new_word==word:
    print(f"Yes the given word/number {word} is pallindrome ")
else:
    print(f"No the given word/number {word} is not pallindrome ")
    
        
    


# In[ ]:




