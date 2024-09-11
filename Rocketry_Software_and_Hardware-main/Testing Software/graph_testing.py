# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# from random import randrange
#
# fig = plt.figure(figsize=(6, 3))
# x = [0]
# y = [0]
#
# ln, = plt.plot(x, y, '-')
# plt.axis([0, 100, 0, 10])
#
#
# def update(frame):
#     a = int(input("Enter Data"))
#     x.append(x[-1] + 1)
#     y.append(a)
#     ln.set_data(x, y)
#     return ln,
#
#
# animation = FuncAnimation(fig, update, interval=500)
# plt.show()


'''Input Data From User'''
#
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# # initial data
# data = [3, 6, 2, 1, 8]
#
# # create figure and axes objects
# fig, ax = plt.subplots()
#
# # animation function
# def animate(i):
#     with open('data.txt','a+') as f:
#         for line in f:
#             data.append(int(line.strip()))
#     ax.clear()
#     ax.plot(data[-5:]) # plot the last 5 data points
#
# # call the animation
# ani = FuncAnimation(fig, animate, interval=1000)
#
# # show the plot
# plt.show()


'''Image Ploter'''
# import numpy as np
# from live_plotter import LiveImagePlotter, scale_image
#
# N = 25
# DEFAULT_IMAGE_HEIGHT = 100
# DEFAULT_IMAGE_WIDTH = 100
#
# live_plotter = LiveImagePlotter()
#
# x_data = []
# for i in range(N):
#     x_data.append(0.5 * i)
#     image_data = (
#         np.sin(x_data)[None, ...]
#         .repeat(DEFAULT_IMAGE_HEIGHT, 0)
#         .repeat(DEFAULT_IMAGE_WIDTH // N, 1)
#     )
#     live_plotter.plot(image_data_list=[scale_image(image_data, min_val=-1.0, max_val=1.0)])


'''From Web Apis'''
import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Create figure for plotting
fig, ax = plt.subplots()
xs = []
ys = []

def animate(i, xs:list, ys:list):

    flt = int(input("Enter Data"))

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(flt)
    # Limit x and y lists to 10 items
    xs = xs[-10:]
    ys = ys[-10:]
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.20)
    ax.set_title('Altitude')
    ax.set_xlabel('Date Time (hour:minute:second)')
    ax.set_ylabel('Altitude (in Feet)')

# Set up plot to call animate() function every 1000 milliseconds

ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys), interval=0)
plt.show()