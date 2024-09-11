import customtkinter as ctk
from tkinter import Label
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to clear the content of a frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Function to display graphs in the frame (Dashboard)
def display_dashboard(frame):
    clear_frame(frame)  # Clear previous content

    # Example of creating a graph using Matplotlib
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    ax = figure.add_subplot(111)
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])  # Example plot

    canvas = FigureCanvasTkAgg(figure, frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

    # Add a label or more graphs as needed
    label = ctk.CTkLabel(frame, text="Dashboard - Graphs")
    label.pack(pady=10)

# Function to display values in the frame
def display_values(frame):
    clear_frame(frame)  # Clear previous content

    # Add labels to show values
    label_1 = ctk.CTkLabel(frame, text="Value 1: 123")
    label_1.pack(pady=10)

    label_2 = ctk.CTkLabel(frame, text="Value 2: 456")
    label_2.pack(pady=10)

    label_3 = ctk.CTkLabel(frame, text="Value 3: 789")
    label_3.pack(pady=10)

# Main window setup
root = ctk.CTk()
root.geometry("800x600")
root.title("Dynamic Frame Content")

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
