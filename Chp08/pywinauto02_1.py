from pywinauto.application import Application
from pywinauto import timings
# from pywinauto import findwindows
import time
import os

app = Application().start("C:/KiwoomFlash3/Bin/NKMiniStarter.exe")

title = "번개3 Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys('naige95')  # 로그인 ID 비밀 번호 입력

btn_ctrl = dlg.Button0
btn_ctrl.Click()

time.sleep(50)

app2 = Application().start("C:/KiwoomFlash3/Bin/NKMiniStarter.exe")
title2 = "번개3"
dlg2 = timings.WaitUntilPasses(20, 0.5, lambda: app2.window_(title=title2))
btn_ctrl2 = dlg2.Button1
btn_ctrl2.Click()

'''
cert_ctrl = dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKeys('cert_password')   # 공인인증서 비밀번호
'''

# 공인인증서 안넣었을 때 뜨는 창을 시스템적으로 확인 버튼 누르는 방법
# pywinauto를 위한 window나 dialog 찾아내는 inspection/spy Program 찾을 것


