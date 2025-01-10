
# 
# Graphical
# User
# Interface


# 
# widgets = GUI elements: buttons, textboxes, labels, image
# window = serves as a container to hold or contain these widgets

from tkinter import *
window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title("Ongthing first GUI Program")

icon = PhotoImage(file='thumb-1920-1337527.png')
window.iconphoto(True,icon)
window.config(background="black") # you can set # value


window.mainloop() # place window on computer screen, listen for events

# label
# an area widget that holds text and/or an image within a window
# from tkinter import *

window = Tk()


photo = PhotoImage(file='FKbqpDHYxsDeGfcraQYk2B-320-80.png')


label = Label(window,
              text="Hello World",
              font=('arial',40,'bold'),
              fg='green', # you can use '#00FF00'
              bg='black',
              relief=RAISED, # SUNKEN . and that is border style
              bd=10, # border size
              padx=20, # width border space
              pady=20,   # length text and border
              image=photo,
              compound='bottom') # 'top' .photo move
label.pack() # write note display world

#label.place(x=0,y=0) # position text


window.mainloop()


# 
# button = you click it, then it does stuff
from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)
    print("you click the button")

window = Tk()


photo = PhotoImage(file='img.png')
button = Button(window,text="click me!",
                fg='#00FF00',
                bg='black',
                command=click,
                image=photo,
                activeforeground='#00FF00',
                activebackground='black',
                compound='bottom',)
                #state=DISABLED) # disabled click
button.pack()

window.mainloop()

# 
# entry widget = text box that accepts a single line of users input

from tkinter import *


def submit():
    user_name = entry.get()
    print(user_name)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()
entry = Entry(window,font=('arial',40),
              fg='#00FF00',
              bg='black')

# entry.insert(0,'spongebob')
# entry.config(show="*")
# entry.config(state=DISABLED)


entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)

back_space_button = Button(window,text="backspace",command=backspace)
back_space_button.pack(side=RIGHT)

window.mainloop()





# check_button

from tkinter import *

def display():
    if (x.get()==1): # if (x.get)) # if (x.get()=="Yes")
        print("You agree!")
    else:
        print("You don't agree:(")

window = Tk()

x = IntVar() # onvalue= 1 offvalue = 0
# x = BooleanVar() # onevalue = True offvalue=False
# x = StringVar()

photo = PhotoImage(file='img_1.png')
check_button = Checkbutton(window,text= 'I agree to something',
                           variable=x,
                           onvalue=1, # True # 'Yes'
                           offvalue=0, # False # 'No'
                           command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           activebackground='black',
                           activeforeground='#00FF00',
                           pady=10,
                           padx=20,
                           image=photo,
                           compound='right')

check_button.pack()
window.mainloop()




# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ['pizza','hamburger','hotdog']

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered hamburger!")
    elif(x.get()==2):
        print("You ordered hotdog!")
    else:
        print("Huh")
window = Tk()
pizza_image = PhotoImage(file='img_2.png')
hamburger_image = PhotoImage(file='img_3.png')
hotdog_image = PhotoImage(file='img_4.png')
food_image = [pizza_image,hamburger_image,hotdog_image]


x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], # adds text to radio buttons
                              variable=x, # groups radiobuttons together if they share the variable
                              value=index, # assigns each radiobutton a different value
                              padx=500, # adds padding on x-axis
                              font=('impact',50),
                              image=food_image[index], # adds image to radiobutton
                              compound='left', # adds image & text (left-side)
                              indicatoron=1, # eliminate circle indicators
                              width=2000, # sets width of radio buttons
                              command=order # set command of radio button to function
                              )
    radiobutton.pack(anchor=W)



window.mainloop()

# tkinter temperature scale




from tkinter import *

def submit():
    print("the temperature is: "+str(scale.get())+ "degree c")

window = Tk()

hot_image = PhotoImage(file='img.png')
hotlabel = Label(image=hot_image)
hotlabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=300,
              orient=VERTICAL, # orientation of scale
              font=('consolas',20),
              tickinterval=10, # adds numeric indicators for value
              resolution=5, # increment of slider
              # showvalue=0, hide current value
              troughcolor='#69eaff',
              fg ='#ff1c00',
              bg='#111111')
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

coldimage = PhotoImage(file='img_1.png')
coldlabel = Label(image=coldimage)
coldlabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()




import time
# listbox = a listing of selectable text items within it's own container

def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("you have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())
def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())


from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('constantia',35),
                  width=12,
                  selectmode=MULTIPLE)

listbox.pack()

listbox.insert(1,'pizza')
listbox.insert(2,'pasta')
listbox.insert(3,'garlic bread')
listbox.insert(4,'soup')
listbox.insert(5,'salad')

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

submitbutton = Button(window,text='submit',command=submit)
submitbutton.pack()

addbutton = Button(window,text='add',command=add)
addbutton.pack()

delete_button = Button(window,text='delete',command=delete)
delete_button.pack()



window.mainloop()


from tkinter import *
from tkinter import messagebox  # messagebox library

def click():

    messagebox.showinfo(title='this is an info message box',message='you are a person')
    messagebox.showwarning(title='warning!',message='you have a virus!!!')
    while(True):
        messagebox.showwarning(title='warning!',message='you have a virus!!!')
    # messagebox.showerror(title='error!',message='something went wrong : (')

if messagebox.askokcancel(title='ask ok cancel',message='do you want to do the thing?'):
    print('you did a thing')
else:
    print('you canceled a thing(')


if messagebox.askretrycancel(title='ask or cancel',message='do you want retry the thing?'):
    print('you did a thing')
else:print('you canceled a thing(')
if messagebox.askyesno(title='ask yes or no',message='do you like cake?'):
    print("i like cake tooo :)")
else:
    print("why do you not like cake? :(")

messagebox.askquestion(title='ask question',message='do you like pie?')
answer = messagebox.askquestion(title='ask question',message='do you like pie?')
if (answer=='yes'):
    print("i like pie too :)")
else:
    print('why do you not like pie? :(')

messagebox.askyesnocancel(title='yes no cancel',message='do you like to code?')

answer = messagebox.askyesnocancel(title='yes no cancel', message='do you like to code?',icon='warning') #info, error
if (answer==True):
    print("you like to code :)")
elif(answer==False):
    print("then why are you watching a vidoe on coding?")
else:
    print("you have dodged the question")



# colorchooser
from tkinter import *
from tkinter import colorchooser # submodule

def click():
    color = colorchooser.askcolor() # assign color to a variable
    print(color)
    colorhex = color[1] # assigns elements at index 1 to a variable
    print(colorhex)
    window.config(bg=colorhex) #change background color # change background color
window = Tk()

window.geometry('420x420')

button = Button(text='click me',command=click)
button.pack()

window.mainloop()


# text widget = functions like a text area, you can enter multiple lines of text

from tkinter import *

def submit():
    input = text.get('1.0',END)
    print(input)

window = Tk()

text = Text(window,
            bg='light yellow',
            font=8,
            width=20,
            padx=20,
            pady=20,
            fg='purple')
text.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()


# file open and read direct print
def openfile():
    filepath = filedialog.askopenfilename()#initialdir="c:\\users\\arfun  uddin\\pycharmprojects\pythonproject1\\",
    #                                       title="open file okay?",
    #                                       filetypes= (("text file","*.txt"),
    #                                       ('all files','*.*')))
    # print(filepath)
    file = open(filepath,'r') # that is a file read and run
    print(file.read())
    file.close()


from tkinter import *
from tkinter import filedialog

window = Tk()
button = Button(window,text='open',command=openfile)
button.pack()

window.mainloop()


# save file and text
from tkinter import *
from tkinter import filedialog

def savefile():
    file = filedialog.asksaveasfile(initialdir="c:\\users\\arfun  uddin\\pycharmprojects\\pythonproject1",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("text file",".txt"),
                                        ("html file", ".html"),
                                        ("all files", ".*")
                                    ])

    filetext = str(text.get('1.0',END)) # filetext = input ("enter some text i guess: ") # that show the print main file

    file.write(filetext)
    file.close()

window = Tk()

button = Button(text='save',command=savefile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()


# file menu from tkinter
from tkinter import *

def openfile():
    print('file has been opened!')
def savefile():
    print('file has been saved!')
def cut():
    print('you cut some text')
def copy():
    print('you copied some text!')
def paste():
    print('you pasted some text')


window = Tk()

openimage = PhotoImage(file='img_6.png')
saveimage = PhotoImage(file='img_7.png')
exitimage = PhotoImage(file='img_8.png')



menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0,)
menubar.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='open',command=openfile,image=openimage,compound='left')
filemenu.add_command(label='save',command=savefile,image=saveimage,compound='left')
filemenu.add_separator()
filemenu.add_command(label='exit',command=quit,image=exitimage,compound='left')

editmenu = Menu(menubar,tearoff=0,)
menubar.add_cascade(label='edit',menu=editmenu)
editmenu.add_command(label='cut',command=cut)
editmenu.add_command(label='copy',command=copy)
editmenu.add_command(label='paste',command=paste)


window.mainloop()



# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg='pink',bd=5,relief=SUNKEN)
frame.pack() # side=bottom)
# frame.place(x=0,y=0)

Button(frame,text='w',font=('consolas',25),width=3).pack(side=TOP)
Button(frame,text='a',font=('consolas',25),width=3).pack(side=LEFT)
Button(frame,text='s',font=('consolas',25),width=3).pack(side=LEFT)
Button(frame,text='d',font=('consolas',25),width=3).pack(side=LEFT)

window.mainloop()


# created  window
from tkinter import *

def create_window():
    new_window = Tk()  #Toplevel() = new window 'on top' of other windows,linked to a 'bottom' window
                             #TK() = new independent window

    old_window.destroy()    # close out of old window


old_window = Tk()
Button(old_window,text='create new window',command=create_window).pack()

old_window.mainloop()


# tab tab notebook

from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) # widget that manages a collection of windows / display
tab1 = Frame(notebook) # new frame for tab1
tab2 = Frame(notebook)

notebook.add(tab1,text='tab 1')
notebook.add(tab2,text='tab 2')
notebook.pack(expand=True,fill='both') # expand = expand to fill any space not otherwise used
                                    # fill = fill space on x and y azix
Label(tab1,text='hello, this is tab 1',width=50,height=25).pack()
Label(tab2,text='good bye , this is tab 2',width=50,height=25).pack()

window.mainloop()

# grid() = geometry manager that organizes widgets in a table- like structure in a parents

from tkinter import *

window = Tk()
titlelabel = Label(window,text="enter your info",font=('arial',25)).grid(row=0,column=0,columnspan=2)

first_namelabel = Label(window,text='first name: ',width=20,bg='red').grid(row=1,column=0)
first_nameentry = Entry(window).grid(row=1,column=1)

email_label = Label(window,text='email: ',bg='green').grid(row=2,column=0)
email_entry = Entry(window).grid(row=2,column=1)

passl_abel = Label(window,text='password: ',bg='blue',width=30).grid(row=3,column=0)
pass_entry = Entry(window).grid(row=3,column=1)

submit_button = Button(window,text='submit',).grid(row=4,column=0,columnspan=2)

window.mainloop()


# download method tkinter
from tkinter import *
from tkinter .ttk import *
import time

def star():
    tasks = 10
    x = 0
    while(x<tasks):
        time.sleep(1)
        bar['value']+=10
        x += 1

        percent.set(str(int((x/tasks)*100))+"%")
        text.set(str(x)+"/"+str(tasks)+" tasks completed ")
        window.update_idletasks()
window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

parcentlavel = Label(window,textvariable=percent).pack()
tasklabel = Label(window,textvariable=text).pack()

button = Button(window,text='download',command=star).pack()

window.mainloop()

from tkinter import *
from tkinter .ttk import *
import time

def star():
    gb = 10
    download = 0
    speed = 1
    while(download<gb):
        time.sleep(0.05)
        bar['value']+=(speed/gb)*100
        download+=speed


        percent.set(str(int((download/gb)*100))+"%")
        text.set(str(download)+"/"+str(gb)+" gb completed ")
        window.update_idletasks()
window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

parcentlavel = Label(window,textvariable=percent).pack()
tasklabel = Label(window,textvariable=text).pack()

button = Button(window,text='download',command=star).pack()

window.mainloop()


# canvas = widget that is used to draw graphs, plots, image in a window

from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)

canvas.create_line(0,0,500,500,fill='blue',width=5)
canvas.create_line(0,500,500,0,fill='red',width=5)
canvas.create_rectangle(50,50,250,250,fill='purple')
points = [250,0,500,500,0,500]
canvas.create_polygon(points,fill='yellow',outline='black',width=5)


canvas.create_arc(0,0,500,500,style=PIESLICE,start=180) # style=chord,arc

# simple project
# canvas.create_arc(0,0,500,500,fill='red',extent=180,width=7)
# canvas.create_arc(0,0,500,500,fill='white',extent=180,start=180,width=7)
# canvas.create_oval(190,190,310,310,fill='white',width=10)
#
canvas.pack()


window.mainloop()



# game control button show tap
from tkinter import *

def dosomething(event):
    # print('you did a thing')
    # print('you pressed: '+event.keysym)
    label.config(text=event.keysym)

window = Tk()

# window.bind('<return>',dosomething) # event, function
window.bind('<Key>',dosomething) # <q>
label = Label(window,font=('helvetica',100),)
label.pack()
#
window.mainloop()




# move  Recetangle tkinter

from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startx = event.x
    widget.starty = event.y
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startx + event.x
    y = widget.winfo_x() - widget.starty + event.y
    widget.place(x=x,y=y)

window = Tk()

label = Label(window,bg='red',width=10,height=5)
label.place(x=0,y=0)

label2 = Label(window,bg='blue',width=10,height=5)
label2.place(x=0,y=0)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)
#
label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()


# image move from tkinter

from tkinter import *
def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)
def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())

window = Tk()

window.geometry("820x820")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

my_image = PhotoImage(file='img_10.png')
label = Label(window,image=my_image)
label.place(x=0,y=0)


window.mainloop()



# canvas image move
from tkinter import *

def move_up(event):
    canvas.move(myimage,0, -10)
def move_down(event):
    canvas.move(myimage,0, 10)
def move_left(event):
    canvas.move(myimage,-10, 0)
