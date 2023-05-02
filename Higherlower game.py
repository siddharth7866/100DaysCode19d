#!/usr/bin/env python
# coding: utf-8

# In[17]:


import random
data=[
    {'name':"siddharth",
     'follower':3400
       
    },
    {'name':"Amit",
     'follower':3900
       
    },
    {'name':"Sumit",
     'follower':7900
       
    },
    {'name':"sam",
     'follower':9900
       
    }
]



# In[ ]:


play=True
while play:
    d=[]
    data1=random.choice(data)
    data2=random.choice(data)
    while data1==data2:
        data1=random.choice(data)

    d.append(data1)
    d.append(data2)
#     print(d)
#     print(data2)
#     print(data1)
    highest=0
    answer=''

    for i in d:
        follower=i["follower"]
        if follower>highest:
            highest=follower
            answer=i['name']
        else:
             pass
               
            
            
                
                
                  

    # print(f"higest follower is {highest} for {answer} ")
    name1=data1["name"]
    name2=data2["name"]
    print(f"which one has more follower {name1} or {name2} enter the name ")
    user=input("enter the name")

    if answer==user:
        print("good")

    else:
        play=False
    
    
    
    
    


# In[15]:


highest=0
answer=''
while Play:
    for i in data:
        follower=i["follower"]
        if follower>highest:
            highest=follower
            answer=i['name']
        else:
            pass
        
       
print(f"higest follower is {highest} for {answer} ")

user=input("enter the name")

if answer==user:
    print()


        
        


# In[35]:


d=[]
data1=random.choice(data)
data2=random.choice(data)
while data1==data2:
    data1=random.choice(data)

d.append(data1)
d.append(data2)
print(d)
# print(data2)
# print(data1)
print(data1["name"])
print(data2["name"])


# In[ ]:




