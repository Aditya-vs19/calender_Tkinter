from tkinter import *
import tkinter as tk
import calendar
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('400x300')
root.title('Calendar')
root.configure(bg='#e3f2fd')  

def show():
    cal.delete(1.0, 'end')  
    m = int(month.get())
    y = int(year.get())
    output = calendar.TextCalendar().formatmonth(y, m)
    cal.insert('end', output)

def clear():
    cal.delete(1.0, 'end')

def exit():
    root.destroy()

# Load image
img = ImageTk.PhotoImage(Image.open('calendar.png'))
label = Label(root, image=img)
label.place(x=170, y=3)

# Month Label and Input
m_label = Label(root, text="Month", fg='#002147', bg='#e3f2fd', font=('verdana', '10', 'bold'))
m_label.place(x=70, y=80)
month = Spinbox(root, from_=1, to=12, width="5", fg='#002147', font=('verdana', '10'))
month.place(x=140, y=80)

# Year Label and Input
y_label = Label(root, text="Year", fg='#002147', bg='#e3f2fd', font=('verdana', '10', 'bold'))
y_label.place(x=210, y=80)
year = Spinbox(root, from_=2020, to=3000, width="8", font=('verdana', '10'))
year.place(x=260, y=80)

# Calendar Text Box
cal = Text(root, width=33, height=8, relief=RIDGE, borderwidth=2, font=('courier', '10'), bg='#ffffff', fg='#000000')
cal.place(x=70, y=110)

# Buttons
show_btn = Button(root, text="Show", bg='#1565C0', fg='#ffffff', font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=show)
show_btn.place(x=140, y=250)

clear_btn = Button(root, text="Clear", bg='#4FC3F7', fg='#ffffff', font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=clear)
clear_btn.place(x=200, y=250)

exit_btn = Button(root, text="Exit", bg='#F44336', fg='#ffffff', font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=exit)
exit_btn.place(x=260, y=250)

root.mainloop()
