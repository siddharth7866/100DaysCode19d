#!/usr/bin/env python
# coding: utf-8

# In[103]:


class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return '''
        Account owner:Mr {}
        Account balance:${}
        
        '''.format(self.owner.upper(),self.balance)
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("The amount of {} is added to main balance".format(amount))
    def withdrawl(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Please collect your {} remaining balnce is {} ".format(amount,self.balance))
        else:
            print("Unsufficient Fund")
        
        


# In[104]:


acc1=Account("siddharth",500)


# In[105]:


acc1.balance


# In[106]:


acc1.owner


# In[107]:


print(acc1)


# In[108]:


acc1.deposit(500)


# In[110]:


acc1.withdrawl(300)


# In[ ]:




