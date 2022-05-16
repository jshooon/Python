#!/usr/bin/env python
# coding: utf-8

# # exam04(file)_22.05.06
# * 파일 다루기

# In[16]:


# with절 없이 파일 정보 불러오는 방법
fstream = open('emp.py', mode = 'r', encoding='UTF-8')
data = fstream.read()
print(data)
fstream.close()


# In[17]:


# with절을 사용하여 파일 정보 불러오는 방법
with open('emp.py', 'r', encoding='UTF-8') as fstream:
    data = fstream.read()
    print(data)


# In[20]:


# with절을 사용하여 파일 정보의 전체 행을 리스트로 가져오기
with open('emp.py', 'r', encoding='UTF-8') as fstream:
    data = fstream.readlines()
    print(data)

