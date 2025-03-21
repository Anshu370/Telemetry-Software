from tkinter import *

ws = Tk()
ws.geometry('400x450+1000+300')
ws.title('PythonGuides: Stopwatch')
ws.config(bg='#299617')
ws.resizable(0, 0)

counter = -1
running = False


def counter_label(lbl):
    def count():
        if running:
            global counter
            if counter == -1:
                display = "00"
            else:
                display = str(counter)

            lbl['text'] = display

            lbl.after(1000, count)
            counter += 1

    count()


def StartTimer(lbl):
    global running
    running = True
    counter_label(lbl)
    start_btn['state'] = 'disabled'
    stop_btn['state'] = 'normal'
    reset_btn['state'] = 'normal'


def StopTimer():
    global running
    start_btn['state'] = 'normal'
    stop_btn['state'] = 'disabled'
    reset_btn['state'] = 'normal'
    running = False


def ResetTimer(lbl):
    global counter
    counter = -1
    if running == False:
        reset_btn['state'] = 'disabled'
        lbl['text'] = '00'
    else:
        lbl['text'] = ''




lbl = Label(
    ws,
    text="00",
    fg="black",
    bg='#299617',
    font="Verdana 40 bold"
)

label_msg = Label(
    ws, text="minutes",
    fg="black",
    bg='#299617',
    font="Verdana 10 bold"
)

lbl.place(x=160, y=170)
label_msg.place(x=170, y=250)

start_btn = Button(
    ws,
    text='Start',
    width=15,
    command=lambda: StartTimer(lbl)
)

stop_btn = Button(
    ws,
    text='Stop',
    width=15,
    state='disabled',
    command=StopTimer
)

reset_btn = Button(
    ws,
    text='Reset',
    width=15,
    state='disabled',
    command=lambda: ResetTimer(lbl)
)

start_btn.place(x=30, y=390)
stop_btn.place(x=150, y=390)
reset_btn.place(x=270, y=390)

ws.mainloop()