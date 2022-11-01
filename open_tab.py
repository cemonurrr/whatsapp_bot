import pymysql.cursors
import pyautogui 
import webbrowser as wb
import time
from datetime import datetime


db = pymysql.connect(host='localhost', port=3306, user='user',
    passwd='pass',db='db', charset="utf8")

while True:

  c = db.cursor()
  update=db.cursor()
  sql1=('select * from hastalar')
  c.execute(sql1)
  print("Hasta bekleniyor.....")
  for row in c:

#row[6]=tel
#row[4]=name
#row[5]=surname etc..

     gun=row[0]
     dateStr = str(gun.day)+ "/" + str(gun.month) + "/" + str(gun.year) 
     print (dateStr)
     wb.open("https://web.whatsapp.com/send?phone=90"+ row[6] +"&text=Say%C4%B1n+"+ row[4] +" "+ row[5] +" "+ dateStr +"+saat+"+ row[1] +"+da+"+ row[2] +"+Dr+"+ row[3] +"+ile+muayene randevunuz olusturulmustur.")
     time.sleep(10)
   
     print(row [1])
   
     sql2=('update hastalar set wp_msj='1' where id=id ')
     update.execute(sql2)
     time.sleep(5)
     pyautogui.keyDown("ctrl")
     pyautogui.press("f4")
     pyautogui.keyUp("ctrl")

  db.close()
