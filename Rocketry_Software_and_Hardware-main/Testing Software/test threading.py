import tkinter as tk
import threading
import time
import serial

# Global variables to simulate data from Arduino and flag to ensure the message is sent only once
arduino_data = {}
send_message_once = False  # To ensure the message is sent only once

# Function to start the counter (Task 1)
def start_counter(label):
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        label.config(text=f"Counter: {counter}")

# Function to send request to Arduino (Task 2) - This will only be called once
def send_request_to_arduino():
    global send_message_once
    if not send_message_once:
        try:
            # Open the serial connection to Arduino
            arduino = serial.Serial('COM3', 9600)  # Adjust the COM port and baud rate as needed
            arduino.write(b'START')  # Send the 'START' command once
            send_message_once = True  # Prevent further requests
            print("Sent 'START' to Arduino")
        except serial.SerialException as e:
            print(f"Serial error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Function to receive data from Arduino and update labels (Task 3)
def collect_data_and_update_labels(latitude_label, longitude_label):
    try:
        # Open the serial connection to Arduino
        arduino = serial.Serial('COM3', 9600)  # Adjust the COM port and baud rate as needed
        while True:
            if arduino.in_waiting:  # Check if there is data waiting in the buffer
                data_packet = arduino.readline().decode('utf-8').strip()  # Read and decode the data
                # Assuming data is in format: id,latitude,longitude
                id, latitude, longitude = data_packet.split(',')
                arduino_data['id'] = id
                arduino_data['latitude'] = latitude
                arduino_data['longitude'] = longitude

                # Update the labels with the new data
                latitude_label.config(text=f"Latitude: {latitude}")
                longitude_label.config(text=f"Longitude: {longitude}")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Function to start all tasks when button is pressed
def start_tasks(counter_label, latitude_label, longitude_label, start_button):
    # Disable the button after it's clicked
    start_button.config(state=tk.DISABLED)

    # Send the request to Arduino once
    send_request_to_arduino()

    # Start counter in a new thread
    threading.Thread(target=start_counter, args=(counter_label,), daemon=False).start()

    # Collect data and update labels in another thread
    threading.Thread(target=collect_data_and_update_labels, args=(latitude_label, longitude_label), daemon=True).start()

# Tkinter UI setup
root = tk.Tk()
root.title("Arduino Data")

# Create and pack labels for counter, latitude, and longitude
counter_label = tk.Label(root, text="Counter: 0", font=('Helvetica', 16))
counter_label.pack(pady=20)

latitude_label = tk.Label(root, text="Latitude: --", font=('Helvetica', 16))
latitude_label.pack(pady=10)

longitude_label = tk.Label(root, text="Longitude: --", font=('Helvetica', 16))
longitude_label.pack(pady=10)

# Create a button that starts the tasks
start_button = tk.Button(root, text="Start", command=lambda: start_tasks(counter_label, latitude_label, longitude_label, start_button))
start_button.pack(pady=20)

root.mainloop()