def move_right(event):
    canvas.move(myimage, 10, 0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("Left>",move_left)
window.bind("<Right>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoimage = PhotoImage(file='img_10.png')
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)


window.mainloop()


# mouse control button

from tkinter import *

def dosomething(event):
    print('mouse coordinates: '+str(event.x)+","+str(event.y))

window = Tk()

window.bind("<Button-1>",dosomething) # left mouse click
window.bind("<Button-2>",dosomething) # scroll wheel
window.bind("<Button-3>",dosomething) # right mouse click
window.bind("<ButtonRelease>",dosomething) # all mouse direction
window.bind("<enter>",dosomething) # enter the window
window.bind("<leave>",dosomething) # leave the window
window.bind("<motion>",dosomething) # where the mouse moved
window.mainloop()


# animation move tkinter something maybe problem

from tkinter import *
import time


width = 500
height = 500
xVelocity = 3
yVelocity = 2


window = Tk()

canvas = Canvas(window,width=width,height=height)
canvas.pack()

background_photo = PhotoImage(file='img_15.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW)


photo_image = PhotoImage(file='img_14.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    # print(coordinates)
    if(coordinates[0]>=(width-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(height-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)  # (my_image,xvelocity,0) left -> (my_image,0,yvelocity)
    window.update()
    time.sleep(0.01)
window.mainloop()


# ball animation tkinter

from tkinter import *
from Ball import *
import time

window = Tk()

width = 500
height = 500

canvas = canvas(window,width=width,height=height)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,'white')
tennis_ball = Ball(canvas,0,0,50,4,3,'yellow')
basket_ball = Ball(canvas,0,0,125,8,7,'orange')



while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()

    window.update()
    time.sleep(0.01)

window.mainloop()




# clock program tkinter
from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%a")
    day_label.config(text=day_string)

    date_string = strftime("%B %D, %Y")
    date_label.config(text=date_string)


    time_label.after(1000,update)

window = Tk()

time_label = Label(window,font=('arial',50),fg="#00ff00",bg='black')
time_label.pack()

day_label = Label(window,font=('ink free',25))
day_label.pack()

date_label = Label(window,font=('ink free',35))
date_label.pack()

update()
window.mainloop()


# sent email python
import smtplib
sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"
subject = "python email test"
body = "i wrote an email! :d"

#header
message = f""""from: snoop dogg{sender}
to: bro code{receiver}
subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("logged in....")
    server.sendmail(sender, receiver, message)
    print('email has been sent')
except smtplib.SMTPAuthenticationError:
    print('unable to sign in')
# this fake email sender



# run .py file with cmd
# save file as .py (python file)
# go to command prompt
#  navigate to directory w/ your file: cd c:\users\arfun uddin\dekstop
# invoke python interpreter + script: python hello_word.py

print("hello world")
name = input("what is your name? ")
print("hello "+name)


# python pip
# ********************************************************************
# pip = package manager for packages and modules from python package index
#
#           included for python version
#            open command prompt

#          help:                                    pip
#          check:                                   pip --version
#          update:                                  pip install --upgrade pip
#          installed packages:                      pip list
#          check outdated packages                  pip list --outdated
#          install a package:                       pip install "package name"

# ***********************************
# python calculator
# ********************************8**
# #
from tkinter import *

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)
def equals():
    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")

        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")

        equation_text = ""
def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""

window = Tk()
window.title("calculator program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window,textvariable=equation_label,font=("consolas",20),bg='white',width=24,height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,height=4,width=9,font=35,
                 command=lambda: button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text=2,height=4,width=9,font=35,
                 command=lambda: button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text=3,height=4,width=9,font=35,
                 command=lambda: button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,height=4,width=9,font=35,
                 command=lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame,text=5,height=4,width=9,font=35,
                 command=lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame,text=6,height=4,width=9,font=35,
                 command=lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,height=4,width=9,font=35,
                 command=lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame,text=8,height=4,width=9,font=35,
                 command=lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame,text=9,height=4,width=9,font=35,
                 command=lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame,text=0,height=4,width=9,font=35,
                 command=lambda: button_press(0))
button0.grid(row=3,column=0)

plus = Button(frame,text='+',height=4,width=9,font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0,column=3)

minus = Button(frame,text='-',height=4,width=9,font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1,column=3)

multiply = Button(frame,text='*',height=4,width=9,font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2,column=3)

divide = Button(frame,text='/',height=4,width=9,font=35,
                 command=lambda: button_press('/'))
divide.grid(row=3,column=3)

equal = Button(frame,text='=',height=4,width=9,font=35,
                 command=equals)
equal.grid(row=3,column=2)

decimal = Button(frame,text='.',height=4,width=9,font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=3,column=1)

clear = Button(window,text='clear',height=4,width=12,font=35,
                 command=clear)
clear.pack()

window.mainloop()



# font arial box

from tkinter import *

# create the root window
root = Tk()
root.title("font selector example")

# text area
text_area = Text(root, font=("arial", 12))
text_area.pack()

# frame for dropdown menus
frame = Frame(root)
frame.pack()

# font options
font_name = StringVar()
font_name.set("arial")  # default font
font_box = OptionMenu(frame, font_name, "arial", "courier", "times new roman")
font_box.pack(side=LEFT)

# font size options
size_var = StringVar()
size_var.set("12")  # default font size
size_box = OptionMenu(frame, size_var, "8", "10", "12", "14", "16", "18", "20", "24")
size_box.pack(side=LEFT)

 # function to change the font and size
def change_font(*args):
    # update the text area's font
    text_area.config(font=(font_name.get(), size_var.get()))

# link the dropdown menus to the change_font function
font_name.trace("w", change_font)
size_var.trace("w", change_font)

# start the main loop
root.mainloop()





# full font text arial save from tkinter

import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="pick a color...or else")
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    window.title("untitled")
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("all files", "*,*"),
                                 ("text documents", "*.txt")])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")

        text_area.insert(1.0, file.read())
    except Exception:
        print("couldn't read file")
    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialfile='untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("all files ", "*.*"),
                                                   ("text documents", "*.txt")])

    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))
        except Exception:
            print("couldn't save file")
        finally:
            file.close()

def cut():
    text_area.event_generate("<<cut>>")

def copy():
    text_area.event_generate("<<copy>>")

def paste():
    text_area.event_generate("<<paste>>")

def about():
    showinfo("about this program", "this is a program written by you")

def quit():
    window.destroy()

window = Tk()

window.title("text editor program")

file = None

window_width = 500
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height /2))

window.geometry("{}x{}+{}+{}".format(window_width,window_height, x,y))

font_name = StringVar(window)
font_name.set("arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)


frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color",command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="new", command=new_file)
file_menu.add_command(label="open", command=open_file)
file_menu.add_command(label="save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="edit", menu=edit_menu)
edit_menu.add_command(label="cut", command=cut)
edit_menu.add_command(label="copy", command=copy)
edit_menu.add_command(label="paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="help", menu=help_menu)
help_menu.add_command(label="about", command=about)

window.mainloop()



# "tic-tac-toe")

from tkinter import *
import random

def next_turn(row,column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
            elif check_winner() == "tie":
                label.config(text=("tie!"))
        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is False:
                label.config(text=(players[1] + " wins"))
            elif check_winner() == "tie":
                label.config(text=("tie!"))

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='yellow')
        return "tie"
    else:
        return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1
    if spaces == 0:
        return False
    else:
        return True
def new_game():
    global player

    player = random.choice(players)
    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#f0f0f0")

window = Tk()
window.title("tic-tac-toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0,],
           [0,0,0,],
           [0,0,0,]]

label = Label(text=player +" turn",font=("consolas",40))
label.pack(side='top')

reset_button = Button(text='restart',font=("consolas",20), command=new_game)
reset_button.pack(side='top')

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame,text="",font=("consolas",40),width=5,height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)


window.mainloop()





# snake game tkinter in python

from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00ff00"
FOOD_COLOR = "#ff0000"
BACKGROUND_COLOR = "#000000"

class Snake():
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0,BODY_PARTS):
            self.coordinates.append(([0, 0]))


        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food():

    def __init__(self):

        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
         x += SPACE_SIZE

    snake.coordinates.insert(0, (x,y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)



def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != 'right':
            direction = new_direction
    elif new_direction == "right":
        if direction != 'left':
            direction = new_direction
    elif new_direction == "up":
        if direction != 'down':
            direction = new_direction
    elif new_direction == "down":
        if direction != 'up':
            direction = new_direction





def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:

        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("game over")
            return True

    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="game over", fill="red", tag="gameover")

window = Tk()
window.title("snake game")
window.resizable(False,False)

score = 0
direction = 'down'

label = Label(window,text='score:{}'.format(score),font=('consolas',40))
label.pack()

canvas = Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()


window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


snake = Snake()
food = Food()

next_turn(snake, food)
window.mainloop()

