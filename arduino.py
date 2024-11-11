import serial
import openpyxl
from openpyxl import Workbook
import time

class Arduino():
    def __init__(self,com):
       self.device = serial.Serial(port=f'COM{com}', baudrate=115200, timeout=.1)
       print("正在建立通訊...")
       self.wb = Workbook() #建立EXCEL 
       self.ws = self.wb.active
       self.ws.append(["Time", "Voltage"])  # 標題行           
       time.sleep(2)
       print(f"已連線成功COM{com}")

    def write_read(self):
        self.device.write(bytes('v',"utf-8"))
        time.sleep(0.5)
        data = self.device.readline().decode().strip()
        try:
            voltage = float(data) /1023 * 5
            return voltage
        except ValueError:
            return 'error'
        
    def record_data(self,voltage:float):
        self.ws.append([time.strftime("%H:%M:%S"), float(f'{voltage:.2f}')])  # 加入時間與電壓
        
        
    def save_data(self): # 儲存 Excel 檔案
        self.wb.save("data.xlsx")
        self.device.close() 
        
    def getVoltage(self,count:int,delay:float=0.5):
        voltage = []
        for i in range(count):
            value  = self.write_read()
            if value == 'error':
                value   = self.write_read()
            print(f'{value:.2f}')
            voltage.append(value)
            time.sleep(delay)
        avg = sum(voltage)/len(voltage)
        self.record_data(avg)
        return avg
    
if __name__ == '__main__' :
    arduino = Arduino(6)
    input("Enter")
    value = arduino.getVoltage(5,0.5)
    print(f'平均值等於{value:.2f}')
    #arduino.record_data(value)
    arduino.save_data()