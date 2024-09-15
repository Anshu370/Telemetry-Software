
import threading
import time
import matplotlib.pyplot as plt
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.animation import FuncAnimation

# Global values and functions
T_time = -10


animation_objects = []
data_dict = {
    'Acceleration': np.zeros(10),
    'Speed': np.zeros(10),
    'Altitude': np.zeros(10),
    'Temperature': np.zeros(10)
}

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Tkinter data values
APP = ctk.CTk()

width  = APP.winfo_screenwidth()
height = APP.winfo_screenheight()

APP.after(1, APP.wm_state, 'zoomed')
APP.title("Team Sudarshan Ground Control")
APP.iconbitmap("c:/Users/tiwar/Rocketry_Software_and_Hardware/Testing Software/sudarshan.ico")

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

graph_frames = []
axes = []
canvas_list = []

def dashboard():
    '''Function to bring dashboard in window frame'''
    clear_frame(windowFrame)

    global axes, canvas_list, graph_frames
    axes, canvas_list = [], []

    # Destroy any existing graph frames
    for frame in graph_frames:
        frame.destroy()

    graph_frames = [ctk.CTkFrame(windowFrame, fg_color='#222222', corner_radius=15) for _ in range(4)]

    graph_frames[0].grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    graph_frames[1].grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
    graph_frames[2].grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
    graph_frames[3].grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    windowFrame.grid_rowconfigure(0, weight=1)
    windowFrame.grid_rowconfigure(1, weight=1)
    windowFrame.grid_columnconfigure(0, weight=1)
    windowFrame.grid_columnconfigure(1, weight=1)

    # Plot empty graphs and initialize live data plotting
    titles = ['Acceleration', 'Speed', 'Altitude', 'Temperature']
    for i, title in enumerate(titles):
        plot_empty_graph(graph_frames[i], title, f'{title} (units)')
        ani = plot_live_data(axes[i], canvas_list[i], title)
        animation_objects.append(ani)

def plot_empty_graph(frame, title, ylabel):
    '''Plot empty graph with just axes, no data'''
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_title(title, fontsize=14, color='white')
    ax.set_ylabel(ylabel, fontsize=12, color='white')
    ax.set_xlabel("Time (s)", fontsize=12, color='white')
    ax.set_facecolor('#000000')
    fig.patch.set_facecolor('#000000')
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
    ax.tick_params(axis='both', colors='white')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

    axes.append(ax)
    canvas_list.append(canvas)

def plot_live_data(ax, canvas, ylabel):
    '''Plot live data on the graph after launch using animation'''
    x = np.arange(10)
    y = data_dict[ylabel]  # Use global data dictionary

    line, = ax.plot(x, y, linestyle='-', color='cyan', linewidth=2)
    fig = ax.get_figure()

    def update(frame):
        # Shift the existing data left and append a new data point
        y[:-1] = y[1:]
        new_ydata = np.random.random() * (10 if ylabel == 'Acceleration' else 50)
        y[-1] = new_ydata

        line.set_ydata(y)
        ax.relim()
        ax.autoscale_view()
        canvas.draw()

    ani = FuncAnimation(fig, update, interval=1000, blit=False)
    return ani
 
