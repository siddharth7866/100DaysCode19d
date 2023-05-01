#!/usr/bin/env python
# coding: utf-8

# In[ ]:


d=3
bid={}
while d!=0:
#     bid={}
    name=input("name ")
    amount=int(input("amount"))
    bid[name]=amount
    
#     updated_bid={**bid,name:amount}
    
    d-=1
print(bid)


# In[ ]:


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
for keys in student_scores:
    if student_scores[keys] >91:
       student_scores[keys]="Outstanding"
    elif  81 <= student_scores[keys] < 91:
        student_scores[keys]="Exceeds expectations"
    elif  71 < student_scores[keys] < 80:
        student_scores[keys]="Acceptable"
    elif   student_scores[keys] <= 70:
        student_scores[keys]="Fails"
    print(student_scores[keys])
    print(keys)
print(student_scores)




# In[ ]:


a=['sid','vishen','shahi']
amount=[32,43,98]
b={}
for i in a:
    b.update({i:98})
print(b)


# In[ ]:


my_dict = {}

# Ask the user for input and add to the dictionary until they enter 'quit'
while True:
    key = input("Enter a key (or 'quit' to exit): ")
    if key == 'quit':
        break
    value = input("Enter a value: ")
    my_dict[key] = value

# Print the dictionary
print(my_dict)


# In[ ]:


travel_log={
    "France":["paris","Lille","Dijon"],
    "Germany":["berlin","munich","Hamburg"]
}
travel_log['cities_visited']=travel_log
travel_log


# In[ ]:


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


# In[ ]:


travel_log[0]


# In[ ]:


def add_new_country(a,b,c):
    new_contry={}
    new_contry["country"]=a
    new_contry["visits"]=b
    new_contry["cities"]=c
    travel_log.append(new_contry)
    print(travel_log)
    
    

    


# In[ ]:


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])


# In[ ]:


a=['sid',"Amit"]

def update_list(v):
    a.append(v)
    print(a)
    


# In[ ]:


update_list("vishen")


# In[ ]:


update_list({"sid":"vishen"})


# In[ ]:


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}


# In[ ]:


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
for key in dict:
    print(key)
    dict[key]=dict[key]+1
print(dict)


# In[ ]:


dict[1]=4


# In[ ]:


print(dict["a"])


# In[ ]:


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}


# In[ ]:


print(order['main'][2][0])


# bid={}
# Yes=True
# d=0
# name=''
# while Yes:
#     name=input('enter the name ')
#     amount=int(input("enter the amount "))
#     bid[name]=amount
#     user=input(" Any another bidder Yes or No ")
#     if user == "No":
#         Yes=False
#         print(bid)
#         for i in bid:
#             if bid[i]>d:
#                 d=bid[i]
#                 name=i
#     else:
#         pass
# print(d)
# print(name)

# In[ ]:


d=0
a={'sid': 789, '450': 58, 'goldu': 7866}
for i in a:
    if a[i]>d:
        d=a[i]
    #print(a[i])
    #print(i)
print(d


# In[11]:


bid={} 

Yes=True
d=0
name=''
while Yes:
    name=input('enter the name ') 
    amount=int(input("enter the amount "))
    bid[name]=amount
    user=input(" Any another bidder Yes or No ")
    if user == "No":
        Yes=False
        print(bid)
        for i in bid:
            if bid[i]>d:
                d=bid[i] 
                name=i
    else: pass
print(f"The auction is won by {name} for the maximum amount of {d}")


# In[ ]:




