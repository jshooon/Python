#!/usr/bin/env python
# coding: utf-8

# # exam04_22.05.06
# * list, dict를 사용한 emp프로그램을 class를 사용하여 만들어보기
# * emp.py 파일안에 Emp 클래스 정의하고 앞에서 작성된 프로그램 실행하기.
# * import 연습하기

# In[5]:


from emp import Emp


# In[45]:


e1 = Emp(1, 'koon', '111') #파라미터
print(e1)


# In[46]:


e2 = Emp(2, 'rim', '112') #파라미터
print(e2)


# In[4]:


e1.__eq__(e2)


# In[9]:


e3 = Emp(2, '', '')
e2.__eq__(e3)


# In[10]:


e2==e3


# In[11]:


e1==e2


# In[8]:


emp_list =[e1, e2]
for e in emp_list:
    print(e)


# In[12]:


list([e1, e2, e3]) # 16진수 주소에 있는 emplooye객체라는 뜻.


# In[6]:


emps = []


# In[7]:


def is_duplicate(num):
    nums = [emp.num for emp in emps]
    nums.append(num)
    if len(nums)!=len(set(nums)):
        return True
    else:
        return False


# In[8]:


def emp_list():
    print("번호\t이름\t전화")
    for emp in emps:
            print(emp)


# In[9]:


def find_emp(ename):
    emp = None
    for e in emps:
        if e.name==ename:
            emp = e
            print(e)
    return emp


# In[10]:


def update_emp( new_phone ):
    num,phone = new_phone
    updated = False
    if is_duplicate(int(num)):
        for emp in emps:
            if emp.num==num:
                emp.phone = phone
                updated = True
    return updated


# In[11]:


def delete_emp(num):
    deleted = False
    for emp in emps:
        if emp.num==num:
            try:
                emps.remove(emp)
                deleted = True
            except ValueErorr as ve:
                pass # 빈 블럭을 표시할 때 pass를 사용한다.
    return deleted


# In[13]:


while True:
    print("------------------------------------------------------")
    menu = input("추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x):")
    print("------------------------------------------------------\n")
    if menu.upper()=='A':
        num,name,phone = input("사원 번호 이름 전화:").split()
        if is_duplicate(int(num)):
            print('사원번호 중복, 다시 입력해주세요')
            continue
       # emps.append({'num':num,'name':name,'phone':phone})
        emps.append(Emp(int(num),name,phone))
        print('사원정보 저장 성공')
        
    elif menu.upper()=='S':
        emp_list()
        
    elif menu.upper()=='F':
        ename = input("검색할 사원 이름:")
        if find_emp(ename) == None:
            print('해당 이름의 사원정보 없음')                
    elif menu.upper()=='U':
        num,phone = input("수정할 사원번호 및 전화번호:").split()
        if update_emp((int(num),phone)):
            print("수정 성공")
        else:
            print("수정 실패")
                
    elif menu.upper()=='D':
        num = input('삭제할 사원번호:').strip()
        if delete_emp(int(num)):
            print('삭제 성공')
        else:
            print('삭제 실패')
            
    elif menu.upper()=='X':
        print('프로그램 종료...')
        break
        
    else:
        print('********* 메뉴 입력 오류 **********')


# In[41]:


import random # random.randint() import 방식 
random.randint(1,10)


# In[63]:


from random import randint # randint() import 방식 
randint(1,10)

