#!/usr/bin/env python
# coding: utf-8

# # exam02_22.05.03
# * list : 저장순서 유지, 중복가능
# * try except
# * dictionary : key, value 쌍으로 저장
# * set : 저장순서 없음, 중복불가

# In[ ]:


import random # random 함수를 사용하기 위한 import
rd_num = random.randint(0,10) # 0~10사이의 무작위 정수 하나를 가져오는 함수
rd_num
# 임의의 갯수 한개를 구함(5~10)
# 위에서 구해진 갯수만큼의 임의의 정수를 구함
# 구해진 모든 정수를 화면에 표시해 보세요.
# 표시 예) 1. 6, 2. 7


# In[7]:


# 임의의 정수 10개 추출하고
# 내림차순으로 정렬하고,
# 화면에 표시
# 오름차순으로 정렬
# 맨 마지막에 있는 정수 1개 삭제
# 중간에 위치한 수를 추출하여 화면에 표시
# 중간에 수가 없다면 중간 양쪽에 있는 수의 평균값

# ex)avg = (3+5) / 2

# python 모듈을 사용하겠다. (.py 이름) 자바 클래스와같다.
import random as rd # as rd는 sql as와 같다.


# In[8]:


num_list = []
for _ in range(10): #10번 반복 돌린다.
    num_list.append(rd.randint(0,10)) # (0과 10사이의 숫자)


# In[9]:


num_list


# In[10]:


num_list.sort(reverse=True) # 내림차순 정렬
num_list


# In[11]:


num_list.sort() # 오름차순 정렬
num_list


# In[12]:


num_list.pop() # list맨뒤의 수를 삭제
num_list


# In[13]:


# 9/2 = 4.5 이기때문에 정수화 시킨 뒤 가운데 값 추출 
# int() = java 인트로 자료형전환시키는것
num_list[int(len(num_list)/2)] # int(len(num_list)/2) 인덱싱이라한다.


# In[22]:


# 1~10 사이의 정수 중에서 짝수만 선택하여 리스트의 원소에 저장하고 
# 홀수는 0으로 변경하여 저장한 후, 리스트의 모든 원소를 화면에 표시해보세요.
num = [i if i%2==0 else 0 for i in range(1,11)]
print(num)


# In[23]:


nums = list(range(1,11))
nums


# In[24]:


# list index 5부터 7까지 출력
nums2 = nums[4:7]
nums2


# In[25]:


nums2[0] = 100
nums2[0]


# In[26]:


nums


# In[31]:


# nums3에 nums의 객체의 주소를 준다.
# 객체의 주소를 복사하는 것을 Shallow Copy(얕은 복사)라한다.  뿌리까지 복사X
# nums3[0]의 값을 100으로 업데이트한다
nums3 = nums
nums3
nums3[0] = 100
nums3


# In[32]:


# nums[0]도 바뀌어있다. 객체는 하나이지만 참조변수는 여러개인 것과 같다.
nums


# In[35]:


# list주소값 복사가 아닌 list자체 복사
# 그 주소가 가리키는 곳의 데이터를 복사하는 것을 Deep Copy(깊은복사)라한다.
nums4 = nums[:]
nums4
nums4[0] = 200
nums4


# In[36]:


# nums[0]이 바뀌지 않는것을 볼 수 있다.
nums


# In[41]:


nums.append(-5)
nums


# In[46]:


num_list = [4,5,6]
num_list


# In[48]:


# 괄호가 생략된 Tuple
a,b,c = num_list
a,b,c


# In[61]:


# 무작위  정수 10개를 준비하고 처음 3개를 추출하여 튜플에 저장하고 화면에 표시
# list comprehension 활용
import random as rd
rnum = [rd.randint(0,11) for i in range(1,11)]
# tuple에 저장 방법 1
a,b,c = rnum[:3]
a,b,c
# tuple에 저장 방법 2
tp = (a,b,c)
tp


