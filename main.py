from function import *

if __name__=='__main__':
    while True:
        print('Program is in preparation……')
        beginning()
        equation=input('请输入要计算的整数乘法算式(格式：x*y，x、y为非0整数)：')
        x,y=cut(equation)
        if x%1==0 and y%1==0:
            print('Program is in preparation……')
            calcu(x,y)
        elif x<0 or y<0:
            print('I didn\'t thought about the situation that the number can be a minus number.\nMay the program will crash ,but I still try to calculate for you.')
            print('Program is in preparation……')
            calcu(x,y)
