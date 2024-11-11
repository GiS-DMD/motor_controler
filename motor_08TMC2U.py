import serial

class M08TMC2U():
    def __init__(self,com):
       self.device = serial.Serial(port=f'COM{com}', baudrate=38400, timeout=.1,xonxoff=True)
       print(f"已連線成功COM{com}")
       
    def rotate_speed(self,high_speed):    #旋轉速度
        for i in range (1,3,1):
            if high_speed <= 16000 and high_speed >0 :
                self.device.write(bytes(f'@0{i}HSPD\r'.encode("utf-8")))
                if i ==1 :
                    print(f"設定馬達X軸旋轉速度上限為{high_speed}")  
                else :
                    print(f"設定馬達Y軸旋轉速度上限為{high_speed}")
            else :
                self.stop(f'馬達旋轉速度設定值錯誤')
                  
    def rotate_home(self,axis):           #回原點
        if axis == 1 or axis == 2 :
            self.device.write(bytes(f'@0{axis}HL-\r'.encode("utf-8")))   #\n待確認
            print(f"馬達{axis}回到原點")   
        else:
            self.stop("馬達回到原點指令錯誤")             
        
    def rotate_mode(self,mode='ABS'):    #移動模式
        for i in range (1,3,1):
            if mode == 'ABS':
                self.device.write(bytes(f'@0{i}ABS\r'.encode("utf-8")))   #\n\r待確認
                print('馬達已設定絕對移動模式')
                
            elif mode == 'INC':
                self.device.write(bytes(f'@0{i}INC\r'.encode("utf-8")))   
                print('馬達已設定相對移動模式')
                         
            else:
                self.stop(f'馬達{i}移動模式設定錯誤')
                
    def rotate_moving_mode(self,mod):    #旋轉曲線
        for i in range (1,3,1):        
            if mod == 0:
                self.device.write(bytes(f'@0{i}SCV=[{mod}]\r'.encode("utf-8")))   #\n\r待確認
                print(f'馬達{i}已設定梯形移動模式')
                       
            elif mod == 1:
                self.device.write(bytes(f'@0{i}SCV=[{mod}]\r'.encode("utf-8")))   #\n\r待確認
                print(f'馬達{i}已設定曲線移動模式')
            else:
                self.stop(f'馬達{i}移動型態設定錯誤 0為梯形、1為S形')    
                           
    def rotate_degreed(self,axis:int,rotate:float): #旋轉角度
        rotate = float(rotate)
        if axis == 1 or axis == 2:
            self.device.write(bytes(f'@0{axis}X[{rotate}]\r'.encode("utf-8")))
            print(f"馬達{axis}軸轉{rotate}度")
        else:
            self.stop('馬達轉軸設定錯誤')
            
    def rotate_stop(self):                  #強迫停止
        for i in range (1,3,1):
            self.device.write(bytes(f'@0{i}ABORT\r'.encode("utf-8")))
            print(f"馬達{i}停止運作")      
          
    def stop(self,code):                #錯誤代碼
        print(f"{code}")

