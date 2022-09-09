import os
import os.path
import datetime
import re
import stat
import time

x=r"D:\main"

print("started")
os.chdir(x)

def listDir(dir):
    file=os.listdir(dir)
   
    for files in file:
        if files.endswith('.jpg'):
           #print(os.getcwd())
           c=os.path.abspath(files)
           m_time = os.path.getmtime(c)
           modificationtime=time.strftime('%d%m%y',time.localtime(os.path.getmtime(c)))
           Modificationtime=str(modificationtime)
           print(Modificationtime)
    #for i in range(10):
        #print(Modificationtime[i]+'_',i)
           #print("last modified time:",modificationtime)
          
           #dt_m = datetime.datetime.fromtimestamp(m_time)
           #print('Modified on:', dt_m,split(","))
           
          
           
           #print(files)
           #c= os.path.abspath(files)
           #print(c)
           #d=datetime.datetime.strptime(file,"%d %b %y")
           #print(time.ctime(os.path.getmtime(x)))
           #d=datetime.datetime.strptime(file,"%d %b %y")
           #print(files)
           #print(d.year)
listDir(x)


