import time

import customtkinter as ctk

T_time = -10
APP = ctk.CTk()

width  = APP.winfo_screenwidth()
height = APP.winfo_screenheight()

APP.after(1, APP.wm_state, 'zoomed')
APP.title("Team Sudarshan Ground Control")
APP.iconbitmap("sudarshan.ico")

# Set the background color for the entire window
APP.configure(fg_color="#111010")

# Title Frame at the top
titleFrame = ctk.CTkFrame(APP, fg_color='#000000', height=80)
titleFrame.pack(side="top", fill="x")

# Option Frame on the left
optionFrame = ctk.CTkFrame(APP, fg_color='#000000', width=300)
optionFrame.pack(side="left", fill="y")

# Window Frame takes the remaining space
windowFrame = ctk.CTkFrame(APP, fg_color='#111010')
windowFrame.pack(side="left", fill="both", expand=True)

# topics in top frame
# Flight status
statusFixedLabel = ctk.CTkLabel(titleFrame, text='Status', font=("Font Awesome 5 Brands", 30))
statusFixedLabel.grid(row=0, column=1, padx='20', pady='25')

statusVariableLabel = ctk.CTkLabel(titleFrame, text='Preparing', font=("Font Awesome 5 Brands", 30))
statusVariableLabel.configure(text_color="#ABFFA9")
statusVariableLabel.grid(row=0, column=2)

# Flight Name
nameFixedLabel = ctk.CTkLabel(titleFrame, text='Flight Name', font=("Font Awesome 5 Brands", 30))
nameFixedLabel.grid(row=0, column=3, padx=(370, 20))

nameVariableLabel = ctk.CTkLabel(titleFrame, text='Trishul', font=("Font Awesome 5 Brands", 30))
nameVariableLabel.configure(text_color="Yellow")
nameVariableLabel.grid(row=0, column=4)

# Time
def live_Time():
    t = time.strftime('%H:%M:%S')
    timeLabel.configure(text = t)
    timeLabel.after(1000, live_Time)

timeLabel = ctk.CTkLabel(titleFrame, text='20:20:20', font=("Font Awesome 5 Brands", 30))
live_Time()
timeLabel.grid(row=0, column=5, padx=(500,20))


# topics in left frame
def dashboard():
    '''Function to bring dashboard in window frame'''
    dashboardButton.configure(fg_color="#111010")
    valuesButton.configure(fg_color="#000000")
    gyroButton.configure(fg_color="#000000")
    trajectoryButton.configure(fg_color='#000000')

def values():
    '''Function to bring values in window frame'''
    dashboardButton.configure(fg_color="#000000")
    valuesButton.configure(fg_color="#111010")
    gyroButton.configure(fg_color="#000000")
    trajectoryButton.configure(fg_color='#000000')
def gyro():
    '''Function to bring gyro section as separate window'''
    dashboardButton.configure(fg_color="#000000")
    valuesButton.configure(fg_color="#000000")
    gyroButton.configure(fg_color="#111010")
    trajectoryButton.configure(fg_color='#000000')
def trajectory():
    '''Function to bring gyro section as separate window'''
    dashboardButton.configure(fg_color="#000000")
    valuesButton.configure(fg_color="#000000")
    gyroButton.configure(fg_color="#000000")
    trajectoryButton.configure(fg_color='#111010')

def launch():
    '''To Launch the rocket and stat the time button'''
    statusVariableLabel.configure(text='Launching', text_color="#ABFFA9")
    launchButton.configure(state='DISABLED')

    def count():
        '''Function To start timer and goes till end'''
        global T_time

        if T_time == -10:
            display = "-10"
        else:
            display = str(T_time)

        tLable.configure(text=f'T {display}')

        tLable.after(1000, count)
        if T_time > 0:
            statusVariableLabel.configure(text='Launched', text_color="#52F44F")
        T_time += 1

    count()

dashboardButton = ctk.CTkButton(optionFrame, width=290, height=80, text='Dashboard', font=("Font Awesome 5 Brands", 30), fg_color='#000', hover_color='#111010', corner_radius=20, command=dashboard)
dashboardButton.grid(row=0, column=1, padx=10, pady=(25, 5))

valuesButton = ctk.CTkButton(optionFrame, width=290, height=80, text='Values', font=("Font Awesome 5 Brands", 30), fg_color='#000', hover_color='#111010', corner_radius=20, command=values)
valuesButton.grid(row=1, column=1, padx=10, pady=(5, 5))

gyroButton = ctk.CTkButton(optionFrame, width=290, height=80, text='Gyro Visuals', font=("Font Awesome 5 Brands", 30), fg_color='#000', hover_color='#111010', corner_radius=20, command=gyro)
gyroButton.grid(row=2, column=1, padx=10, pady=(5, 5))

trajectoryButton = ctk.CTkButton(optionFrame, width=290, height=80, text='Trajectory', font=("Font Awesome 5 Brands", 30), fg_color='#000', hover_color='#111010', corner_radius=20, command=trajectory)
trajectoryButton.grid(row=3, column=1, padx=10, pady=(5, 5))

launchButton = ctk.CTkButton(optionFrame, width=290, height=80, text='Launch', text_color='red', font=("Font Awesome 5 Brands", 30), fg_color='#000', hover_color='#111010', corner_radius=20, command=launch)
launchButton.grid(row=4, column=1, padx=10, pady=(5, 5))

tLable = ctk.CTkLabel(optionFrame, text='T -10', font=("Font Awesome 5 Brands", 50))
tLable.grid(row=5, column=1, padx=10, pady=(150, 5))

APP.mainloop()