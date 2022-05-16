#!/usr/bin/env python
# coding: utf-8

# # 클래스 실습
# * 클래스와 인스턴스
# * 초기자, __init__()
# * 인스턴스 메소드 : 인스턴스에 포함된 메소드

# In[9]:


class Emp:
    def __init__(self, num, name, phone):
        self.num = num
        self.name = name
        self.phone = phone
        
    def __str__(self):
        return (f"{self.num}\t{self.name}\t{self.phone}")
    
    def __eq__(self, other):
        return self.num == other.num


# In[10]:


e1 = Emp(11, 'koon', '112')
print(e1)


# In[11]:


e2 = Emp(12, 'rim', '113')
print(e2)


# In[12]:


e1.__eq__(e2)


# In[13]:


e3 = Emp(12, '', '')

e2.__eq__(e2)


# In[7]:


emplist = [e1,e2]
for emp in emplist:
    print(emp)

