import tkinter as tk

import Calendar
MyWindow = tk.Tk()
MyWindow.title("Calendar")
MyWindow.geometry('1200x700')

Year = tk.StringVar()
Month = tk.StringVar()
Day = tk.StringVar()


LabelYear = tk.Label(MyWindow, text="Enter the Year")
LabelMonth = tk.Label(MyWindow, text="Enter the Month")
LabelDay = tk.Label(MyWindow, text="Enter the Day")
LabelDate = tk.Label(MyWindow, text="The Date is")

LabelYear.grid(row=1, column=1)
LabelMonth.grid(row=2, column=1)
LabelDay.grid(row=3, column=1)
LabelDate.grid(row=4, column=1)

EntryYear = tk.Entry(MyWindow, textvariable=Year)
EntryYear. grid(row=1, column=2)
EntryMonth = tk.Entry(MyWindow, textvariable=Month)
EntryMonth. grid(row=2, column=2)
EntryDay = tk.Entry(MyWindow, textvariable=Day)
EntryDay. grid(row=3, column=2)

def clicked():
    Year = (Year.get())
    Month = (Month.get())
    Day = (Day.get())
    labelDate.config(text= "%d/%d/%d" % Year, Month, Day)

buttonDate = tk.Button(MyWindow, text="Set Date", command=clicked)
buttonDate.grid(row=5, column=0)


MyWindow.mainloop()
