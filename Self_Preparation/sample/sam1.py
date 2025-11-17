
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import random  # Replace this with your actual data source
from collections import deque

# Initialize data storage for CPU usage and time
cpu_percentages = deque(maxlen=60)  # Stores last 60 CPU percentages

# Data storage
x_data = []
y_data = []

# Create figure and axis
fig, ax = plt.subplots()
line, = ax.plot_date([], [], 'b-', label='Live  Value')

ax.set_title("Real-time Plot")
ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.legend()
fig.autofmt_xdate()  # Auto-format the date labels


# Update function
def update(frame):
    now = datetime.now()
    value = random.randint(0, 100)  # Replace with your real-time data source
    ct1 = now.strftime("%X")

    # Append new data
    x_data.append(now)
    y_data.append(value)

    # Trim data to last 100 points
    x_data_trimmed = x_data[-100:]
    y_data_trimmed = y_data[-100:]

    # Update plot
    line.set_data(x_data_trimmed, y_data_trimmed)
    ax.relim()
    ax.autoscale_view()

    return line,


# Animation
ani = animation.FuncAnimation(fig, update, interval=1000)  # update every second
plt.show()

