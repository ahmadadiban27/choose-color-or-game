from tkinter import*
from tkinter import messagebox
import random

n=[1,2,3]
o=['+','-']
list1=[]
result=0
timer1=30
timer2=4
s=0
score=0
for n1 in n:
    for n2 in n:
        for n3 in n:
            for o1 in o:
                for o2 in o:
                   h= str(n1)+o1+str(n2)+o2+str(n3)
                   e=eval(h)
                   if e==3 or e==2 or e==1:
                       list1.append(h)
result = random.choices(list1)
s = eval(result[0])
#------------------------main-----------------------
win=Tk()
x=win.winfo_screenwidth()
y=win.winfo_screenheight()
x1=400
y1=400
xwin=(x//2)-(x1//2)
ywin=(y//2)-(y1//2)
win.geometry(f'{x1}x{y1}+{xwin}+{ywin}')
win.config(bg='#272BD9')
win.title('color and game')
#------------------------------function main-------------
def abut():
     messagebox.showinfo('abut', 'program name: The color or game selction  \n programer: Ahmad Adiban\n Data:02/10/2024')
def exit_win():
            mes=messagebox.askyesno('exit' , 'are you sure?')
            if mes:
                win.destroy()
def selc():
    if var.get()==1:
        win.destroy()
        win1=Tk()
        x=win1.winfo_screenwidth()
        y=win1.winfo_screenheight()
        x1=400
        y1=400
        xwin1=(x//2)-(x1//2)
        ywin1=(y//2)-(y1//2)
        win1.geometry(f'{x1}x{y1}+{xwin}+{ywin}')
        win1.title('color window')
        win1.config(bg='#A6CACA')

#---------------------function in wincolor-------------------------------
        def exit_color():
            mes=messagebox.askyesno('exit' , 'are you sure?')
            if mes:
                win1.destroy()
        def set2():
            tag=call_color.get()
            win1.config(bg=tag)
            lable_color.config(bg=tag)
#---------------------widgt in wincolor------------------------

        lable_color=Label(win1 , text = ' choose a color' , font=15,bg='#A6CACA',fg='#5C5CDE')
        set_b=Button(win1 ,text='set',font=('titr',10) ,width=12,bg='#0f0025', fg='#851230', command=set2)
        exit_but=Button(win1 , text = 'exit',font=('titr',10) ,width=12,bg='#0f0025', fg='#851230', command=exit_color)
        call_color=StringVar()
        call_color.set('none')
        color_list={'black':'black' , 'red':'red', 'white':'white', 'blue':'blue','yellow':'yellow', 'green':'green'}
        for name , color in color_list.items():
            rd=Radiobutton(win1 , text =name ,value=color,bg=color,fg='#854205' ,font=15,variable=call_color)
            rd.pack(side=TOP , pady=10)

        set_b.place(x=10, y=350)
        exit_but.place(x=260, y=350)
        lable_color.place(x=10 , y=100)
        win1.mainloop()
    elif var.get()==2:
        win.destroy()
        win2=Tk()
        x=win2.winfo_screenwidth()
        y=win2.winfo_screenheight()
        xw=400
        yw=400
        win2.geometry(f'{xw}x{yw}+{(x//2)-(xw//2)}+{(y//2)-(yw//2)}')
        win2.config(bg='#D8AA98')
        win2.title('playing numbers')
        #-------------------function-------------------------
        def one():
            global score
            global result
            global s
            if s == 1:
                score += 1
                score_n.config(text=score)
            result = random.choices(list1)
            s = eval(result[0])
            question_l.config(text=result)

        def two():
            global score
            global s
            global result
            if s==2:
                score += 1
                score_n.config(text=score)
            result = random.choices(list1)
            s = eval(result[0])
            question_l.config(text=result)

        def tree():
            global score
            global result
            global s
            if s == 3:
                score += 1
                score_n.config(text=score)
            result = random.choices(list1)
            s = eval(result[0])
            question_l.config(text=result)

        def ol():
            global timer1
            if timer1 != 0:
                # question_l.config(bg='#DBC229')
                fun_l.config(text='')
                timer1 -= 1
                timer_n.config(text=timer1)
                timer_n.after(1000, ol)
            else:
                fun_l.config(text=f'your scores:\n{score}', font=('zar',49))
                but1.config(state=DISABLED)
                but2.config(state=DISABLED)
                but3.config(state=DISABLED)
                new_b.config(state=NORMAL)
        def start():
            global timer1
            global timer2
            global s
            global result
            global list1
            # s=eval(result[0])
            # print(str(s))
            start_b.config(state=DISABLED)
            but1.config(state=NORMAL)
            but2.config(state=NORMAL)
            but3.config(state=NORMAL)
            new_b.config(state=DISABLED)
            # question_l.config(text=result ,font=('zar',20))
            if timer2 != 0:
                timer2-=1
                fun_l.config(text=f'**{timer2}**',font=('titr',105))
                win2.after(1000 , start)
            else:
                result = random.choices(list1)
                s = eval(result[0])
                question_l.config(text=result , font=('titr',20))
                ol()



        def exit():
            mas=messagebox.askyesno('Exit' ,'are you sure?')
            if mas:
                win2.destroy()
        def newgame():
            global timer1
            global  s
            global score
            global timer2
            global result
            timer1=30
            timer2=4
            start_b.config(state=NORMAL)
            score_n.config(text='0')
            score=0
            # result = random.choices(list1)
            # s = eval(result[0])
            question_l.config(text='click the start',font=('titr', 10) )
            fun_l.config(text='')



        #--------------------widget--------------------
        score_l=Label(win2 , text='your score:',font=10, bg='#D8AA98')
        timer_l=Label(win2, text='Time:',font=10, bg='#D8AA98')
        score_n=Label(win2 , text=score,font=10, bg='#D8AA98')
        timer_n=Label(win2, text='30', font=10,bg='#D8AA98')
        question_l=Label(win2 , text = 'click the Start' , font=('titr', 10) ,bg='#D8AA98' )
        but1=Button(win2 , text = '1' , state=DISABLED , width=10 ,bd=3 , fg='#F4D620',bg='#2B292F' , command=one )
        but2=Button(win2 , text = '2', state=DISABLED, width=10,bd=3 , fg='#F4D620',bg='#2B292F' , command=two)
        but3=Button(win2 , text = '3', state=DISABLED, width=10,bd=3 , fg='#F4D620',bg='#2B292F', command=tree)
        start_b=Button(win2 , text ='start', width=10,bd=3 , fg='#F4D620',bg='#2B292F' , command=start)
        exit_b=Button(win2,text='Exit', width=10,bd=3 , fg='#F4D620',bg='#2B292F' , command=exit)
        fun_l=Label(win2 , text ='' , font=('titr',105),fg='red' , bg='#D8AA98')
        new_b=Button(win2,text='New Game', state= DISABLED ,width=10,bd=3 , fg='#F4D620',bg='#2B292F' , command=newgame )
        score_l.place(x=20 , y=20)
        timer_l.place(x=270 , y=20)
        score_n.place(x=110 , y=20)
        timer_n.place(x=310 , y=20)
        question_l.place(x=140 , y=130)
        but1.place(x=70 , y=200)
        but2.place(x=150 , y=200)
        but3.place(x=230 , y=200)
        start_b.place(x=150 , y=270)
        exit_b.place(x=150 , y=350)
        fun_l.place(x=10 , y=15)
        new_b.place(x=150 , y=310)
        win2.mainloop()

#---------------------------------widget--------------------------------
labl1=Label(win , text='select an option and press start' ,bg='#272BD9',fg='#FCF004' ,font=('bzar',15))
select_b=Button(win ,font=('titr',10) ,width=8,bg='#FCF004', fg='#851230',bd=5, text='Start',command=selc )
exit_b=Button(win ,font=('titr',10) ,width=8,bg='#FCF004', fg='#851230',bd=5, text='Exit',command=exit_win )
help_b=Button(win ,font=('titr',10) ,width=8,bg='#FCF004', fg='#851230',bd=5, text='Help' )
abut_b=Button(win ,font=('titr',10) ,width=8,bg='#FCF004', fg='#851230',bd=5, text='Abut', command=abut )
var=IntVar()
r={'color':1,'game':2}
for i,j in r.items():
    rad= Radiobutton(win ,text=i , value=j  ,variable=var)
    rad.place(x=120*j,y=130)
select_b.place(x=150 , y=185)
exit_b.place(x=220 , y=260)
help_b.place(x=80 , y=260)
labl1.place(x=50 , y=50)
abut_b.place(x=150,y=330)
win.mainloop()