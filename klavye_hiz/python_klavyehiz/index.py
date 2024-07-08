from tkinter import *
import random
from tkinter import messagebox
from words import words






def time():
    global timer,score,miss
    if timer>10:
        pass
    else:
        timerlabelcount.configure(fg='red')
    if timer>0:
        timer -=1
        timerlabelcount.configure(text=timer)
        timerlabelcount.after(1000,time)
    else:
        gameinstruction.configure(text='Doğru = {} | Yanlış= {} | Toplam Score = {}'
                                  .format(score,miss,score-miss))


        seviye=score-miss
        durum=0
        if seviye < 20:
         durum="Seviyen Yavaş"
        
        
        elif 20 <= seviye < 40:
         durum="Seviyen Normal"
        
        
        elif 40 <= seviye < 60:
         durum="Seviyen Hızlı"
         
        
        else: 
         durum="Seviyen Çok Hızlı" 

        rr= messagebox.askretrycancel('Bilgi',durum)
        if rr==True:
            score=0
            miss=0
            timer=60
            timerlabelcount.configure(text=timer)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)
            wordentry.delete(0, END)
        else:
                root.destroy()




def startgame(event):
    global score, miss
    if timer==60:
        time()
    gameinstruction.configure(text='')
    startlabel.configure(text='')
    if wordentry.get()== wordlabel['text']:
        score +=1
        scorelabelcount.configure(text=score)
    else:
        miss +=1
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0,END)


root= Tk()
root.geometry('800x600+400+100')
root.title('Klavye Hız Testi')

score=0
miss=0
timer=60
count=0



startlabel=Label(root,text='Yazmaya Başla',font=('airal',40,
                  'italic bold'),fg='black',bg='yellow')
startlabel.place(x=260,y=30)



random.shuffle(words)
wordlabel=Label(root,text=words[0],font=('airal',45,
                'italic bold'),fg='green')
wordlabel.place(x=350,y=240)




scorelabel=Label(root,text='Doğru kelimeler:',font=('arial',25,
                'italic bold'),fg='red')
scorelabel.place(x=10,y=100)

scorelabelcount=Label(root,text=score,font=('arial',25,
                'italic bold'),fg='blue')
scorelabelcount.place(x=150,y=180)





timerlabel=Label(root,text='Kalan Zaman:',font=('arial',25,
                'italic bold'),fg='red')
timerlabel.place(x=600,y=100)

timerlabelcount=Label(root,text=timer,font=('arial',25,
                'italic bold'),fg='blue')
timerlabelcount.place(x=600,y=180)



gameinstruction= Label(root,text=' ',
                       font=('arial',25,'italic bold'),fg='grey')
gameinstruction.place(x=120,y=500)



wordentry= Entry(root,font=('airal',25,'italic bold'),bd=10,justify='center')
wordentry.place(x=240,y=400)
wordentry.focus_set()


root.bind('<Return>',startgame)
root.mainloop()