def values():
    '''Function to bring values in window frame'''
    clear_frame(windowFrame)
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
    accelerationFixedLabel = ctk.CTkLabel(accelerationFrame, text="Acceleration", font=("Font Awesome 5 Brands", 30),text_color="white")
    accelerationFixedLabel.place(relx=0.5, rely=0.3, anchor="center")
    accelerationcanvas = ctk.CTkCanvas(accelerationFrame, height=1, width=595, bg="white")
    accelerationcanvas.place(relx=0.5, rely=0.5, anchor="center")
    accelerationData = ctk.CTkLabel(accelerationFrame, text=("X : 0 \t Y : 0 \t Z : 0"),font=("Font Awesome 5 Brands", 30), text_color="white")
    accelerationData.place(relx=0.5, rely=0.7, anchor="center")

    # Data of velocity frame
    velocityFixedLabel = ctk.CTkLabel(velocityFrame, text="Velocity", font=("Font Awesome 5 Brands", 30), text_color="white")
    velocityFixedLabel.place(relx=0.5, rely=0.3, anchor="center")
    velocitycanvas = ctk.CTkCanvas(velocityFrame, height=1, width=595, bg="white")
    velocitycanvas.place(relx=0.5, rely=0.5, anchor="center")
    velocityData = ctk.CTkLabel(velocityFrame, text=("X : 0 \t Y : 0 \t Z : 0"), font=("Font Awesome 5 Brands", 30), text_color="white")
    velocityData.place(relx=0.5, rely=0.7, anchor="center")

    # For longitude and latitude labels (different layout without canvas)
    longitudeLabel = ctk.CTkLabel(llFrame, text="Longitude :", font=("Font Awesome 5 Brands", 30), text_color="white")
    longitudeLabel.place(relx=0.04, rely=0.25)

    longitudeData = ctk.CTkLabel(llFrame, text="000.00000", font=("Font Awesome 5 Brands", 30), text_color="white")
    longitudeData.place(relx=0.18, rely=0.25)

    latitudeLabel = ctk.CTkLabel(llFrame, text="Latitude :", font=("Font Awesome 5 Brands", 30), text_color="white")
    latitudeLabel.place(relx=0.55, rely=0.25)

    latitudeData = ctk.CTkLabel(llFrame, text="000.00000", font=("Font Awesome 5 Brands", 30), text_color="white")
    latitudeData.place(relx=0.67, rely=0.25)

    # data of humidity frame
    humidityFrameFixedLabel = ctk.CTkLabel(humidityFrame, text="Humidity", font=("Font Awesome 5 Brands", 30),text_color="white")
    humidityFrameFixedLabel.place(relx=0.5, rely=0.3, anchor="center")
    humidityFramecanvas = ctk.CTkCanvas(humidityFrame, height=1, width=285, bg="white")
    humidityFramecanvas.place(relx=0.5, rely=0.5, anchor="center")
    humidityFrameData = ctk.CTkLabel(humidityFrame, text=("0"), font=("Font Awesome 5 Brands", 30), text_color="white")
    humidityFrameData.place(relx=0.5, rely=0.7, anchor="center")

    # data of altitude frame
    altitudeFrameFixedLabel = ctk.CTkLabel(altitudeFrame, text="Altitude", font=("Font Awesome 5 Brands", 30),text_color="white")
    altitudeFrameFixedLabel.place(relx=0.5, rely=0.3, anchor="center")
    altitudeFramecanvas = ctk.CTkCanvas(altitudeFrame, height=1, width=285, bg="white")
    altitudeFramecanvas.place(relx=0.5, rely=0.5, anchor="center")
    altitudeFrameData = ctk.CTkLabel(altitudeFrame, text=("0  ft"), font=("Font Awesome 5 Brands", 30), text_color="white")
    altitudeFrameData.place(relx=0.5, rely=0.7, anchor="center")

    # data for pressure frame

    pressureFrameFixedLabel = ctk.CTkLabel(pressureFrame, text="Pressure", font=("Font Awesome 5 Brands", 30),text_color="white")
    pressureFrameFixedLabel.place(relx=0.5, rely=0.3, anchor="center")
    pressureFramecanvas = ctk.CTkCanvas(pressureFrame, height=1, width=285, bg="white")
    pressureFramecanvas.place(relx=0.5, rely=0.5, anchor="center")
    pressureFrameData = ctk.CTkLabel(pressureFrame, text=("0  psi"), font=("Font Awesome 5 Brands", 30), text_color="white")
    pressureFrameData.place(relx=0.5, rely=0.7, anchor="center")

    # data of temperature frame
    tempratureFrameFixedLabel = ctk.CTkLabel(tempratureFrame, text="Temperature", font=("Font Awesome 5 Brands", 30), text_color="white")
    tempratureFrameFixedLabel.place(relx=0.5, rely=0.3, anchor="center")
    tempratureFramecanvas = ctk.CTkCanvas(tempratureFrame, height=1, width=285, bg="white")
    tempratureFramecanvas.place(relx=0.5, rely=0.5, anchor="center")
    tempratureFrameData = ctk.CTkLabel(tempratureFrame, text=("0  F"), font=("Font Awesome 5 Brands", 30), text_color="white")
    tempratureFrameData.place(relx=0.5, rely=0.7, anchor="center")

    # data of mf frame
    mfFrameFixedLabel = ctk.CTkLabel(mfFrame, text="Magnetic Field", font=("Font Awesome 5 Brands", 30), text_color="white")
    mfFrameFixedLabel.place(relx=0.5, rely=0.3, anchor="center")
    mfFramecanvas = ctk.CTkCanvas(mfFrame, height=1, width=590, bg="white")
    mfFramecanvas.place(relx=0.5, rely=0.5, anchor="center")
    mfFrameData = ctk.CTkLabel(mfFrame, text=("X : 0 \t Y : 0 \t Z : 0"), font=("Font Awesome 5 Brands", 30),text_color="white")
    mfFrameData.place(relx=0.5, rely=0.7, anchor="center")

    # data of co frame

    coFrameFixedLabel = ctk.CTkLabel(coFrame, text="CO", font=("Font Awesome 5 Brands", 30), text_color="white")
    coFrameFixedLabel.place(relx=0.5, rely=0.3, anchor="center")
    coFramecanvas = ctk.CTkCanvas(coFrame, height=1, width=285, bg="white")
    coFramecanvas.place(relx=0.5, rely=0.5, anchor="center")
    coFrameData = ctk.CTkLabel(coFrame, text=("0  psi"), font=("Font Awesome 5 Brands", 30), text_color="white")
    coFrameData.place(relx=0.5, rely=0.7, anchor="center")

    # data of h2 frame
    h2FrameFixedLabel = ctk.CTkLabel(h2Frame, text="H2", font=("Font Awesome 5 Brands", 30), text_color="white")
    h2FrameFixedLabel.place(relx=0.5, rely=0.3, anchor="center")
    h2Framecanvas = ctk.CTkCanvas(h2Frame, height=1, width=285, bg="white")
    h2Framecanvas.place(relx=0.5, rely=0.5, anchor="center")
    h2FrameData = ctk.CTkLabel(h2Frame, text=("0  F"), font=("Font Awesome 5 Brands", 30), text_color="white")
    h2FrameData.place(relx=0.5, rely=0.7, anchor="center")

    # Title for the Log Frame (Log Packet) on the extreme left
    logFrameFixedLabel = ctk.CTkLabel(logFrame, text="Log", font=("Font Awesome 5 Brands", 30), text_color="white",anchor="w", justify="left")
    logFrameFixedLabel.place(relx=0.1, rely=0.2, anchor="center")  # anchor and padding adjusted

    # Removed the Canvas for a horizontal line
    logFrameCanvas = ctk.CTkCanvas(logFrame, height=1, width=1290, bg="black")
    logFrameCanvas.place(relx=0.5, rely=0.33, anchor="center")

    # Multi-line log display (using a label to show the log data)
    logFrameData = ctk.CTkLabel(logFrame, text="No logs yet...", font=("Font Awesome 5 Brands", 20), text_color="white",anchor="nw", justify="left")
    logFrameData.place(relx=0.5, rely=0.7, anchor="center")

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

def count():
    '''Function To start timer and goes till end'''
    global T_time

    tLable.configure(text=f'T {T_time}')

    tLable.after(1000, count)
    if T_time > 0:
        statusVariableLabel.configure(text='Launched', text_color="#52F44F")
    T_time += 1

# Thread declaration
counter_thred = threading.Thread(target=count, daemon=True)

def launch():
    '''To Launch the rocket and stat the time button'''
    statusVariableLabel.configure(text='Launching', text_color="#ABFFA9")
    launchButton.configure(state=ctk.DISABLED, text_color="Green")

    # Thread started for counter
    counter_thred.start()

    # Set up live plotting
    for i, (ax, canvas) in enumerate(zip(axes, canvas_list)):
        ylabel = 'Acceleration' if i == 0 else 'Speed' if i == 1 else 'Altitude' if i == 2 else 'Temperature'
        ani = plot_live_data(ax, canvas, ylabel)
        ani_list.append(ani)  # Keep reference to animations
        canvas.draw()


# Buttons

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