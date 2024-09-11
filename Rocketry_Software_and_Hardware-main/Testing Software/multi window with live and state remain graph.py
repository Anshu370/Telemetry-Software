import customtkinter as ctk
from tkinter import Label
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time

# Global variables to store graph data (to maintain state)
x_data = []
y_data = []

# Function to clear the content of a frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# Real-time values (simulated data)
real_time_data = {
    "value_1": 0,
    "value_2": 0,
    "value_3": 0
}
# Function to update values in real-time (Task 2)
def update_values(label_1, label_2, label_3):
    # Simulate real-time data updates
    real_time_data["value_1"] = random.randint(100, 200)
    real_time_data["value_2"] = random.randint(200, 300)
    real_time_data["value_3"] = random.randint(300, 400)

    # Update labels
    label_1.configure(text=f"Value 1: {real_time_data['value_1']}")
    label_2.configure(text=f"Value 2: {real_time_data['value_2']}")
    label_3.configure(text=f"Value 3: {real_time_data['value_3']}")

    # Keep updating the values every second
    label_1.after(1000, update_values, label_1, label_2, label_3)

# Function to update the graph (Task 1)
def update_graph(canvas, ax):
    # Append new data for graph in real time
    x_data.append(time.time())
    y_data.append(random.randint(0, 100))

    # Clear the axis and replot
    ax.clear()
    ax.plot(x_data, y_data)

    # Redraw the canvas with the new data
    canvas.draw()

    # Call this function again after 1 second for real-time updates
    canvas.get_tk_widget().after(1000, update_graph, canvas, ax)

# Function to display the dashboard with real-time graphs
def display_dashboard(frame):
    clear_frame(frame)  # Clear previous content

    # Create a graph using Matplotlib
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    ax = figure.add_subplot(111)
    canvas = FigureCanvasTkAgg(figure, frame)
    canvas.get_tk_widget().pack(pady=20)

    # Start real-time graph updates (maintaining previous state)
    update_graph(canvas, ax)

    # Add a label for the dashboard
    label = ctk.CTkLabel(frame, text="Dashboard - Real-time Graphs")
    label.pack(pady=10)

# Function to display real-time values
def display_values(frame):
    clear_frame(frame)  # Clear previous content

    # Create labels for values
    label_1 = ctk.CTkLabel(frame, text="Value 1: 0")
    label_1.pack(pady=10)

    label_2 = ctk.CTkLabel(frame, text="Value 2: 0")
    label_2.pack(pady=10)

    label_3 = ctk.CTkLabel(frame, text="Value 3: 0")
    label_3.pack(pady=10)

    # Start real-time updates of the values
    update_values(label_1, label_2, label_3)

# Main window setup
root = ctk.CTk()
root.geometry("800x600")
root.title("Dynamic Real-time Graphs and Values")

# Create a frame that will hold the dynamic content (graphs/values)
dynamic_frame = ctk.CTkFrame(root, width=600, height=400)
dynamic_frame.pack(pady=20)

# Buttons to switch between Dashboard and Values
dashboard_button = ctk.CTkButton(root, text="Dashboard", command=lambda: display_dashboard(dynamic_frame))
dashboard_button.pack(side="left", padx=20)

values_button = ctk.CTkButton(root, text="Values", command=lambda: display_values(dynamic_frame))
values_button.pack(side="right", padx=20)

# Initially display the dashboard (graphs)
display_dashboard(dynamic_frame)

root.mainloop()
