import tkinter
import tkinter.filedialog as dialog
import time
import  webbrowser

def exe():
       web=webbrowser.open_new_tab("http://google.com/?#q=")   
       web.open()
       
       web.close()

def book():
       web=webbrowser.open_new_tab("https://facebook.com")

def youtube():
        web=webbrowser.open_new_tab("https://www.youtube.com/?gl=IN")
        

def irtc():
        web=webbrowser.open_new_tab("https://www.services.irctc.co.in/")
        


def news():
        web=webbrowser.open_new_tab("http://www.hindustantimes.com/")
        
def tweet():
       web=webbrowser.open_new_tab("http://www.hindustantimes.com/")


linux=tkinter.Tk()
linux.title("search eng")
linux.geometry()

counter=tkinter.IntVar()
counter.set(2)
def click(var,value):
         var.set(var.get()+value)


         
         
#def search(Url):
  #entry.get(0.0,tkinter.END)     
  #tabUrl=("http://google.com/?#q=")
  #webbrowser.open(Url)
  


#frame2=tkinter.Frame(linux,cursor='mouse',bd=9,bg="blue")
#frame2.pack(side="left")
         
frame=tkinter.Frame(linux,cursor='mouse',bd=50,bg="powder blue")            
frame.pack(ipady=150,ipadx=700)



#we are going to create imge button using python

b1=tkinter.Button(frame,text="",command=exe)
b1.pack()
mi=tkinter.PhotoImage(file="e:\\GOOGLE.png")
b1.config(image=mi,compound="top")
tmi=mi.subsample(3,2)
b1.place(x=0,y=0)
#web=webbrowser.open_new_tab("http://google.com/?#q=")
b1.config(image=tmi)





#facebook image

b3=tkinter.Button(frame,text="",command=book)
b3.pack()
fi=tkinter.PhotoImage(file="e:\\facebook.png")
b3.config(image=fi,compound="right")
fmi=fi.subsample(3,6)
b3.place(x=4,y=90)
b3.config(image=fmi)


b4=tkinter.Button(frame,text="",command=youtube)
b4.pack()
yi=tkinter.PhotoImage(file="e:\\Youtube-256.png")
ymi=yi.subsample(2,4)
b4.place(x=1150,y=-2)
b4.config(image=ymi)

b5=tkinter.Button(frame,text="")
b5.pack()
twi=tkinter.PhotoImage(file="e:\\Twitter-256.png")
twmi=twi.subsample(2,4)
b5.place(x=1150,y=96)
b5.config(image=twmi)

b6=tkinter.Button(frame,text="")
b6.pack()
flipcart=tkinter.PhotoImage(file="e:\\flipcart.png")
iflipcart=flipcart.subsample(2,4)
b6.place(x=980,y=-2)
b6.config(image=iflipcart)

#train boking

b7=tkinter.Button(frame,text="IRTC",bg="black",command=irtc)
b7.pack()
train=tkinter.PhotoImage(file="e:\\train.png")
itrain=train.subsample(1,2)
b7.place(x=810,y=-4)
b7.config(image=itrain)

# news papper  

b8=tkinter.Button(frame,text="",command=news)
b8.pack()
news=tkinter.PhotoImage(file="e:\\news.png")
inews=news.subsample(1,2)
b8.place(x=650,y=-4)
b8.config(image=inews)

# music 
b9=tkinter.Button(frame,text="")
b9.pack()
music=tkinter.PhotoImage(file="e:\\music.png")
imusic=music.subsample(1,2)
b9.place(x=480,y=-2)
b9.config(image=imusic)

#cricbuzz
b10=tkinter.Button(frame,text="")
b10.pack()
cri=tkinter.PhotoImage(file="e:\\crikbuzz.png")
icri=cri.subsample(3,4)
b10.place(x=280,y=-2)
b10.config(image=icri)




#button=tkinter.Button(frame,text='up',command=lambda:click(counter,1),relief='groove')
#button.pack(side='left')
#button=tkinter.Button(frame,text='down',command=lambda:click(counter,-1))
#button.pack(side='right')
#label=tkinter.Label(frame,textvariable=counter)
#label.pack()
#cheakbutton=tkinter.Checkbutton(frame,text='keep me as log',fg="green",bg="powder blue",font=("Castellar",20,'bold'))
#cheakbutton.pack()
#button=tkinter.Button(linux,text="close",command=quit)
#button.pack()





text=tkinter.Text(linux,width=400,height=400,fg="white",bg="black",font=("Magneto",20),bd=54)
text.pack(side="top")


filename=None
def UpdateFile():
       f=text.get(0.0,tkinter.END)
       filename=dialog.askopenfilename(parent=linux,filetypes=[('Text','*.txt')],
       title='save as')
       
       new=open(filename,'r+')

       new.write(f)
       new.close()
       
 



text.delete (0.0,tkinter.END)

def saveFile():
       data=text.get(0.0,tkinter.END)
       filename=dialog.asksaveasfilename(parent=linux,filetypes=[('Text','*.txt')],
       title='save as')
       writer=open(filename,'w')
       writer.write(data)
       writer.close()

       
def EditFile():
        t=text.get(0.0,tkinter.END)
        filename=dialog.askopenfilename(parent=linux,filetypes=[('Text','*.txt')],
       title='save as')
        f=open(filename,'r')
        f.read(t)
        f.close()
        filename=dialog.asksaveasfilename(parent=linux,filetypes=[('Text','*.txt')],
        title='save as')
        f=open(filename,'w')
        f.write(t)
        f.close()

    #def click():
      #     entry.insert(0,1)
              
def openFile():
        f=open("url.py")
        t=f.read()
        text.insert(0.0,t)

        
       

menubar=tkinter.Menu(linux,bg="purple",bd=9,cursor='heart')
filemenu=tkinter.Menu(menubar,fg="purple",font=("old english text MT",20,"bold"),bd=9,cursor='heart')
filemenu.add_command(label="UpdateFile",command=UpdateFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="EditFile",command=EditFile)
filemenu.add_separator()


filemenu.add_command(label="close",command=quit)
menubar.add_cascade (label="   File    ",menu=filemenu)

linux.config(menu=menubar)
linux.config(background="gray99")

linux.mainloop()

