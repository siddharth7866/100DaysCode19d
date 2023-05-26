#!/usr/bin/env python
# coding: utf-8

# In[4]:


s='siddharth'
s[1:]


# In[12]:


s=input("enter the word")
s=s.lower()
new_s=s[::-1]
new_s
if new_s==s:
    print("It is pallindrome")
else:
    print("Not Pallindrome")


# In[13]:


print("siddharth {2} {0} {1}".format('good','boy',"is"))


# In[1]:


sidlist=[1,2,3,4,5,6]


# In[5]:


sidlist.insert(6,"sid")


# In[6]:


sidlist


# In[7]:


sid=[1,2,3


# In[8]:


sid[2][1]


# In[9]:


sid=[1,2,3]
sid[1:]


# In[10]:


d={"key1":100,"Key2":200}


# In[14]:


s=d.values()


# In[16]:


type(s)


# In[17]:


d["key3"]=400
d


# In[18]:


d=(1,2,3,"sid")


# In[25]:


d.index("sid")


# In[26]:


d=[1,2,3,"sid"]


# In[28]:


d.index("sid")


# In[29]:


d={"key1":100,"Key2":200}


# In[30]:


d=(1,2,3,"sid")


# In[33]:


d[0]


# In[34]:


d=(1,2,[1,2])


# In[35]:


type(d)


# In[36]:


d[2][1]=3


# In[37]:


d


# In[38]:


print(set('Mississippi'))


# In[45]:


s=set('Mississippei')
p=set('parrallel')


# In[46]:


s.intersection(p)


# In[47]:


s=set('Mississippei')
s


# In[49]:


s.add("t")


# In[50]:


s


# In[51]:


pwd


# In[52]:


get_ipython().run_cell_magic('writefile', 'sid.txt', 'Hello siddharth\nthis is first line\nthis second line\nthis is third line')


# In[53]:


get_ipython().run_cell_magic('writefile', 'filetute.txt', 'Hello siddharth\nthis is first line\nthis second line\nthis is third line')


# In[54]:


myfile=open("filetute.txt")


# In[55]:


myfile.read()


# In[56]:


myfile.read()


# In[57]:


myfile.seek(0)


# In[58]:


myfile.read()


# In[59]:


myfile.close()


# In[60]:


with open("filetute.txt",mode="w") as d:
    d.write("siddharth")


# In[63]:


with open("filetute.txt",mode="r") as d:
    print(d.read())


# In[1]:


d={"key1":100,"Key2":200}


# In[2]:


d["key1"]=400
d


# In[3]:


200/4*2+.75-.25


# In[4]:


s = 'hello'
# Print out 'e' using indexing

s[1]


# In[9]:


s ='hello'
# Reverse the string using slicing

s[::-1]


# In[ ]:




