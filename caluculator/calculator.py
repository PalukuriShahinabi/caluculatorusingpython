from os import system
system('cls')
#====================================
import tkinter   
home = tkinter.Tk()
home.title('caluculator')
home.minsize(275,360)
home.maxsize(275,360)
screen = '0'

def btn_7(): #for 7 button clicking purpose same like below all
    global screen 
    if screen =='0':
        screen= '7'
    else:
        screen += '7'
    screenLbl.config(text=screen)

def btn_8():
    global screen 
    if screen =='0':
        screen= '8'
    else:
        screen += '8'
    screenLbl.config(text=screen)


def btn_9():
    global screen 
    if screen =='0':
        screen= '7'
    else:
        screen += '9'
    screenLbl.config(text=screen)

def btn_6():
    global screen 
    if screen =='0':
        screen= '6'
    else:
        screen += '6'
    screenLbl.config(text=screen)

def btn_5():
    global screen 
    if screen =='0':
        screen= '5'
    else:
        screen += '5'
    screenLbl.config(text=screen)

def btn_4():
    global screen 
    if screen =='0':
        screen= '4'
    else:
        screen += '4'
    screenLbl.config(text=screen)

def btn_3():
    global screen 
    if screen =='0':
        screen= '3'
    else:
        screen += '3'
    screenLbl.config(text=screen)

def btn_2():
    global screen 
    if screen =='0':
        screen= '2'
    else:
        screen += '2'
    screenLbl.config(text=screen)

def btn_1():
    global screen 
    if screen =='0':
        screen= '1'
    else:
        screen += '1'
    screenLbl.config(text=screen)

def btn_0():
    global screen 
    if screen =='0':
        screen= '0'
    else:
        screen += '0'
    screenLbl.config(text=screen)

def btn_c(): #for clearing the screen data
    global screen
    screen='0'
    screenLbl.config(text=screen)

def btn_b(): #for to get or remove i digit back value 
    global screen
    if len(screen) > 1:
        screen=screen[0:-1]
    else:
        screen ='0'
    screenLbl.config(text=screen)

def btn_A():
    global screen
    #if screen[-1] != '+' and screen[-1] != '-' and screen[-1] != '/' and screen[-1] != '*': #for not getting +-/* by clicking on it side by side
       #instead of this length line simply we use isdigit()
    if screen[-1].isdigit():
        screen += '+'
    screenLbl.config(text=screen)

def btn_S():
    global screen
    #if screen[-1] != '-' and screen[-1] != '+' and screen[-1] != '/' and screen[-1] != '*':
    if screen[-1].isdigit():
        screen += '-'
    screenLbl.config(text=screen)

def btn_D():
    global screen
    #if screen[-1] != '/' and screen[-1] != '-' and screen[-1] != '+' and screen[-1] != '*':
    if screen[-1].isdigit():   
        screen += '/'
    screenLbl.config(text=screen)

def btn_M():
    global screen
    #if screen[-1] != '*' and screen[-1] != '-' and screen[-1] != '/' and screen[-1] != '+':
    if screen[-1].isdigit():   
        screen += '*'
    screenLbl.config(text=screen)

def btn_Dot():
    global screen
    if screen[-1] != '.':
        screen += '.'
    screenLbl.config(text=screen)

def btn_E():
    global screen
    if screen[-1].isdigit():  
        screen = str(eval(screen)) #for evaluating input integers
    screenLbl.config(text=screen)




screenLbl = tkinter.Label(home, borderwidth=1,relief='groove',bg="#66FFFF", fg="black", anchor='e',padx=7, justify="right", text=screen, font=('bold', 22), width=14)
screenLbl.place(x=10, y=20)
btnc= tkinter.Button(home,command=btn_c, text='C', padx=10, font=("bold", 20))
btnc.place(x=10, y=75)
btnb= tkinter.Button(home, command=btn_b, text='Back', padx=19, font=("bold", 20))
btnb.place(x=70, y=75)
btnD= tkinter.Button(home, command=btn_D,text='/', padx=23, font=("bold", 20))
btnD.place(x=190, y=75)

btn7= tkinter.Button(home, command=btn_7, text='7', padx=12, font=("bold", 20))
btn7.place(x=10, y=130)
btn8= tkinter.Button(home, command=btn_8, text='8', padx=12, font=("bold", 20))
btn8.place(x=70, y=130)
btn9= tkinter.Button(home, command=btn_9,text='9', padx=12, font=("bold", 20))
btn9.place(x=130, y=130)
btnM= tkinter.Button(home,command=btn_M, text='*',  padx=21, font=("bold", 20))
btnM.place(x=190, y=130)

btn4= tkinter.Button(home, command=btn_4, text='4', padx=12, font=("bold", 20))
btn4.place(x=10, y=185)
btn5= tkinter.Button(home,  command=btn_5,text='5', padx=12, font=("bold", 20))
btn5.place(x=70, y=185)
btn6= tkinter.Button(home, command=btn_6,text='6', padx=12, font=("bold", 20))
btn6.place(x=130, y=185)
btnS= tkinter.Button(home,command=btn_S, text='-', padx=22, font=("bold", 20))
btnS.place(x=190, y=185)

btn1= tkinter.Button(home, command=btn_1, text='1', padx=12, font=("bold", 20))
btn1.place(x=10, y=240)
btn2= tkinter.Button(home, command=btn_2,text='2', padx=12, font=("bold", 20))
btn2.place(x=70, y=240)
btn3= tkinter.Button(home, command=btn_3,text='3', padx=12, font=("bold", 20))
btn3.place(x=130, y=240)
btnA= tkinter.Button(home,command=btn_A, text='+', padx=19, font=("bold", 20))
btnA.place(x=190, y=240)

btn0= tkinter.Button(home, command=btn_0, text='0', padx=12, font=("bold", 20))
btn0.place(x=10, y=295)
btnDot= tkinter.Button(home,command=btn_Dot,text='.', padx=15, font=("bold", 20))
btnDot.place(x=70, y=295)
btnE= tkinter.Button(home, command=btn_E,text='=', padx=49, font=("bold", 20))
btnE.place(x=130, y=295)

home.mainloop()