import tkinter as tk
import serial
import time

# Set up the serial connection to the Arduino.
arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino port.
time.sleep(2)  # Wait for the connection to be established.

def led_on():
    arduino.write(b'1')  # Send '1' to turn the LED on.

def led_off():
    arduino.write(b'0')  # Send '0' to turn the LED off.

# Create the main window.
root = tk.Tk()
root.title("Arduino LED Control")

# Create and place the buttons.
on_button = tk.Button(root, text="Turn LED On", command=led_on)
on_button.pack(pady=10)

off_button = tk.Button(root, text="Turn LED Off", command=led_off)
off_button.pack(pady=10)

# Run the Tkinter event loop.
root.mainloop()

# Close the serial connection when the program ends.
arduino.close()
