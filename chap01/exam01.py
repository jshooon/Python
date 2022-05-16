#!/usr/bin/env python
# coding: utf-8

# # exam01_22.05.02
# * 파이썬 인터프리터의 이해
# * Jupyter notebook 활용하기
# * 주석문의 종류
# * python의 list와 Tuple 기능

# In[4]:


print('Hello World')
 # CTRL + ENTER = 셀 실행
 # 주석문은 #
 # ALT + ENTER 중간셀의 실행과 동시에 아래 셀추가


# In[5]:


a = 5
b = 7
c = a + b
c #c CTRL + ENTER = 실행, SHIFT + ENTER = 맨아래 셀을 실행과 동시에 아래 셀추가
print('c = ', c)


# In[11]:


msg = "Hello"
print(msg)
msg = 'World'
print(msg)
msg = """This
            is
              String
                  Test"""
print(msg)

# 메모리상에는 있지만 주석문과 같다. 문자열로 출력된다.
"""
print("a")
print("b")
print("c")
"""


# In[16]:


msg = "Hello 'World'"
msg #따옴표 에러


# In[19]:


name = "ada lovelace"
title = name.title() #title 기능은 문자열의 첫단어 앞부분을 대문자로 변환시켜준다.
print(title)


# In[22]:


dir(name) 
help(str) #메소드명과 사용법이 출력된다.


# In[23]:


name = "Smith"
age = 29
info = f"{name} {age}"
print(info) #서식문자열 출력 f String이라한다.


# In[24]:


input('이름을 입력해주세요 : ')
# 셀 실행이 끝나지 않는다면 In[*] 표시가 된다.


# In[25]:


name = input('이름을 입력해주세요 : ') # 출력이 되지않는다. 변수에 저장될 뿐
name # 이렇게 해줘야 출력이된다.


# In[27]:


# 키보드에서 번호, 이름, 전화번호를 입력받아서 서식 문자열로
# 화면에 표시해보세요.

num = input('번호를 입력해주세요')
name =  input('이름을 입력해주세요')
phone =input('전화번호를 입력해주세요')
# 이전방법
# info = "{} {} {}".format(num, name, phone)
info = f"{num} {name} {phone}"
print(info)


# In[37]:


greeting = "Hello "
res = greeting.rstrip(); #원본의 문자열을 복사하여 사본을 리턴한다.
res


# In[32]:


a,b,c = 1,2,3
print(a,b,c)


# In[35]:


nums = [1,2,3]
print(nums)
a,b,c = nums # 변수별로 배열에 들어있는 값이 저장된다.
print(a,b)


# In[42]:


msg = """A
    B
     C"""
print(msg)
msg = '''
    A
    B
    C
'''
print(msg)


# In[47]:


names =['koon', 'rim', 'gu'] #List와 같다. 수정삭제가 가능.
len(names) #list의 size와 문자열의 length와 같다.
names[1].title()


# In[50]:


print(names[0], names[2])


# In[51]:


type(['a']) #자료형을 알아보기위해 type을 사용한다.


# In[63]:


num = [1,2,3]
num[2] = 5 # 업데이트 
num.append(3) # list 값 추가 
num.remove(5) # list 값 삭제
del num[1]
dir(num)
num


# In[55]:


# 원소가 한개인 Tuple 선언하고 자료형 확인하기
data = (10,) # 원소 한개라 하더라도 ,를 널어준다.
type(data)


# In[ ]:


data     # 인덱스에 -를준다면 제일 마지막을 지정한다. 
data[-1] #  index -숫자가 커질수록 마지막에서 앞의 값으로 땡겨진다.


# In[58]:


data = 1,2,3
type(data)


# In[64]:


(names[0], names[2]) # Tuple : 리스트가아닌 자료구조 # 리스트완 다르게 []아닌 ()
                     # 수정삭제가 불가능하다.


# In[ ]:


# 0부터 3까지 올라가면서 루프가 돈다. (0부터 2까지) 3은 stop이기 때문에 제외
# i 는 0,3 이 0부터2까지 도는데 0부터2까지의 값이 루프를 돌면서 i에 들어간다.
# java의 for문 i 와 같다.
for i in range(0,3):
    print (i)


