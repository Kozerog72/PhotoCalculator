from tkinter import *

root = Tk()
root["bg"] = '#FFFDD0'
root.title("Calculator of Photographer")
root.geometry("520x420")
root.resizable(False, False)

# Calculator_1

frame1 = LabelFrame(root, text="< CALCULATOR - 1 >", bg="#FFFDD0")
frame1.pack(padx=5, pady=5)


def calculator1():
    calc1 = int(e3.get()) * float(e1.get()) / int(e2.get())

    if calc1 < 0:
        result1["text"] = "NN"
    else:
        result1["text"] = round(calc1, 6)

    print(round(calc1, 6))


frame2 = LabelFrame(frame1, text="< OBJECT SIZE IN THE CAMERA MATRIX >", fg="maroon", bg="#FFDC85")
frame2.pack(padx=20, pady=15)

l1 = Label(frame2, text='Enter Camera Matrix size in mm:', width=35, pady=5, bg="#FFDC85")
l1.grid(row=0, column=0)

e1 = Entry(frame2, width=10, borderwidth=3)
e1.get()
e1.grid(row=0, column=1)
e1.insert(0, '')

l2 = Label(frame2, text='Enter Image Full size in pixels:', width=35, pady=5, bg="#FFDC85")
l2.grid(row=1, column=0)

e2 = Entry(frame2, width=10, borderwidth=3)
e2.get()
e2.insert(0, '')
e2.grid(row=1, column=1)

l3 = Label(frame2, text='Enter Measured Object size on the Image in pixels:', width=35, pady=5, bg="#FFDC85")
l3.grid(row=2, column=0)

e3 = Entry(frame2, width=10, borderwidth=3)
e3.get()
e3.insert(0, '')
e3.grid(row=2, column=1)

calculate1 = Button(frame2, text="CALCULATE >> (result - mm):", width=36, pady=6, fg="blue", command=calculator1)
calculate1.grid(row=3, column=0)

result1 = Label(frame2, width=10, borderwidth=3)
result1.grid(row=3, column=1)

result1.bind("<Button-1>", calculator1)

# Calculator_2

frame3 = LabelFrame(root, text="< CALCULATOR - 2 >", bg="#FFFDD0")
frame3.pack(padx=5, pady=5)


def calculator2():
    calc2 = ((int(e4.get()) / 10) * ((float(e6.get()) / 10) + (float(e5.get()))) / (float(e6.get()) / 10))

    if calc2 < 0:
        result2["text"] = "NN"
    else:
        result2["text"] = round(calc2, 4)

    print(round(calc2, 8))


frame4 = LabelFrame(frame3, text="< DISTANCE TO OBJECT >", fg="maroon", bg="#FFDC85")
frame4.pack(padx=20, pady=15)

b4 = Label(frame4, text='Enter the Lens Focal Length in mm:', width=35, pady=5, bg="#FFDC85")
b4.grid(row=0, column=0)

e4 = Entry(frame4, width=10, borderwidth=3)
e4.get()
e4.insert(0, '')
e4.grid(row=0, column=1)

b5 = Label(frame4, text='Enter True size of the Object in centimeter:', width=35, pady=5, bg="#FFDC85")
b5.grid(row=1, column=0)

e5 = Entry(frame4, width=10, borderwidth=3)
e5.get()
e5.insert(0, '')
e5.grid(row=1, column=1)

b6 = Label(frame4, text='Enter Object size on the Camera Matrix in mm:', width=35, pady=5, bg="#FFDC85")
b6.grid(row=2, column=0)

e6 = Entry(frame4, width=10, borderwidth=3)
e6.get()
e6.insert(0, '')
e6.grid(row=2, column=1)

calculate2 = Button(frame4, text="CALCULATE >> (centimeter):", width=36, pady=5, fg="blue", command=calculator2)
calculate2.grid(row=3, column=0)

result2 = Label(frame4, width=10, borderwidth=3)
result2.grid(row=3, column=1)

result2.bind("<Button-2>", calculator2)


root.mainloop()
