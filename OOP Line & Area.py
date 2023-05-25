#!/usr/bin/env python
# coding: utf-8

# In[35]:


class Cylinder:
    
    pi=3.14
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        pi_value=float(self.pi)
        volume_cylinder=(pi_value)*(self.radius)*(self.radius)*(self.height)
        answer=round(volume_cylinder,2)
        print(answer)
    
    def surface_area(self):
        surface_areacal=2*(self.pi)*(self.radius)*(self.height)+2*(self.pi)*(self.radius)*(self.radius)
        answer=round(surface_areacal,2)
        
        print(answer)
        


# In[36]:


cylinder=Cylinder(2,3)


# In[37]:


cylinder.volume()


# In[38]:


cylinder.surface_area()


# In[ ]:


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        pass
    
    def slope(self):
        pass


# In[52]:


class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
        
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    def __add__(self,other):
        temp_n=self.num*other.den+self.den*other.num
        temp_d=self.den*other.den
        return "{}/{}".format(temp_n,temp_d)


# In[53]:


x=Fraction(4,5)


# In[54]:


print(x)


# In[55]:


y=Fraction(5,6)


# In[56]:


print(y)


# In[57]:


print(x+y)


# In[58]:


a=(1,3)


# In[65]:


a[1]


# In[110]:


import math
class Line:
    
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
        self.x1=self.coor1[0]
        self.x2=self.coor2[0]
        self.y1=self.coor1[1]
        self.y2=self.coor2[1]
        
    
    def distance(self):
        distance=(self.x2-self.x1)**2 + (self.y2-self.y1)**2
        answer=math.sqrt(distance)
        print(answer)
    
    def slope(self):
        m=(self.y2-self.y1)/(self.x2-self.x1)
        answer=float(m)
        print(answer)


# In[111]:


coor1=(3,2)
coor2=(8,10)
line=Line(coor1,coor2)


# In[112]:


line.slope()


# In[113]:


line.distance()


# In[ ]:





# In[ ]:




