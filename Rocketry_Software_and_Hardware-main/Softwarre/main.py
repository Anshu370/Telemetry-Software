import time

from tkinter import Scrollbar

import customtkinter as ctk

T_time = -10
APP = ctk.CTk()

width  = APP.winfo_screenwidth()
height = APP.winfo_screenheight()

APP.after(1, APP.wm_state, 'zoomed')
APP.title("Team Sudarshan Ground Control")
APP.iconbitmap(r"C:\Users\ARJITA\Documents\GitHub\Rocketry_Software_and_Hardware\Softwarre\sudarshan.ico")  

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

    accelerationFrame = ctk.CTkFrame(windowFrame, fg_color="#000000", width=590, height=130)
    accelerationFrame.grid(row=0, columnspan=2, padx=(10, 5), pady=(10, 5))

    velocityFrame = ctk.CTkFrame(windowFrame, fg_color="#000000", width=590, height=130)
    velocityFrame.grid(row=0, column=2, columnspan=2, padx=(5, 10), pady=(10, 5))

    llFrame = ctk.CTkFrame(windowFrame, fg_color="#000000", width=1190, height=60)
    llFrame.grid(row=1, columnspan=4, padx=(10, 5), pady=(10, 5))

    humidityFrame = ctk.CTkFrame(windowFrame, fg_color="#000000", width=285, height=130)
    humidityFrame.grid(row=2, column=0, padx=(5, 5), pady=(10, 5))

    altitudeFrame = ctk.CTkFrame(windowFrame, fg_color="#000000", width=285, height=130)
    altitudeFrame.grid(row=2, column=1, padx=(5, 5), pady=(10, 5))

    pressureFrame = ctk.CTkFrame(windowFrame, fg_color="#000000", width=285, height=130)
    pressureFrame.grid(row=2, column=2, padx=(5, 10), pady=(10, 5))

    tempratureFrame = ctk.CTkFrame(windowFrame, fg_color="#000000", width=285, height=130)
    tempratureFrame.grid(row=2, column=3, padx=(5, 10), pady=(10, 5))

    mfFrame = ctk.CTkFrame(windowFrame, fg_color="#000000", width=590, height=130)
    mfFrame.grid(row=3, columnspan=2, padx=(10, 5), pady=(10, 5))

    coFrame = ctk.CTkFrame(windowFrame, fg_color="#000000", width=285, height=130)
    coFrame.grid(row=3, column=2, padx=(5, 10), pady=(10, 5))

    h2Frame = ctk.CTkFrame(windowFrame, fg_color="#000000", width=285, height=130)
    h2Frame.grid(row=3, column=3, padx=(5, 10), pady=(10, 5))

    logFrame = ctk.CTkFrame(windowFrame, fg_color="#000000", width=1190, height=160)
    logFrame.grid(row=4, columnspan=4, padx=(10, 5), pady=(10, 5))

    # data of acceleration frame
    accelerationFixedLabel = ctk.CTkLabel(accelerationFrame, text="Acceleration", font=("Font Awesome 5 Brands", 30), text_color="white")
    accelerationFixedLabel.pack(side="top", padx=210, pady=15)
    accelerationcanvas = ctk.CTkCanvas(accelerationFrame, height=1, width=595, bg="white")
    accelerationcanvas.pack(side="top")
    accelerationData = ctk.CTkLabel(accelerationFrame, text=("X : 0 \t Y : 0 \t Z : 0"), font=("Font Awesome 5 Brands", 30), text_color="white")
    accelerationData.pack(side="bottom", pady=15)

    # data of velocity frame
    velocityFixedLabel = ctk.CTkLabel(velocityFrame, text = "Velocity", font=("Font Awesome 5 Brands", 30),text_color="white")
    velocityFixedLabel.pack(side="top", padx=210, pady=15 )
    velocitycanvas = ctk.CTkCanvas(velocityFrame, height=1, width=595, bg="white")
    velocitycanvas.pack(side="top")
    velocityData = ctk.CTkLabel(velocityFrame, text=("X : 0 \t Y : 0 \t Z : 0"), font=("Font Awesome 5 Brands", 30), text_color="white")
    velocityData.pack(side="bottom", pady=15)

    # data of ll frame

    # Longitude data
    longitudeLabel = ctk.CTkLabel(llFrame, text="Longitude:", font=("Font Awesome 5 Brands", 30), text_color="white")
    longitudeLabel.pack(side="left", padx=210, pady=15)

    longitudeData = ctk.CTkLabel(llFrame, text="0", font=("Font Awesome 5 Brands", 30), text_color="white")  # Replace with actual longitude value
    longitudeData.pack(side="left", padx=20, pady=15)

    # Latitude data
    latitudeData = ctk.CTkLabel(llFrame, text="0", font=("Font Awesome 5 Brands", 30), text_color="white")  # Replace with actual latitude value
    latitudeData.pack(side="right", padx=20, pady=15)
    latitudeLabel = ctk.CTkLabel(llFrame, text="Latitude:", font=("Font Awesome 5 Brands", 30), text_color="white")
    latitudeLabel.pack(side="right", padx=210, pady=15)

    
    # data of humidity frame
    humidityFrameFixedLabel = ctk.CTkLabel(humidityFrame, text = "Humidity", font=("Font Awesome 5 Brands", 30),text_color="white")
    humidityFrameFixedLabel.pack(side="top", padx=12, pady=15 )
    humidityFramecanvas = ctk.CTkCanvas(humidityFrame, height=1, width=285, bg="white")
    humidityFramecanvas.pack(side="top")
    humidityFrameData = ctk.CTkLabel(humidityFrame, text=("0"), font=("Font Awesome 5 Brands", 30), text_color="white")
    humidityFrameData.pack(side="bottom", pady=15)

    
    # data of altitude frame
    altitudeFrameFixedLabel = ctk.CTkLabel(altitudeFrame, text = "Altitude", font=("Font Awesome 5 Brands", 30),text_color="white")
    altitudeFrameFixedLabel.pack(side="top", padx=12, pady=15 )
    altitudeFramecanvas = ctk.CTkCanvas(altitudeFrame, height=1, width=285, bg="white")
    altitudeFramecanvas.pack(side="top")
    altitudeFrameData = ctk.CTkLabel(altitudeFrame, text=("0  ft"), font=("Font Awesome 5 Brands", 30), text_color="white")
    altitudeFrameData.pack(side="bottom", pady=15)

    #data for pressure frame
    
    pressureFrameFixedLabel = ctk.CTkLabel(pressureFrame, text = "Pressure", font=("Font Awesome 5 Brands", 30),text_color="white")
    pressureFrameFixedLabel.pack(side="top", padx=12, pady=15 )
    pressureFramecanvas = ctk.CTkCanvas(pressureFrame, height=1, width=285, bg="white")
    pressureFramecanvas.pack(side="top")
    pressureFrameData = ctk.CTkLabel(pressureFrame, text=("0  psi"), font=("Font Awesome 5 Brands", 30), text_color="white")
    pressureFrameData.pack(side="bottom", pady=15)

    
    # data of temperature frame
    tempratureFrameFixedLabel = ctk.CTkLabel(tempratureFrame, text = "Temperature", font=("Font Awesome 5 Brands", 30),text_color="white")
    tempratureFrameFixedLabel.pack(side="top", padx=12, pady=15 )
    tempratureFramecanvas = ctk.CTkCanvas(tempratureFrame, height=1, width=285, bg="white")
    tempratureFramecanvas.pack(side="top")
    tempratureFrameData = ctk.CTkLabel(tempratureFrame, text=("0  F"), font=("Font Awesome 5 Brands", 30), text_color="white")
    tempratureFrameData.pack(side="bottom", pady=15)

    
    # data of mf frame
    mfFrameFixedLabel = ctk.CTkLabel(mfFrame, text = "Magnetic Field", font=("Font Awesome 5 Brands", 30),text_color="white")
    mfFrameFixedLabel.pack(side="top", padx=12, pady=15 )
    mfFramecanvas = ctk.CTkCanvas(mfFrame, height=1, width=590, bg="white")
    mfFramecanvas.pack(side="top")
    mfFrameData = ctk.CTkLabel(mfFrame, text=("X : 0 \t Y : 0 \t Z : 0"), font=("Font Awesome 5 Brands", 30), text_color="white")
    mfFrameData.pack(side="bottom", pady=15)

    #data of co frame

    coFrameFixedLabel = ctk.CTkLabel(coFrame, text = "CO", font=("Font Awesome 5 Brands", 30),text_color="white")
    coFrameFixedLabel.pack(side="top", padx=12, pady=15 )
    coFramecanvas = ctk.CTkCanvas(coFrame, height=1, width=285, bg="white")
    coFramecanvas.pack(side="top")
    coFrameData = ctk.CTkLabel(coFrame, text=("0  psi"), font=("Font Awesome 5 Brands", 30), text_color="white")
    coFrameData.pack(side="bottom", pady=15)

    
    # data of h2 frame
    h2FrameFixedLabel = ctk.CTkLabel(h2Frame, text = "H2", font=("Font Awesome 5 Brands", 30),text_color="white")
    h2FrameFixedLabel.pack(side="top", padx=12, pady=15 )
    h2Framecanvas = ctk.CTkCanvas(h2Frame, height=1, width=285, bg="white")
    h2Framecanvas.pack(side="top")
    h2FrameData = ctk.CTkLabel(h2Frame, text=("0  F"), font=("Font Awesome 5 Brands", 30), text_color="white")
    h2FrameData.pack(side="bottom", pady=15)

    
    # Title for the Log Frame (Log Packet) on the extreme left
    logFrameFixedLabel = ctk.CTkLabel(logFrame, text="Log", font=("Font Awesome 5 Brands", 30), text_color="white", anchor="w", justify="left")
    logFrameFixedLabel.pack(side="top", padx=10, pady=10, anchor="w")  # anchor and padding adjusted

    # Removed the Canvas for a horizontal line
    logFrameCanvas = ctk.CTkCanvas(logFrame, height=1, width=1190, bg="black")
    logFrameCanvas.pack(side="top", padx=10, pady=5)

    # Multi-line log display (using a label to show the log data)
    logFrameData = ctk.CTkLabel(logFrame, text="No logs yet...", font=("Font Awesome 5 Brands", 20), text_color="white", anchor="nw", justify="left")
    logFrameData.pack(side="left", padx=10, pady=5, fill="both", expand=True)




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