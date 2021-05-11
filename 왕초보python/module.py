import calendar
calendar.prmonth(2022,5)

from tkinter import *
widget = Label(None, text='i love')
widget.pack()

print([v for v in dir(calendar) if 'leap' in v])
print(help(calendar.isleap))
print(calendar.isleap(2017))