#!/usr/bin/env python
# coding: utf-8

# # exam06_22.05.10 Thread
# * Thread, Runnable, run()

# In[ ]:


# Thread, Runnable, run()
# Process : 현재 실행중인 프로그램
# Thread : Process 안에서 동시에 실행 가능한 소규모 Process


# In[ ]:


# 함수, 메소드, run()


# In[ ]:


import threading
import time
import datetime


# In[ ]:


def t1(name):
    while True:
        print(name, datetime.datetime.now())
        time.sleep(1)


# In[ ]:


# t1('Date Thread')


# In[ ]:


def t2(name):
    i = 0
    while True:
        i += 1
        print(name, i)
        time.sleep(1)


# In[ ]:


# t2('Num Thread')


# In[ ]:


th1 = threading.Thread(target=t1, args=('Date Thread',))
th1.daemon = True
th1.start()

th2 = threading.Thread(target=t2, args=('Num Thread',))
th2.daemon = True
th2.start()


# In[ ]:


# 객체 맴버 메소드(내부의 메소드)를 Thread의 타겟으로 하는법
threading.Thread(target=obj.method, args=('Date Thread',))


# In[ ]:


import threading
import time
import datetime
# 가상의 CPU역할을 하는 클래스 정의
# java의 extends
class MyGame(threading.Thread):         # Thread 클래스 상속
    def __init__(self, name):
        threading.Thread.__init__(self)
        print(name, 'instanciated')
        self.daemon = True
        
    def run(self):
        while True:
            print(datetime.datetime.now())
            time.sleep(1)  # 1초 쉼

my_thread = MyGame('game thread')
my_thread.start()


# In[ ]:


# 키보드에서 숫자가 입력될 때 마다 해당 숫자로부터 1씩 감소하면서 출력하는 기능
# 숫자가 0에 도달할 때 까지 반복해서 1초에 한번씩 화면에 표시함.


# In[15]:


import threading
import time
class CountDownThread(threading.Thread):
    def __init__(self, name, num):
        threading.Thread.__init__(self)
        self.name = name
        self.num = num
        self.daemon = True
        
    def run(self):
        print(self.name + '쓰레드 시작')
        while True:
            self.num -= 1
            print(self.name, '=>',self.num)
            if self.num==0:
                print(self.name + '쓰레드 종료')
                break
            time.sleep(1)


# In[16]:


num = input('카운트 다운 수 입력')
CountDownThread(num,int(num)).start()

