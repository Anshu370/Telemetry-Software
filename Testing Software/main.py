import time
import matplotlib.pyplot as plt
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.animation import FuncAnimation
T_time = -10
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
 # Create empty frames for graphs (on dashboard load)
graph_frames = []
axes = []
canvas_list = []
ani_list = []
is_launched = False
def dashboard():
    '''Function to bring dashboard in window frame'''
    dashboardButton.configure(fg_color="#111010")
    valuesButton.configure(fg_color="#000000")
    gyroButton.configure(fg_color="#000000")
    trajectoryButton.configure(fg_color='#000000')
  


    global axes, canvas_list
    axes, canvas_list = [], []

    # Creating empty frames for graphs
    for i in range(4):
        frame = ctk.CTkFrame(windowFrame, fg_color='#222222', corner_radius=15)
        graph_frames.append(frame)

    # Layout for the frames (2x2 grid)
    graph_frames[0].grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    graph_frames[1].grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
    graph_frames[2].grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
    graph_frames[3].grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    windowFrame.grid_rowconfigure(0, weight=1)
    windowFrame.grid_rowconfigure(1, weight=1)
    windowFrame.grid_columnconfigure(0, weight=1)
    windowFrame.grid_columnconfigure(1, weight=1)

    # Plot empty graphs (no data yet)
    plot_empty_graph(graph_frames[0], 'Acceleration', 'Acceleration (m/s²)')
    plot_empty_graph(graph_frames[1], 'Speed', 'Speed (km/h)')
    plot_empty_graph(graph_frames[2], 'Altitude', 'Altitude (m)')
    plot_empty_graph(graph_frames[3], 'Temperature', 'Temperature (°C)')

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

    # Create a canvas for the empty plot
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

    # Store for future use in launch (as placeholder for plotting data)
    axes.append(ax)
    canvas_list.append(canvas)

 
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
    '''To Launch the rocket and start the time button'''
    global is_launched

    if not is_launched:  # Avoid multiple launches
        is_launched = True

        statusVariableLabel.configure(text='Launching', text_color="#ABFFA9")
        launchButton.configure(state='DISABLED')
        count()  # Start countdown timer

        # Set up live plotting
        for i, (ax, canvas) in enumerate(zip(axes, canvas_list)):
            ylabel = 'Acceleration' if i == 0 else 'Speed' if i == 1 else 'Altitude' if i == 2 else 'Temperature'
            ani = plot_live_data(ax, canvas, ylabel)
            ani_list.append(ani)  # Keep reference to animations
            canvas.draw()  # Ensure canvas is drawnep reference to animations
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
   
    

def plot_live_data(ax, canvas, ylabel):
    '''Plot live data on the graph after launch using animation'''
    x = np.arange(10)
    y = np.zeros_like(x)  # Initial empty data

    line, = ax.plot(x, y, linestyle='-', color='cyan', linewidth=2)
    fig = ax.get_figure()

    def update(frame):
        new_ydata = np.random.random(10) * (10 if ylabel == 'Acceleration' else 50)
        line.set_ydata(new_ydata)
        ax.relim()
        ax.autoscale_view()
        canvas.draw()

    ani = FuncAnimation(fig, update, interval=1000)
    return ani
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