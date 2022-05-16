#!/usr/bin/env python
# coding: utf-8

# # exam03_22.05.04
# * 실습 문제
# * 프로그램이 시작된다면, 
# * 아래처럼 메뉴 목록을 제시한다.
# * 추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x)
# * 메뉴목록이 실행되는 프로그램 만들기
# * py파일 생성 후 import하여 사용하기.

# In[5]:


nums = [1,2,3,3,4,5]
nums


# In[6]:


set(nums)


# In[7]:


len(nums),len(set(nums))


# In[8]:


if len(nums)!=len(set(nums)):
    print('데이터 중복 발견')
else:
    print('데이터 중복 없음')


# In[64]:


def is_duplicated(num):
    nums = [emp['num'] for emp in emps]
    nums.append(num)
    if len(nums)!=len(set(nums)):
        return True
    else:
        return False


# In[62]:


def is_duplicate(nums, num):
    if len(nums)!=len(set(nums)):
        return True
    else:
        return False


# In[65]:


def emp_list():
    for emp in emps:
            print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")


# In[74]:


def find_emp(ename):
    for emp in emps:
        if emp['name']==ename:
            return emp
    return None


# In[80]:


def update_emp(new_phone):
    num,phone = new_phone
    updated = False
    for emp in emps:
        if emp['num']==enum:
            emp['phone'] = phone
            updated = True
    return updated


# In[83]:


def delete_emp(enum):
    delete = False
    for emp in emps:
            if emp['num']==enum:
                emps.remove(emp)
                delete = True
    return delete


# In[ ]:


emps = []
while True:
    print("----------------------------------------------------------------")
    menu = input('"추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x) : "')
    print("----------------------------------------------------------------\n")
    if menu.upper() == 'A':
        num,name,phone = input('사원의 번호 이름 전화번호 입력 : ').split()
        nums = [user['num'] for user in emps]        # 기존 등록된 번호
        nums.append(num)                                # 새로 추가할 사원번호
        if is_duplicate(nums, num):                  # 사원번호 중복검사
            print('사원번호 중복, 다시 입력해주세요.')
        emps.append({'num' : num, 'name' : name, 'phone' : phone})
        print('사원정보 저장 성공')
        
    elif menu.upper()=='S':
        emp_list()
        
    elif menu.upper()=='F':
        ename = input('검색할 사원 이름을 입력해주세요.')
        emp = find_emp(ename)
        if emp:
            print(f"{emp['num']}\t{emp['name']}\t{emp['phone']}")
        else:
            print('사원정보 없음')
            
    elif menu.upper()=='U':
        (enum, phone) = input('수정할 사원 번호와 전화번호를 입력해주세요. :').split()
        if update_emp((num,phone)):
            print('수정 성공')
        else:
            print('수정 실패')
            
    elif menu.upper()=='D':
        enum = input('삭제할 사원번호를 입력해주세요. :')
        if delete_emp(enum):
            print('삭제 성공')
        else:
            print('삭제 실패')
            
    elif menu.upper()=='X':
        print('프로그램 종료')
        break
    else:
        print('*************메뉴 입력 오류*************')


# In[95]:


import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# In[97]:


# import 방법 1
import sample
sample.test()
sample.add(3,5)


# In[98]:


# import 방법 2
from sample import add
add(3,5)


# In[99]:


# import 방법 3
import sample as s
s.add(3,5)


# In[100]:


import mymodule as my
my.show('내 이름은','지', '성', '훈')


# In[101]:


from mymodule import show as s
s('내 이름은','지', '성', '훈')


# In[102]:


# import 방법 4
from sample import *
test()
add(3,5)


# In[104]:


class Emp:
    
    def __init__(self, num, name, phone):
        self.num = num
        self.name = name
        self.phone = phone
        
    def __str__(self):
        return (f"{self.num}\t{self.name}\t{self.phone}")
    
    def __eq__(self, other):
        return self.num == other.num

