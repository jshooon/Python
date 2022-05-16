#!/usr/bin/env python
# coding: utf-8

# # exam05_22.05.09
# * 파일 다루기
#     * 파일 열기 : open(), 'r' 은 기본 default기 때문에 작성하지 않아도 된다.
#     * CRUD      : read, write, readlines
#     * 파일 닫기 : close()
#     * isinstance
#     * 목록을 받아서 화면에 표시 할 함수 만들기.
#     * 파일을 이용한 CRUD

# In[5]:


fobj = open('emp.py', 'r', encoding='utf-8')
type(fobj)  # _io.TextIOWrapper : 파일에 입출력 기능을 감싼 것.
dir(fobj)   # iterator, __next__(), 반복문에 적용 가능
fobj.close()


# In[10]:


fobj = open('emp.py', 'r', encoding='utf-8') 
for data in fobj:
    # 줄바꿈기능이 적용된 객체와 print함수를 사용할 때 공백 없애는 법1
    # print 함수에는 \n이 default값으로 적용 되 있다.
    # fobj에도 \n이 되있기 때문에 end를 ''해준다.
    print(data, end='')  
fobj.close()             


# In[35]:


fobj = open('emp.py', 'r', encoding='utf-8') 
for data in fobj:
    # 줄바꿈기능이 적용된 객체와 print함수를 사용할 때 공백 없애는 법2
    # print 함수에는 \n이 default값으로 적용 되 있다.
    # fobj에도 \n이 적용되었기 때문에 rstrip메소드를 사용하여 오른쪽공백만 삭제한다.
    print(data.rstrip())  
fobj.close() 


# In[18]:


from collections.abc import Iterable, Iterator

nums = [1, 2, 3]
dir(nums)

# 자바의 instanceof와 같다.  # nums객체는 Iterable클래스의 인스턴스냐라는 함수.
isinstance(nums, Iterable)   # True, Iterable클래스와 인스턴스는 __getitem__()함수 사용가능

nums.__iter__()


# In[21]:


nums.__getitem__(0)
nums[0]


# In[22]:


# 메소드를 사용하여 iterator로 변경
itr = nums.__iter__()
# 함수를 사용하여 iterator로 변경
iter(nums)
isinstance(itr, Iterator)


# In[26]:


isinstance(fobj, Iterator)
isinstance(fobj, Iterable)


# In[34]:


fobj = open('emp.py', 'r', encoding='utf-8')
fdata = fobj.read() # 파일 정보를 화면출력할 때에 read()를 사용하면 좋다.
print(fdata)
type(fdata) 
fobj.close()


# In[33]:


fobj = open('emp.py', 'r', encoding = 'utf-8')
datalist = fobj.readlines() # 파일정보를 한행한행 가져오기때문에 분석할 때 좋다.
type(datalist) 

for line in datalist:
    print(line.rstrip())
fobj.close()


# In[48]:


# for루프의 원리 1. __next__()매소드의 실행결과 확인
fobj = open('emp.py', 'r', encoding = 'utf-8')
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
fobj.close()


# In[51]:


# for루프의 원리 2. next()함수의 실행결과 확인
fobj = open('emp.py', 'r', encoding = 'utf-8')
# fobj.__next__()
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
fobj.close()


# In[52]:


# with절을 사용한다면, close()함수를 사용하지 않아도 자동으로 닫아준다.
with open('emp.py', 'r', encoding = 'utf-8') as fobj:
    for line in fobj:
        print(line.rstrip())


# In[114]:


# Emp 클래스가 포함된 module을 import한다
from emp import Emp
e = []
# with 절을 이용하여 emps.txt를 읽기 모드로 열고 객체를 emps에 저장
with open('emps.txt', 'r') as fobj:
    # 한 행을 읽어서 공백 기준으로 쪼갠다.
    for line in fobj:
        num,name,phone = line.strip().split()
        # list에 추가
        e.append(Emp(num,name,phone))
        
# 목록을 받아서 화면에 표시한다.
show_list(e)


# In[25]:


