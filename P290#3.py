from tkinter import *

def Celsius():
    temperaturevalue = float(CelsiusRes.get())
    convert_temp_val = (temperaturevalue * 9 / 5) + 32
    FahrenheitRes.set(convert_temp_val)

def Fahrenheit():
    temperaturevalue = float(FahrenheitRes.get())
    convert_temp_val = (temperaturevalue - 32) * (5 / 9)
    CelsiusRes.set(convert_temp_val)

windows = Tk()
windows.geometry("300x100")
windows.title("Temperature Converter")

Label1=Label(windows,text="Celsius")
Label2=Label(windows,text="Fahrenheit")

CelsiusRes=StringVar()
CelsiusRes.set("0.0")

FahrenheitRes=StringVar()
FahrenheitRes.set("32.0")

Entry1=Entry(windows,textvariable=CelsiusRes)
Entry2=Entry(windows,textvariable=FahrenheitRes)

Button1=Button(windows,text=">>>>",bg="gray",command=Celsius)
Button2=Button(windows,text="<<<<",bg="gray",command=Fahrenheit)

Label1.grid(row=0,column=0)
Label2.grid(row=0,column=1)

Entry1.grid(row=1,column=0)
Entry2.grid(row=1,column=1)

Button1.grid(row=2,column=0)
Button2.grid(row=2,column=1)

windows.mainloop()
