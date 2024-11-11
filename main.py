from motor_08TMC2U import M08TMC2U
from arduino import Arduino

import time
driver1 = M08TMC2U(11)
driver2 = M08TMC2U(4)

driver1.rotate_speed(15000)     #driver1 速度上限
driver2.rotate_speed(15000)     #driver2 速度上限

driver1.rotate_mode(1)          #driver1 相對移動
driver2.rotate_mode(1)          #driver2 相對移動
driver1.rotate_moving_mode(1)   #driver1 S曲線
driver2.rotate_moving_mode(1)   #driver2 S曲線

arduino = Arduino(6)

try:
    x = int(input("請輸入次數:"))
except ValueError:
    print('輸入整數')
    x = 0
    
#馬達1=1次轉1度 馬達2=1次轉5度
for i in range(1,x+1,1):
    driver1.rotate_mode('INC')
    driver1.rotate_degreed(1,1)
    time.sleep(0.5)
    driver1.rotate_mode('INC')
    driver1.rotate_degreed(2,5)
    time.sleep(0.5)
    arduino.getVoltage(3,0.5)
arduino.save_data()