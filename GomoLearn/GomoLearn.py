from tkinter.ttk import *
from tkinter import Tk, scrolledtext
from PIL import ImageTk, Image
import json

# Global
f = open('Data.json')
data = json.load(f)
attempt = 0


# Function
def check_valid():
    global label8, attempt, btn2
    user_input = entry1.get()
    user_input = user_input.split(' ')
    answer = True
    while '' in user_input:
        user_input.remove('')
    if not user_input:
        label8.config(text='False', foreground='red', font='bold')
        attempt += 1
        answer = False
    for i in user_input:
        if i not in valid_move:
            label8.config(text='False', foreground='red', font='bold')
            attempt += 1
            answer = False
            break
    if answer:
        label8.config(text='True', foreground='green', font='bold')
    if attempt >= 3:
        btn2.config(state='normal')
    return


def load_setting():
    global label2, label5, image, valid_move, entry1, btn1
    try:
        var = combo.get()

        # Change Image
        img = data[var]["image"]
        image = Image.open(img)
        image = ImageTk.PhotoImage(image)
        label2.config(image=image)

        # Show problem
        label5.config(text=data[var]["problem"])

        # Init Valid move
        valid_move = data[var]["solution"]

        # Unlock
        entry1.config(state='normal')
        btn1.config(state='normal')
    except:
        entry1.config(state='disable')
        btn1.config(state='disable')
        img = 'Gomolearn.png'
        image = Image.open(img)
        image = ImageTk.PhotoImage(image)
        label2.config(image=image)


def show():
    global label9
    var = combo.get()
    text = '\n'.join(data[var]['solution']).upper()
    print('Solution:', text)
    label9.config(text=text, font=('Times New Roman', 11, 'bold'))
    return


# Build GUI
window = Tk()
window.geometry("")
window.resizable(0, 0)
window.title('GomoLearn by Nguyen Cong Minh')
window.iconbitmap('Gomolearn.ico')

label0 = Label(window)
label0.grid(column=0, row=0)

label1 = Label(window, text='Choose exercise:')
label1.grid(column=1, row=1, sticky='W')

combo = Combobox(window, width=23)
combo.grid(column=2, columnspan=1, row=1, sticky='W')
combo['values'] = data['Ex']

btn = Button(window, text='Choose', command=load_setting)
btn.grid(column=3, columnspan=3, row=1, sticky='E', padx=10)

image = Image.open('Gomolearn.png')
image = ImageTk.PhotoImage(image)
label2 = Label(window, image=image)
label2.grid(column=1, columnspan=5, row=2, sticky='W', padx=10, pady=10)

label3 = Label(window)
label3.grid(column=1, row=3)

label4 = Label(window, text='Problem:')
label4.grid(column=1, row=4, sticky='W')

label5 = Label(window, text='')
label5.grid(column=2, columnspan=2, row=4, rowspan=3, sticky='WE')

label6 = Label(window, text='Type your solution:')
label6.grid(column=1, row=8, sticky='W')

entry1 = Entry(window, width=35, state='disable')
entry1.grid(column=2, columnspan=4, row=8, sticky='E', padx=10)

label7 = Label(window, text='Status:')
label7.grid(column=1, row=9, sticky='W')

label8 = Label(window, text='')
label8.grid(column=2, row=9)

label9 = Label(window, text='')
label9.grid(column=1, row=10, padx=10, pady=10, sticky='w')

btn1 = Button(window, text='Submit', command=check_valid, state='disable')
btn1.grid(column=3, columnspan=3, row=10, sticky='E', padx=10)

btn2 = Button(window, text='Show answer', state='disable', command=show)
btn2.grid(column=2, row=10, sticky='E', pady=10, ipadx=10)
window.mainloop()