# In[76]:


# 키보드에서 회원의 정보를 입력받아서 리스트에 저장하는 프로그램 작성
# 3인의 회원정보를 입력 받아서 리스트에 저장하고 화면에 표시해보세요.
# JavaScript의 obj에 제이슨 오브젝트를 넣는방법과 같다.
num = []
name = []
phone = []

for _ in range(0,3):
    
    strMem = input('번호 이름 전화 : ')
    memInfo = strMem.split(' ')

    num.append(memInfo[0])
    name.append(memInfo[1])
    phone.append(memInfo[2])
# i 는 0,3 이 0부터2까지 도는데 0부터2까지의 값이 루프를 돌면서 i에 들어간다.
# java의 for문 i 와 같다.
for i in range(0,3):
    print(num[i], name[i], phone[i])


# In[77]:


name # 위의 저장된 리스트값이 유지된다.


# In[ ]:


# List CRUD
 # - C : append()
 # - R : name[0]
 # - U : name[0] = 'Koon'
 # - D : name.remove('Koon'), or del name[0]


# In[ ]:


# 수정기능
#   - 리스트에 포함된 모든 정보를 출력한다.
#   - 리스트 하단에 수정할 회원번호 새 전화번호 입력
#   - 새로 입력된 전화번호를 해당 회원의 정보에 업데이트 한다.
#   - 리스트를 다시 출력한다.


# In[84]:


for i in range(0,3):
    print(num[i], name[i], phone[i])

strc = input('수정할 회원번호 , 새 전화번호를 입력하세요 : ')
n, change = strc.split(' ') # 이런경우는 Tuple로 받는다.
idx = num.index(n) # input으로 받은 값으로 인덱스를 찾는다. 그것을 idx에 넣는다.
phone[idx] = change # 전화번호 업데이트
    
print('\n', '수정된 정보')
    for i in range(0,3):
        print(num[i], name[i], phone[i])
    


# In[ ]:


# 삭제기능
  # 리스트 하단에 '삭제할 회원번호 : '
  # 입력받은 후 리스트에서 해당 회원정보(num, name, phone)를 삭제.
  # 삭제를 위한 회원번호가 발견되지 않으면 삭제실패 출력.


# In[85]:


for i in range(0,3):
    print(num[i], name[i], phone[i])
    
# 예외가 발생할 수 있다.
memnum = input('삭제할 회원번호')
# Java의 try catch 문    
try:
    idx = num.index(memnum)
    del num[idx]
    print('삭제 성공')
except:
    print('삭제 실패')


# In[88]:


for i in range(0,3):
    print(num[i], name[i], phone[i])
    
    # 예외가 발생할 수 있다.
memnum = input('삭제할 회원번호')
# Java의 try catch 문    
try:
    idx = num.index(memnum)
    del num[idx]
    print('삭제 성공')
except ValueError as e: # e변수에 ValueError가 들어간다.
    print('삭제 실패이유 : ' + str(e))


# In[91]:


# api클래스들마다 리턴값이 다르기때문에 
# 리턴값이 없다면 원본이 바뀌지만,
# 리턴값이 있다면 원본이 바뀌지 않는다.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # 문자열 알파벳순 오름차순 정렬.
cars
cars.sort(reverse=True) # 문자열 알파벳순 내림차순 정렬.
cars
sorted(cars) # 오름차순 정렬 
copy_list = sorted(cars)
print('사본' , copy_list)
print('원본', cars)


# In[93]:


# reverse는 리스트의 정렬순서가아니고, 순서를 앞뒤로 바꾼다.
nums = [2,1,3]
nums.reverse()
nums


# In[96]:


import random # random 함수를 사용하기 위한 import
rd_num = random.randint(0,10) # 0~10사이의 무작위 정수 하나를 가져오는 함수
rd_num
# 임의의 갯수 한개를 구함(5~10)
# 위에서 구해진 갯수만큼의 임의의 정수를 구함
# 구해진 모든 정수를 화면에 표시해 보세요.
# 표시 예) 1. 6, 2. 7