# In[87]:


uid_list = ['KOON', 'RIM', 'GOO']
pwd_list = ['1111','2222','3333']


# In[97]:


for _ in range(3):
    try:
        uid, pwd = input('아이디 암호').split() # 짤라서 받은 후 tuple이 된다.
        idx = uid_list.index(uid.upper()) # upper() = 대문자로 변경 후 비교.
        if uid_list[idx]==uid.upper():
            if pwd_list[idx]==pwd:
                print('로그인 성공')
                break
    except ValueError as e:
        print('로그인 실패' + str(e))


# In[89]:


1 < 2 # True


# In[92]:


1 < 2 and 3 > 2


# In[100]:


# boolean표현식으로
# list 안에 값이 있는지 확인하는 것은
# in 을 사용한다.
'x' in ['a','b','c']


# In[101]:


uid_list = ['KOON', 'RIM', 'GOO']
pwd_list = ['1111','2222','3333']


# In[110]:


for _ in range(3):
        uid, pwd = input('아이디 암호').split() # 짤라서 받은 후 tuple이 된다.
        if uid.upper() in uid_list: # 사용자가 입력한 uid가  uid_list에 있다면
            idx = uid_list.index(uid.upper())
            if uid_list[idx]==uid.upper() and pwd_list[idx]==pwd:
                print('로그인 성공')
                break
        else:
            print('로그인 실패')


# In[131]:


# dictionary 
user = [{}, {}, {}]
# type(users[0]['key'])


# In[132]:


for i in range(3):
    user[i]['num'], user[i]['name'], user[i]['phone'] = input('번호 이름 전화:').split()
print(user)


# In[133]:


for u in user:
    s = f"{u['num']}\t{u['name']}\t{u['phone']}"
    print(s)


# In[147]:


users = []
for i in range(3):
    num,name,phone = input('번호 이름 전화:').split()
    users.append({'num' : num, 'name' : name, 'phone' : phone})
users


# In[142]:


for user in users:
    s = f"{user['num']}\t{user['name']}\t{user['phone']}"
    print(s)


# In[139]:


users[0]['phone'] = '123'
print(users[0])


# In[148]:


# 리스트에 저장된 마지막 회원정보 중에서 phone 정보 삭제
# 삭제된 상태로 리스트 출력
del users[-1]['phone']


# In[149]:


users


# In[145]:


# phone 정보가 없는 경우 '전화기 분실' 표시
for user in users:
    s = f"{user['num']}\t{user['name']}\t{user.get('phone', '전화기 분실')}"
    print(s)


# In[161]:


# 자료구조
# [{}, {}, ......] 리스트안에 딕셔너리(Map)
# 위의 리스트에 몇 사람 정보를 저장한다.

member = []
member.append({'num': '1', 'name':'지', 'phone': '112'})
member.append({'num': '2', 'name':'김', 'phone': '113'})
member.append({'num': '3', 'name':'구', 'phone': '114'})
member


# In[163]:


# strip 쓸데없는 공백 삭제하기
num = input('검색할 회원번호').strip()


# In[164]:


# 키보드에서 회원번호를 입력하여 해당 회원을 검색하고,
# 그 결과를 화면에 표시한다.
for mem in member:
    if mem['num']==num:
        s = f"{mem['num']}\t{mem['name']}\t{mem.get('phone', '전화기 분실')}"
        print(s)


# In[ ]:


# list, set, dictionary
# list : 저장순서 유지, 중복가능 각 방이 있다.
# set : 저장순서 없음, 중복불가 각 방이 없다.
# dict : key, value 쌍으로 저장


# In[ ]:


set1 = set([1,1,1,1,2])


# In[ ]:


len(set1)


# In[ ]:


import random as rd
set2 = set()

while True:
    num = rd.randint(1,11)
    set2.add(num)
    if len(set2) == 7:
        break
print(set2)

