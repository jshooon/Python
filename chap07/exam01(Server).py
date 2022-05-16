#!/usr/bin/env python
# coding: utf-8

# # exam07_22.05.11
# * Server_Socket

# In[ ]:


# 서버에 접속, 데이터 송수신
# 서버는 클라이언트 접속 대기 상태로 존재해야 함
# 서버는 특정 클라이언트 간의 통신 중개 역할


# In[ ]:


from socket import *
import pickle
import time
from chat import ChatMsg
import threading


# In[ ]:


class ChatThread(threading.Thread):
    def __init__(self, soc, addr, num, soc_dict):
        threading.Thread.__init__(self)
        self.soc = soc
        self.addr = addr
        self.soc_dict = soc_dict
        self.num = num
    def run(self):
        for i,s in self.soc_dict.items():
            print(i,s)
            if s is self.soc:
                continue
            cmsg = pickle.dumps(ChatMsg(str(self.addr) + '접속'))
            s.send(cmsg)
        while True:
            try:
                msg = self.soc.recv(7168)
                chatmsg = pickle.loads(msg)
                if chatmsg.To:
                    soc_dict[chatmsg.To].send(msg)
                else:
                    for i,s in self.soc_dict.items():
                        if s is self.soc:
                            continue
                        s.send(msg)
            except:
                print(str(self.addr) + '퇴장')
                del self.soc_dict[self.num]
                for i,s in self.soc_dict.items():
                    cmsg = pickle.dumps(ChatMsg(str(self.addr) + '퇴장'))
                    s.send(cmsg)
                break
        print('ChatThread 종료')


# In[ ]:


serverSock = socket(AF_INET, SOCK_STREAM)   # 소켓 생성
serverSock.bind(('', 1122))                 # ip주소/포트번호
serverSock.listen(1)                        # 동시접속자를 1명으로 제한

soc_dict = {}
num = 0

while True:   
    print('서버 대기 중...')                    # 클라이언트가 접속할 때 까지 대기
    soc, addr = serverSock.accept()         # 클라이언트가 접속하면 통신소켓과 주소 리턴
    num += 1
    soc_dict[num] = soc
    ChatThread(soc, addr, num, soc_dict).start()
    
print('서버 종료...')

