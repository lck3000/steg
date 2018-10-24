import os
from steg import steg_img
from PIL import Image,ImageTk
from tkinter import Frame,Tk,PhotoImage,Label,Entry,IntVar,StringVar,BooleanVar,Button,Checkbutton,W,E,N,S,LEFT,RIGHT,HORIZONTAL,VERTICAL
from tkinter.ttk import Notebook,Separator
import tkinter.filedialog as tfd
from steg import steg_img

def truncate(text:str):
    if len(text)>30:
        return text[0:8]+'...'+text[-20:-1]+text[-1]
    else:
        return text

def filepick(element):
    xpath = tfd.askopenfilename()
    if xpath:
        element.set('')
        element.set(xpath)

def folderpick(element):
    pass

def filehide(textfile,imagefile):
    print('[+] Hiding',textfile,'on',imagefile)
    a = steg_img.IMG(payload_path=textfile,image_path=imagefile)
    a.hide()

def extract(imagefile):
    print('[+] Extracting data from',imagefile)
    b = steg_img.IMG(image_path=imagefile)
    b.extract()

class SFrame:
    def __init__(self, *args, **kwargs):
        self.look = Frame()
        self.look.grid_columnconfigure(0,minsize=40)
        self.look.grid_columnconfigure(5,minsize=40)
        self.look.grid_columnconfigure(10,minsize=40)
        self.look.grid_rowconfigure(0,minsize=40)
        self.look.grid_rowconfigure(7,minsize=40)
        self.look.grid_rowconfigure(10,minsize=40)
    
    def show(self):
        return self.look

class Hide(SFrame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.label1 = Label(self.look,text='Texto:')
        self.label1.grid(row=1,column=1,sticky=W,pady=10)
        self.var1 = StringVar()
        self.label2 = Label(self.look,width=20,anchor=W,textvariable=self.var1)
        self.label2.grid(row=1,column=2,sticky=W,pady=10)
        self.button1 = Button(self.look,text='Examinar',command=lambda:filepick(self.var1))
        self.button1.grid(row=2,column=2,pady=10)

        self.label3 = Label(self.look,text='Imagen:')
        self.label3.grid(row=4,column=1,sticky=W,pady=10)
        self.var2 = StringVar()
        self.label4 = Label(self.look,width=20,anchor=W,textvariable=self.var2)
        self.label4.grid(row=4,column=2,sticky=W,pady=10)
        self.button2 = Button(self.look,text='Examinar',command=lambda:filepick(self.var2))
        self.button2.grid(row=5,column=2,pady=10)

        self.button3 = Button(self.look,text='Ejecutar',command=lambda:filehide(self.var1.get(),self.var2.get()))
        self.button3.grid(row=6,column=2,pady=10)

class Unhide(SFrame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.label1 = Label(self.look,text='Imagen:')
        self.label1.grid(row=1,column=1,sticky=W,pady=10)
        self.var3 = StringVar()
        self.label2 = Label(self.look,width=20,anchor=W,textvariable=self.var3)
        self.label2.grid(row=1,column=2,sticky=W,pady=10)
        self.button1 = Button(self.look,text='Examinar',command=lambda:filepick(self.var3))
        self.button1.grid(row=2,column=2,pady=10)

        self.button3 = Button(self.look,text='Ejecutar',command=lambda:extract(self.var3.get()))
        self.button3.grid(row=6,column=2,pady=10)

class MainWindow:
    def __init__(self, *args, **kwargs):
        self.window_title = 'Steg - Fredy Arias'
        self.hide_title = 'Ocultar'
        self.unhide_title = 'Revelar'
        self.w = 330
        self.h = 335
        self.notebook_w = 310
        self.notebook_h = 290
        self.notebook_p = 10
        
    def show(self):
        self.main = Tk()
        self.main.title(self.window_title)
        self.n1 = Notebook(self.main)
        self.hide = Hide()
        self.unhide = Unhide()
        self.n1.add(self.hide.show(),text=self.hide_title)
        self.n1.add(self.unhide.show(),text=self.unhide_title)
        self.n1.configure(width=self.notebook_w,
                        height=self.notebook_h,
                        padding=self.notebook_p)
        self.n1.grid(row=0,column=0)
        self.ws = self.main.winfo_screenwidth()
        self.hs = self.main.winfo_screenheight()
        self.x = (self.ws/2) - (self.w/2)
        self.y = (self.hs/2) - (self.h/2)
        self.main.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.main.mainloop()

if __name__ == '__main__':
    window = MainWindow()
    window.show()
    

