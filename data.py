#encoding:utf-8
import serial
import sqlite3
import time
import os

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.close()
ser.open()
command="S"  #命令
cost=0   #时间修正值
i=0   #次数参数
ts=10   #刷新时间
cache=ser.readall()
print(cache)
root_dir="pic/"
file_list = os.listdir(root_dir)
time.sleep(1)

try:
    while 1:
        t = time.localtime(time.time())
        h = t.tm_hour
        m = t.tm_min
        s = t.tm_sec
        if (s+cost)%ts==0:    #每ts秒记一次数据，提前cost秒
            T1 = time.time()
            print("T1:%s"%T1)
            ser.write(command.encode())
            print('sent:%s'%command)
            state = ser.readline()
            if (len(state)>0):
                print('State:%s'%state.strip())
            humiditye = ser.readline()
            if (len(humiditye)>0):
                print('Humiditye:%s'%humiditye.strip())
            temperture = ser.readline()
            if (len(temperture)>0):
                print('Temperture:%s'%temperture.strip())

            if filter(str.isalpha,state) == "OK":
                try:
                    now = int(time.time())   #赋值实时时间（hhmmss）给now
                    T2=time.time()
                    print("T2:%s"%T2)
                    f= open("cache.txt","w")
                    f.write( "%s%s%s"%(temperture,humiditye,now))
                    f.close()

                    cost=int(round(T2-T1))
                    print("cost: %s"%cost)
                    i=i+1
                    print("i1:%s\n"%i)
                    time.sleep(1)

                    if i%(60/ts)==0:    #每分钟记一次数据
                        try:
                            conn = sqlite3.connect('DATA.db',timeout=10)
                            cursor = conn.cursor()  #建立指针
                            cursor.execute("SELECT ID FROM DATA_2HOURS ORDER BY ID ASC LIMIT 1;")  #排顺序
                            first_ID=cursor.fetchone() #获得第一个数据的ID
                            print (first_ID)
                            cursor.execute("SELECT count(*) FROM DATA_2HOURS;")  #返回现在数据库中的总行数到指针
                            count=cursor.fetchone()[0]   #用fetchone[0]输出总行数（不然类型是指针形的）
                            if count >= 120:#最大120个数据
                                conn.execute("DELETE from DATA_2HOURS where ID=?",(first_ID))
                                print("deleted: id=%s"%first_ID)
                            conn.commit()   #提交更改
                            print("DATA_2HOURS, time:%s,temp:%s,humi:%s"%(now,temperture.strip(),humiditye.strip()))
                            conn.execute("INSERT INTO DATA_2HOURS (ID,TEMP,HUM) \
                                VALUES (?,?,?)",(now,temperture.strip(),humiditye.strip()));   #记录数据
                            conn.commit()
                            print("DATA_2HOURS recorded i2:%s \n"%i)


                            if i%(720/ts)==0:   #12分钟记一次数据
                                try:
                                    conn = sqlite3.connect('DATA.db',timeout=10)
                                    cursor = conn.cursor()  #建立指针
                                    cursor.execute("SELECT ID FROM DATA_24HOURS ORDER BY ID ASC LIMIT 1;")  #排顺序
                                    first_ID=cursor.fetchone() #获得第一个数据的ID
                                    print (first_ID)
                                    cursor.execute("SELECT count(*) FROM DATA_24HOURS;")  #返回现在数据库中的总行数到指针
                                    count=cursor.fetchone()[0]   #用fetchone[0]输出总行数（不然类型是指针形的）
                                    if count >= 120:#最大120个数据
                                        conn.execute("DELETE from DATA_24HOURS where ID=?",(first_ID))
                                        print("deleted: id=%s"%first_ID)
                                    conn.commit()   #提交更改
                                    print("DATA_24HOURS, time:%s,temp:%s,humi:%s"%(now,temperture.strip(),humiditye.strip()))
                                    conn.execute("INSERT INTO DATA_24HOURS (ID,TEMP,HUM) \
                                        VALUES (?,?,?)",(now,temperture.strip(),humiditye.strip()));   #记录数据
                                    conn.commit()
                                    i=0
                                    print("DATA_24HOURS recorded i3:%s\n"%i)
                                except KeyboardInterrupt:
                                   conn.close()  #关闭连接
                                conn.close()
                                #删除旧图片（24hours）
                                if os.path.isfile('pic/temp_24hours.png'):
                                   os.remove('pic/temp_24hours.png')
                                   print("temp_24hours.png removed")
                                if os.path.isfile('pic/hum_24hours.png'):
                                   os.remove('pic/hum_24hours.png')
                                   print("hum_24hours.png removed")
                            if i!=0:
                                conn.close()
                            #删除旧图片（2hours）
                            if os.path.isfile('pic/temp_2hours.png'):
                                os.remove('pic/temp_2hours.png')
                                print("temp_2hours.png removed")
                            if os.path.isfile('pic/hum_2hours.png'):
                                os.remove('pic/hum_2hours.png')
                                print("hum_2hours.png removed")

                        except KeyboardInterrupt:
                            conn.close()  #关闭连接
                except KeyboardInterrupt:
                    sys.exit(1)
            else:
                print("There is a error occured in DHT11 ：%s"%state)
                i=i+1
                time.sleep(2)
except KeyboardInterrupt:
    ser.close()