# 목록을 받아서 화면에 표시 할 함수를 만들자.
def show_list(e):
    for emp in e:
        print(emp)


# In[28]:


# 파일데이터 읽어오기 메소드
from emp import Emp
def load_emps():
    emps = []
    with open('emps.txt', 'r') as fobj:
        for line in fobj:
            num,name,phone = line.strip().split()
            emps.append(Emp(num,name,phone))
    return emps


# In[2]:


# 데이터 파일에 저장 메소드
def save_emp(emp):
    # line = f"{emp.num} {emp.name} {emp.phone}" fstring방식
    line = "{} {} {}".format(emp.num, emp.name, emp.phone)
    with open('emps.txt', 'a') as emp:
        emp.write(line + '\n')


# In[58]:


# 파일에 한 행 추가
# 키보드에서 num, name, phone 을 입력 받아서 emps.txt에 한 행으로 추가
# 목록보기 기능을 실행하면 추가된 정보가 표시되어야 함
#키보드에서 한 사원정보를 입력 받는다.
num,name,phone = input('번호 이름 전화 : ').strip().split()
save_emp(Emp(num,name,phone))
show_list(load_emps())


# In[54]:


# 내 방법
# 파일에 있는 정보 입력받은 값으로 검색 함수
def find_emp(empno):
    for emp in load_emps():
        if empno == emp.num:
            return print(emp)
        else:
            return print('잘못된 번호를 입력하셨습니다.')


# In[173]:


# 내 방법
# 키보드에서 입력된 사원번호를 키워드로 emps.txt 에서 검색하여
# 검색된 사원정보를 화면에 표시한다
# find_emp(empno) : Emp객체 리턴
empno = input('검색할 사원번호 : ')
find_emp(empno)


# In[52]:


# 선생님 방법
# 파일에 있는 정보 입력받은 값으로 검색 함수
def find_emp(emp):
    emplist = load_emps()
    found = None
    if emp in load_emps():
        found = emplist[emplist.index(emp)]
    return found


# In[37]:


# 선생님 방법
sNum = input('검색하려는 사원의 번호 : ')
emp = Emp(sNum.strip())
found = find_emp(emp)
if found:
    print(found)
else:
    print('검색실패')


# In[81]:


# 키보드에서 사번, 전화번호를 받아서 해당 사원의 정보를 갱신
# update_emp(emp) : True/False
num,phone = input('사원번호 새 전화 : ').split()
key = Emp(num, phone=phone)


# In[115]:


# 메모리에 저장된 수정된 파일정보 덮어쓰기
def overwrite(emplist):
    try:
        with open('emps.txt', 'w') as fobj:
            for emp in emplist:
                line = '{} {} {}'.format(emp.num, emp.name, emp.phone)
                fobj.write(line + '\n')
        return True
    except:
        return False


# In[80]:


# 파일정보 수정 하기
def update_emp(key):
    updated = False
    emplist = load_emps()
    if key in emplist:
        emplist[emplist.index(key)].phone = key.phone
        updated = overwrite(emplist)
    return updated


# In[82]:


if update_emp(key):
    print('수정 성공')
else:
    print('수정 실패')
show_list(load_emps())


# In[ ]:


# 로드, 리스트에서 삭제대상 찾아서 삭제, 수정된 리스트로 파일 덮어쓰기


# In[116]:


def delete_emp(key):
    deleted = False
    emplist = load_emps()
    if key in emplist:
        emplist.remove(key)
        deleted = overwrite(emplist)
    return deleted


# In[117]:


empno = input('삭제할 사원 번호 : ')
key = Emp(empno.strip())


# In[118]:


deleted = delete_emp(key)
if deleted:
    print('삭제 성공')
else:
    print('삭제 실패')


# ## 객체 직렬화(Serialization)
# * 메모리상에 저장된 객체를 파일이나 네트워크로 전송할 때 필요함

# In[ ]:


emp = Emp(15, 'Scott', '000-1111-2222')
with open('empObj.pickle', 'wb') as fw:
    pickle.dump(emp, fw)

