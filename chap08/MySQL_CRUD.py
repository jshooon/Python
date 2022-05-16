#!/usr/bin/env python
# coding: utf-8

# # 22.05.13
# * PyMySQL 모듈을 사용하여 DB연결 후 CRUD 기능 만들기

# ### CRUD 목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x)
# 1. 프로그램이 시작되면 위에서 제시한 6가지 메뉴가 표시된다
# 2. 추가(a) 기능을 구현한다
#    - 키보드에서 num, name, phone, email을 받아서 User객체 초기화, user 테이블에 저장
# 3. 목록(s) 기능 구현
# 4. 검색(f) 기능 구현(번호/이름으로 검색)
# 5. 수정(u)
#    - 키보드에서 num, phone, email을 받아서 기존 정보 갱신
# 6. 삭제(d)
#    - 키보드에서 num을 받아서 기존 정보 삭제
# 7. 종료(x) x 누르면 프로그램 종료

# In[1]:


from vo import User
from dao import UserDAO


# In[11]:


def user_list():
    dao = UserDAO()
    userlist = dao.show_users()
    for user in userlist:
        print(user)


# In[4]:


def user_add(user):
    dao = UserDAO()
    return dao.add_user(user)


# In[5]:


def user_find():
    n_m = input('번호(n)로 검색 혹은 이름(m)으로 검색:').strip().upper()
    udao = UserDAO()
    user = None
    if n_m=='N':
        sNum = input('검색대상 번호:').strip()
        user = udao.find_by_num(int(sNum))
    elif n_m=='M':
        name = input('검색대상 이름:').strip()
        user = udao.find_by_name(name)
    print(user)


# In[6]:


def user_update():
    num, phone, email = input('수정할 사원 번호, 변경할 전화번호, 이메일 : ').strip().split()
    dao = UserDAO()
    return dao.update_user(int(num), phone = phone, email = email)


# In[7]:


def user_delete():
    num = input('삭제할 사원 번호 : ')
    dao = UserDAO()
    return dao.delete_user(int(num))


# In[13]:


while True:
    print('----------------------------------------------------')
    print('목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x)')
    print('----------------------------------------------------\n')
    menu = input('메뉴 선택 : ')
    if menu.upper() == 'S':
        user_list()
    elif menu.upper() == 'A':
        name,phone,email = input('이름, 전화, 이메일 : ').strip().split()
        user = User(name = name, phone = phone, email = email)
        if user_add(user):
            print('추가 성공')
            continue
        else:
            print('추가 실패.')
    elif menu.upper() == 'F':
        user_find()
    elif menu.upper() == 'U':
        if user_update():
            print('수정 성공')
            continue
        else:
            print('수정 실패')
    elif menu.upper() == 'D':
        if user_delete():
            print('삭제 성공')
            continue
        else:
            print('삭제 실패')
    elif menu.upper() == 'X':
        print('프로그램 종료..~')
        break
    else:
        print('--------------------메뉴입력 오류-------------------')
    

