import time,random,os,winreg,re
from threading import Thread

def beginning():
    time.sleep(1)
    if not os.path.exists(check_path):
        check_file_create(check_path)
        print('/ '*20+'WARNING'+' /'*20)
        print(' '*28+'此程序仅供整活，如有雷同，他抄我的。')
        print('/ '*20+'WARNING'+' /'*20)
        time.sleep(3)
        print('\n\n')
    try:
        start()
    except OverflowError as error:
        print('Fortune over flow:\n',error)
        exit()
    except  ConnectionError as error:
        print('Something wrong with your Python!\n')
        exit()
    except SystemError as error:
        print('Something happened to you computer:(\n',error)
        exit()

def check_file_create(path):
    with open(path,'w') as file:
        file.write('This file just for check.')

def start():
    fortune=random.randint(1,10000)
    if fortune==6666:
        raise OverflowError('You\'re so lucky!Try to find the reason from the code after palying.')
    elif (fortune+1)%1000==0:
        raise ConnectionError('Make sure you have installed Python correctly,and have setted environment variable.')
    elif fortune%100==0:
        raise SystemError('Meybe you can restart your computer or rerun this program')

def cut(temp):
    if not os.path.exists(desktop_check_path):
        n=0
        while True:
            print('Processing……')
            time.sleep(1)
            if check(temp) and n<2:
                x=int(temp.split('*')[0])
                y=int(temp.split('*')[1])
                print('输入符合规范√')
                return x,y
            elif check(temp) and n>=2:
                x=int(temp.split('*')[0])
                y=int(temp.split('*')[1])
                print('你可算是做个人了')
                return x,y
            elif n<2:
                temp=input('请输入乘法算式:')
                n+=1
            elif n==2:
                print('你确定('+temp+')这玩意儿是乘法算式?')
                temp=input('请输入乘法算式:')
                n+=1
            elif n==3:
                print('你tm来找茬的是吧？')
                temp=input('虽说事不过三，但我再给你一次机会：')
                n+=1
            elif n==4:
                try:
                    putout()
                except SystemError as error:
                    print('你不配合那我也不配合\n',error)
                finally:
                    check_file_create(desktop_check_path)

    else:
        while True:
            if check(temp):
                x=int(temp.split('*')[0])
                y=int(temp.split('*')[1])
                print('输入符合规范√')
                return x,y
            else:
                temp=input('请输入乘法算式:')

def check(temp):
    pattern='^\d+\*\d+$' #感觉此处正则不对劲，摆了(
    result=re.search(pattern,temp)
    if result!=None:
        return True
    else:
        return False

def putout():
    raise SystemError('滚吧滚吧，自己爱哪玩哪玩去')

def calcu(x,y):
    time.sleep(random.randint(2000,5000)/1000)
    try:
        calculate(x,y)
    except RuntimeError as error:
        print('The program think you are despising it\n')
    except SystemError as error:
        print('Too boring,right?\n') 
    except MemoryError as error:
        print('Memory out!\n',error)
    finally:
        exit()

def calculate(x,y):
    if abs(x*y)<=10**6:
        sleep(150,100,600,250,1200,500,7000,3000)
        raise RuntimeError('Maybe try some number farther to zero.')
    elif abs(x)<10**10 and abs(y)<10**10:
        temp=0
        start_time=time.time()
        t1=Thread(target=thread1,args=(abs(x),abs(y)))
        t2=Thread(target=thread2,args=(abs(x),abs(y)))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        end_time=time.time()
        print('计算结果为：'+str(x*y)+'\n计算时间为：'+str(end_time-start_time))
        raise SystemError('Maybe try some number farther or closer to zero.')
    else:
        sleep(300,100,1000,500,3000,1000,10000,3000)
        raise MemoryError('But we still gat the anwser,'+(x)+'*'+(y)+'='+str(x*y)+'Maybe try some number closer to zero')

def thread1(x,y):
    global temp
    total=0
    while temp<x:
            total+=y
            temp+=1

def thread2(x,y):
    global temp
    time.sleep(10)
    if temp<x*0.4 and temp>x*0.15:
        print('开始计算')
        n=0
        t=0
        persent=x//100
        while n<x:
            t+=y
            n+=1
            if n%persent==0:
                print('计算进度：'+(temp//persent)+'%')
    else:
        sleep(400,200,600,200,1000,300,7000,2000)
        
def sleep(temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8):
    print('计算开始')
    for persent in range(1,91):
        time.sleep(random.randint((temp1-temp2),(temp1+temp2))/1000)
        print('计算进度：'+str(persent)+'%')
    for persent in range(1,10):
        time.sleep(random.randint((temp3-temp4),(temp3+temp4))/1000)
        print('计算进度：'+str(persent+90)+'%')
    for temp in range(1,6):
        time.sleep(random.randint((temp5-temp6),(temp5+temp6))/1000)
        print('计算进度：99%')
    time.sleep(random.randint((temp7-temp8),(temp7+temp8))/1000)

self_path=os.path.abspath(__file__)
check_path='\\'.join(self_path.split('\\')[:-1])+'\\check.txt'\
    
desktop_path=winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'), "Desktop")[0]
# 这行是复制粘贴再稍加修改的
# 版权声明：本文为CSDN博主「有情怀的机械男」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_45769063/article/details/124707721
desktop_check_path=desktop_path+'\\check.txt'
