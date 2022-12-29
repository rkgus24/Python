from PyQt5.QtWidgets import *
import sys
import threading
            
from myjoystick import MyJoystick

from PyQt5 import QtWidgets
import socket
import time
import struct
import numpy as np
import cv2
from PyQt5 import QtGui

HOST_CAM = '192.168.137.34'
PORT_MOT = 81
url = f'rtsp://{HOST_CAM}:8554/mjpeg/1'

client_mot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_mot.connect((HOST_CAM, PORT_MOT))

t_now = time.time()
t_prev = time.time()
cnt_frame = 0
total_frame = 0
cnt_time = 0

def camMain() :
   global t_now, t_prev, cnt_frame, total_frame, cnt_time

   width = 320
   height = 240
   label.resize(width, height)
   cap = cv2.VideoCapture(url)

   while True:   

      ret, frame = cap.read()
      frame2 = cv2.resize(frame, (320, 240))
       
      h,w,c = frame2.shape
      qImg = QtGui.QImage(frame2.data, w, h, w*c, \
      QtGui.QImage.Format_RGB888)
      pixmap = QtGui.QPixmap.fromImage(qImg.rgbSwapped())
      label.setPixmap(pixmap)

      cnt_frame += 1
      t_now = time.time()
      if t_now - t_prev >= 1.0 :
         t_prev = t_now
         total_frame += cnt_frame
         cnt_time += 1
         print("frame count : %f, %d average : %f" \
         %(cnt_frame, cnt_time, total_frame/cnt_time))
         cnt_frame = 0
         
def cbJoyPos(joystickPosition) :
   posX, posY = joystickPosition
      
   # 자동차 방향
   right, left = -1, -1
   if posY < -0.5:
      right, left = 1, 1 # brake
   elif posY > 0.15 :
      if -0.15 <= posX <= 0.15 :
         right, left = 0, 0 # forward
      elif posX < -0.15 : 
         right, left = 1, 0 # left
      elif posX > 0.15 :
         right, left = 0, 1 # right
   else : # -0.5 <= posY <= 0.15
      right, left = 1, 1 # stop driving
   
   rl = right << 1 | left
   print(rl)
   rl_byte = struct.pack('B', rl)
   client_mot.sendall(rl_byte)

# Create main application window
app = QApplication([])
app.setStyle(QStyleFactory.create("Cleanlooks"))
mw = QMainWindow()
mw.setWindowTitle('RC Car Joystick')
mw.setGeometry(100, 100, 300, 200)

# Create and set widget layout
# Main widget container
cw = QWidget()
ml = QGridLayout()
cw.setLayout(ml)
mw.setCentralWidget(cw)

# Create Screen
label = QtWidgets.QLabel()
ml.addWidget(label,0,0)

# Create joystick
joystick = MyJoystick(cbJoyPos)
ml.addWidget(joystick,1,0)

camThread = threading.Thread(target=camMain)
camThread.start()

mw.show()

# Start Qt event loop 
sys.exit(app.exec_())