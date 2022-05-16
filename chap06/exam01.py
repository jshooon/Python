#!/usr/bin/env python
# coding: utf-8

# # exam06_22.05.10 직렬화/역직렬화
# * 파일,메모리 변수 대상
# * pickle 모듈을 사용한 직렬화/역직렬화 응용 CRUD 실습
# * 메모리상에 저장된 객체를 파일이나 네트워크로 전송할 때 필요함
# * 객체 직렬화/역직렬화를 이용한 CRUD
# * global variable
# * sort()함수안에 lambda를 사용하여 객체 정렬(문자열,숫자 정렬)

# In[1]:


from emp import Emp


# In[2]:


import pickle


# In[4]:


emp = Emp(11, 'Koon', '000-1111-1111')


# ### 객체 직렬화(Object Serialization)

# In[5]:


# 객체 직렬화(Serialization)
fw = open('empObj.pickle', 'wb') # empObj.pickle는 임의의 파일이고, wb는 writebinary.
pickle.dump(emp, fw) # 위에 생성한 emp객체를 직렬화(pickle.dump) 한다음 fw(파일)에 저장한다.
fw.close()
print('객체 직렬화 성공')


# ### 역직렬화(De-Serialization)

# In[8]:


# 역직렬화(De-Serialization)
fr = open('empObj.pickle', 'rb') # empObj.pickle는 emp객체 파일이고, rb는 binary를 읽겠다는 것.
emp2 = pickle.load(fr) # 데이터를 역직렬화 하여 디스크 저장된 emp객체를 디스크에서 메모리로 복사 이동하는 것.
fw.close()
print(emp2)
print(emp2.name)


# In[9]:


emp==emp2    # emp.__eq__(emp2)


# In[16]:


emplist = [Emp(11), Emp(12), Emp(13)]


# In[17]:


with open('emplist.pickle', 'wb') as fw:
    pickle.dump(emplist, fw)
print('리스트 직렬화 완료')


# In[20]:


with open('emplist.pickle', 'rb') as fr:
    emps = pickle.load(fr)

print(emps[0])
print('리스트 역직렬화 성공')


# In[ ]:


# 데이터를 파일로 다룰 때 , 데이터 다룰 때 객체 > 텍스트 파일, 데이터 가져올 때 텍스트 파일 > 객체 매핑
# 데이터 다룰 때 객체 > 객체 , 데이터 가져올 때 객체 > 객체


# ### 프로그램이 시작되면 메뉴 6개 표시와 기능구현.
# * 목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x)
# * 추가(a)하고 목록보기가 되도록 기능을 작성해보세요.

# ### pickle module import

# In[32]:


import pickle
from emp import Emp


# In[33]:


emplist = []


# ### emplist에 들어있는 emp객체 직렬화하여 하드디스크에 저장

# In[51]:


def save_emplist():
    saved = False
    try:
        with open('emplist.txt', 'wb') as fw:
            pickle.dump(emplist, fw)
            saved = True
    except:
        pass
    return saved


# ### save_emplist()함수사용하여 직렬화하여 emp객체 추가 하기

# In[35]:


def add_emp(emp):
    emplist.append(emp)
    return save_emplist()


# In[96]:


def add_emp(emp):
    global emplist
    with open('emplist.txt', 'rb') as fr:
        emplist = pickle.load(fr)
        if emp not in emplist:
            added = True
            emplist.append(emp)
            return save_emplist()


# ### 역직렬화 하여 디스크에 저장된 emplist 메모리에서 읽어오기

# In[106]:


def show_list():
    with open('emplist.txt', 'rb') as fr:
        emps = pickle.load(fr)
        # emps.sort(key=lambda e:e.num) 문자정렬
        emps.sort(key=lambda e:int(e.num)) # 숫자정렬
        for emp in emps:
            print(emp)


# ### 역직렬화 하여 디스크에 저장된 emplist중 emp객체 찾기

# In[40]:


def find_emp(emp):
    found = None
    with open('emplist.txt', 'rb') as fr:
        emps = pickle.load(fr)
        if emp in emps:
            found = emps[emps.index(emp)]
    return found


# ### 역직렬화 하여 emplist 읽어온뒤 update한다음 다시 직렬화 하여 디스크에 저장

# In[65]:


def update_emp(key):
    updated = False
    global emplist        # 현재 함수 외부에 선언된 (전역)변수(global)
    with open('emplist.txt', 'rb') as fr:
        emplist = pickle.load(fr)
        if key in emplist:
            emplist[emplist.index(key)].phone = key.phone
            updated = save_emplist()
    return updated


# ### 역직렬화 하여 emplist에서 emp객체 찾은뒤 삭제하고 삭제된 emplist    다시 직렬화 하여 디스크에 저장

# In[76]:


def delete_emp(emp):
    deleted = False
    global emplist
    with open('emplist.txt', 'rb') as fr:
        emplist = pickle.load(fr)
        if emp in emplist:
            emplist.remove(emp)
            deleted = save_emplist()
    return deleted


# ### 사원번호 중복방지하기

# In[ ]:


def is_duplicate(emp):
    with open('emplist.txt', 'rb') as fr:
        emplist = pickle.load(fr)
        if emp in emplist:
            return True
    return False


# In[107]:


while True:
    menu = input('추가(a), 목록(s), 검색(f), 수정(u), 삭제(d), 종료(x)').strip()
    
    if menu.upper() == 'A':
        num, name, phone = input('사원번호 이름 전화번호').strip().split()
        emp = Emp(num,name,phone)
        # if is_duplicate(emp):
        #    print('번호 중복, 추가 실패')
        #    continue
        if add_emp(Emp(num,name,phone)):
            print('사원정보 추가 성공')
        else:
            print('중복된 사원번호 입니다.')
    elif menu.upper() =='S':
        show_list()
    elif menu.upper() == 'F':
        empno = input('조회할 사원번호 : ').strip()
        emp = Emp(empno.strip())
        found = find_emp(emp)
        if found:
            print(found)
        else:
            print('검색하신 사원은 존재하지 않습니다.')
        pass
    elif menu.upper() == 'U':
        num,phone = input('사원번호 새 전화번호 : ').strip().split()
        if update_emp(Emp(num, phone = phone)):
            print('수정 성공')
        else:
            print('수정 실패')
    elif menu.upper() == 'D':
        empno = input('삭제할 사원번호 : ').strip()
        if delete_emp(Emp(empno.strip())):
            print('삭제 성공')
        else:
            print('삭제 실패')
    elif menu.upper() == 'X':
        break
    


# ### list 정렬 법

# In[100]:


with open('emplist.txt', 'rb') as fr:
    elist = pickle.load(fr)
elist
for e in elist:
    print(e)


# In[101]:


# sort함수안에서 lambda e:e.num 함수가 호출된다.
# e는 elist에서 나온 emp객체이며, key에는 e.num값이 들어가며 정렬이 된다.
elist.sort(key=lambda e:e.num)
for e in elist:
    print(e)


# ### global variable

# In[57]:


outer_num = 100


# In[59]:


def value_use():
    print(outer_num+10)


# In[60]:


value_use()


# In[67]:


def value_change():
    global outer_num  # 전역변수
    outer_num = 10     # 지역변수였지만, 전역변수 선엄되어 전역변수됨.
    print(outer_num)   # 10


# In[68]:


value_change()


# In[69]:


outer_num


# In[70]:


def value_use2():
    num = outer_num + 100
    print(num)


# In[71]:


value_use2()


# ### 메모리 변수대상 직렬화/역직렬화
# * dumps, loads

# In[108]:


with open('emplist.txt', 'rb') as fr:
    elist = pickle.load(fr)
elist
for e in elist:
    print(e)


# In[109]:


elist
byte_arr = pickle.dumps(elist)
print(byte_arr)


# In[110]:


elist2 = pickle.loads(byte_arr)
elist2.sort(key=lambda e:int(e.num))
for e in elist2:
    print(e)

