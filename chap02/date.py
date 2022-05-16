#!/usr/bin/env python
# coding: utf-8

# # 날짜 다루기

# In[1]:


# 파이썬 날짜 다루기
import datetime


# In[8]:


from datetime import date


# In[18]:


today = date.today()
today


# In[19]:


year = today.year
month = today.month
day = today.day
wday = today.weekday() # 월(0), 화(1), 수(2),.....
isoweekday = today.isoweekday() # 월(1), 화(2), 수(3),.....

strday = ' '

if wday ==0:
    strday = '월'
elif wday ==1:
    strday = '화'
elif wday ==2:
    strday = '수'
elif wday ==3:
    strday = '목'
elif wday ==4:
    strday = '금'
elif wday ==5:
    strday = '토'
elif wday ==6:
    strday = '일'


# In[25]:


# list 함수에 문자열을 넣어준다면, 문자열을 쪼개서 list를 만들어준다.
days = list('월화수목금토일')
days[0]
days[wday]


# In[20]:


strday = list('월화수목금토일')[wday]


# In[21]:


print(f"{year}년 {month}월 {day}일, {strday}요일")

