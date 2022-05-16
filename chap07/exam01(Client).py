#!/usr/bin/env python
# coding: utf-8

# # exam07_22.05.11
# * Client_Socket

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


class sendThread(threading.Thread):
    def __init__(self, soc):
        threading.Thread.__init__(self)
        self.soc = soc
        
    def run(self):
        while True:
                sMsg = input('입력 : ')
                in_list = sMsg.split('/')
                chatmsg = None
                if len(in_list)==1:                            # 모두에게 보내는 메시지
                    chatmsg = ChatMsg(sMsg)
                elif len(in_list)==2:                          # 특정인에게 보내는 메시지
                    n, msg = in_list
                    chatmsg = ChatMsg(msg, To = int(n))
                elif len(in_list)==3:                          # 특정인에게 파일첨부 보내기
                    n, msg, fname = in_list
                    with open(fname, 'rb') as fin:
                        fdata = fin.read()
                        chatmsg = ChatMsg(msg, To = int(n), attach = fdata)
                        print('보내는 파일크기 : ', len(chatmsg.attach))
                cmsg = pickle.dumps(chatmsg)
                self.soc.send(cmsg)


# In[ ]:


soc = socket(AF_INET, SOCK_STREAM)   # 소켓 생성
soc.connect(('127.0.0.1', 1122))     # 서버에 접속 ip주소/포트번호

sendThread(soc).start()

while True:
    msg = soc.recv(7168)        # 서버 데이터 수신 대기 (한꺼번에 받을 데이터 크기1KB )
    smsg = pickle.loads(msg)
    print(smsg)                 # 서버로부터 수신된 데이터를 화면에 표시
    if smsg.attach:
        print('받은 파일크기 : ', len(smsg.attach))
        with open('copy.jpg', 'wb') as fout:
            fout.write(smsg.attach)
            print('파일 저장 성공')

print('클라이언트 종료..~')


# In[ ]:


n,msg,fname = '3/msg/fname'.split('/')
with open('test.jpg', 'rb') as fin:
    img_data = fin.read()
print('이미지 로드 완료')

