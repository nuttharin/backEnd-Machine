from pyModbusTCP.client import ModbusClient
from tkinter import *
#import tkinter
localhost = "192.168.250.1"
portTCP = 502
#auto_open = True

#tkinter._test()
window = Tk()
window.title("Welcome to Gas Machine")
window.geometry('350x200')
lbl0 = Label(window,text="")
lbl0.grid(column=5,row=3)


# lbl = Label(window,text="xxx")
# lbl.grid(column=6,row=3)

#c = ModbusClient(host=localhost,port=portTCP,auto_open=True)
#print(c)
#is_ok = c.write_single_coil(0,1)
#print(is_ok)
# if is_ok:
#     lbl.configure(text="OKKKKK")
# else:
#     lbl.configure(text="Noneee")




#print("Hello world")

window.mainloop()
